#!/usr/bin/env python3
"""Genera el gráfico SVG del Stack tecnológico (docs/img/stack.<idioma>.svg).

Las tecnologías y los títulos de cada categoría (por idioma) viven en
scripts/stack_data.json: es la fuente de verdad del Stack; el README solo
muestra el gráfico y la evidencia que el gráfico no contiene.
Los logos se incrustan en el SVG (sin depender de internet) desde una caché
(scripts/stack_icons.json); si falta, se descarga de skillicons.dev y
simple-icons y se guarda.

Uso, desde la raíz del repositorio:

    python3 scripts/stack_graphic.py            # genera los 22 SVG y sella los nombres
    python3 scripts/stack_graphic.py --refresh   # vuelve a descargar los logos

Para cambiar el Stack, edita scripts/stack_data.json y vuelve a ejecutarlo.
Requiere Pillow (medir texto) y opencc-python-reimplemented (chino tradicional).
"""
import base64
import concurrent.futures as cf
import glob
import json
import os
import re
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAIZ)
from PIL import ImageFont  # noqa: E402

FUENTE = next((p for p in (r"C:\Windows\Fonts\arial.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
                           "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/Library/Fonts/Arial.ttf") if os.path.exists(p)), None)
LANGS = ["es", "en", "pt", "it", "fr", "zh", "zh-TW", "ja", "ko", "tr", "ru", "vi", "th", "de", "uk", "pl", "ar", "fa", "id", "nl", "hi", "el"]
NOTA = {
    "es": "evidencia de uso, no años de experiencia", "en": "evidence of use, not years of experience",
    "pt": "evidência de uso, não anos de experiência", "it": "evidenza d'uso, non anni di esperienza",
    "fr": "preuve d'usage, pas des années d'expérience", "de": "Nutzungsnachweis, keine Berufsjahre",
    "nl": "bewijs van gebruik, geen jaren ervaring", "id": "bukti penggunaan, bukan tahun pengalaman",
    "tr": "kullanım kanıtı, deneyim yılı değil", "pl": "dowód użycia, nie lata doświadczenia",
    "ru": "свидетельство использования, а не лет опыта", "uk": "свідчення використання, а не років досвіду",
    "zh": "使用证据，而非工作年限", "zh-TW": "使用證據，而非工作年資", "ja": "使用の証拠であり、経験年数ではありません", "ko": "사용 근거이며 경력 연수가 아닙니다",
    "vi": "bằng chứng sử dụng, không phải số năm kinh nghiệm", "th": "หลักฐานการใช้งาน ไม่ใช่จำนวนปีประสบการณ์",
    "ar": "دليل على الاستخدام لا سنوات الخبرة", "fa": "شواهد استفاده، نه سال‌های تجربه",
    "hi": "उपयोग का प्रमाण, अनुभव के वर्ष नहीं", "el": "απόδειξη χρήσης, όχι έτη εμπειρίας",
}
EMO = ["💻", "🧱", "🏗️", "🗄️", "📊", "☁️", "🟧", "📡", "🧠", "🤖", "🛡️", "🖥️", "🚀"]
PAL = [("#ddf4ff", "#0969da", "#0a3069"), ("#ddf4ff", "#0969da", "#0a3069"), ("#fbefff", "#8250df", "#3b1d73"),
       ("#dafbe1", "#1a7f37", "#0f3d1e"), ("#fff8c5", "#9a6700", "#4d2d00"), ("#fff1e5", "#bc4c00", "#5c2200"),
       ("#fff1e5", "#bc4c00", "#5c2200"), ("#ffeff7", "#bf3989", "#5c1541"), ("#fbefff", "#8250df", "#3b1d73"),
       ("#fbefff", "#8250df", "#3b1d73"), ("#ffeff7", "#bf3989", "#5c1541"), ("#f6f8fa", "#6e7781", "#24292f"),
       ("#f6f8fa", "#6e7781", "#24292f")]
