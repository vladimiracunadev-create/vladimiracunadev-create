#!/usr/bin/env python3
"""Paso 3 de 3 — escribe docs/STACK_SOURCES.<idioma>.md (22 idiomas).

Lee docs/data/stack_evidence.json (paso 2), los títulos de scripts/stack_data.json,
las cadenas traducidas de scripts/stack_evidence/i18n.json y los iconos de
scripts/stack_evidence/icons.json. Las tablas son idénticas en todos los idiomas
(nombres de tecnologías y repositorios); solo cambian los textos de alrededor.
"""
import json
import os
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LANGS = ["es", "en", "pt", "it", "fr", "zh", "zh-TW", "ja", "ko", "tr", "ru", "vi", "th", "de", "uk", "pl", "ar", "fa", "id", "nl", "hi", "el"]
GH = "https://github.com/vladimiracunadev-create/"
GL = "https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab"
EMO = ["💻", "🧱", "🏗️", "🗄️", "📊", "☁️", "🟧", "📡", "🧠", "🤖", "🛡️", "🖥️", "🚀"]
# código de evidencia → icono (el orden es el de la leyenda y de las celdas)
ICONO = {"lang": "🧩", "manifest": "📦", "workflow": "⚙️", "docker": "🐳", "iac": "☁️", "path": "📁", "readme": "📝", "curated": "📝"}
ORDEN = ["🧩", "📦", "⚙️", "🐳", "☁️", "📁", "📝"]
VISIBLES = 6          # repositorios que se muestran sin desplegar
TODOS = 60            # a partir de aquí se dice «todos los repositorios»


def sf(lg):
    return "" if lg == "es" else "." + lg


def leer(*ruta):
    return json.load(open(os.path.join(ROOT, *ruta), encoding="utf-8"))


def insignia(etiqueta, valor, color):
    return f"![{etiqueta} {valor}](https://img.shields.io/badge/{urllib.parse.quote(etiqueta, safe='')}-{valor}-{color}?style=for-the-badge)"


def evidencia(hit):
    return "".join(sorted({ICONO[e] for e in hit["evidencia"] if e in ICONO}, key=ORDEN.index))


def enlace_repo(hit):
    if hit["plataforma"] == "gitlab":
        return f"[{hit['repo']}]({GL}) 🦊 {evidencia(hit)}".rstrip()
    return f"[{hit['repo']}]({GH}{hit['repo']}) {evidencia(hit)}".rstrip()


def celda_repos(hits, s, total_repos):
    if len(hits) >= TODOS:
        return f"{s['ALLREPOS']} ([{total_repos}]({GH}?tab=repositories&type=source))"
    vis = " · ".join(enlace_repo(h) for h in hits[:VISIBLES])
    resto = hits[VISIBLES:]
    if resto:
        vis += f" · <details><summary>+{len(resto)} {s['MORE']}</summary>" + " · ".join(enlace_repo(h) for h in resto) + "</details>"
    return vis


def celda_evidencia(hits):
    todo = {ICONO[e] for h in hits for e in h["evidencia"] if e in ICONO}
    return "".join(sorted(todo, key=ORDEN.index)) or "—"


