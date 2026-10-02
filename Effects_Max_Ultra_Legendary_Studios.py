# -*- coding: utf-8 -*-
"""
Effects Max Ultra Legendary Studios v1.1 — interface gráfica (antigo BT3 Effect Studio)
Requer Python 3.8+ (tkinter já vem junto no Windows).
Uso: python bt3_effect_studio.py
"""
import os, sys, json, shutil
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk, filedialog, messagebox, colorchooser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bt3eff_core import (Effect, PakError, SUPPORT_NAME, CLASS_NAMES, container_entries, container_get,
                         container_put, scene_table, scene_set, SCENE_MAPS, SCENE_EVENTS, MAP_NAMES)
from lang import LANGS, PRESET_GROUPS, tr, group_label
from recursos import Resources

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, "config.json")
TEMPLATES = os.path.join(HERE, "modelos")
SCENES = os.path.join(HERE, "cenas")
EXPLOSION = "explosao_vfx5.pak"
RES = Resources(HERE)
EXTRAS = os.path.join(HERE, "extras")
SIZE_WARN_KB = 200
PARAM_FIELDS = ["dbt", "tex", "delay_a", "delay_b", "dur_a", "dur_b", "invoke",
                "pos_x", "pos_y", "pos_z", "size1", "size2", "size3", "time1", "time2", "unk30"]
INT_FIELDS = {"dbt", "tex", "delay_a", "delay_b", "dur_a", "dur_b", "invoke", "unk9", "unkA", "unkB"}


def rgb_hex(rgba):
    r, g, b = [max(0, min(255, int(round(v)))) for v in rgba[:3]]
    return "#%02x%02x%02x" % (r, g, b)


class MiniList(ttk.Frame):
    """Lista de mini-efeitos com caixas de marcar."""
    COLS = ("chk", "idx", "type", "group", "tex", "inv", "size", "color")

    def __init__(self, master, app, on_select=None):
        super().__init__(master)
        self.app, self.on_select = app, on_select
        self.on_check = None
        self.minis, self.checked = [], set()
        self.tree = ttk.Treeview(self, columns=self.COLS, show="headings", selectmode="browse", height=12)
        widths = (34, 36, 120, 120, 70, 80, 80, 80)
        for c, w in zip(self.COLS, widths):
            self.tree.column(c, width=w, anchor="center", stretch=(c == "group"))
        sb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        self.tree.bind("<Button-1>", self._click)
        self.tree.bind("<<TreeviewSelect>>", lambda e: self.on_select and self.on_select(self.selected()))
        self.tree.tag_configure("hit", foreground="#b00020")

    def headings(self):
        L = self.app.lang
        for c in self.COLS:
            self.tree.heading(c, text=tr("col_" + c, L))

    def fill(self, effect):
        self.tree.delete(*self.tree.get_children())
        self.minis = effect.all_minis() if effect else []
        self.checked &= set(id(m) for m in self.minis)
        L = self.app.lang
        for i, m in enumerate(self.minis):
            rows = m.color_rows()
            col = rgb_hex(m.read_rgba(rows[0])) if rows else "—"
            has_dbt = m.type != 0x00
            vals = ("☑" if id(m) in self.checked else "☐", i, "%02X %s" % (m.type, CLASS_NAMES.get(m.type, "")), group_label(m.group, L),
                    "%d/%d" % (m.get("dbt"), m.get("tex")) if has_dbt else "—",
                    "%02X" % m.get("invoke"), "%.2f" % m.get("size1") if m.type else "—", col)
            self.tree.insert("", "end", iid=str(i), values=vals, tags=("hit",) if m.hits else ())

    def _click(self, ev):
        if self.tree.identify_region(ev.x, ev.y) != "cell" or self.tree.identify_column(ev.x) != "#1":
            return
        iid = self.tree.identify_row(ev.y)
        if not iid:
            return
        m = self.minis[int(iid)]
        if id(m) in self.checked:
            self.checked.discard(id(m))
        else:
            self.checked.add(id(m))
        self.tree.set(iid, "chk", "☑" if id(m) in self.checked else "☐")
        if self.on_check:
            self.on_check()
        return "break"

    def set_all(self, on, pred=None):
        for m in self.minis:
            if pred and not pred(m):
                continue
            (self.checked.add if on else self.checked.discard)(id(m))
        for i, m in enumerate(self.minis):
            self.tree.set(str(i), "chk", "☑" if id(m) in self.checked else "☐")
        if self.on_check:
            self.on_check()

    def marked(self):
        return [m for m in self.minis if id(m) in self.checked]

    def selected(self):
        s = self.tree.selection()
        return self.minis[int(s[0])] if s else None

    def groups(self):
        seen = []
        for m in self.minis:
            if m.group not in seen:
                seen.append(m.group)
        return seen


class ScrollFrame(ttk.Frame):
    """Área com barra de rolagem vertical: nada fica escondido em telas pequenas."""

    def __init__(self, master, padding=10):
        super().__init__(master)
        self.canvas = tk.Canvas(self, highlightthickness=0, bd=0)
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.inner = ttk.Frame(self.canvas, padding=padding)
        self._win = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.vsb.pack(side="right", fill="y")
        self.inner.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfigure(self._win, width=e.width))
        for w in (self.canvas, self.inner):
            w.bind("<Enter>", lambda e: self.canvas.bind_all("<MouseWheel>", self._wheel))
            w.bind("<Leave>", lambda e: self.canvas.unbind_all("<MouseWheel>"))

    def _wheel(self, ev):
        if self.inner.winfo_height() > self.canvas.winfo_height():
            self.canvas.yview_scroll(int(-ev.delta / 120) or (-1 if ev.delta > 0 else 1), "units")


