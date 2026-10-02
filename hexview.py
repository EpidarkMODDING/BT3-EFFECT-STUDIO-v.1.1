# -*- coding: utf-8 -*-
"""Editor hexadecimal com as informações conhecidas de cada byte dos arquivos de efeito."""
import os, struct
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from bt3eff_core import (Effect, PakError, pak_pack, dbt_info, SHAPE_SHADER, CLASS_NAMES, SCENE_MAPS, SCENE_EVENTS)
from lang import tr

FLAG_TXT = {1: "?", 2: "efeitos lançados", 4: "?", 8: "ossos dos parâmetros", 16: "?", 32: "sempre na frente da câmera",
            64: "posição fixa", 128: "corrige anéis (choque/cena)"}
MINI_FIELDS = [
    (0x00, 1, "Flags (1/2/4/8/16/32/64/128 somados)"),
    (0x01, 1, "DBT usado (índice dentro da classe)"),
    (0x02, 1, "Textura (imagem dentro do DBT)"),
    (0x03, 1, "Desconhecido"),
    (0x04, 1, "Atraso A (aparição)"), (0x05, 1, "Atraso B (aparição)"),
    (0x06, 1, "Duração A (depois da animação)"), (0x07, 1, "Duração B (depois da animação)"),
    (0x08, 1, "Grupo de invocação: 00 carregamento, 01 lançamento, 02 saídas de luz/fim, 03 auras, 04 Vfx 5 (explosão), 05 iluminação"),
    (0x09, 1, "Permanência: 00 some no fim do tempo, 02 fica até o lançamento, 03 some na ceninha, 04 continua na ceninha"),
    (0x0A, 1, "Posição: 01 estático na referência, 02 ao redor do personagem, 04 centro do personagem, 05 segue a referência até o oponente"),
    (0x0B, 1, "04 = continua enquanto o estado estiver ativo (auras / até usar especial) — hipótese"),
    (0x10, 4, "Posição (float)"), (0x14, 4, "Posição Y? (float)"), (0x18, 4, "Posição Z? (float)"),
    (0x1C, 4, "Tamanho 1 (float)"), (0x20, 4, "Tamanho 2 (float)"), (0x24, 4, "Tamanho 3 (float)"),
    (0x28, 4, "Tempo tamanho 1→2 (float)"), (0x2C, 4, "Tempo tamanho 2→3 (float)"), (0x30, 4, "Desconhecido (float)"),
]


def annotate_params(f, start_note=""):
    """Anotações do arquivo de parâmetros (03_.dat nos golpes/suportes, 00 nas auras)."""
    a = []
    a.append((0, 3, "Bitmask das classes presentes (classe T → byte T÷8, bit T%8)"))
    a.append((3, 1, "Sempre 00"))
    a.append((4, 1, "Quantidade de classes"))
    a.append((5, 1, "Total de mini-efeitos"))
    a.append((6, 1, "Tipo de lançamento (07/08 verticais, 09 kikoho, 0A projétil...)"))
    a.append((7, 1, "Desconhecido"))
    for i in range(6):
        a.append((8 + 4 * i, 4, "Parâmetro %d do cabeçalho (float; alcance/tempos, varia por golpe)" % (i + 1)))
    a.append((0x20, 1, "Desconhecido"))
    a.append((0x21, 1, "Cena: 01 = o golpe aparece durante a ceninha"))
    a.append((0x22, 1, "Cena: 01 = feixe vertical (de cima p/ baixo ou de baixo p/ cima)"))
    a.append((0x23, 2, "Desconhecido"))
    a.append((0x25, 1, "Cena: 05 = projétil na ceninha"))
    a.append((0x26, 1, "Cena: 10 habitual quando aparece na ceninha (50 no Ultimate do Kid Gohan)"))
    a.append((0x27, 1, "Modo barragem: 02 = barragem, 03 = barragem que aparece na ceninha"))
    for i in range(6):
        a.append((0x28 + 4 * i, 4, "Parâmetro %d do cabeçalho (float)" % (i + 7)))
    ncat = f[4] if len(f) > 4 else 0
    k = 0
    base = 64 + 32 * ncat
    types = []
    for c in range(ncat):
        o = 64 + 32 * c
        t, n, db = f[o], f[o + 1], f[o + 2]
        types += [t] * n
        a.append((o, 1, "Classe %02X (%s)" % (t, CLASS_NAMES.get(t, "?"))))
        a.append((o + 1, 1, "Quantidade de mini-efeitos da classe %02X" % t))
        a.append((o + 2, 1, "Quantidade de DBTs da classe %02X" % t))
        a.append((o + 3, 29, "Não usado (zeros)"))
    for i, t in enumerate(types):
        b = base + 64 * i
        extra = " — mini-efeito GLOBAL de listras brancas (não pode ser removido; tamanho 0 esconde)" if t == 0 and i == 0 else ""
        for off, size, txt in MINI_FIELDS:
            a.append((b + off, size, "Mini #%d (classe %02X)%s: %s" % (i, t, extra if off == 0 else "", txt)))
    return a