def generar():
    ev = leer("docs", "data", "stack_evidence.json")
    datos = leer("scripts", "stack_data.json")
    i18n = leer("scripts", "stack_evidence", "i18n.json")
    iconos = leer("scripts", "stack_evidence", "icons.json")
    techs = ev["tecnologias"]
    total_repos = ev["meta"]["repositorios_github"]
    unicas = len(techs)
    con_repo = sum(1 for v in techs.values() if v["repos"])
    sin_repo = [n for n, v in techs.items() if not v["repos"]]
    for lg in LANGS:
        s = i18n[lg]
        eco = open(os.path.join(ROOT, "docs", f"ECOSYSTEM{sf(lg)}.md"), encoding="utf-8").read().split("\n")
        volver = eco[2]
        cambio = next(l for l in eco if l.startswith("**🌐**")).replace("ECOSYSTEM", "STACK_SOURCES")
        titulos = datos["titles"][lg]
        L = ['<div align="center">', "", f"# 🔎 {s['T']}", "", volver, "", cambio, "",
             " ".join([insignia(s["SUM_TECH"], unicas, "0969da"), insignia(s["SUM_EV"], con_repo, "1a7f37"), insignia(s["SUM_DECL"], len(sin_repo), "9a6700"),
                       insignia(s["SUM_REPOS"], total_repos + ev["meta"]["repositorios_gitlab"], "6e7681")]),
             "", f"<sub><b>{s['DATE']}:</b> {ev['meta']['fecha']}</sub>", "", "</div>", "", f"> {s['INTRO']}", "",
             f"## 📑 {s['IDX']}", ""]
        for i, t in enumerate(titulos):
            L.append(f"- [{EMO[i]} {t}](#b{i + 1:02d})")
        L += ["- [⚠️ " + s["D_H"] + "](#declarado)", "", f"## 🧭 {s['R_H']}", "", f"1. {s['R1']}", f"2. {s['R2']}", f"3. {s['R3']}", f"4. {s['R4']}", "",
              f"## 🔬 {s['LEG_H']}", "", s["LEG_INTRO"], "", "| | |", "|:-:|---|"]
        for ic, k in zip(ORDEN, ["E_LANG", "E_MAN", "E_WF", "E_DOCK", "E_IAC", "E_PATH", "E_DOC"]):
            L.append(f"| {ic} | {s[k]} |")
        L += [f"| 🦊 | {s['GL_NOTE']} |", ""]
        vistos = set()
        for b, items in enumerate(datos["items"]):
            L += [f'<a id="b{b + 1:02d}"></a>', "", f"## {EMO[b]} {titulos[b]} · {len(items)}", "",
                  f"| | {s['TH_TECH']} | {s['TH_WHERE']} | {s['TH_EV']} |", "|:-:|---|---|:-:|"]
            for n in items:
                hits = techs[n]["repos"]
                slug = iconos.get(n)
                if slug == "__local__":
                    ico = '<img src="https://raw.githubusercontent.com/vladimiracunadev-create/vladimiracunadev-create/main/docs/img/icon-powerbi.svg" width="24" height="24" alt="">'
                elif slug:
                    ico = f'<img src="https://skillicons.dev/icons?i={slug}" width="24" height="24" alt="">'
                else:
                    ico = ""
                if hits:
                    L.append(f"| {ico} | **{n}** | {celda_repos(hits, s, total_repos)} | {celda_evidencia(hits)} |")
                else:
                    L.append(f"| {ico} | **{n}** | _{s['NONE']}_ | — |")
            L.append("")
        L += ['<a id="declarado"></a>', "", f"## ⚠️ {s['D_H']}", "", s["D_INTRO"], ""]
        L += [f"- {s['D1']}", f"- {s['D2']}", f"- {s['D3']}", "", f"## ✅ {s['V_H']}", "", s["V_INTRO"], "",
              "```bash", "gh repo list vladimiracunadev-create --visibility public --source --limit 200",
              "gh api repos/vladimiracunadev-create/<repo>/languages", 'gh search code "<tech>" --owner vladimiracunadev-create', "```", "",
              f"## 🔄 {s['M_H']}", "", f"- {s['M1']}", f"- {s['M2']}", "", f"## 🚧 {s['X_H']}", "", f"- {s['X1']}", f"- {s['X2']}", ""]
        open(os.path.join(ROOT, "docs", f"STACK_SOURCES{sf(lg)}.md"), "w", encoding="utf-8", newline="\n").write("\n".join(L))
    print("documentos:", len(LANGS), "| tecnologías únicas:", unicas, "| con repositorio:", con_repo, "| declaradas:", sin_repo)


if __name__ == "__main__":
    generar()
