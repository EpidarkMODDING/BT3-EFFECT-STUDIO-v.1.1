# -*- coding: utf-8 -*-
"""
Recursos protegidos do BT3 Effect Studio (modelos, extras, cenas).
Os .pak base do projeto ficam dentro de 'recursos.dat', comprimidos e cifrados, e só são
lidos em memória pelo programa. Arquivos que o usuário colocar nas pastas 'modelos', 'extras'
e 'cenas' continuam funcionando (e são somados aos protegidos).
"""
import os, json, zlib, hashlib, struct

MAGIC = b"BT3ES\x02"
_P = (0x5A17, 0x0B7E, 0x3C3D, 0x1D2A, 0x6E61, 0x0521)


def _key():
    s = b"".join(struct.pack("<H", (v * 7919 + i * 104729) & 0xFFFF) for i, v in enumerate(_P))
    return hashlib.sha256(s + b"ariel-kaya-bt3").digest()


def _stream(key, nonce, n):
    out = bytearray()
    ctr = 0
    while len(out) < n:
        out += hashlib.sha256(key + nonce + struct.pack("<Q", ctr)).digest()
        ctr += 1
    return bytes(out[:n])


def _xor(data, ks):
    a = int.from_bytes(data, "little")
    b = int.from_bytes(ks, "little")
    return (a ^ b).to_bytes(len(data), "little")


def build_bundle(entries, out_path):
    """entries: {'modelos/Nome.pak': bytes, 'extras/x.pak': bytes, 'extras/extras.json': bytes, ...}"""
    index, blob = [], bytearray()
    for name in sorted(entries):
        comp = zlib.compress(entries[name], 9)
        index.append([name, len(blob), len(comp)])
        blob += comp
    head = json.dumps(index, ensure_ascii=False).encode("utf-8")
    plain = struct.pack("<I", len(head)) + head + bytes(blob)
    nonce = os.urandom(16)
    key = _key()
    body = _xor(plain, _stream(key, nonce, len(plain)))
    mac = hashlib.sha256(key + nonce + body).digest()[:16]
    with open(out_path, "wb") as fh:
        fh.write(MAGIC + nonce + mac + body)


class Resources:
    def __init__(self, base):
        self.base = base
        self._files = {}          # nome -> bytes (protegidos, em memória)
        self.protected = set()    # hashes dos .pak protegidos
        path = os.path.join(base, "recursos.dat")
        if os.path.exists(path):
            self._load_bundle(path)

    def _load_bundle(self, path):
        with open(path, "rb") as fh:
            raw = fh.read()
        if raw[:6] != MAGIC:
            return
        nonce, mac, body = raw[6:22], raw[22:38], raw[38:]
        key = _key()
        if hashlib.sha256(key + nonce + body).digest()[:16] != mac:
            return
        plain = _xor(body, _stream(key, nonce, len(body)))
        hl = struct.unpack_from("<I", plain, 0)[0]
        index = json.loads(plain[4:4 + hl].decode("utf-8"))
        data = plain[4 + hl:]
        for name, off, size in index:
            content = zlib.decompress(data[off:off + size])
            self._files[name] = content
            if name.lower().endswith(".pak"):
                self.protected.add(hashlib.sha256(content).hexdigest())

    # ---- genérico: primeiro a pasta do usuário, depois o pacote protegido
    def _user(self, sub, name):
        p = os.path.join(self.base, sub, *name.split("/"))
        return p if os.path.isfile(p) else None

    def list(self, sub, ext=".pak"):
        names = set(n.split("/", 1)[1] for n in self._files if n.startswith(sub + "/") and n.lower().endswith(ext))
        d = os.path.join(self.base, sub)
        if os.path.isdir(d):
            for root, _dirs, files in os.walk(d):
                for f in files:
                    if f.lower().endswith(ext):
                        names.add(os.path.relpath(os.path.join(root, f), d).replace(os.sep, "/"))
        return sorted(names)

    def get(self, sub, name):
        p = self._user(sub, name)
        if p:
            with open(p, "rb") as fh:
                return fh.read()
        return self._files.get(sub + "/" + name)

    def extras_manifest(self):
        items = []
        raw = self._files.get("extras/extras.json")
        if raw:
            items += json.loads(raw.decode("utf-8"))
        p = self._user("extras", "extras.json")
        if p:
            try:
                with open(p, encoding="utf-8") as fh:
                    known = set(x["file"] for x in items)
                    items += [x for x in json.load(fh) if x.get("file") not in known]
            except (OSError, ValueError):
                pass
        return [x for x in items if self.get("extras", x.get("file", "")) is not None]

    def is_protected(self, data):
        return hashlib.sha256(data).hexdigest() in self.protected