# bloques cuyos elementos salen de las insignias (alt) y no del <sub>
DESDE_INSIGNIAS = {2, 6, 9, 10}
ICONOS = {
    "JavaScript": ["js"], "TypeScript": ["ts"], "Python": ["py"], "C#": ["cs"], "WebAssembly": ["wasm"], "F#": ["fsharp"],
    "GDScript": ["godot"], "HCL": ["terraform"], "Node.js": ["nodejs"], "Spring Boot": ["spring"], "ASP.NET / .NET": ["dotnet"],
    "Qt / PySide6": ["qt"], "scikit-learn": ["sklearn"], "Transformers": ["huggingface"], "PEFT / LoRA": ["huggingface"],
    "PostgreSQL": ["postgres"], "SQL Server": ["microsoftsqlserver"], "pgvector": ["postgres"], "GabySQL (Rust)": ["rust"],
    "PostgREST": ["postgresql"], "Power BI (.pbix ×3)": ["__powerbi__"], "Docker / Compose": ["docker"],
    "Google Cloud": ["gcp"], "GitHub Actions": ["githubactions"], "OpenTelemetry": ["opentelemetry"],
    "MQTT (Mosquitto)": ["mqtt"], "Elasticsearch / Kibana": ["kibana", "elasticsearch"], "Claude Code": ["claude"],
    "Claude Skills": ["claude"], "Codex Skills": ["openai"], "Codex": ["openai"], "ChatGPT Plus": ["openai"],
    "Whisper": ["openai"], "MCP": ["modelcontextprotocol"], "LangGraph": ["langchain"], "VS Code": ["vscode"],
    "CodeQL": ["github"], "Dependabot": ["dependabot"], "macOS": ["apple"], "iOS": ["apple"],
    "Android": ["androidstudio"], "Web / PWA": ["html"], "GitHub Pages": ["github"], "Antigravity": ["google"],
    "Inno Setup": [], "CI/CD": [], "FinOps": [], "Make": [], "SQL": [], "DAX": [], "Star schema": [], "RAG": [],
    "Agentic Plugins": [], "OpenCode": [],
}


