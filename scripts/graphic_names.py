#!/usr/bin/env python3
"""Pone un sello de contenido en el nombre de cada gráfico del ecosistema.

GitHub (raw.githubusercontent.com) guarda en caché cada URL de imagen y no la
renueva aunque el archivo cambie, ni con Ctrl+F5. Si el nombre incluye un hash
del contenido, cada cambio del gráfico estrena una URL y el perfil lo muestra
al instante.

Uso (desde la raíz del repositorio, tras editar un SVG):

    python3 scripts/graphic_names.py

Renombra docs/img/ecosystem.<idioma>[.<hash>].svg a
docs/img/ecosystem.<idioma>.<hash>.svg y actualiza la referencia en el README
de ese idioma. Es idempotente: si nada cambió, no toca nada.
"""
import glob
import hashlib
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)

REF = re.compile(r"docs/img/ecosystem\.([A-Za-z-]+?)(?:\.[0-9a-f]{8})?\.svg")


def readme_de(lg):
    return "README.md" if lg == "es" else f"README.{lg}.md"


def actual(lg):
    """Archivo vigente de ese idioma (con o sin sello)."""
    cand = sorted(glob.glob(f"docs/img/ecosystem.{lg}.svg") + glob.glob(f"docs/img/ecosystem.{lg}.[0-9a-f]" + "[0-9a-f]" * 7 + ".svg"))
    return cand


def main():
    cambios = 0
    idiomas = sorted({m.group(1) for f in glob.glob("docs/img/ecosystem.*.svg")
                      for m in [re.match(r"docs/img/ecosystem\.([A-Za-z-]+?)(?:\.[0-9a-f]{8})?\.svg$", f.replace("\\", "/"))] if m})
    for lg in idiomas:
        archivos = actual(lg)
        if len(archivos) != 1:
            print(f"{lg}: se esperaba 1 archivo y hay {len(archivos)}: {archivos}")
            sys.exit(1)
        src = archivos[0].replace("\\", "/")
        h = hashlib.sha1(open(src, "rb").read()).hexdigest()[:8]
        nuevo = f"docs/img/ecosystem.{lg}.{h}.svg"
        if src != nuevo:
            subprocess.run(["git", "mv", src, nuevo], check=True)
            cambios += 1
        rd = readme_de(lg)
        t = open(rd, encoding="utf-8", newline="").read()
        t2, n = REF.subn(nuevo, t)
        if n != 1:
            print(f"{rd}: se esperaba 1 referencia al gráfico y hay {n}")
            sys.exit(1)
        if t2 != t:
            open(rd, "w", encoding="utf-8", newline="").write(t2)
            cambios += 1
    print("gráficos actualizados:" if cambios else "sin cambios:", cambios)


if __name__ == "__main__":
    main()