class GroupChips(ttk.Frame):
    """Caixas de marcar por grupo: marcar/desmarcar vários grupos de uma vez."""

    def __init__(self, master, app, lst, per_row=4):
        super().__init__(master)
        self.app, self.lst, self.per_row = app, lst, per_row
        self.vars = {}
        lst.on_check = self.sync

    def rebuild(self):
        for w in self.winfo_children():
            w.destroy()
        self.vars = {}
        groups = self.lst.groups()
        if not groups:
            return
        ttk.Label(self, text=self.app.t("mark_groups")).grid(row=0, column=0, sticky="w", padx=(0, 6))
        for i, g in enumerate(groups):
            n = sum(1 for m in self.lst.minis if m.group == g)
            v = tk.BooleanVar(value=False)
            ttk.Checkbutton(self, text="%s (%d)" % (group_label(g, self.app.lang), n), variable=v,
                            command=lambda g=g, v=v: self.lst.set_all(v.get(), lambda m: m.group == g)
                            ).grid(row=i // self.per_row, column=1 + i % self.per_row, sticky="w", padx=3)
            self.vars[g] = v
        self.sync()

    def sync(self):
        for g, v in self.vars.items():
            ms = [m for m in self.lst.minis if m.group == g]
            v.set(bool(ms) and all(id(m) in self.lst.checked for m in ms))


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cfg = self._load_cfg()
        self.lang = self.cfg.get("lang", "pt")
        self.eff, self.path, self.dirty, self.history = None, None, False, []
        self.src, self.src_path = None, None
        self.keep_sat = tk.BooleanVar(value=False)
        self.tex_color = tk.BooleanVar(value=True)
        self.beh_tpl, self.beh_tpl_path = None, None
        self.scale = float(self.cfg.get("scale", 1.0))
        self._set_icon()
        self.apply_theme()
        self.splash()
        if "lang" not in self.cfg:
            self.first_run()
        self.apply_display(first=True)
        self.protocol("WM_DELETE_WINDOW", self.quit_app)
        self.bind("<Control-z>", lambda e: self.undo())
        self.bind("<Control-s>", lambda e: self.save())
        self.build_ui()

    # ------------------------------------------------------------ config
    def _load_cfg(self):
        try:
            with open(CONFIG, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def _save_cfg(self):
        try:
            with open(CONFIG, "w", encoding="utf-8") as f:
                json.dump(self.cfg, f)
        except Exception:
            pass

    def t(self, key, **kw):
        return tr(key, self.lang, **kw)

    # ------------------------------------------------------------ ícone, capa e modo noturno
    def _photo(self, data):
        import base64
        try:
            return tk.PhotoImage(data=base64.b64encode(data).decode())
        except tk.TclError:
            return None

    def _set_icon(self):
        data = RES.get("arte", "icone64.png")
        if data:
            img = self._photo(data)
            if img is not None:
                self._icon_img = img
                try:
                    self.iconphoto(True, img)
                except tk.TclError:
                    pass
        ico = os.path.join(HERE, "icone.ico")
        if os.name == "nt" and os.path.exists(ico):
            try:
                self.iconbitmap(ico)
            except tk.TclError:
                pass

    def splash(self):
        """Capa ao abrir: fica na tela até apertar Enter (ou clicar)."""
        data = RES.get("arte", "capa.png")
        img = self._photo(data) if data else None
        if img is None:
            return
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        k = 1
        while img.width() // k > sw * 0.85 or img.height() // k > sh * 0.85:
            k += 1
        if k > 1:
            img = img.subsample(k, k)
        self._splash_img = img
        self.withdraw()
        w = tk.Toplevel(self)
        w.overrideredirect(True)
        x, y = (sw - img.width()) // 2, (sh - img.height()) // 2
        w.geometry("%dx%d+%d+%d" % (img.width(), img.height(), x, y))
        tk.Label(w, image=img, bd=0).pack()
        done = tk.BooleanVar(value=False)
        for ev in ("<Return>", "<KP_Enter>", "<Button-1>", "<Escape>"):
            w.bind(ev, lambda e: done.set(True))
        w.focus_force()
        w.grab_set()
        self.wait_variable(done)
        w.destroy()
        self.deiconify()

    DARK = {"bg": "#1f2126", "fg": "#e6e6e6", "field": "#2b2e35", "sel": "#3d6fb5", "btn": "#30343c", "border": "#3a3d44"}

    def apply_theme(self):
        dark = bool(self.cfg.get("dark"))
        st = ttk.Style(self)
        if not hasattr(self, "_theme0"):
            self._theme0 = st.theme_use()
        if dark:
            c = self.DARK
            try:
                st.theme_use("clam")
            except tk.TclError:
                pass
            for w in ("TFrame", "TLabel", "TCheckbutton", "TRadiobutton", "TLabelframe", "TLabelframe.Label", "TPanedwindow"):
                st.configure(w, background=c["bg"], foreground=c["fg"])
            st.configure("TButton", background=c["btn"], foreground=c["fg"], bordercolor=c["border"])
            st.map("TButton", background=[("active", c["sel"])])
            st.configure("TMenubutton", background=c["btn"], foreground=c["fg"])
            st.configure("TNotebook", background=c["bg"], bordercolor=c["border"])
            st.configure("TNotebook.Tab", background=c["btn"], foreground=c["fg"])
            st.map("TNotebook.Tab", background=[("selected", c["sel"])])
            for w in ("TEntry", "TCombobox", "TSpinbox"):
                st.configure(w, fieldbackground=c["field"], foreground=c["fg"], background=c["btn"])
            st.map("TCombobox", fieldbackground=[("readonly", c["field"])], foreground=[("readonly", c["fg"])])
            st.configure("Treeview", background=c["field"], fieldbackground=c["field"], foreground=c["fg"])
            st.configure("Treeview.Heading", background=c["btn"], foreground=c["fg"])
            st.map("Treeview", background=[("selected", c["sel"])])
            st.map("TCheckbutton", background=[("active", c["bg"])])
            st.map("TRadiobutton", background=[("active", c["bg"])])
            self.configure(bg=c["bg"])
            for k, v in (("*Background", c["bg"]), ("*Foreground", c["fg"]), ("*Text.Background", c["field"]),
                         ("*Canvas.Background", c["bg"]), ("*Menu.Background", c["btn"]), ("*Menu.Foreground", c["fg"]),
                         ("*TCombobox*Listbox.Background", c["field"]), ("*TCombobox*Listbox.Foreground", c["fg"]),
                         ("*insertBackground", c["fg"])):
                self.option_add(k, v)
        else:
            try:
                st.theme_use(self._theme0)
            except tk.TclError:
                pass

    def toggle_dark(self):
        self.cfg["dark"] = not self.cfg.get("dark")
        self._save_cfg()
        if not self.cfg["dark"]:
            messagebox.showinfo(self.t("app_title"), self.t("dark_restart"))
        self.apply_theme()
        self.build_ui()

    def show_image(self, key, title=""):
        """Imagem ilustrativa de um formato/extra/aura (resources: imagens/mapa.json)."""
        import json as _json
        try:
            mp = _json.loads(RES.get("imagens", "mapa.json").decode("utf-8"))
        except Exception:
            mp = {}
        fn = mp.get(key)
        data = RES.get("imagens", fn) if fn else None
        img = self._photo(data) if data else None
        if img is None:
            messagebox.showinfo(self.t("app_title"), self.t("no_image"))
            return
        w = tk.Toplevel(self)
        w.title(title or key.split("/")[-1].replace(".pak", ""))
        w.transient(self)
        lb = tk.Label(w, image=img, bd=0)
        lb.image = img
        lb.pack()
        ttk.Button(w, text=self.t("close"), command=w.destroy).pack(pady=6)

    def has_image(self, key):
        import json as _json
        try:
            return key in _json.loads(RES.get("imagens", "mapa.json").decode("utf-8"))
        except Exception:
            return False

    # ------------------------------------------------------------ menus em árvore (grupos de formatos)
    def fill_tree_menu(self, menu, names, callback):
        """names: caminhos 'Grupo/Subgrupo/Nome.pak' → submenus aninhados."""
        tree = {}
        for n in names:
            node = tree
            parts = n.split("/")
            for p in parts[:-1]:
                node = node.setdefault(p + "/", {})
            node[parts[-1]] = n
        def build(m, node):
            for k in sorted([k for k in node if k.endswith("/")], key=str.lower):
                sub = tk.Menu(m, tearoff=0)
                build(sub, node[k])
                m.add_cascade(label=k[:-1], menu=sub)
            for k in sorted([k for k in node if not k.endswith("/")], key=str.lower):
                m.add_command(label=os.path.splitext(k)[0], command=lambda n=node[k]: callback(n))
        build(menu, tree)

    def tree_button(self, parent, sub, callback, width=34):
        """Botão que abre o menu em árvore de uma pasta de recursos e mostra a escolha."""
        var = tk.StringVar(value=self.t("choose"))
        box = ttk.Frame(parent)
        mb = ttk.Menubutton(box, textvariable=var, width=width)
        mb.pack(side="left")
        chosen = {"key": None}
        ib = ttk.Button(box, text="🖼", width=3, state="disabled",
                        command=lambda: chosen["key"] and self.show_image(chosen["key"], var.get()))
        ib.pack(side="left", padx=2)
        menu = tk.Menu(mb, tearoff=0)
        def pick(name):
            var.set(os.path.splitext(name)[0].replace("/", " › "))
            chosen["key"] = sub + "/" + name
            ib.config(state="normal" if self.has_image(chosen["key"]) else "disabled")
            callback(name)
        self.fill_tree_menu(menu, RES.list(sub), pick)
        mb["menu"] = menu
        return box

    def first_run(self):
        """Primeira execução: pergunta idioma, tamanho da janela e escala."""
        self.withdraw()
        w = tk.Toplevel(self)
        w.title("BT3 Effect Studio")
        w.resizable(False, False)
        lang = tk.StringVar(value="pt")
        win = tk.StringVar(value="auto")
        sc = tk.StringVar(value="1.0")
        box = ttk.Frame(w, padding=16)
        box.pack(fill="both", expand=True)
        ttk.Label(box, text="Idioma / Idioma / Language", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        for code, name in LANGS.items():
            ttk.Radiobutton(box, text=name, value=code, variable=lang).pack(anchor="w", padx=10)
        ttk.Separator(box).pack(fill="x", pady=10)
        ttk.Label(box, text="Resolução / Resolución / Resolution", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        ttk.Label(box, text="Monitor: %d × %d" % (sw, sh)).pack(anchor="w", padx=10)
        opts = ["auto"] + self.WINDOW_SIZES
        cb = ttk.Combobox(box, state="readonly", width=28,
                          values=["Automático / Automatic"] + [x.replace("x", " × ") if x != "max" else "Maximizada / Maximized" for x in self.WINDOW_SIZES])
        cb.current(0)
        cb.pack(anchor="w", padx=10, pady=2)
        ttk.Label(box, text="Escala / Escala / Scale").pack(anchor="w", pady=(8, 0))
        cs = ttk.Combobox(box, state="readonly", width=10, values=["%d%%" % round(x * 100) for x in self.SCALES])
        cs.current(self.SCALES.index(1.0))
        cs.pack(anchor="w", padx=10, pady=2)

        def ok():
            self.cfg["lang"] = lang.get()
            self.cfg["window"] = opts[max(0, cb.current())]
            self.cfg["scale"] = self.SCALES[max(0, cs.current())]
            self._save_cfg()
            w.destroy()
        ttk.Button(box, text="OK", command=ok).pack(fill="x", pady=(14, 0))
        w.protocol("WM_DELETE_WINDOW", ok)
        w.grab_set()
        self.wait_window(w)
        self.lang = self.cfg.get("lang", "pt")
        self.scale = float(self.cfg.get("scale", 1.0))
        self.deiconify()

    # ------------------------------------------------------------ exibição
    WINDOW_SIZES = ["1024x600", "1280x720", "1366x768", "1600x900", "1920x1080", "max"]
    SCALES = [0.8, 0.9, 1.0, 1.15, 1.3]

    def fs(self, n):
        return max(6, int(round(n * self.scale)))

    def wrap(self):
        return int(380 * self.scale)

    def apply_display(self, first=False):
        for name in ("TkDefaultFont", "TkTextFont", "TkHeadingFont", "TkMenuFont", "TkCaptionFont"):
            try:
                tkfont.nametofont(name).configure(size=self.fs(9))
            except tk.TclError:
                pass
        try:
            ttk.Style(self).configure("Treeview", rowheight=int(20 * self.scale))
        except tk.TclError:
            pass
        size = self.cfg.get("window", "auto")
        if size == "auto":
            sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
            size = "max" if sw < 1400 or sh < 800 else "1280x760"
        self.minsize(760, 480)
        if size == "max":
            try:
                self.state("zoomed")
            except tk.TclError:
                self.attributes("-zoomed", True)
        else:
            try:
                self.state("normal")
            except tk.TclError:
                pass
            self.geometry(size)

    def set_display(self, window=None, scale=None, layout=None):
        if window is not None:
            self.cfg["window"] = window
        if scale is not None:
            self.cfg["scale"] = scale
            self.scale = scale
        if layout is not None:
            self.cfg["layout"] = layout
        self._save_cfg()
        self.apply_display()
        self.build_ui()

    def _tab(self, nb, key):
        sf = ScrollFrame(nb)
        nb.add(sf, text=self.t(key))
        self._tabs[key] = sf
        return sf.inner

    def info(self, key):
        w = tk.Toplevel(self)
        w.title(self.t("info_title"))
        w.transient(self)
        txt = tk.Text(w, wrap="word", width=70, height=24, font=("Segoe UI", self.fs(10)), padx=10, pady=10)
        txt.insert("1.0", self.t(key))
        txt.config(state="disabled")
        txt.pack(fill="both", expand=True)
        ttk.Button(w, text=self.t("close"), command=w.destroy).pack(pady=6)

    def info_btn(self, parent, key, text=None):
        return ttk.Button(parent, text=text or "?", width=(3 if text is None else 0),
                          command=lambda: self.info(key))

    # ------------------------------------------------------------ UI
    def cur_kind(self):
        return getattr(self.eff, "kind", "skill") if self.eff else "skill"

    def build_ui(self):
        self._ui_kind = self.cur_kind()
        self._tabs = {}
        for w in self.winfo_children():
            w.destroy()
        self.title(self.t("app_title") + (" — " + os.path.basename(self.path) if self.path else ""))
        self._menu()
        top = ttk.Frame(self, padding=6)
        top.pack(fill="x")
        self.lbl_file = ttk.Label(top, font=("Segoe UI", self.fs(11), "bold"))
        self.lbl_file.pack(side="left")
        self.lbl_sum = ttk.Label(top)
        self.lbl_sum.pack(side="left", padx=16)
        self.lbl_size = tk.Label(top, font=("Segoe UI", self.fs(10), "bold"))
        self.lbl_size.pack(side="left")
        ttk.Button(top, text=self.t("w_btn"), command=self.show_weight).pack(side="left", padx=6)
        ttk.Button(top, text=self.t("btn_textures"), command=self.open_textures).pack(side="left")
        ttk.Button(top, text=self.t("btn_hex"), command=self.open_hex).pack(side="left", padx=6)
        self.info_btn(top, "info_classes", self.t("btn_classes")).pack(side="right")

        body = ttk.PanedWindow(self, orient="vertical" if self.cfg.get("layout") == "bottom" else "horizontal")
        body.pack(fill="both", expand=True, padx=6, pady=(0, 6))
        left = ttk.Frame(body)
        body.add(left, weight=3)
        bar = ttk.Frame(left)
        bar.pack(fill="x", pady=(0, 4))
        ttk.Button(bar, text=self.t("mark_all"), command=lambda: self.list.set_all(True)).pack(side="left")
        ttk.Button(bar, text=self.t("unmark_all"), command=lambda: self.list.set_all(False)).pack(side="left", padx=4)
        ttk.Button(bar, text=self.t("remove_marked"), command=self.remove_marked).pack(side="right")
        ttk.Button(bar, text=self.t("hide_marked"), command=lambda: self.hide_minis(self.list.marked())).pack(side="right", padx=4)
        chips_holder = ttk.Frame(left)
        chips_holder.pack(fill="x", pady=(0, 4))
        self.list = MiniList(left, self, on_select=self.on_select)
        self.list.pack(fill="both", expand=True)
        self.chips = GroupChips(chips_holder, self, self.list)
        self.chips.pack(fill="x")
        self.list.headings()

        nb = ttk.Notebook(body)
        body.add(nb, weight=2)
        self.tab_colors(nb)
        self.tab_params(nb)
        self.tab_groups(nb)
        self.tab_combine(nb)
        self.tab_behavior(nb)
        self.tab_scene(nb)
        self.tab_extras(nb)
        self.tab_aura(nb)
        self.tab_support(nb)
        self.tab_support_params(nb)
        self.tab_flags(nb)
        visible = {"aura": ("tab_colors", "tab_params", "tab_extras", "tab_aura", "tab_flags"),
                   "support": ("tab_colors", "tab_params", "tab_extras", "tab_support", "tab_sparams", "tab_aura", "tab_flags")}
        for key, sf in self._tabs.items():
            if self._ui_kind in visible:
                hide = key not in visible[self._ui_kind]
            else:
                hide = key in ("tab_aura", "tab_support", "tab_sparams")
            if hide:
                nb.hide(sf)
        self.refresh()

    def _menu(self):
        mb = tk.Menu(self)
        mf = tk.Menu(mb, tearoff=0)
        mf.add_command(label=self.t("open"), command=self.open, accelerator="Ctrl+O")
        mf.add_command(label=self.t("save"), command=self.save, accelerator="Ctrl+S")
        mf.add_command(label=self.t("save_as"), command=lambda: self.save(as_new=True))
        mf.add_separator()
        mf.add_command(label=self.t("undo"), command=self.undo, accelerator="Ctrl+Z")
        mf.add_separator()
        mf.add_command(label=self.t("quit"), command=self.quit_app)
        mtools = tk.Menu(mb, tearoff=0)
        mtools.add_command(label=self.t("btn_textures"), command=self.open_textures)
        mtools.add_command(label=self.t("btn_hex"), command=self.open_hex)
        mtools.add_command(label=self.t("hex_external"), command=self.open_hex_external)
        mb.add_cascade(label=self.t("tools"), menu=mtools)
        mb.add_cascade(label=self.t("file"), menu=mf)
        mt = tk.Menu(mb, tearoff=0)
        tpls = RES.list("modelos")
        if tpls:
            self.fill_tree_menu(mt, tpls, lambda f: self.open_template(f))
        else:
            mt.add_command(label=self.t("no_templates"), state="disabled")
        for sub, key in (("auras", "tab_aura"), ("suportes", "tab_support"), ("pre_disparo", "pre_title")):
            names = RES.list(sub)
            if names:
                sm = tk.Menu(mt, tearoff=0)
                self.fill_tree_menu(sm, names, lambda f, sub=sub: self.open_template(f, sub))
                mt.add_separator()
                mt.add_cascade(label=self.t(key), menu=sm)
        mb.add_cascade(label=self.t("templates"), menu=mt)
        ml = tk.Menu(mb, tearoff=0)
        self.lang_var = tk.StringVar(value=self.lang)
        for code, name in LANGS.items():
            ml.add_radiobutton(label=name, value=code, variable=self.lang_var,
                               command=lambda c=code: self.set_lang(c))
        mb.add_cascade(label=self.t("language"), menu=ml)
        md = tk.Menu(mb, tearoff=0)
        mw = tk.Menu(md, tearoff=0)
        self.win_var = tk.StringVar(value=self.cfg.get("window", "auto"))
        mw.add_radiobutton(label=self.t("win_auto"), value="auto", variable=self.win_var, command=lambda: self.set_display(window="auto"))
        for ws in self.WINDOW_SIZES:
            mw.add_radiobutton(label=self.t("win_max") if ws == "max" else ws.replace("x", " × "), value=ws,
                               variable=self.win_var, command=lambda ws=ws: self.set_display(window=ws))
        md.add_cascade(label=self.t("win_size"), menu=mw)
        msc = tk.Menu(md, tearoff=0)
        self.scale_menu_var = tk.StringVar(value=str(self.scale))
        for sc in self.SCALES:
            msc.add_radiobutton(label="%d%%" % round(sc * 100), value=str(sc), variable=self.scale_menu_var,
                                command=lambda sc=sc: self.set_display(scale=sc))
        md.add_cascade(label=self.t("ui_scale"), menu=msc)
        mlay = tk.Menu(md, tearoff=0)
        self.layout_var = tk.StringVar(value=self.cfg.get("layout", "right"))
        mlay.add_radiobutton(label=self.t("layout_right"), value="right", variable=self.layout_var, command=lambda: self.set_display(layout="right"))
        mlay.add_radiobutton(label=self.t("layout_bottom"), value="bottom", variable=self.layout_var, command=lambda: self.set_display(layout="bottom"))
        md.add_cascade(label=self.t("panel_pos"), menu=mlay)
        self.dark_var = tk.BooleanVar(value=bool(self.cfg.get("dark")))
        md.add_checkbutton(label=self.t("dark_mode"), variable=self.dark_var, command=self.toggle_dark)
        mb.add_cascade(label=self.t("display"), menu=md)
        mh = tk.Menu(mb, tearoff=0)
        mh.add_command(label=self.t("btn_classes"), command=lambda: self.info("info_classes"))
        mh.add_command(label=self.t("about"), command=lambda: messagebox.showinfo(self.t("about"), self.t("about_text")))
        mb.add_cascade(label=self.t("help"), menu=mh)
        self.config(menu=mb)
        self.bind("<Control-o>", lambda e: self.open())

    def set_lang(self, code):
        self.lang = code
        self.cfg["lang"] = code
        self._save_cfg()
        self.build_ui()

    # ---- aba cores
    def tab_colors(self, nb):
        f = self._tab(nb, "tab_colors")
        self.info_btn(f, "info_colors", self.t("more_info")).pack(anchor="e")
        ttk.Checkbutton(f, text=self.t("keep_sat"), variable=self.keep_sat).pack(anchor="w")
        ttk.Checkbutton(f, text=self.t("tex_color"), variable=self.tex_color).pack(anchor="w")
        fr = ttk.Frame(f)
        fr.pack(fill="x", pady=(2, 8))
        ttk.Label(fr, text=self.t("force_color")).pack(side="left")
        self.force_var = tk.DoubleVar(value=float(self.cfg.get("force", 0)))
        self.lbl_force = ttk.Label(fr, text="%d%%" % round(self.force_var.get() * 100), width=5)
        ttk.Scale(fr, from_=0.0, to=1.0, variable=self.force_var, orient="horizontal",
                  command=lambda v: self.lbl_force.config(text="%d%%" % round(float(v) * 100))).pack(side="left", fill="x", expand=True, padx=4)
        self.lbl_force.pack(side="left")
        ttk.Button(f, text=self.t("color_all"), command=lambda: self.recolor(self.list.minis, whole=True)).pack(fill="x")
        ttk.Button(f, text=self.t("color_marked"), command=lambda: self.recolor(self.list.marked())).pack(fill="x", pady=4)
        cr = ttk.Frame(f)
        cr.pack(fill="x", pady=(0, 4))
        ttk.Button(cr, text=self.t("color_contrast"), command=self._recolor_contrast).pack(side="left", fill="x", expand=True)
        ttk.Label(cr, text=self.t("contrast_shift")).pack(side="left", padx=(6, 2))
        self.contrast_var = tk.StringVar(value="-35")
        ttk.Spinbox(cr, from_=-90, to=90, increment=5, width=5, textvariable=self.contrast_var).pack(side="left")
        self.info_btn(cr, "info_contrast").pack(side="left", padx=4)
        g = ttk.Frame(f)
        g.pack(fill="x", pady=4)
        ttk.Label(g, text=self.t("color_group")).pack(side="left")
        self.cb_colorgroup = ttk.Combobox(g, state="readonly", width=16)
        self.cb_colorgroup.pack(side="left", padx=4)
        ttk.Button(g, text=self.t("pick"), command=self._color_group).pack(side="left")
        ttk.Separator(f).pack(fill="x", pady=10)
        self._opacity_section(f)
        ttk.Separator(f).pack(fill="x", pady=10)
        hdr = ttk.Frame(f)
        hdr.pack(fill="x")
        ttk.Label(hdr, text=self.t("nerf_title"), font=("Segoe UI", self.fs(10), "bold")).pack(side="left")
        self.info_btn(hdr, "info_nerf", self.t("more_info")).pack(side="right")
        self.lbl_depth = ttk.Label(f, text="")
        self.lbl_depth.pack(anchor="w", pady=2)
        nr = ttk.Frame(f)
        nr.pack(fill="x", pady=(2, 0))
        ttk.Button(nr, text=self.t("nerf_all"), command=lambda: self._nerf(None)).pack(side="left", fill="x", expand=True)
        ttk.Button(nr, text=self.t("nerf_marked"), command=lambda: self._nerf(self.list.marked())).pack(side="left", fill="x", expand=True, padx=(4, 0))
        ttk.Separator(f).pack(fill="x", pady=10)
        ttk.Label(f, text=self.t("manual_rgb"), font=("Segoe UI", self.fs(10), "bold")).pack(anchor="w")
        self.rgb_box = ttk.Frame(f)
        self.rgb_box.pack(fill="both", expand=True, pady=6)

    def _fill_rgb(self, m):
        for w in self.rgb_box.winfo_children():
            w.destroy()
        if m is None:
            ttk.Label(self.rgb_box, text=self.t("select_one")).pack(anchor="w")
            return
        rows = m.color_rows()
        if not rows:
            ttk.Label(self.rgb_box, text=self.t("no_colors")).pack(anchor="w")
            return
        canvas = tk.Canvas(self.rgb_box, highlightthickness=0, height=300)
        sb = ttk.Scrollbar(self.rgb_box, orient="vertical", command=canvas.yview)
        inner = ttk.Frame(canvas)
        inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=inner, anchor="nw")
        canvas.configure(yscrollcommand=sb.set)
        canvas.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        tools = ttk.Frame(self.rgb_box)
        tools.pack(side="top", fill="x", pady=(0, 4))
        chans = [self.t("ch_red"), self.t("ch_green"), self.t("ch_blue"), self.t("ch_int")]
        ttk.Label(tools, text=self.t("ch_color1")).pack(side="left")
        self.ch_a = ttk.Combobox(tools, state="readonly", width=9, values=chans)
        self.ch_a.current(0)
        self.ch_a.pack(side="left", padx=2)
        ttk.Label(tools, text=self.t("ch_color2")).pack(side="left", padx=(6, 0))
        self.ch_b = ttk.Combobox(tools, state="readonly", width=9, values=chans)
        self.ch_b.current(2)
        self.ch_b.pack(side="left", padx=2)
        ttk.Button(tools, text=self.t("ch_swap"), command=lambda: self._rgb_entries("swap")).pack(side="left", padx=2)
        ttk.Button(tools, text=self.t("ch_copy"), command=lambda: self._rgb_entries("copy")).pack(side="left")
        self.info_btn(tools, "info_channels").pack(side="left", padx=4)
        canvas.pack_forget()
        sb.pack_forget()
        canvas.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        for c, h in enumerate(("", "R", "G", "B", "A", "")):
            ttk.Label(inner, text=h).grid(row=0, column=c)
        self.rgb_vars = []
        for i, row in enumerate(rows):
            vals = m.read_rgba(row)
            lbl = self.t("session_row", s=i // 3 + 1, r=i % 3 + 1) if row[2] == 'f' else "%s %d" % (self.t("row"), i + 1)
            ttk.Label(inner, text=lbl).grid(row=i + 1, column=0, padx=2, sticky="w")
            vs = []
            for k in range(4):
                v = tk.StringVar(value=("%g" % vals[k]))
                ttk.Spinbox(inner, from_=0, to=255, width=6, textvariable=v).grid(row=i + 1, column=k + 1, padx=1, pady=1)
                vs.append(v)
            sw = tk.Label(inner, width=3, bg=rgb_hex(vals), relief="solid", bd=1)
            sw.grid(row=i + 1, column=5, padx=4)
            sw.bind("<Button-1>", lambda e, vs=vs: self._pick_into(vs))
            self.rgb_vars.append((row, vs))
        ttk.Button(inner, text=self.t("apply"), command=lambda: self._apply_rgb(m)).grid(row=len(rows) + 1, column=1, columnspan=4, pady=6, sticky="ew")

    def _rgb_entries(self, mode):
        """Como no Skill Shader Editor: 'Inverter' troca os valores de duas colunas em todas as linhas;
           'Copiar' copia a Cor 1 para a Cor 2. Depois é só clicar em Aplicar."""
        a, b = self.ch_a.current(), self.ch_b.current()
        if a == b or not getattr(self, "rgb_vars", None):
            return
        for row, vs in self.rgb_vars:
            va, vb = vs[a].get(), vs[b].get()
            if mode == "swap":
                vs[a].set(vb)
                vs[b].set(va)
            else:
                vs[b].set(va)

    def _pick_into(self, vs):
        cur = rgb_hex([float(v.get() or 0) for v in vs[:3]])
        res = colorchooser.askcolor(color=cur, parent=self)
        if res and res[0]:
            for k in range(3):
                vs[k].set(str(int(res[0][k])))

    def _apply_rgb(self, m):
        self.snapshot()
        try:
            for row, vs in self.rgb_vars:
                m.write_rgba(row, [float(v.get()) for v in vs])
        except ValueError as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self.changed()

    def recolor(self, minis, whole=False):
        if not self.eff:
            return
        if not minis:
            messagebox.showinfo(self.t("app_title"), self.t("nothing_marked"))
            return
        res = colorchooser.askcolor(parent=self)
        if not res or not res[0]:
            return
        self.snapshot()
        rgb = [int(c) for c in res[0]]
        for m in minis:
            m.recolor(rgb, self.keep_sat.get(), self._force())
        n = self.eff.recolor_textures(rgb, self.keep_sat.get(), self._force()) if whole and self.tex_color.get() else None
        self.changed()
        if n is not None:
            messagebox.showinfo(self.t("ok"), self.t("tex_done", n=n))

    def _force(self):
        try:
            v = float(self.force_var.get())
        except (AttributeError, ValueError, TypeError):
            v = 0.0
        self.cfg["force"] = v
        return max(0.0, min(1.0, v))

    def _recolor_contrast(self):
        if not self.eff:
            return
        res = colorchooser.askcolor(parent=self)
        if not res or not res[0]:
            return
        try:
            shift = float(self.contrast_var.get())
        except ValueError:
            shift = -35
        self.snapshot()
        alt = self.eff.recolor_contrast([int(c) for c in res[0]], shift, self._force(), self.tex_color.get())
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("contrast_done", c="#%02x%02x%02x" % alt))

    def _channels(self, mode):
        if not self.eff:
            return
        a, b = self.ch_a.current(), self.ch_b.current()
        if a == b:
            return
        sc = self.ch_scope.get()
        if sc == "sel":
            m = self.list.selected()
            ms = [m] if m else []
        elif sc == "marked":
            ms = self.list.marked()
        else:
            ms = self.eff.all_minis()
        ms = [m for m in ms if m.color_rows()]
        if not ms:
            messagebox.showinfo(self.t("app_title"), self.t("nothing_marked"))
            return
        self.snapshot()
        for m in ms:
            m.channels(a, b, mode)
        self.changed()

    def _nerf(self, minis):
        if not self.eff:
            return
        if minis is not None and not minis:
            messagebox.showinfo(self.t("app_title"), self.t("nothing_marked"))
            return
        self.snapshot()
        self.config(cursor="watch")
        self.update_idletasks()
        try:
            n, before, after = self.eff.reduce_colors(minis, 16)
        finally:
            self.config(cursor="")
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("nerf_done", n=n, b=before / 1024.0, a=after / 1024.0))

    def _depth_status(self):
        if hasattr(self, "lbl_depth"):
            if self.eff:
                a, b = self.eff.color_depth()
                self.lbl_depth.config(text=self.t("depth", a=a, b=b))
            else:
                self.lbl_depth.config(text="")

    def _color_group(self):
        g = self._combo_group(self.cb_colorgroup)
        if g is not None:
            self.recolor([m for m in self.list.minis if m.group == g])

    # ---- aba parâmetros
    def tab_params(self, nb):
        f = self._tab(nb, "tab_params")
        s = ttk.Frame(f)
        s.pack(fill="x")
        self.info_btn(f, "h_size", self.t("more_info")).pack(anchor="e")
        ttk.Label(s, text=self.t("scale_marked")).pack(side="left")
        self.scale_var = tk.StringVar(value="1.5")
        ttk.Spinbox(s, from_=0.1, to=10, increment=0.1, width=6, textvariable=self.scale_var).pack(side="left", padx=4)
        ttk.Button(s, text=self.t("apply"), command=self._scale).pack(side="left")
        s2 = ttk.Frame(f)
        s2.pack(fill="x", pady=(8, 0))
        ttk.Label(s2, text=self.t("scale_group")).pack(side="left")
        self.cb_scalegroup = ttk.Combobox(s2, state="readonly", width=16)
        self.cb_scalegroup.pack(side="left", padx=4)
        ttk.Label(s2, text="×").pack(side="left")
        self.scale_var2 = tk.StringVar(value="1.5")
        ttk.Spinbox(s2, from_=0.1, to=10, increment=0.1, width=6, textvariable=self.scale_var2).pack(side="left", padx=4)
        ttk.Button(s2, text=self.t("apply"), command=self._scale_group).pack(side="left")
        # padrões de crescimento
        ttk.Separator(f).pack(fill="x", pady=10)
        hdr = ttk.Frame(f)
        hdr.pack(fill="x")
        ttk.Label(hdr, text=self.t("grow_title"), font=("Segoe UI", self.fs(10), "bold")).pack(side="left")
        self.info_btn(hdr, "info_grow", self.t("more_info")).pack(side="right")
        g1 = ttk.Frame(f)
        g1.pack(fill="x", pady=2)
        self.grow_keys = ["turles", "bills"]
        self.cb_grow = ttk.Combobox(g1, state="readonly", width=26, values=[self.t("grow_" + k) for k in self.grow_keys])
        self.cb_grow.current(0)
        self.cb_grow.pack(side="left")
        self.grow_rev = tk.BooleanVar(value=False)
        ttk.Checkbutton(g1, text=self.t("grow_reverse"), variable=self.grow_rev).pack(side="left", padx=6)
        g2 = ttk.Frame(f)
        g2.pack(fill="x", pady=2)
        ttk.Button(g2, text=self.t("grow_marked"), command=lambda: self._grow(None)).pack(side="left", fill="x", expand=True)
        self.cb_growgroup = ttk.Combobox(g2, state="readonly", width=14)
        self.cb_growgroup.pack(side="left", padx=4)
        ttk.Button(g2, text=self.t("grow_group"), command=lambda: self._grow(self._combo_group(self.cb_growgroup))).pack(side="left")
        ttk.Separator(f).pack(fill="x", pady=10)
        ttk.Label(f, text=self.t("params_of"), font=("Segoe UI", self.fs(10), "bold")).pack(anchor="w")
        self.param_box = ttk.Frame(f)
        self.param_box.pack(fill="both", expand=True, pady=6)

    SECTIONS = [("sec_when", ["invoke", "delay_a", "delay_b"], ["h_invoke", "h_delay", "h_delay"]),
                ("sec_behave", ["unk9", "unkA", "unkB"], ["h_b9", "h_bA", "h_bB"]),
                ("sec_dur", ["dur_a", "dur_b"], ["h_dur", "h_dur"]),
                ("sec_size", ["size1", "size2", "size3", "time1", "time2"], ["h_size"] * 5),
                ("sec_where", ["pos_x", "pos_y", "pos_z"], ["h_pos"] * 3),
                ("sec_tex", ["dbt", "tex"], ["h_dbt", "h_tex"]),
                ("sec_unk", ["unk30"], ["h_unk"])]

    def _fill_params(self, m):
        for w in self.param_box.winfo_children():
            w.destroy()
        if m is None:
            ttk.Label(self.param_box, text=self.t("select_one")).pack(anchor="w")
            return
        self.param_vars = {}
        g = ttk.Frame(self.param_box)
        g.pack(fill="x")
        row = 0
        if m.type == 0x00:
            ttk.Label(g, text=self.t("type00_note"), wraplength=self.wrap() - 20, justify="left",
                      foreground="#7a4b00").grid(row=row, column=0, columnspan=3, sticky="w", pady=(0, 6))
            row += 1
        for sec, fields, helps in self.SECTIONS:
            if m.type == 0x00:
                fields_h = [(f, h) for f, h in zip(fields, helps) if f in ("invoke", "delay_a", "delay_b", "dur_a", "dur_b")]
            else:
                fields_h = list(zip(fields, helps))
            if not fields_h:
                continue
            ttk.Label(g, text=self.t(sec), font=("Segoe UI", self.fs(9), "bold")).grid(row=row, column=0, columnspan=3, sticky="w", pady=(6, 1))
            row += 1
            for k, h in fields_h:
                ttk.Label(g, text=self.t("p_" + k)).grid(row=row, column=0, sticky="w", padx=(10, 0))
                v = m.get(k)
                var = tk.StringVar(value=str(v) if k in INT_FIELDS else "%g" % v)
                ttk.Entry(g, textvariable=var, width=12).grid(row=row, column=1, padx=6, pady=1)
                self.info_btn(g, h).grid(row=row, column=2)
                self.param_vars[k] = var
                row += 1
        fh = ttk.Frame(g)
        fh.grid(row=row, column=0, columnspan=3, sticky="ew", pady=(8, 1))
        ttk.Label(fh, text=self.t("sec_flags"), font=("Segoe UI", self.fs(9), "bold")).pack(side="left")
        self.info_btn(fh, "h_flags").pack(side="right")
        row += 1
        self.flag_vars = {}
        b0 = m.param[0]
        for bit in (1, 2, 4, 8, 16, 32, 64, 128):
            v = tk.BooleanVar(value=bool(b0 & bit))
            ttk.Checkbutton(g, text="%d — %s" % (bit, self.t("flag_%d" % bit)), variable=v).grid(row=row, column=0, columnspan=3, sticky="w", padx=(10, 0))
            self.flag_vars[bit] = v
            row += 1
        ttk.Button(g, text=self.t("apply"), command=lambda: self._apply_params(m)).grid(row=row, column=0, columnspan=3, pady=8, sticky="ew")

    def _apply_params(self, m):
        self.snapshot()
        try:
            for k, var in self.param_vars.items():
                v = var.get().replace(",", ".")
                m.set(k, int(float(v)) if k in INT_FIELDS else float(v))
            if getattr(self, "flag_vars", None):
                m.param[0] = sum(bit for bit, var in self.flag_vars.items() if var.get())
        except ValueError as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self.changed()

    def _scale(self):
        ms = [m for m in self.list.marked() if m.type != 0x00]
        if not ms:
            messagebox.showinfo(self.t("app_title"), self.t("nothing_marked"))
            return
        try:
            fac = float(self.scale_var.get().replace(",", "."))
        except ValueError:
            return
        self.snapshot()
        for m in ms:
            m.scale_size(fac)
        self.changed()

    def _grow(self, group):
        if not self.eff:
            return
        ms = self.list.marked() if group is None else [m for m in self.list.minis if m.group == group]
        ms = [m for m in ms if m.type != 0x00]
        if not ms:
            messagebox.showinfo(self.t("app_title"), self.t("nothing_marked"))
            return
        key = self.grow_keys[max(0, self.cb_grow.current())]
        self.snapshot()
        n = sum(1 for m in ms if m.apply_growth(key, self.grow_rev.get()))
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("scaled", n=n))

    def _stripes(self, hide):
        if not self.eff:
            return
        self.snapshot()
        ok = self.eff.hide_stripes(hide)
        self.changed()
        if not ok:
            messagebox.showinfo(self.t("app_title"), self.t("stripes_none"))

    def _scale_group(self):
        g = self._combo_group(self.cb_scalegroup)
        if g is None or not self.eff:
            return
        try:
            fac = float(self.scale_var2.get().replace(",", "."))
        except ValueError:
            return
        ms = [m for m in self.list.minis if m.group == g and m.type != 0x00]
        self.snapshot()
        for m in ms:
            m.scale_size(fac)
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("scaled", n=len(ms)))

    # ---- aba grupos
    def tab_groups(self, nb):
        f = self._tab(nb, "tab_groups")
        self._groups_extra(f)

    def _groups_extra(self, f):
        hdr = ttk.Frame(f)
        hdr.pack(fill="x")
        ttk.Label(hdr, text=self.t("phase_tools"), font=("Segoe UI", self.fs(10), "bold")).pack(side="left")
        self.info_btn(hdr, "info_hide", self.t("more_info")).pack(side="right")
        r = ttk.Frame(f)
        r.pack(fill="x", pady=6)
        ttk.Label(r, text=self.t("group_or_phase")).pack(side="left")
        self.cb_hidegroup = ttk.Combobox(r, state="readonly", width=18)
        self.cb_hidegroup.pack(side="left", padx=4)
        self.hide_method = tk.StringVar(value="alpha")
        ttk.Radiobutton(f, text=self.t("hide_alpha"), value="alpha", variable=self.hide_method).pack(anchor="w")
        ttk.Radiobutton(f, text=self.t("hide_size"), value="size", variable=self.hide_method).pack(anchor="w")
        b = ttk.Frame(f)
        b.pack(fill="x", pady=6)
        ttk.Button(b, text=self.t("hide_group"), command=lambda: self._group_action("hide")).pack(side="left", fill="x", expand=True)
        ttk.Button(b, text=self.t("remove_group"), command=lambda: self._group_action("remove")).pack(side="left", fill="x", expand=True, padx=(4, 0))

    def _group_action(self, action):
        g = self._combo_group(self.cb_hidegroup)
        if g is None or not self.eff:
            return
        ms = [m for m in self.list.minis if m.group == g]
        if action == "hide":
            self.hide_minis(ms)
        else:
            self._remove(ms)

    def hide_minis(self, ms):
        ms = [m for m in ms if m.type != 0x00]
        if not ms:
            messagebox.showinfo(self.t("app_title"), self.t("nothing_marked"))
            return
        method = self.hide_method.get() if hasattr(self, "hide_method") else "alpha"
        self.snapshot()
        skipped = sum(1 for m in ms if not m.hide(method))
        self.changed()
        msg = self.t("hidden", n=len(ms) - skipped)
        if skipped:
            msg += "\n" + self.t("hidden_skip", n=skipped)
        messagebox.showinfo(self.t("ok"), msg)

    def _set_group(self):
        txt = self.cb_setgroup.get().strip()
        if not txt:
            return
        key = next((g for g in PRESET_GROUPS if group_label(g, self.lang) == txt), txt)
        ms = self.list.marked()
        if not ms:
            messagebox.showinfo(self.t("app_title"), self.t("nothing_marked"))
            return
        self.snapshot()
        for m in ms:
            m.group = key
        self.changed()

    # ---- aba combinar
    def tab_combine(self, nb):
        f = self._tab(nb, "tab_combine")
        ttk.Label(f, text=self.t("combine_hint"), wraplength=self.wrap(), justify="left").pack(anchor="w")
        self.info_btn(f, "info_phases", self.t("what_phases")).pack(anchor="e", pady=(2, 8))
        ttk.Button(f, text=self.t("src_open"), command=self.open_source).pack(fill="x")
        self.lbl_src = ttk.Label(f, text="")
        self.lbl_src.pack(anchor="w", pady=4)
        # controles de aplicar ficam embaixo e sempre visíveis
        bottom = ttk.Frame(f)
        bottom.pack(side="bottom", fill="x")
        self.rep_mode = tk.StringVar(value=self.cfg.get("rep_mode", "phase"))
        ttk.Radiobutton(bottom, text=self.t("rep_phase"), value="phase", variable=self.rep_mode).pack(anchor="w")
        r2 = ttk.Frame(bottom)
        r2.pack(fill="x")
        ttk.Radiobutton(r2, text=self.t("rep_group"), value="group", variable=self.rep_mode).pack(side="left")
        self.cb_replace = ttk.Combobox(r2, state="readonly", width=16)
        self.cb_replace.pack(side="left", padx=4)
        ttk.Radiobutton(bottom, text=self.t("rep_add"), value="add", variable=self.rep_mode).pack(anchor="w")
        r3 = ttk.Frame(bottom)
        r3.pack(fill="x", pady=(4, 0))
        ttk.Label(r3, text=self.t("import_phase")).pack(side="left")
        self.cb_phase = ttk.Combobox(r3, state="readonly", width=16,
                                     values=[self.t("keep")] + [group_label("phase%d" % i, self.lang) for i in range(6)])
        self.cb_phase.current(0)
        self.cb_phase.pack(side="left", padx=4)
        ttk.Button(bottom, text=self.t("import_marked"), command=self.import_marked).pack(fill="x", pady=(8, 0), ipady=4)
        r = ttk.Frame(f)
        r.pack(fill="x")
        ttk.Button(r, text=self.t("mark_all"), command=lambda: self.srclist.set_all(True)).pack(side="left")
        ttk.Button(r, text=self.t("unmark_all"), command=lambda: self.srclist.set_all(False)).pack(side="left", padx=4)
        chips_holder = ttk.Frame(f)
        chips_holder.pack(fill="x", pady=4)
        self.srclist = MiniList(f, self)
        self.srclist.tree.configure(height=10)
        self.srclist.pack(fill="both", expand=True, pady=4)
        self.srclist.headings()
        self.src_chips = GroupChips(chips_holder, self, self.srclist, per_row=3)
        self.src_chips.pack(fill="x")
        if self.src:
            self.srclist.fill(self.src)
            self.src_chips.rebuild()
            self.lbl_src.config(text=self.t("source") + ": " + os.path.basename(self.src_path or ""))

    def open_source(self):
        p = filedialog.askopenfilename(filetypes=[("PAK", "*.pak"), ("*", "*.*")], parent=self)
        if not p:
            return
        try:
            self.src = Effect.load(p)
            self._load_groups(self.src, p)
        except (PakError, OSError) as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self.src_path = p
        self.lbl_src.config(text=self.t("source") + ": " + os.path.basename(p))
        self.srclist.fill(self.src)
        self.src_chips.rebuild()
        self._refresh_combos()

    def import_marked(self):
        if not self.eff or not self.src:
            return
        ms = [m for m in self.srclist.marked() if m.type != 0x00]
        if not ms:
            messagebox.showinfo(self.t("app_title"), self.t("nothing_marked"))
            return
        self.snapshot()
        ph = self.cb_phase.current()
        mode = self.rep_mode.get()
        self.cfg["rep_mode"] = mode
        self._save_cfg()
        removed = []
        if mode == "phase":
            phases = {ph - 1} if ph > 0 else set(m.get("invoke") for m in ms)
            removed = [m for m in self.eff.all_minis() if m.type != 0x00 and m.get("invoke") in phases]
        elif mode == "group":
            rg = self._combo_group(self.cb_replace)
            if rg is not None:
                removed = [m for m in self.eff.all_minis() if m.group == rg and m.type != 0x00]
        if removed:
            self.eff.remove_minis(removed)
        sig = self.eff.phase_signature(ph - 1) if ph > 0 else None
        added = self.eff.import_minis(self.src, ms)
        if ph > 0:
            for m in added:
                m.move_to_phase(ph - 1, sig)
                m.group = "impact" if m.hits else "phase%d" % (ph - 1)
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("imported2", n=len(added), r=len(removed)))
        return
        messagebox.showinfo(self.t("ok"), self.t("imported", n=len(added)))

    # ---- aba comportamento
    def tab_behavior(self, nb):
        f = self._tab(nb, "tab_behavior")
        self.info_btn(f, "info_behavior", self.t("more_info")).pack(anchor="e")
        r = ttk.Frame(f)
        r.pack(fill="x", pady=4)
        ttk.Label(r, text=self.t("beh_model")).pack(side="left")
        self.tree_button(r, "modelos", self._load_beh_name).pack(side="left", padx=4)
        ttk.Button(f, text=self.t("beh_browse"), command=self._browse_beh).pack(anchor="w")
        self.lbl_beh = ttk.Label(f, text="", wraplength=self.wrap(), justify="left")
        self.lbl_beh.pack(anchor="w", pady=10)
        self.beh_launch = tk.BooleanVar(value=True)
        self.beh_recolor = tk.BooleanVar(value=True)
        self.beh_header = tk.BooleanVar(value=True)
        self.beh_scene = tk.BooleanVar(value=True)
        self.beh_mode = tk.StringVar(value="shape")
        ttk.Radiobutton(f, text=self.t("beh_mode_shape"), value="shape", variable=self.beh_mode).pack(anchor="w")
        ttk.Radiobutton(f, text=self.t("beh_mode_only"), value="only", variable=self.beh_mode).pack(anchor="w", pady=(0, 6))
        ttk.Checkbutton(f, text=self.t("beh_opt_hits"), state="disabled", variable=tk.BooleanVar(value=True)).pack(anchor="w")
        ttk.Checkbutton(f, text=self.t("beh_opt_launch"), variable=self.beh_launch).pack(anchor="w")
        ttk.Checkbutton(f, text=self.t("beh_opt_header"), variable=self.beh_header).pack(anchor="w")
        ttk.Checkbutton(f, text=self.t("beh_opt_color"), variable=self.beh_recolor).pack(anchor="w", pady=(0, 8))
        ttk.Checkbutton(f, text=self.t("beh_opt_scene"), variable=self.beh_scene).pack(anchor="w")
        bb = ttk.Frame(f)
        bb.pack(fill="x", pady=(4, 4))
        self.lbl_barrage = ttk.Label(bb, text="")
        self.lbl_barrage.pack(side="left")
        ttk.Button(bb, text=self.t("barrage_on"), command=lambda: self._barrage(True)).pack(side="left", padx=4)
        ttk.Button(bb, text=self.t("barrage_off"), command=lambda: self._barrage(False)).pack(side="left")
        self.info_btn(bb, "info_barrage").pack(side="left", padx=4)
        st = ttk.Frame(f)
        st.pack(fill="x", pady=(2, 6))
        ttk.Button(st, text=self.t("stripes_hide"), command=lambda: self._stripes(True)).pack(side="left", fill="x", expand=True)
        ttk.Button(st, text=self.t("stripes_show"), command=lambda: self._stripes(False)).pack(side="left", fill="x", expand=True, padx=4)
        self.info_btn(st, "info_stripes").pack(side="left")
        ttk.Button(st, text="🖼", width=3, command=lambda: self.show_image("info:stripes", self.t("stripes_hide"))).pack(side="left", padx=2)
        ttk.Button(f, text=self.t("beh_apply"), command=self._apply_beh).pack(fill="x")
        # formatos pré-disparo
        ttk.Separator(f).pack(fill="x", pady=12)
        hdr = ttk.Frame(f)
        hdr.pack(fill="x")
        ttk.Label(hdr, text=self.t("pre_title"), font=("Segoe UI", self.fs(10), "bold")).pack(side="left")
        self.info_btn(hdr, "info_pre", self.t("more_info")).pack(side="right")
        pr = ttk.Frame(f)
        pr.pack(fill="x", pady=4)
        self.pre_choice = None
        self.tree_button(pr, "pre_disparo", self._pick_pre).pack(side="left")
        ttk.Button(f, text=self.t("pre_apply"), command=self._apply_pre).pack(fill="x", pady=4)
        self._beh_summary()

    def _browse_beh(self):
        p = filedialog.askopenfilename(filetypes=[("PAK", "*.pak"), ("*", "*.*")], parent=self)
        if p:
            self._load_beh(p)

    def _barrage(self, on):
        if not self.eff:
            return
        self.snapshot()
        self.eff.set_barrage(on, in_scene=self.eff.header[0x27] == 3 and on)
        self.changed()

    def _apply_pre(self):
        if not self.eff or not self.pre_choice:
            return
        try:
            pre = Effect.from_bytes(RES.get("pre_disparo", self.pre_choice))
        except (PakError, TypeError) as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self.snapshot()
        added, color = self.eff.apply_prelaunch(pre, recolor=self.beh_recolor.get())
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("pre_done", n=len(added)))

    WARNINGS = (("Cortes de Espada", "warn_magic344"), ("Cortes Trunks", "warn_magic344"),
                ("Espada de Ki", "warn_params"), ("Paralisia General Blue", "warn_scene_only"))

    def _warn_for(self, name):
        for key, msg in self.WARNINGS:
            if key in name:
                messagebox.showwarning(self.t("app_title"), self.t(msg))
                return

    def _pick_pre(self, name):
        self.pre_choice = name
        self._warn_for(name)

    def _load_beh_name(self, name):
        self._warn_for(name)
        try:
            self.beh_tpl, self.beh_tpl_path = Effect.from_bytes(RES.get("modelos", name)), name
        except (PakError, TypeError) as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self._beh_summary()

    def _load_beh(self, p):
        try:
            self.beh_tpl, self.beh_tpl_path = Effect.load(p), p
        except (PakError, OSError) as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self._beh_summary()

    def _describe_hits(self, eff):
        hs = eff.behavior_summary() if eff else []
        if not hs:
            return self.t("beh_none"), ""
        desc = ", ".join("%02X/inv %d" % (m.type, m.get("invoke")) for m in hs)
        bits = sorted(set(m.get("invoke") for m in hs))
        b = ", ".join({4: "00100000", 5: "01000000"}[i] for i in bits)
        return desc, b

    def _beh_summary(self):
        if not hasattr(self, "lbl_beh"):
            return
        lines = []
        if self.eff:
            d, _ = self._describe_hits(self.eff)
            lines.append(self.t("beh_current") + " " + d)
        if self.beh_tpl:
            d, b = self._describe_hits(self.beh_tpl)
            lines.append("")
            lines.append(os.path.basename(self.beh_tpl_path))
            lines.append(self.t("beh_tpl") + " " + d)
            if b:
                lines.append(self.t("beh_bits", b=b))
        self.lbl_beh.config(text="\n".join(lines))

    def _apply_beh(self):
        if not self.eff or not self.beh_tpl:
            return
        if not self.beh_tpl.all_minis():
            self.snapshot()
            ok = self.eff.copy_scene(self.beh_tpl)
            self.changed()
            messagebox.showinfo(self.t("ok"), self.t("scene_copied") if ok else self.t("scene_empty"))
            return
        self.snapshot()
        scene_copied = self.beh_scene.get() and self.beh_mode.get() != "only" and self.eff.copy_scene(self.beh_tpl)
        added, color = self.eff.apply_behavior(self.beh_tpl, launch=self.beh_launch.get(), recolor=self.beh_recolor.get(),
                                                 header=self.beh_header.get(),
                                                 keep_shape=self.beh_mode.get() == "only")
        self.changed()
        msg = self.t("beh_done_only", n=len(added), p=self.eff.launch_phase()) if self.beh_mode.get() == "only" \
            else self.t("beh_done2", n=len(added))
        if color:
            msg += "\n" + self.t("painted", c="#%02x%02x%02x" % color)
        if scene_copied:
            msg += "\n" + self.t("scene_copied")
        messagebox.showinfo(self.t("ok"), msg)

    # ---- aba cena ao acertar
    SCENE_PRESETS = [("none", None), ("ground", "chao.bin"), ("air", "ar.bin")]

    def _scene_data(self, fname):
        return RES.get("cenas", fname)

    def tab_scene(self, nb):
        f = self._tab(nb, "tab_scene")
        self.info_btn(f, "info_scene", self.t("more_info")).pack(anchor="e")
        self.lbl_scene = ttk.Label(f, text="", font=("Segoe UI", self.fs(10), "bold"))
        self.lbl_scene.pack(anchor="w", pady=(0, 8))
        self.scene_var = tk.StringVar(value="")
        for key, fname in self.SCENE_PRESETS:
            ok = fname is None or self._scene_data(fname) is not None
            rb = ttk.Radiobutton(f, text=self.t("scene_" + key) + ("" if ok else "  " + self.t("scene_missing")),
                                 value=key, variable=self.scene_var, state="normal" if ok else "disabled")
            rb.pack(anchor="w", pady=2)
        ttk.Button(f, text=self.t("apply"), command=self._apply_scene).pack(fill="x", pady=8)
        ttk.Separator(f).pack(fill="x", pady=6)
        ttk.Button(f, text=self.t("scene_copy"), command=self._copy_scene).pack(fill="x")
        r = ttk.Frame(f)
        r.pack(fill="x", pady=(8, 0))
        ttk.Label(r, text=self.t("scene_save_as")).pack(side="left")
        ttk.Button(r, text=self.t("scene_ground"), command=lambda: self._save_scene("chao.bin")).pack(side="left", padx=4)
        ttk.Button(r, text=self.t("scene_air"), command=lambda: self._save_scene("ar.bin")).pack(side="left")
        ttk.Button(f, text=self.t("scene_table_btn"), command=self._scene_table).pack(fill="x", pady=(8, 0))
        # como o golpe aparece na ceninha (bytes 0x21-0x27 do 03.dat)
        ttk.Separator(f).pack(fill="x", pady=12)
        hdr = ttk.Frame(f)
        hdr.pack(fill="x")
        ttk.Label(hdr, text=self.t("appear_title"), font=("Segoe UI", self.fs(10), "bold")).pack(side="left")
        self.info_btn(hdr, "info_appear", self.t("more_info")).pack(side="right")
        self.appear_var = tk.StringVar(value="none")
        for k in ("none", "beam", "projectile", "vertical"):
            ttk.Radiobutton(f, text=self.t("appear_" + k), value=k, variable=self.appear_var).pack(anchor="w")
        self.appear_barrage = tk.BooleanVar(value=False)
        ttk.Checkbutton(f, text=self.t("appear_barrage"), variable=self.appear_barrage).pack(anchor="w", pady=(4, 0))
        ttk.Button(f, text=self.t("apply"), command=self._apply_appear).pack(fill="x", pady=6)
        # grupo 01 durante a ceninha
        ttk.Separator(f).pack(fill="x", pady=8)
        hdr = ttk.Frame(f)
        hdr.pack(fill="x")
        ttk.Label(hdr, text=self.t("persist_scene_title"), font=("Segoe UI", self.fs(10), "bold")).pack(side="left")
        self.info_btn(hdr, "info_persist_scene", self.t("more_info")).pack(side="right")
        pr = ttk.Frame(f)
        pr.pack(fill="x", pady=4)
        ttk.Button(pr, text=self.t("persist_scene_on"), command=lambda: self._scene_persist(True)).pack(side="left", fill="x", expand=True)
        ttk.Button(pr, text=self.t("persist_scene_off"), command=lambda: self._scene_persist(False)).pack(side="left", fill="x", expand=True, padx=(4, 0))
        # explosão (Vfx 5)
        ttk.Separator(f).pack(fill="x", pady=12)
        hdr = ttk.Frame(f)
        hdr.pack(fill="x")
        ttk.Label(hdr, text=self.t("expl_title"), font=("Segoe UI", self.fs(10), "bold")).pack(side="left")
        self.info_btn(hdr, "info_expl", self.t("more_info")).pack(side="right")
        cr = ttk.Frame(f)
        cr.pack(fill="x", pady=6)
        ttk.Label(cr, text=self.t("dominant")).pack(side="left")
        self.sw_dom = tk.Label(cr, width=4, relief="solid", bd=1)
        self.sw_dom.pack(side="left", padx=6)
        self.lbl_dom = ttk.Label(cr, text="")
        self.lbl_dom.pack(side="left")
        self.expl_recolor = tk.BooleanVar(value=True)
        ttk.Checkbutton(f, text=self.t("expl_color"), variable=self.expl_recolor).pack(anchor="w")
        ttk.Button(f, text=self.t("expl_add"), command=self._add_explosion,
                   state="normal" if RES.get("extras", EXPLOSION) else "disabled").pack(fill="x", pady=6)
        self._scene_status()

    def _scene_status(self):
        if not hasattr(self, "lbl_scene"):
            return
        if not self.eff:
            self.lbl_scene.config(text="")
            return
        cur = self.eff.pre[2] if len(self.eff.pre) > 2 else b""
        state = "custom"
        if not cur:
            state = "none"
        else:
            for key, fname in self.SCENE_PRESETS:
                if fname and self._scene_data(fname) == cur:
                    state = key
        self.lbl_scene.config(text=self.t("scene_current") + " " + self.t("scene_" + state))
        ap = self.eff.scene_appear()
        self.appear_var.set(ap if ap != "custom" else "")
        self.appear_barrage.set(self.eff.header[0x27] == 3)
        dom = self.eff.dominant_color()
        if dom:
            hx = "#%02x%02x%02x" % dom
            self.sw_dom.config(bg=hx)
            self.lbl_dom.config(text=hx)
        else:
            self.lbl_dom.config(text="—")
        self.scene_var.set(state if state != "custom" else "")

    def _apply_scene(self):
        if not self.eff:
            return
        key = self.scene_var.get()
        data = b""
        for k, fname in self.SCENE_PRESETS:
            if k == key and fname:
                data = self._scene_data(fname)
                if data is None:
                    return
        if key not in dict(self.SCENE_PRESETS):
            return
        self.snapshot()
        self.eff.pre[2] = data
        self.changed()

    def _apply_appear(self):
        if not self.eff:
            return
        want_barrage = self.appear_barrage.get()
        if want_barrage and not self.eff.is_barrage():
            if not messagebox.askyesno(self.t("app_title"), self.t("appear_need_barrage")):
                return
        self.snapshot()
        self.eff.set_scene_appear(self.appear_var.get())
        if want_barrage:
            self.eff.set_barrage(True, in_scene=True)
        elif self.eff.header[0x27] == 3:
            self.eff.header[0x27] = 2
        self.changed()

    def _scene_persist(self, on):
        if not self.eff:
            return
        self.snapshot()
        n = self.eff.scene_persist(on)
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("persist_scene_done", n=n))

    def _scene_table(self):
        if not self.eff or len(self.eff.pre) < 3:
            return
        w = tk.Toplevel(self)
        w.title(self.t("scene_table_btn"))
        w.transient(self)
        box = ttk.Frame(w, padding=10)
        box.pack(fill="both", expand=True)
        ttk.Label(box, text=self.t("scene_table_hint"), wraplength=460, justify="left").grid(row=0, column=0, columnspan=4, sticky="w")
        ttk.Label(box, text=self.t("scene_map")).grid(row=1, column=0, sticky="w", pady=6)
        cb = ttk.Combobox(box, state="readonly", values=["%02d - %s" % (i, MAP_NAMES[i]) for i in range(SCENE_MAPS)], width=28)
        cb.current(0)
        cb.grid(row=1, column=1, sticky="w")
        vars_ = []
        ttk.Label(box, text=self.t("scene_event")).grid(row=2, column=0)
        ttk.Label(box, text=self.t("scene_y")).grid(row=2, column=1)
        ttk.Label(box, text=self.t("scene_z")).grid(row=2, column=2)
        for ev in range(SCENE_EVENTS):
            vy, vz = tk.StringVar(), tk.StringVar()
            ttk.Label(box, text=str(ev + 1)).grid(row=3 + ev, column=0)
            ttk.Entry(box, textvariable=vy, width=10).grid(row=3 + ev, column=1, padx=2, pady=1)
            ttk.Entry(box, textvariable=vz, width=10).grid(row=3 + ev, column=2, padx=2, pady=1)
            vars_.append((vy, vz))

        def load(_=None):
            tab = scene_table(self.eff.pre[2] or bytes(2816))
            mp = cb.current()
            for ev, (vy, vz) in enumerate(vars_):
                _, _, y, z = tab[mp * SCENE_EVENTS + ev]
                vy.set("%g" % y)
                vz.set("%g" % z)
        cb.bind("<<ComboboxSelected>>", load)

        def apply(all_maps=False):
            try:
                vals = [(float(vy.get().replace(",", ".")), float(vz.get().replace(",", "."))) for vy, vz in vars_]
            except ValueError as ex:
                messagebox.showerror(self.t("err"), str(ex), parent=w)
                return
            self.snapshot()
            data = self.eff.pre[2] or bytes(2816)
            for mp in (range(SCENE_MAPS) if all_maps else [cb.current()]):
                for ev, (y, z) in enumerate(vals):
                    data = scene_set(data, mp, ev, y, z)
            self.eff.pre[2] = data
            self.changed()
        br = ttk.Frame(box)
        br.grid(row=9, column=0, columnspan=4, sticky="ew", pady=8)
        ttk.Button(br, text=self.t("scene_apply_map"), command=apply).pack(side="left", fill="x", expand=True)
        ttk.Button(br, text=self.t("scene_apply_all"), command=lambda: apply(True)).pack(side="left", fill="x", expand=True, padx=4)
        load()

    def _add_explosion(self):
        if not self.eff:
            return
        try:
            ex = Effect.from_bytes(RES.get("extras", EXPLOSION))
        except (PakError, OSError, TypeError) as e:
            messagebox.showerror(self.t("err"), str(e))
            return
        if not self.eff.pre[2] and not messagebox.askyesno(self.t("app_title"), self.t("expl_noscene")):
            return
        self.snapshot()
        added, color = self.eff.add_explosion(ex, recolor=self.expl_recolor.get())
        self.changed()
        msg = self.t("expl_done", n=len(added))
        if color:
            msg += "\n" + self.t("painted", c="#%02x%02x%02x" % color)
        messagebox.showinfo(self.t("ok"), msg)

    def _copy_scene(self):
        if not self.eff:
            return
        p = filedialog.askopenfilename(filetypes=[("PAK", "*.pak"), ("*", "*.*")], parent=self)
        if not p:
            return
        try:
            data = Effect.load(p).pre[2]
        except (PakError, OSError) as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self.snapshot()
        self.eff.pre[2] = data
        self.changed()

    def _save_scene(self, fname):
        if not self.eff or not self.eff.pre[2]:
            messagebox.showinfo(self.t("app_title"), self.t("scene_empty"))
            return
        os.makedirs(SCENES, exist_ok=True)
        with open(os.path.join(SCENES, fname), "wb") as fh:
            fh.write(self.eff.pre[2])
        self.build_ui()

    # ---- peso
    def show_weight(self):
        if not self.eff:
            return
        lines = [self.t("w_total", kb=len(self.eff.to_bytes()) / 1024.0), ""]
        rows = []
        for c in self.eff.cats:
            for i, d in enumerate(c.dbts):
                users = [m for m in c.minis if m.get("dbt") == i]
                gs = sorted(set(group_label(m.group, self.lang) for m in users))
                rows.append((len(d), "  DBT %02X/%d — %.1f KB — %d mini — %s" % (c.type, i, len(d) / 1024.0, len(users), ", ".join(gs))))
        dbt_total = sum(r[0] for r in rows)
        other = sum(len(f) for m in self.eff.all_minis() for f in m.files)
        lines.append(self.t("w_dbt", kb=dbt_total / 1024.0))
        lines += [r[1] for r in sorted(rows, reverse=True)]
        lines += ["", self.t("w_other", kb=other / 1024.0), self.t("w_pre", kb=sum(len(x) for x in self.eff.pre) / 1024.0),
                  "", self.t("w_tip"), "", self.t("w_scene_tip") if len(self.eff.pre) > 2 and self.eff.pre[2] else ""]
        w = tk.Toplevel(self)
        w.title(self.t("w_title"))
        txt = tk.Text(w, wrap="word", width=80, height=26, font=("Consolas", self.fs(9)), padx=10, pady=10)
        txt.insert("1.0", "\n".join(lines))
        txt.config(state="disabled")
        txt.pack(fill="both", expand=True)
        ttk.Button(w, text=self.t("close"), command=w.destroy).pack(pady=6)

    # ---- aba extras
    def _extras_list(self):
        return RES.extras_manifest()

    def _extra_tag(self, x):
        return "extra:%s:%s" % (x.get("kind", "x"), x.get("slot", "launch"))

    def tab_extras(self, nb):
        f = self._tab(nb, "tab_extras")
        self.info_btn(f, "info_extras", self.t("more_info")).pack(anchor="e")
        ttk.Label(f, text=self.t("extras_hint"), wraplength=self.wrap(), justify="left").pack(anchor="w", pady=(0, 8))
        self.extra_vars = {}
        self.extra_widgets = {}
        items = self._extras_list()
        for slot in (("aura", "charge", "pair") if self._ui_kind == "aura" else ("aura", "charge", "pair", "launch")):
            ttk.Label(f, text=self.t("slot_" + slot), font=("Segoe UI", self.fs(10), "bold")).pack(anchor="w", pady=(6, 2))
            found = False
            for x in items:
                if x.get("slot") != slot:
                    continue
                found = True
                v = tk.BooleanVar(value=False)
                tag = self._extra_tag(x)
                row = ttk.Frame(f)
                row.pack(anchor="w", padx=12, fill="x")
                label = self.t("kind_" + x.get("kind", "x"))
                if x.get("requires") == "beam":
                    label += "  " + self.t("needs_beam")
                cbw = ttk.Checkbutton(row, text=label, variable=v)
                cbw.pack(side="left")
                if self.has_image("extras:" + tag[6:]):
                    ttk.Button(row, text="🖼", width=3,
                               command=lambda t=tag, l=label: self.show_image("extras:" + t[6:], l)).pack(side="left", padx=4)
                self.extra_vars[tag] = (v, x)
                self.extra_widgets[tag] = cbw
            if not found:
                ttk.Label(f, text="—").pack(anchor="w", padx=12)
        self.extra_recolor = tk.BooleanVar(value=True)
        ttk.Checkbutton(f, text=self.t("expl_color"), variable=self.extra_recolor).pack(anchor="w", pady=(10, 0))
        ttk.Button(f, text=self.t("extras_apply"), command=self._apply_extras).pack(fill="x", pady=8)
        self._extras_status()

    def _extras_status(self):
        if not hasattr(self, "extra_vars"):
            return
        present = set(m.group for m in self.eff.all_minis()) if self.eff else set()
        has_beam = bool(self.eff) and any(m.type == 0x11 for m in self.eff.all_minis())
        for tag, (v, x) in self.extra_vars.items():
            v.set(tag in present)
            wdg = self.extra_widgets.get(tag)
            if wdg is not None and x.get("requires") == "beam":
                wdg.config(state="normal" if has_beam or tag in present else "disabled")

    def _apply_extras(self):
        if not self.eff:
            return
        want = {tag: v.get() for tag, (v, x) in self.extra_vars.items()}
        for tag, (v, x) in self.extra_vars.items():      # um extra que já inclui outro desliga o outro
            if want.get(tag):
                for cov in x.get("covers", []):
                    if cov in want:
                        want[cov] = False
                        self.extra_vars[cov][0].set(False)
        present = set(m.group for m in self.eff.all_minis())
        todo = [(tag, on, self.extra_vars[tag][1]) for tag, on in want.items() if on != (tag in present)]
        if not todo:
            return
        self.snapshot()
        added = removed = 0
        for tag, on, x in sorted(todo, key=lambda t: t[1]):   # remove antes de adicionar
            if on:
                try:
                    ex = Effect.from_bytes(RES.get("extras", x["file"]))
                except (PakError, OSError, TypeError) as e:
                    messagebox.showerror(self.t("err"), str(e))
                    continue
                added += len(self.eff.add_extra(ex, x.get("slot", "launch"), tag, recolor=self.extra_recolor.get(),
                                                src_lp=int(x.get("src_lp", 1)), to_charge=bool(x.get("to_charge"))))
            else:
                removed += self.eff.remove_extra(tag)
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("extras_done", a=added, r=removed, p=self.eff.launch_phase()))

    # ---- aba formato da aura (arquivos 01_charge_aura.pak)
    def tab_aura(self, nb):
        f = self._tab(nb, "tab_aura")
        self.info_btn(f, "info_aura", self.t("more_info")).pack(anchor="e")
        if self._ui_kind == "support":
            tk.Label(f, text=self.t("aura_on_support_warn"), fg="#b00020", wraplength=self.wrap(), justify="left").pack(anchor="w", pady=(0, 6))
        ttk.Label(f, text=self.t("aura_hint"), wraplength=self.wrap(), justify="left").pack(anchor="w", pady=(0, 8))
        self.aura_files = RES.list("auras")
        r = ttk.Frame(f)
        r.pack(fill="x", pady=4)
        ttk.Label(r, text=self.t("aura_model")).pack(side="left")
        self.cb_aura = ttk.Combobox(r, state="readonly", width=28, values=[os.path.splitext(x)[0] for x in self.aura_files])
        ttk.Button(r, text="🖼", width=3, command=lambda: self.cb_aura.current() >= 0 and self.show_image(
            "auras/" + self.aura_files[self.cb_aura.current()], self.cb_aura.get())).pack(side="right")
        self.cb_aura.pack(side="left", padx=4)
        self.aura_recolor = tk.BooleanVar(value=True)
        ttk.Checkbutton(f, text=self.t("aura_keep_color"), variable=self.aura_recolor).pack(anchor="w")
        ttk.Button(f, text=self.t("aura_apply"), command=self._apply_aura).pack(fill="x", pady=8)

    def _apply_aura(self):
        if not self.eff or self.cb_aura.current() < 0:
            return
        try:
            tpl = Effect.from_bytes(RES.get("auras", self.aura_files[self.cb_aura.current()]))
        except (PakError, TypeError) as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self.snapshot()
        new, color = self.eff.swap_aura(tpl, recolor=self.aura_recolor.get(), force=self._force())
        self.eff = new
        self.changed()
        msg = self.t("aura_done")
        if color:
            msg += "\n" + self.t("painted", c="#%02x%02x%02x" % color)
        messagebox.showinfo(self.t("ok"), msg)

    # ---- aba suporte / skills (00_skill_001, 01_skill_002, 00_effect_skill_1, 01_effect_skill_2)
    MOVING_REF = "Paralisia Hitto (móvel).pak"

    def tab_support(self, nb):
        f = self._tab(nb, "tab_support")
        self.info_btn(f, "info_support", self.t("more_info")).pack(anchor="e")
        ttk.Label(f, text=self.t("support_hint"), wraplength=self.wrap(), justify="left").pack(anchor="w", pady=(0, 8))
        r = ttk.Frame(f)
        r.pack(fill="x", pady=4)
        ttk.Label(r, text=self.t("aura_model")).pack(side="left")
        self.sup_choice = None
        self.tree_button(r, "suportes", lambda n: setattr(self, "sup_choice", n), width=30).pack(side="left", padx=4)
        self.sup_recolor = tk.BooleanVar(value=True)
        ttk.Checkbutton(f, text=self.t("aura_keep_color"), variable=self.sup_recolor).pack(anchor="w")
        ttk.Button(f, text=self.t("support_apply"), command=self._apply_support).pack(fill="x", pady=8)

    def _apply_support(self):
        if not self.eff or not self.sup_choice:
            return
        try:
            tpl = Effect.from_bytes(RES.get("suportes", self.sup_choice))
        except (PakError, TypeError) as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self.snapshot()
        new, color = self.eff.swap_content(tpl, recolor=self.sup_recolor.get(), force=self._force())
        self.eff = new
        self.changed()
        msg = self.t("support_done")
        if color:
            msg += "\n" + self.t("painted", c="#%02x%02x%02x" % color)
        messagebox.showinfo(self.t("ok"), msg)

    # ---- aba parâmetros de suporte
    MOVING_REF = "Paralisias/Paralisia Hitto (móvel).pak"

    def tab_support_params(self, nb):
        f = self._tab(nb, "tab_sparams")
        ttk.Label(f, text=self.t("sparams_hint"), wraplength=self.wrap(), justify="left").pack(anchor="w", pady=(0, 6))
        # 1) disparar até o adversário
        hdr = ttk.Frame(f)
        hdr.pack(fill="x")
        ttk.Label(hdr, text=self.t("goto_title"), font=("Segoe UI", self.fs(10), "bold")).pack(side="left")
        self.info_btn(hdr, "info_goto", self.t("more_info")).pack(side="right")
        self.goto_attach = tk.BooleanVar(value=True)
        self.goto_zero = tk.BooleanVar(value=True)
        self.goto_impact = tk.BooleanVar(value=False)
        self.goto_hits = tk.BooleanVar(value=False)
        for var, key in ((self.goto_attach, "goto_attach"), (self.goto_zero, "goto_zero"),
                         (self.goto_impact, "goto_impact"), (self.goto_hits, "goto_hits")):
            ttk.Checkbutton(f, text=self.t(key), variable=var).pack(anchor="w")
        ttk.Button(f, text=self.t("goto_apply"), command=self._go_to_opponent,
                   state="normal" if RES.get("suportes", self.MOVING_REF) else "disabled").pack(fill="x", pady=6)
        # 2) ficar até usar especial
        ttk.Separator(f).pack(fill="x", pady=8)
        hdr = ttk.Frame(f)
        hdr.pack(fill="x")
        ttk.Label(hdr, text=self.t("persist_title"), font=("Segoe UI", self.fs(10), "bold")).pack(side="left")
        self.info_btn(hdr, "info_persist", self.t("more_info")).pack(side="right")
        pr = ttk.Frame(f)
        pr.pack(fill="x")
        self.persist_all = tk.BooleanVar(value=True)
        ttk.Checkbutton(pr, text=self.t("opa_all"), variable=self.persist_all).pack(side="left")
        self.persist_ph = {}
        for p in range(6):
            v = tk.BooleanVar(value=False)
            ttk.Checkbutton(pr, text=str(p), variable=v).pack(side="left")
            self.persist_ph[p] = v
        br = ttk.Frame(f)
        br.pack(fill="x", pady=4)
        ttk.Button(br, text=self.t("persist_on"), command=lambda: self._persist(True)).pack(side="left", fill="x", expand=True)
        ttk.Button(br, text=self.t("persist_off"), command=lambda: self._persist(False)).pack(side="left", fill="x", expand=True, padx=(4, 0))
        # 3) parâmetros de cada suporte (cabeçalho)
        ttk.Separator(f).pack(fill="x", pady=8)
        hdr = ttk.Frame(f)
        hdr.pack(fill="x")
        ttk.Label(hdr, text=self.t("hdr_title"), font=("Segoe UI", self.fs(10), "bold")).pack(side="left")
        self.info_btn(hdr, "info_hdr", self.t("more_info")).pack(side="right")
        r = ttk.Frame(f)
        r.pack(fill="x", pady=4)
        ttk.Label(r, text=self.t("hdr_from")).pack(side="left")
        self.tree_button(r, "suportes", self._hdr_from, width=28).pack(side="left", padx=4)
        self.hdr_box = ttk.Frame(f)
        self.hdr_box.pack(fill="x")
        self._fill_hdr()

    def _fill_hdr(self):
        if not hasattr(self, "hdr_box"):
            return
        for w in self.hdr_box.winfo_children():
            w.destroy()
        if not self.eff:
            return
        import struct as _st
        self.hdr_vars = []
        v6 = tk.StringVar(value=str(self.eff.header[6]))
        ttk.Label(self.hdr_box, text="Byte 0x06").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.hdr_box, textvariable=v6, width=10).grid(row=0, column=1, padx=4, pady=1)
        self.hdr_vars.append(("b6", v6))
        for i in range(14):
            val = _st.unpack_from("<f", self.eff.header, 8 + 4 * i)[0]
            v = tk.StringVar(value="%g" % val)
            r, c = 1 + i // 2, (i % 2) * 2
            ttk.Label(self.hdr_box, text="%s %d (0x%02X)" % (self.t("hdr_param"), i + 1, 8 + 4 * i)).grid(row=r, column=c, sticky="w")
            ttk.Entry(self.hdr_box, textvariable=v, width=10).grid(row=r, column=c + 1, padx=4, pady=1)
            self.hdr_vars.append((8 + 4 * i, v))
        ttk.Button(self.hdr_box, text=self.t("apply"), command=self._apply_hdr).grid(row=9, column=0, columnspan=4, sticky="ew", pady=6)

    def _apply_hdr(self):
        import struct as _st
        self.snapshot()
        try:
            for key, v in self.hdr_vars:
                if key == "b6":
                    self.eff.header[6] = int(float(v.get())) & 0xFF
                else:
                    _st.pack_into("<f", self.eff.header, key, float(v.get().replace(",", ".")))
        except ValueError as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self.changed()

    def _hdr_from(self, name):
        if not self.eff:
            return
        try:
            ref = Effect.from_bytes(RES.get("suportes", name))
        except (PakError, TypeError):
            return
        self.snapshot()
        self.eff.header[6:] = ref.header[6:]
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("hdr_done", n=os.path.splitext(name)[0].split("/")[-1]))

    def _persist(self, on):
        if not self.eff:
            return
        phases = None if self.persist_all.get() else set(p for p, v in self.persist_ph.items() if v.get())
        self.snapshot()
        n = self.eff.persist(phases, on)
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("persist_done" if on else "persist_undone", n=n))

    def _go_to_opponent(self):
        if not self.eff:
            return
        ref = Effect.from_bytes(RES.get("suportes", self.MOVING_REF))
        self.snapshot()
        moved, hits = self.eff.go_to_opponent(ref, attach=self.goto_attach.get(), zero_delay=self.goto_zero.get(),
                                              hits=self.goto_hits.get(), to_impact=self.goto_impact.get())
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("goto_done", m=moved, h=hits))

    # ---- opacidade / intensidade
    def _opacity_section(self, f):
        hdr = ttk.Frame(f)
        hdr.pack(fill="x")
        ttk.Label(hdr, text=self.t("opa_title"), font=("Segoe UI", self.fs(10), "bold")).pack(side="left")
        self.info_btn(hdr, "info_opa", self.t("more_info")).pack(side="right")
        r = ttk.Frame(f)
        r.pack(fill="x", pady=2)
        ttk.Label(r, text=self.t("opa_reduce")).pack(side="left")
        self.opa_var = tk.StringVar(value="30")
        ttk.Spinbox(r, from_=5, to=95, increment=5, width=5, textvariable=self.opa_var).pack(side="left", padx=4)
        ttk.Label(r, text="%").pack(side="left")
        self.opa_alpha = tk.BooleanVar(value=True)
        self.opa_bright = tk.BooleanVar(value=False)
        self.opa_tex = tk.BooleanVar(value=False)
        ttk.Checkbutton(f, text=self.t("opa_alpha"), variable=self.opa_alpha).pack(anchor="w")
        ttk.Checkbutton(f, text=self.t("opa_bright"), variable=self.opa_bright).pack(anchor="w")
        ttk.Checkbutton(f, text=self.t("opa_tex"), variable=self.opa_tex).pack(anchor="w")
        pr = ttk.Frame(f)
        pr.pack(fill="x", pady=(4, 0))
        ttk.Label(pr, text=self.t("opa_phases")).pack(side="left")
        self.opa_all = tk.BooleanVar(value=True)
        ttk.Checkbutton(pr, text=self.t("opa_all"), variable=self.opa_all).pack(side="left", padx=4)
        pr2 = ttk.Frame(f)
        pr2.pack(fill="x")
        self.opa_ph = {}
        for p in range(6):
            v = tk.BooleanVar(value=False)
            ttk.Checkbutton(pr2, text=str(p), variable=v).pack(side="left")
            self.opa_ph[p] = v
        ttk.Button(f, text=self.t("opa_apply"), command=self._apply_opacity).pack(fill="x", pady=6)

    def _apply_opacity(self):
        if not self.eff:
            return
        try:
            pct = float(self.opa_var.get().replace(",", "."))
        except ValueError:
            return
        if self.opa_all.get():
            ms = [m for m in self.eff.all_minis() if m.type != 0x00]
        else:
            ph = set(p for p, v in self.opa_ph.items() if v.get())
            ms = [m for m in self.eff.all_minis() if m.type != 0x00 and m.get("invoke") in ph]
        if not ms:
            messagebox.showinfo(self.t("app_title"), self.t("nothing_marked"))
            return
        self.snapshot()
        self.eff.reduce_opacity(ms, pct, alpha=self.opa_alpha.get(), brightness=self.opa_bright.get(),
                                textures=self.opa_tex.get())
        self.changed()
        messagebox.showinfo(self.t("ok"), self.t("opa_done", n=len(ms), p=pct))

    # ---- aba em breve
    def tab_flags(self, nb):
        """Flags do 03.dat: byte +0x00 do primeiro bloco de parâmetros (as 4 primeiras linhas)."""
        f = self._tab(nb, "tab_flags")
        self.info_btn(f, "h_flags", self.t("more_info")).pack(anchor="e")
        ttk.Label(f, text=self.t("flags_hint2"), wraplength=self.wrap(), justify="left").pack(anchor="w", pady=(0, 8))
        self.lbl_flags_cur = ttk.Label(f, text="", font=("Segoe UI", self.fs(10), "bold"))
        self.lbl_flags_cur.pack(anchor="w", pady=(0, 6))
        self.fl_vars = {}
        for bit in (1, 2, 4, 8, 16, 32, 64, 128):
            v = tk.BooleanVar(value=False)
            ttk.Checkbutton(f, text="%d — %s" % (bit, self.t("flag_%d" % bit)), variable=v,
                            command=self._flags_preview).pack(anchor="w")
            self.fl_vars[bit] = v
        ttk.Button(f, text=self.t("apply"), command=self._flags_apply).pack(fill="x", pady=10)
        self._flags_load()
        if hasattr(self, "lbl_barrage"):
            self.lbl_barrage.config(text=self.t("barrage_state_on") if self.eff and self.eff.is_barrage() else self.t("barrage_state_off"))

    def _flags_block(self):
        ms = self.eff.all_minis() if self.eff else []
        return ms[0] if ms else None

    def _flags_load(self):
        if not hasattr(self, "fl_vars"):
            return
        m = self._flags_block()
        val = m.param[0] if m is not None else 0
        for bit, v in self.fl_vars.items():
            v.set(bool(val & bit))
        self._flags_preview()

    def _flags_preview(self):
        m = self._flags_block()
        if m is None:
            self.lbl_flags_cur.config(text=self.t("flags_none"))
            return
        new = sum(bit for bit, v in self.fl_vars.items() if v.get())
        self.lbl_flags_cur.config(text=self.t("flags_cur", v=m.param[0], n=new))

    def _flags_apply(self):
        m = self._flags_block()
        if m is None:
            return
        self.snapshot()
        m.param[0] = sum(bit for bit, v in self.fl_vars.items() if v.get())
        self.changed()

    # ------------------------------------------------------------ ações
    def _combo_group(self, cb, lst=None):
        lst = lst or self.list
        i = cb.current()
        gs = lst.groups()
        return gs[i] if 0 <= i < len(gs) else None

    def _refresh_combos(self):
        gl = [group_label(g, self.lang) for g in self.list.groups()]
        self.cb_colorgroup["values"] = gl
        self.cb_scalegroup["values"] = gl
        if hasattr(self, "cb_growgroup"):
            self.cb_growgroup["values"] = gl
        if hasattr(self, "cb_hidegroup"):
            self.cb_hidegroup["values"] = gl
        self.cb_replace["values"] = gl
        if self.cb_replace.current() < 0 and gl:
            self.cb_replace.current(0)
        self.chips.rebuild()

    def on_select(self, m):
        self._fill_rgb(m)
        self._fill_params(m)


    def refresh(self):
        if self.cur_kind() != getattr(self, "_ui_kind", "skill"):
            self.build_ui()
            return
        sel = self.list.selected()
        self.list.fill(self.eff)
        if self.eff:
            name = os.path.basename(self.path) if self.path else "?"
            self.lbl_file.config(text=name + (" *" if self.dirty else ""))
            self.lbl_sum.config(text=self.t("summary", n=len(self.eff.all_minis()), c=len(self.eff.cats),
                                            f=len(self.eff.file_list())))
            kb = len(self.eff.to_bytes()) / 1024.0
            self.lbl_size.config(text="%.0f KB" % kb + ("  ⚠ " + self.t("w_warn") if kb > SIZE_WARN_KB else ""),
                                 fg="#b00020" if kb > SIZE_WARN_KB else "#1b6e20")
        else:
            self.lbl_file.config(text=self.t("no_file"))
            self.lbl_sum.config(text="")
            self.lbl_size.config(text="")
        if sel in self.list.minis:
            i = str(self.list.minis.index(sel))
            self.list.tree.selection_set(i)
            self.list.tree.see(i)
        else:
            self.on_select(None)
        self._refresh_combos()
        self._beh_summary()
        self._scene_status()
        self._extras_status()
        self._depth_status()
        self._flags_load()
        self._fill_hdr()

    def snapshot(self):
        if self.eff:
            self.history.append((self.eff.to_bytes(), [m.group for m in self.eff.all_minis()], self.eff.kind))
            self.history = self.history[-30:]

    def undo(self):
        if not self.history:
            return
        data, groups, kind = self.history.pop()
        self.eff = Effect.from_bytes(data)
        self.eff.kind = kind
        for m, g in zip(self.eff.all_minis(), groups):
            m.group = g
        self.dirty = True
        self.refresh()

    def changed(self):
        self.dirty = True
        self.refresh()

    def _groups_path(self, p):
        return p + ".grupos.json"

    def _load_groups(self, eff, p):
        try:
            with open(self._groups_path(p), encoding="utf-8") as f:
                gs = json.load(f)
            ms = eff.all_minis()
            if len(gs) == len(ms):
                for m, g in zip(ms, gs):
                    m.group = g
        except Exception:
            pass

    def open(self, path=None, template=False):
        if self.dirty and not messagebox.askyesno(self.t("app_title"), self.t("unsaved")):
            return
        p = path or filedialog.askopenfilename(filetypes=[("PAK", "*.pak"), ("*", "*.*")], parent=self)
        if not p:
            return
        try:
            with open(p, "rb") as fh:
                raw = fh.read()
            ents = container_entries(raw)
            if ents:
                self._choose_from_container(p, raw, ents)
                return
            self.container = None
            self.eff = Effect.load(p)
            if self.eff.kind == "skill" and SUPPORT_NAME.search(os.path.basename(p)):
                self.eff.kind = "support"
            self._load_groups(self.eff, p)
        except (PakError, OSError) as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self.path = None if template else p
        self.dirty, self.history = bool(template), []
        self.list.checked.clear()
        self.title(self.t("app_title") + (" — " + os.path.basename(p)))
        self.refresh()

    def _choose_from_container(self, p, raw, ents):
        w = tk.Toplevel(self)
        w.title(self.t("cont_title", n=os.path.basename(p)))
        w.transient(self)
        ttk.Label(w, text=self.t("cont_hint"), padding=8, wraplength=460).pack(anchor="w")
        tv = ttk.Treeview(w, columns=("kind", "n"), show="tree headings", height=min(14, len(ents)))
        tv.heading("#0", text=".pak")
        tv.heading("kind", text=self.t("cont_kind"))
        tv.heading("n", text=self.t("summary_minis"))
        tv.column("#0", width=300)
        tv.column("kind", width=90)
        tv.column("n", width=80, anchor="center")
        kinds = {"skill": self.t("kind_skill"), "aura": self.t("kind_aura"), "support": self.t("kind_support")}
        for k, (path, name, kind, n) in enumerate(ents):
            if kind == "skill" and SUPPORT_NAME.search(name):
                kind = "support"
            tv.insert("", "end", iid=str(k), text=name, values=(kinds.get(kind, kind), n))
        tv.pack(fill="both", expand=True, padx=8)

        def go(_=None):
            sel = tv.selection()
            if not sel:
                return
            path, name, kind, n = ents[int(sel[0])]
            try:
                eff = Effect.from_bytes(container_get(raw, path))
            except PakError as ex:
                messagebox.showerror(self.t("err"), str(ex), parent=w)
                return
            if eff.kind == "skill" and SUPPORT_NAME.search(name):
                eff.kind = "support"
            w.destroy()
            self.eff = eff
            self.container = (p, path, name)
            self.path = p
            self.dirty, self.history = False, []
            self.list.checked.clear()
            self.title(self.t("app_title") + " — " + os.path.basename(p) + " › " + name)
            self.refresh()
        tv.bind("<Double-1>", go)
        ttk.Button(w, text=self.t("cont_open"), command=go).pack(fill="x", padx=8, pady=8)

    def open_textures(self):
        if not self.eff:
            return
        import texview
        texview.TextureWindow(self)

    def open_hex(self):
        if not self.eff:
            return
        import hexview
        hexview.HexWindow(self)

    def open_hex_external(self):
        p = filedialog.askopenfilename(filetypes=[("DAT", "*.dat *_"), ("*", "*.*")], parent=self)
        if p:
            import hexview
            hexview.HexWindow(self, external=p)

    def open_template(self, name, sub="modelos"):
        if self.dirty and not messagebox.askyesno(self.t("app_title"), self.t("unsaved")):
            return
        try:
            self.eff = Effect.from_bytes(RES.get(sub, name))
            if sub == "suportes":
                self.eff.kind = "support"
        except (PakError, TypeError) as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self.path, self.dirty, self.history = None, True, []
        self.container = None
        self.list.checked.clear()
        self.title(self.t("app_title") + " — " + os.path.splitext(name)[0])
        self.refresh()

    def save(self, as_new=False):
        if not self.eff:
            return
        if RES.is_protected(self.eff.to_bytes()):
            messagebox.showerror(self.t("err"), self.t("protected_save"))
            return
        probs = self.eff.validate()
        if probs:
            messagebox.showerror(self.t("err"), self.t("invalid") + "\n".join(probs))
            return
        cont = getattr(self, "container", None)
        if cont and not as_new:
            cp, path, name = cont
            try:
                with open(cp, "rb") as fh:
                    raw = fh.read()
                if not os.path.exists(cp + ".bak"):
                    shutil.copy2(cp, cp + ".bak")
                with open(cp, "wb") as fh:
                    fh.write(container_put(raw, path, self.eff.to_bytes()))
            except (OSError, PakError) as ex:
                messagebox.showerror(self.t("err"), str(ex))
                return
            self.dirty = False
            self.refresh()
            messagebox.showinfo(self.t("ok"), self.t("cont_saved", n=name, c=os.path.basename(cp)))
            return
        p = self.path if not cont else None
        if as_new or not p:
            p = filedialog.asksaveasfilename(defaultextension=".pak", filetypes=[("PAK", "*.pak")], parent=self)
            if not p:
                return
        backup = None
        if os.path.exists(p) and not os.path.exists(p + ".bak"):
            backup = p + ".bak"
            shutil.copy2(p, backup)
        try:
            self.eff.save(p)
            with open(self._groups_path(p), "w", encoding="utf-8") as f:
                json.dump([m.group for m in self.eff.all_minis()], f, ensure_ascii=False)
        except OSError as ex:
            messagebox.showerror(self.t("err"), str(ex))
            return
        self.path, self.dirty = p, False
        self.container = None
        self.refresh()
        messagebox.showinfo(self.t("ok"), self.t("saved", b=os.path.basename(backup)) if backup else self.t("saved_nb"))

    def remove_marked(self):
        self._remove(self.list.marked())

    def _remove(self, ms):
        if not ms:
            messagebox.showinfo(self.t("app_title"), self.t("nothing_marked"))
            return
        prot = [m for m in ms if m.type == 0x00]
        ms = [m for m in ms if m.type != 0x00]
        if ms:
            q = self.t("confirm_remove", n=len(ms))
            if any(m.hits for m in ms):
                q += "\n\n" + self.t("warn_hits")
            if messagebox.askyesno(self.t("app_title"), q):
                self.snapshot()
                self.eff.remove_minis(ms)
                self.changed()
        if prot:
            messagebox.showinfo(self.t("app_title"), self.t("protected"))

    def quit_app(self):
        if self.dirty and not messagebox.askyesno(self.t("app_title"), self.t("unsaved")):
            return
        self.destroy()


if __name__ == "__main__":
    App().mainloop()
