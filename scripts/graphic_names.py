#!/usr/bin/env python3
"""Pone un sello de contenido en el nombre de cada gráfico del perfil.

GitHub (raw.githubusercontent.com) guarda en caché cada URL de imagen y no la
renueva aunque el archivo cambie, ni con Ctrl+F5. Si el nombre incluye un hash
del contenido, cada cambio del gráfico estrena una URL y el perfil lo muestra
al instante.

Familias: ecosystem (gráfico del ecosistema) y stack (gráfico del Stack
tecnológico, generado por scripts/stack_graphic.py).

Uso (desde la raíz del repositorio, tras editar un SVG):

    python3 scripts/graphic_names.py

Renombra docs/img/<familia>.<idioma>[.<hash>].svg a
docs/img/<familia>.<idioma>.<hash>.svg y actualiza la referencia en el README
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

FAMILIAS = ("ecosystem", "stack")


def readme_de(lg):
    return "README.md" if lg == "es" else f"README.{lg}.md"


def actuales(fam, lg):
    """Archivos vigentes de ese idioma (con o sin sello)."""
    sel = glob.glob(f"docs/img/{fam}.{lg}.svg") + glob.glob(f"docs/img/{fam}.{lg}." + "[0-9a-f]" * 8 + ".svg")
    return sorted(s.replace("\\", "/") for s in sel)


def main():
    cambios = 0
    for fam in FAMILIAS:
        patron = re.compile(rf"docs/img/{fam}\.([A-Za-z-]+?)(?:\.[0-9a-f]{{8}})?\.svg$")
        idiomas = sorted({m.group(1) for f in glob.glob(f"docs/img/{fam}.*.svg") for m in [patron.match(f.replace("\\", "/"))] if m})
        ref = re.compile(rf"docs/img/{fam}\.([A-Za-z-]+?)(?:\.[0-9a-f]{{8}})?\.svg")
        for lg in idiomas:
            archivos = actuales(fam, lg)
            if len(archivos) != 1:
                print(f"{fam}/{lg}: se esperaba 1 archivo y hay {len(archivos)}: {archivos}")
                sys.exit(1)
            src = archivos[0]
            h = hashlib.sha1(open(src, "rb").read()).hexdigest()[:8]
            nuevo = f"docs/img/{fam}.{lg}.{h}.svg"
            if src != nuevo:
                if subprocess.run(["git", "mv", src, nuevo], capture_output=True).returncode != 0:
                    os.rename(src, nuevo)  # archivo todavía sin versionar
                cambios += 1
            rd = readme_de(lg)
            t = open(rd, encoding="utf-8", newline="").read()
            t2, n = ref.subn(nuevo, t)
            if n != 1:
                print(f"{rd}: se esperaba 1 referencia al gráfico {fam} y hay {n}")
                sys.exit(1)
            if t2 != t:
                open(rd, "w", encoding="utf-8", newline="").write(t2)
                cambios += 1
    print("gráficos actualizados:" if cambios else "sin cambios:", cambios)


if __name__ == "__main__":
    main()
