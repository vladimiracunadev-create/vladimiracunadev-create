#!/usr/bin/env python3
"""Chequeo de coherencia del perfil: enlaces, idiomas, matriz de cargos y cifras.
Uso: python scripts/check_coherence.py   (sale con código 1 si hay problemas)
"""
import glob
import os
import re
import sys
from pathlib import Path

LANGS = ["en", "pt", "it", "fr", "zh", "zh-TW", "ja", "ko", "tr", "ru", "vi", "th", "de",
         "uk", "pl", "ar", "fa", "id", "nl", "hi", "el"]
FAMILIES = ["README", "PROFESIONAL_ROLES", "CONTRIBUTING", "SECURITY", "CODE_OF_CONDUCT",
            "docs/ECOSYSTEM", "docs/MANAGEMENT", "docs/START_HERE",
            *[f"docs/guides/{g}" for g in ("RECRUITER", "FREELANCE", "TECH_LEAD", "BUSINESS", "COLLABORATOR", "LEARNER")]]
errors = []


def read(p):
    return Path(p).read_text(encoding="utf-8")


def err(msg):
    errors.append(msg)


mds = [f for f in glob.glob("**/*.md", recursive=True) if "node_modules" not in f]

# 1) marcadores de conflicto y 2) enlaces relativos
for f in mds:
    t = read(f)
    if re.search(r"^(<<<<<<<|=======$|>>>>>>>)", t, re.M):
        err(f"{f}: marcador de conflicto de git")
    for m in re.finditer(r"\]\(([^)#\s]+?)(?:#[^)]*)?\)", t):
        u = m.group(1)
        if re.match(r"^(https?:|mailto:|data:)", u):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), u))):
            err(f"{f}: enlace roto -> {u}")

# 3) cada familia de documentos existe en los 22 idiomas
for fam in FAMILIES:
    for lg in LANGS:
        p = f"{fam}.{lg}.md"
        if not os.path.exists(p):
            err(f"falta la versión {lg}: {p}")

# 4) la matriz de cargos traducida conserva estructura y URL del español
base = read("PROFESIONAL_ROLES.md")
rows = [l.count("|") for l in base.split("\n") if l.startswith("|")]
urls = sorted(re.findall(r"\]\((https?://[^)]+)\)", base))
for lg in LANGS:
    p = f"PROFESIONAL_ROLES.{lg}.md"
    if not os.path.exists(p):
        continue
    t = read(p)
    r = [l.count("|") for l in t.split("\n") if l.startswith("|")]
    if r != rows:
        err(f"{p}: las tablas no coinciden con el español (filas/columnas)")
    if sorted(re.findall(r"\]\((https?://[^)]+)\)", t)) != urls:
        err(f"{p}: las URL no coinciden con el español")

# 5) cifras: los contadores deben ser iguales en los 22 README y las clases no pueden quedar viejas
def badges(t):
    b = re.search(r"<!-- STATS:START -->(.*?)<!-- STATS:END -->", t, re.S)
    return re.findall(r"img\.shields\.io/badge/[^)]*?-(\d+)-[0-9a-f]{6}", b.group(1)) if b else None

ref = badges(read("README.md"))
if not ref:
    err("README.md: no se pudo leer el bloque STATS")
else:
    for lg in LANGS:
        b = badges(read(f"README.{lg}.md")) if os.path.exists(f"README.{lg}.md") else None
        if b != ref:
            err(f"README.{lg}.md: contadores distintos al README principal ({b} vs {ref})")
    clases = ref[3] if len(ref) > 3 else None
    if clases:
        for f in mds:
            for m in re.finditer(r"(?<![\d.,])(\d{2})[.,\s  ]?(\d{3})(?![\d])", read(f)):
                n = m.group(1) + m.group(2)
                if n.startswith(clases[:2]) and len(clases) == 5 and n != clases and abs(int(n) - int(clases)) < 3000:
                    # cifra cercana a las clases pero distinta: probablemente desactualizada
                    ctx = read(f)[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")
                    if re.search(r"clas|class|aula|lesson|lez|leç|课|課|クラス|수업|ders|урок|занят|bài|คาบ|Unterricht|урок|zajęć|حص|kelas|les|कक्ष|μαθ", ctx, re.I):
                        err(f"{f}: cifra de clases {n} distinta de {clases}")

# 6) la tabla de currículos de cada ECOSYSTEM debe sumar las clases del contador y tener tantas filas como programas declara la insignia
if ref and len(ref) > 3:
    PERS = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")
    badge_prog = re.search(r"img\.shields\.io/badge/[^)?]*?-(\d+)%20(?:programs|programas|programmes|programmi)-3fb950", read("README.md"))
    for lg in [""] + LANGS:
        p = f"docs/ECOSYSTEM{'.' + lg if lg else ''}.md"
        if not os.path.exists(p):
            continue
        sec = re.search(r"\n## 📚(.*?)\n## ", read(p), re.S)
        if not sec:
            err(f"{p}: no se encontró la sección de currículos")
            continue
        total, filas = 0, 0
        for l in sec.group(1).split("\n"):
            if not l.startswith("| ["):
                continue
            cells = [c.strip() for c in l.split("|")]
            num = re.sub(r"[^\d]", "", cells[2].translate(PERS)) if len(cells) > 2 else ""
            if not num:
                err(f"{p}: fila de currículo sin número de clases: {cells[1][:50]}")
                continue
            total += int(num)
            filas += 1
        if total != int(ref[3]):
            err(f"{p}: la tabla de currículos suma {total} clases y el contador dice {ref[3]}")
        if badge_prog and filas != int(badge_prog.group(1)):
            err(f"{p}: {filas} programas en la tabla y la insignia dice {badge_prog.group(1)}")

if errors:
    print(f"{len(errors)} problema(s):")
    for e in errors[:80]:
        print(" -", e)
    sys.exit(1)
print("coherencia OK:", len(mds), "archivos .md revisados")
