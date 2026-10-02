# -*- coding: utf-8 -*-
"""Janela de texturas: ver, exportar/importar PNG, ver quem usa cada textura e ocultar partes por DBT."""
import os, zlib, struct, base64
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
from bt3eff_core import dbt_info, dbt_image_rgba, dbt_replace_image, recolor_dbt, PakError
from lang import tr


# ---------------------------------------------------------------- PNG sem bibliotecas externas
def png_encode(rgba, w, h):
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        for x in range(w):
            raw += bytes(rgba[y * w + x])
    def chunk(t, d):
        c = struct.pack(">I", len(d)) + t + d
        return c + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b""))


def png_decode(data):
    """Decodifica PNG 8 bits (RGBA, RGB, cinza, cinza+alfa ou paleta), sem entrelaçamento."""
    try:
        from PIL import Image
        import io
        im = Image.open(io.BytesIO(data)).convert("RGBA")
        return list(im.getdata()), im.width, im.height
    except ImportError:
        pass
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise PakError("não é um PNG")
    pos, idat, plte, trns = 8, b"", None, None
    while pos < len(data):
        ln = struct.unpack(">I", data[pos:pos + 4])[0]
        t = data[pos + 4:pos + 8]
        d = data[pos + 8:pos + 8 + ln]
        if t == b"IHDR":
            w, h, bd, ct, _, _, il = struct.unpack(">IIBBBBB", d)
        elif t == b"PLTE":
            plte = d
        elif t == b"tRNS":
            trns = d
        elif t == b"IDAT":
            idat += d
        pos += 12 + ln
    if bd != 8 or il != 0:
        raise PakError("PNG precisa ser 8 bits e sem entrelaçamento")
    ch = {6: 4, 2: 3, 0: 1, 4: 2, 3: 1}[ct]
    raw = zlib.decompress(idat)
    stride = w * ch
    out, prev, p = [], bytearray(stride), 0
    for y in range(h):
        f = raw[p]; line = bytearray(raw[p + 1:p + 1 + stride]); p += 1 + stride
        for i in range(stride):
            a = line[i - ch] if i >= ch else 0
            b = prev[i]
            c = prev[i - ch] if i >= ch else 0
            if f == 1: line[i] = (line[i] + a) & 255
            elif f == 2: line[i] = (line[i] + b) & 255
            elif f == 3: line[i] = (line[i] + (a + b) // 2) & 255
            elif f == 4:
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                line[i] = (line[i] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        prev = line
        for x in range(w):
            px = line[x * ch:(x + 1) * ch]
            if ct == 6: out.append(tuple(px))
            elif ct == 2: out.append((px[0], px[1], px[2], 255))
            elif ct == 0: out.append((px[0], px[0], px[0], 255))
            elif ct == 4: out.append((px[0], px[0], px[0], px[1]))
            else:
                k = px[0]
                a = trns[k] if trns and k < len(trns) else 255
                out.append((plte[k * 3], plte[k * 3 + 1], plte[k * 3 + 2], a))
    return out, w, h


def resize(rgba, w, h, nw, nh):
    """Redimensiona (vizinho mais próximo) para caber exatamente na textura original."""
    return [rgba[min(h - 1, y * h // nh) * w + min(w - 1, x * w // nw)] for y in range(nh) for x in range(nw)]


def preview_png(rgba, w, h, size=160):
    """PNG com fundo xadrez, ampliado por repetição para caber em 'size'."""
    k = max(1, size // max(w, h))
    W, H = w * k, h * k
    out = []
    for y in range(H):
        for x in range(W):
            r, g, b, a = rgba[(y // k) * w + (x // k)]
            bg = 90 if ((x // 8) + (y // 8)) % 2 else 60
            out.append((int(r * a / 255 + bg * (1 - a / 255)), int(g * a / 255 + bg * (1 - a / 255)),
                        int(b * a / 255 + bg * (1 - a / 255)), 255))
    return png_encode(out, W, H)


class TextureWindow(tk.Toplevel):
    FIELDS = ("pos_x", "pos_y", "pos_z", "size1", "size2", "size3")

    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.lang = app.lang
        self.title(tr("tex_title", self.lang))
        self.geometry("900x620")
        self.sel = None           # (cat, dbt_index, img_index)
        self._img = None
        left = ttk.Frame(self, padding=6)
        left.pack(side="left", fill="y")
        self.tree = ttk.Treeview(left, columns=("info", "uso"), show="tree headings", height=26)
        self.tree.heading("#0", text="DBT")
        self.tree.heading("info", text=tr("tex_info", self.lang))
        self.tree.heading("uso", text=tr("tex_used", self.lang))
        self.tree.column("#0", width=150)
        self.tree.column("info", width=130)
        self.tree.column("uso", width=60, anchor="center")
        self.tree.pack(fill="y", expand=True)
        self.tree.bind("<<TreeviewSelect>>", lambda e: self._select())
        right = ttk.Frame(self, padding=6)
        right.pack(side="left", fill="both", expand=True)
        self.canvas = tk.Label(right, bg="#303030", width=320, height=320)
        self.canvas.pack(anchor="w")
        bar = ttk.Frame(right)
        bar.pack(fill="x", pady=6)
        ttk.Button(bar, text=tr("tex_export", self.lang), command=self._export).pack(side="left")
        ttk.Button(bar, text=tr("tex_import", self.lang), command=self._import).pack(side="left", padx=4)
        ttk.Button(bar, text=tr("tex_hide_dbt", self.lang), command=self._hide_dbt).pack(side="left")
        ttk.Button(bar, text=tr("tex_recolor", self.lang), command=self._recolor).pack(side="left", padx=4)
        ttk.Label(right, text=tr("tex_users", self.lang), font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(8, 2))
        self.users = ttk.Frame(right)
        self.users.pack(fill="both", expand=True)
        self._fill()

    def _fill(self):
        self.tree.delete(*self.tree.get_children())
        eff = self.app.eff
        if not eff:
            return
        for ci, c in enumerate(eff.cats):
            for di, d in enumerate(c.dbts):
                node = self.tree.insert("", "end", text="%02X / DBT %d" % (c.type, di),
                                        values=("%.1f KB" % (len(d) / 1024.0), len(eff.texture_users(c, di))), open=True)
                for ii, im in enumerate(dbt_info(d)):
                    cols = 256 if im["psm"] == 0x13 else 16
                    self.tree.insert(node, "end", iid="%d/%d/%d" % (ci, di, ii), text="  img %d" % ii,
                                     values=("%d×%d %dc" % (im["w"], im["h"], cols), len(eff.texture_users(c, di, ii))))

    def _select(self):
        s = self.tree.selection()
        if not s or s[0].count("/") != 2:
            if s:
                ci_di = self.tree.item(s[0], "text")
            return
        ci, di, ii = [int(x) for x in s[0].split("/")]
        c = self.app.eff.cats[ci]
        self.sel = (c, di, ii)
        rgba, w, h = dbt_image_rgba(c.dbts[di], ii)
        self._img = tk.PhotoImage(data=base64.b64encode(preview_png(rgba, w, h, 300)).decode())
        self.canvas.config(image=self._img, width=self._img.width(), height=self._img.height())
        self._fill_users()

    def _fill_users(self):
        for w in self.users.winfo_children():
            w.destroy()
        c, di, ii = self.sel
        users = self.app.eff.texture_users(c, di, ii)
        if not users:
            ttk.Label(self.users, text=tr("tex_nouser", self.lang)).pack(anchor="w")
            return
        hdr = ttk.Frame(self.users)
        hdr.pack(fill="x")
        for j, k in enumerate(("#", tr("col_group", self.lang)) + tuple(tr("p_" + f, self.lang) for f in self.FIELDS)):
            ttk.Label(hdr, text=k, width=10 if j > 1 else (4 if j == 0 else 14)).grid(row=0, column=j)
        self.uvars = []
        allm = self.app.eff.all_minis()
        for r, m in enumerate(users, start=1):
            ttk.Label(hdr, text=str(allm.index(m))).grid(row=r, column=0)
            from lang import group_label
            ttk.Label(hdr, text=group_label(m.group, self.lang)).grid(row=r, column=1)
            vs = []
            for j, f in enumerate(self.FIELDS):
                v = tk.StringVar(value="%g" % m.get(f))
                ttk.Entry(hdr, textvariable=v, width=9).grid(row=r, column=2 + j, padx=1)
                vs.append((f, v))
            self.uvars.append((m, vs))
        ttk.Button(self.users, text=tr("apply", self.lang), command=self._apply_users).pack(anchor="w", pady=6)

    def _apply_users(self):
        self.app.snapshot()
        try:
            for m, vs in self.uvars:
                for f, v in vs:
                    m.set(f, float(v.get().replace(",", ".")))
        except ValueError as ex:
            messagebox.showerror(tr("err", self.lang), str(ex), parent=self)
            return
        self.app.changed()

    def _export(self):
        if not self.sel:
            return
        c, di, ii = self.sel
        rgba, w, h = dbt_image_rgba(c.dbts[di], ii)
        p = filedialog.asksaveasfilename(parent=self, defaultextension=".png", filetypes=[("PNG", "*.png")],
                                         initialfile="dbt%d_img%d.png" % (di, ii))
        if p:
            with open(p, "wb") as fh:
                fh.write(png_encode(rgba, w, h))

    def _import(self):
        if not self.sel:
            return
        c, di, ii = self.sel
        p = filedialog.askopenfilename(parent=self, filetypes=[("PNG", "*.png")])
        if not p:
            return
        try:
            with open(p, "rb") as fh:
                rgba, w, h = png_decode(fh.read())
            info = dbt_info(c.dbts[di])[ii]
            if (w, h) != (info["w"], info["h"]):
                rgba = resize(rgba, w, h, info["w"], info["h"])
                w, h = info["w"], info["h"]
            self.config(cursor="watch")
            self.update_idletasks()
            self.app.snapshot()
            c.dbts[di] = dbt_replace_image(c.dbts[di], ii, rgba, w, h)
        except Exception as ex:
            messagebox.showerror(tr("err", self.lang), str(ex), parent=self)
            return
        finally:
            self.config(cursor="")
        self.app.changed()
        self._select()
        messagebox.showinfo(tr("ok", self.lang), tr("tex_imported", self.lang), parent=self)

    def _recolor(self):
        if not self.sel:
            return
        c, di, ii = self.sel
        res = colorchooser.askcolor(parent=self)
        if not res or not res[0]:
            return
        self.app.snapshot()
        c.dbts[di] = recolor_dbt(c.dbts[di], [int(v) for v in res[0]], False, self.app._force())
        self.app.changed()
        self._select()

    def _hide_dbt(self):
        if not self.sel:
            return
        c, di, ii = self.sel
        users = self.app.eff.texture_users(c, di)
        if not users:
            return
        if messagebox.askyesno(tr("app_title", self.lang), tr("tex_hide_q", self.lang, n=len(users)), parent=self):
            self.app.snapshot()
            for m in users:
                m.hide("alpha")
            self.app.changed()