def annotate_shader(f):
    a = []
    for r in range(len(f) // 16):
        if r < 12:
            s, rr = r // 3 + 1, r % 3 + 1
            for k, ch in enumerate("RGBA"):
                a.append((r * 16 + 4 * k, 4, "Shader sessão %d linha %d: %s (float 0-255)" % (s, rr, ch)))
        else:
            a.append((r * 16, 16, "Shader linha %d: parâmetros (4 floats de 0 a 1)" % (r + 1)))
    return a


def annotate_v00(f):
    a = [(0, 4, "Assinatura 'V000'"), (4, 4, "Quantidade de trilhas"), (8, 2, "Início dos quadros-chave")]
    if len(f) >= 10:
        st = struct.unpack_from("<H", f, 8)[0]
        a.append((0x20, max(0, st - 0x20), "Trilhas (32 bytes cada)"))
        i, k = st, 0
        while i + 64 <= len(f):
            a.append((i, 48, "Quadro-chave %d: forma/tamanho/rotação/posição" % k))
            a.append((i + 48, 4, "Quadro-chave %d: cor RGBA (bytes)" % k))
            i += 64
            k += 1
    return a


def annotate_anim02(f):
    a = []
    for s in range(len(f) // 120):
        b = s * 120
        a.append((b, 12, "Classe 02 sessão %d: forma (desconhecido)" % s))
        for j, o in enumerate((0x0C, 0x1C, 0x2C)):
            a.append((b + o, 4, "Classe 02 sessão %d: cor %d RGBA (bytes)" % (s, j + 1)))
    return a


def annotate_dbt(f):
    a = [(0, 4, "Quantidade de imagens"), (8, 4, "Soma dos blocos de pixels"), (12, 4, "Soma dos blocos de paleta")]
    for i, im in enumerate(dbt_info(f)):
        b = 0x20 + 0x40 * i
        a += [(b, 4, "Imagem %d: offset/4 dos pixels" % i), (b + 4, 4, "Imagem %d: offset/4 da paleta" % i),
              (b + 8, 4, "Imagem %d: tamanho do pacote de pixels" % i), (b + 12, 4, "Imagem %d: tamanho do pacote de paleta" % i),
              (b + 0x30, 8, "Imagem %d: registrador TEX0 (%d×%d, %d cores)" % (i, im['w'], im['h'], 256 if im['psm'] == 0x13 else 16))]
        if im['pixels']:
            a.append((im['pixels'][0], im['pixels'][1], "Imagem %d: pixels (embaralhados no formato do PS2)" % i))
        if im['clut']:
            a.append((im['clut'][0], im['clut'][1], "Imagem %d: paleta RGBA (alfa 0-128)" % i))
    return a


def annotate_scene(f):
    a = []
    for mp in range(SCENE_MAPS):
        for ev in range(SCENE_EVENTS):
            o = (mp * SCENE_EVENTS + ev) * 16
            a.append((o + 4, 4, "02_.dat mapa %d evento %d: altura (Y) dos personagens" % (mp + 1, ev + 1)))
            a.append((o + 8, 4, "02_.dat mapa %d evento %d: posição Z (a partir do centro do mapa)" % (mp + 1, ev + 1)))
    a.append((2800, 16, "Última linha, sempre vazia"))
    return a


def describe_files(eff):
    """[(índice, nome, anotador)] para cada arquivo do efeito."""
    out = []
    i = 0
    for k, p in enumerate(eff.pre):
        name = {0: "00_ (modelos 3D)", 1: "01_ (vazio)", 2: "02_ (cena: Y/Z por mapa)"}.get(k, "%02d_" % k)
        out.append((i, name, annotate_scene if k == 2 else None)); i += 1
    out.append((i, "%02d_ parâmetros" % i, annotate_params)); i += 1
    for c in eff.cats:
        for d in c.dbts:
            out.append((i, "%02d_ DBT (classe %02X)" % (i, c.type), annotate_dbt)); i += 1
        for m in c.minis:
            for j, f in enumerate(m.files):
                if c.type == 0x02:
                    out.append((i, "%02d_ classe 02 (saídas de luz)" % i, annotate_anim02))
                elif c.type == 0x0E:
                    out.append((i, "%02d_ V00 (classe 0E)" % i, annotate_v00))
                else:
                    shader = j == getattr(m, "shader_idx", 1)
                    out.append((i, "%02d_ %s (classe %02X)" % (i, "shader" if shader else "shape", c.type),
                                annotate_shader if shader else None))
                i += 1
    return out


def guess_annotator(data, name=""):
    n = os.path.basename(name).lower()
    if data[:4] == b"V000":
        return annotate_v00
    if len(data) == 2816:
        return annotate_scene
    if len(data) in (192, 320) or ("shader" in n):
        return annotate_shader
    if len(data) == 1216:
        return annotate_anim02
    if dbt_info(data):
        return annotate_dbt
    if len(data) >= 64 and data[4] and len(data) >= 64 + 32 * data[4]:
        return annotate_params
    return None


class HexWindow(tk.Toplevel):
    def __init__(self, app, external=None):
        super().__init__(app)
        self.app, self.lang = app, app.lang
        self.external = external          # caminho de um .dat avulso
        self.title(tr("hex_title", self.lang))
        self.geometry("1100x640")
        self.data, self.annot, self.cur = b"", [], None
        top = ttk.Frame(self, padding=4)
        top.pack(fill="x")
        self.files = []
        if external:
            ttk.Label(top, text=os.path.basename(external)).pack(side="left")
        else:
            self.files = describe_files(app.eff)
            self.cb = ttk.Combobox(top, state="readonly", width=46, values=[n for _, n, _ in self.files])
            self.cb.pack(side="left")
            self.cb.bind("<<ComboboxSelected>>", lambda e: self._load(self.cb.current()))
        ttk.Button(top, text=tr("apply", self.lang), command=self._apply).pack(side="left", padx=6)
        self.show_info = tk.BooleanVar(value=True)
        ttk.Checkbutton(top, text=tr("hex_known", self.lang), variable=self.show_info,
                        command=self._toggle).pack(side="left")
        body = ttk.PanedWindow(self, orient="horizontal")
        body.pack(fill="both", expand=True)
        tf = ttk.Frame(body)
        self.text = tk.Text(tf, font=("Consolas", 10), wrap="none", undo=True)
        sb = ttk.Scrollbar(tf, command=self.text.yview)
        self.text.configure(yscrollcommand=sb.set)
        self.text.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        body.add(tf, weight=3)
        self.info = ttk.Treeview(body, columns=("off", "len", "txt"), show="headings")
        for c, w in (("off", 70), ("len", 40), ("txt", 420)):
            self.info.column(c, width=w, anchor="w")
        self.info.heading("off", text="Offset")
        self.info.heading("len", text="Bytes")
        self.info.heading("txt", text=tr("hex_meaning", self.lang))
        self.info.bind("<<TreeviewSelect>>", self._jump)
        self.body, self.info_pane = body, self.info
        body.add(self.info, weight=2)
        self.status = ttk.Label(self, text="", padding=4)
        self.status.pack(fill="x")
        self.text.bind("<ButtonRelease-1>", self._where)
        self.text.bind("<KeyRelease>", self._where)
        if external:
            with open(external, "rb") as fh:
                self.data = fh.read()
            self._show(guess_annotator(self.data, external))
        elif self.files:
            self.cb.current(len(app.eff.pre))
            self._load(len(app.eff.pre))

    def _load(self, k):
        self.cur = k
        self.data = self.app.eff.file_list()[self.files[k][0]]
        self._show(self.files[k][2])

    def _show(self, annotator):
        self.annot = sorted(annotator(self.data), key=lambda t: t[0]) if annotator else []
        lines = []
        for o in range(0, len(self.data), 16):
            chunk = self.data[o:o + 16]
            asc = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
            lines.append("%06X: %-47s  |%s" % (o, " ".join("%02X" % b for b in chunk), asc))
        self.text.delete("1.0", "end")
        self.text.insert("1.0", "\n".join(lines))
        self.info.delete(*self.info.get_children())
        for n, (o, ln, txt) in enumerate(self.annot):
            self.info.insert("", "end", iid=str(n), values=("0x%04X" % o, ln, txt))
        if not self.annot:
            self.info.insert("", "end", values=("", "", tr("hex_unknown", self.lang)))

    def _toggle(self):
        if self.show_info.get():
            self.body.add(self.info_pane, weight=2)
        else:
            self.body.forget(self.info_pane)

    def _offset_at_cursor(self):
        line, col = [int(x) for x in self.text.index("insert").split(".")]
        if col < 8 or col > 8 + 47:
            return None
        return (line - 1) * 16 + (col - 8) // 3

    def _where(self, _=None):
        o = self._offset_at_cursor()
        if o is None or o >= len(self.data):
            return
        found = [t for (s, ln, t) in self.annot if s <= o < s + ln]
        self.status.config(text="0x%04X = %02X  ·  %s" % (o, self.data[o], found[-1] if found else tr("hex_unknown", self.lang)))

    def _jump(self, _=None):
        s = self.info.selection()
        if not s or not s[0].isdigit():
            return
        o = self.annot[int(s[0])][0]
        line, col = o // 16 + 1, 8 + (o % 16) * 3
        self.text.mark_set("insert", "%d.%d" % (line, col))
        self.text.see("insert")
        self._where()

    def _parse(self):
        out = bytearray()
        for ln in self.text.get("1.0", "end").splitlines():
            if ":" not in ln:
                continue
            hexpart = ln.split(":", 1)[1].split("|")[0]
            for tok in hexpart.split():
                out.append(int(tok, 16))
        return bytes(out)

    def _apply(self):
        try:
            new = self._parse()
        except ValueError as ex:
            messagebox.showerror(tr("err", self.lang), str(ex), parent=self)
            return
        if self.external:
            with open(self.external, "wb") as fh:
                fh.write(new)
            self.data = new
            messagebox.showinfo(tr("ok", self.lang), tr("hex_saved", self.lang), parent=self)
            return
        files = self.app.eff.file_list()
        files[self.files[self.cur][0]] = new
        try:
            neweff = Effect.from_bytes(pak_pack(files))
        except PakError as ex:
            messagebox.showerror(tr("err", self.lang), tr("hex_invalid", self.lang) + "\n" + str(ex), parent=self)
            return
        self.app.snapshot()
        old = self.app.eff
        neweff.kind = old.kind
        if len(neweff.all_minis()) == len(old.all_minis()):
            for a, b in zip(neweff.all_minis(), old.all_minis()):
                a.group = b.group
        self.app.eff = neweff
        self.app.changed()
        self.files = describe_files(neweff)
        self.cb["values"] = [n for _, n, _ in self.files]
        self._load(self.cur)