def descargar(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read()
    except Exception:
        return None


def bloques(readme):
    """Devuelve (título H2, [(título, texto del bloque)]) de la sección Stack."""
    t = open(readme, encoding="utf-8").read()
    sec = re.search(r"\n## 🛠️([^\n]*)\n(.*?)(?=\n## )", t, re.S)
    partes = re.split(r"\n\*\*([^*\n]+)\*\*\n", "\n" + sec.group(2))
    return sec.group(1).strip(), [(partes[i], partes[i + 1]) for i in range(1, len(partes), 2)]


def elementos(idx, texto):
    if idx in DESDE_INSIGNIAS:
        return re.findall(r"!\[([^\]]*)\]\(https://img\.shields\.io", texto)
    sub = re.search(r"<sub>(.*?)</sub>", texto, re.S)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", sub.group(1))
    if idx == 4:
        s = s.split(" → ")[0]
    if idx == 12:
        s = re.sub(r"\s*\([^)]*\)", "", s)
    return [x.strip() for x in s.split(" · ") if x.strip()]


def icono(nombre, hexes):
    cand = ICONOS.get(nombre, [re.sub(r"[^a-z0-9]", "", nombre.lower())])
    for c in cand:
        if c == "__powerbi__":
            return open("docs/img/icon-powerbi.svg", "rb").read()
        b = descargar(f"https://skillicons.dev/icons?i={c}")
        if b and len(b) > 400 and b"<svg" in b:
            return b
        b = descargar(f"https://cdn.jsdelivr.net/npm/simple-icons@13.21.0/icons/{c}.svg")
        if b and b"<path" in b:
            h = hexes.get(c, "FFFFFF")
            col = h if sum(int(h[i:i + 2], 16) for i in (0, 2, 4)) > 150 else "FFFFFF"
            d = re.search(rb'd="([^"]+)"', b).group(1).decode()
            return (f'<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 48 48"><rect width="48" height="48" rx="10" fill="#242938"/>'
                    f'<g transform="translate(9,9) scale(1.25)"><path fill="#{col}" d="{d}"/></g></svg>').encode()
    return None


def cache_iconos(nombres, refrescar):
    ruta = "scripts/stack_icons.json"
    cache = {} if refrescar or not os.path.exists(ruta) else json.load(open(ruta, encoding="utf-8"))
    faltan = [n for n in nombres if n not in cache]
    if faltan:
        datos = json.loads(descargar("https://cdn.jsdelivr.net/npm/simple-icons@13.21.0/_data/simple-icons.json") or b"{}")
        hexes = {re.sub(r"[^a-z0-9]", "", x["title"].lower()): x["hex"] for x in datos.get("icons", [])}
        with cf.ThreadPoolExecutor(12) as ex:
            for n, b in zip(faltan, ex.map(lambda n: icono(n, hexes), faltan)):
                cache[n] = base64.b64encode(b).decode() if b else None
        json.dump(cache, open(ruta, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    return {k: v for k, v in cache.items() if v}


def construir(lg, titulos, h2, items, iconos):
    f = ImageFont.truetype(FUENTE, 11)
    W, PAD, CH, GAP, RG, IC = 480, 12, 22, 5, 6, 16
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;")
    cajas = []
    for k, (tit, its) in enumerate(zip(titulos, items)):
        filas, x = [[]], 0
        for it in its:
            w = f.getlength(it) + 14 + IC + 6
            if x + w > W - 2 * PAD and filas[-1]:
                filas.append([]); x = 0
            filas[-1].append((it, w)); x += w + GAP
        cajas.append((k, tit, its, filas, 34 + len(filas) * (CH + RG) + PAD - RG))
    cols, hs = [[], []], [66, 66]
    for b in cajas:
        c = 0 if hs[0] <= hs[1] else 1
        cols[c].append(b); hs[c] += b[4] + 10
    H = max(hs) + 6
    usados = {}
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1000 {H}" width="1000" height="{H}" role="img" aria-labelledby="t" '
           f"font-family=\"system-ui,-apple-system,'Segoe UI',Roboto,'Noto Sans','Noto Sans CJK SC','Noto Sans Arabic','Noto Sans Thai','Noto Sans Devanagari',Arial,sans-serif\">",
           f'<title id="t">🛠️ {esc(h2)}</title>', "@@DEFS@@",
           f'<rect x="0.7" y="0.7" width="998.6" height="{H - 1.4}" rx="12" fill="#ffffff" stroke="#d0d7de"/>',
           '<rect x="16" y="16" width="968" height="40" rx="8" fill="#1f2328"/>',
           f'<text x="32" y="41" font-size="14" font-weight="bold" fill="#ffffff">🛠️ {esc(h2)}</text>',
           f'<text x="968" y="40" text-anchor="end" font-size="11" fill="#c9d1d9" font-style="italic">{esc(NOTA[lg])}</text>']
    for ci, col in enumerate(cols):
        x0, y = 16 + ci * (W + 8), 66
        for k, tit, its, filas, h in col:
            bg, bd, tx = PAL[k]
            out.append(f'<rect x="{x0}" y="{y}" width="{W}" height="{h}" rx="8" fill="{bg}" stroke="{bd}" stroke-width="1.4"/>')
            out.append(f'<text x="{x0 + PAD}" y="{y + 22}" font-size="13" font-weight="bold" fill="{tx}">{EMO[k]} {esc(tit)} · {len(its)}</text>')
            yy = y + 34
            for fila in filas:
                xx = x0 + PAD
                for it, w in fila:
                    out.append(f'<rect x="{xx}" y="{yy}" width="{w:.1f}" height="{CH}" rx="11" fill="#ffffff" stroke="{bd}" stroke-opacity="0.55"/>')
                    if it in iconos:
                        idn = usados.setdefault(it, f"i{len(usados)}")
                        out.append(f'<use href="#{idn}" x="{xx + 4}" y="{yy + 3}"/>')
                    else:
                        out.append(f'<circle cx="{xx + 4 + IC / 2}" cy="{yy + CH / 2}" r="3" fill="{bd}" fill-opacity="0.8"/>')
                    out.append(f'<text x="{xx + 6 + IC + 4}" y="{yy + 15}" font-size="11" fill="#1f2328">{esc(it)}</text>')
                    xx += w + GAP
                yy += CH + RG
            y += h + 10
    defs = "<defs>" + "".join(f'<image id="{i}" width="{IC}" height="{IC}" href="data:image/svg+xml;base64,{iconos[n]}"/>' for n, i in usados.items()) + "</defs>"
    out.append("</svg>")
    svg = "\n".join(out).replace("@@DEFS@@", defs)
    ET.fromstring(svg.encode("utf-8"))
    return svg


def main():
    if FUENTE is None:
        sys.exit("No se encontró una fuente para medir el texto")
    datos = json.load(open("scripts/stack_data.json", encoding="utf-8"))
    items = datos["items"]
    if len(items) != len(EMO):
        sys.exit(f"Se esperaban {len(EMO)} bloques y hay {len(items)}")
    iconos = cache_iconos(sorted({i for its in items for i in its}), "--refresh" in sys.argv)
    for lg in LANGS:
        rd = "README.md" if lg == "es" else f"README.{lg}.md"
        h2, _ = bloques(rd)
        titulos = datos["titles"][lg]
        if len(titulos) != len(items):
            sys.exit(f"{lg}: {len(titulos)} títulos y se esperaban {len(items)}")
        svg = construir(lg, titulos, h2, items, iconos)
        for viejo in glob.glob(f"docs/img/stack.{lg}." + "[0-9a-f]" * 8 + ".svg"):
            os.remove(viejo)  # la versión sellada anterior; graphic_names.py estrena la nueva
        open(f"docs/img/stack.{lg}.svg", "w", encoding="utf-8", newline="\n").write(svg)
    print("SVG generados:", len(LANGS), "| con logo:", sum(1 for its in items for i in its if i in iconos), "de", sum(len(i) for i in items))
    subprocess.run([sys.executable, "-X", "utf8", "scripts/graphic_names.py"], check=True)


if __name__ == "__main__":
    main()
