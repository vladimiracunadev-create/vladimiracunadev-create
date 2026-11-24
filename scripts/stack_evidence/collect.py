#!/usr/bin/env python3
"""Paso 1 de 3 — recoge la evidencia de los repositorios públicos propios.

Descarga, de cada repositorio público propio de la cuenta (y del proyecto
proyectos-aws-gitlab, alojado en GitLab), el árbol de archivos, las estadísticas
de lenguajes, los manifiestos de dependencias, los workflows, los Dockerfile y
Compose, los archivos de infraestructura y el README. Lo guarda en
.cache/stack_evidence/ (no se versiona).

    python3 scripts/stack_evidence/collect.py
    python3 scripts/stack_evidence/detect.py
    python3 scripts/stack_evidence/render.py

Requiere la CLI de GitHub (`gh`) autenticada. Los repositorios ya descargados se
reutilizan: borra .cache/stack_evidence/ para volver a recogerlo todo.
"""
import concurrent.futures as cf
import json
import os
import re
import subprocess
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, ".cache", "stack_evidence")
os.makedirs(OUT, exist_ok=True)
U = "vladimiracunadev-create"
GITLAB = "vladimir.acuna.dev-group/proyectos-aws-gitlab"


def gh(args):
    r = subprocess.run(["gh", "api"] + args, capture_output=True, text=True, encoding="utf-8")
    return r.stdout if r.returncode == 0 else None


def descargar(url, limite=80_000):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as r:
            return r.read(limite).decode("utf-8", "replace")
    except Exception:
        return None


def raw(repo, path, branch):
    return descargar(f"https://raw.githubusercontent.com/{U}/{repo}/{branch}/{path}")


SKIP = re.compile(r"(^|/)(node_modules|vendor|\.venv|venv|dist|build|target|\.git|\.terraform|__pycache__)/")
MANIFEST = re.compile(r"(^|/)(package\.json|pyproject\.toml|requirements[^/]*\.txt|Pipfile|Cargo\.toml|go\.mod|composer\.json|pom\.xml|build\.gradle(\.kts)?|Gemfile|pubspec\.yaml|mix\.exs|Package\.swift|[^/]+\.(csproj|fsproj)|shard\.yml|deps\.edn|project\.clj|rebar\.config|build\.zig(\.zon)?|gleam\.toml|foundry\.toml|hardhat\.config\.[jt]s)$")
WORKFLOW = re.compile(r"^\.github/(workflows/[^/]+\.ya?ml|dependabot\.ya?ml)$")
DOCKER = re.compile(r"(^|/)(Dockerfile[^/]*|docker-compose[^/]*\.ya?ml|compose[^/]*\.ya?ml)$")
IAC = re.compile(r"(\.tf$|(^|/)template\.ya?ml$|(^|/)samconfig\.toml$|(^|/)\.gitlab-ci\.yml$|(^|/)amplify\.yml$|(^|/)vercel\.json$|(^|/)wrangler\.toml$|(^|/)netlify\.toml$|(^|/)serverless\.ya?ml$|(^|/)Chart\.ya?ml$|(^|/)kustomization\.ya?ml$)")
CAPS = {"manifest": 70, "workflow": 40, "docker": 40, "iac": 40, "extra": 1}


def recoger(repo):
    f = os.path.join(OUT, repo + ".json")
    if os.path.exists(f):
        return repo, "en caché"
    info = json.loads(gh([f"repos/{U}/{repo}"]) or "{}")
    rama = info.get("default_branch", "main")
    arbol = json.loads(gh([f"repos/{U}/{repo}/git/trees/{rama}?recursive=1"]) or "{}")
    rutas = [t["path"] for t in arbol.get("tree", []) if t["type"] == "blob" and not SKIP.search(t["path"])]
    langs = json.loads(gh([f"repos/{U}/{repo}/languages"]) or "{}")
    sel = {"manifest": [], "workflow": [], "docker": [], "iac": [], "extra": []}
    for p in rutas:
        if MANIFEST.search(p): sel["manifest"].append(p)
        elif WORKFLOW.match(p): sel["workflow"].append(p)
        elif DOCKER.search(p): sel["docker"].append(p)
        elif IAC.search(p): sel["iac"].append(p)
        elif p == "README.md": sel["extra"].append(p)
    files = {}
    for k, lst in sel.items():
        for p in sorted(lst, key=lambda x: (x.count("/"), x))[:CAPS[k]]:
            t = raw(repo, p, rama)
            if t is not None:
                files[p] = (k, t)
    json.dump({"repo": repo, "platform": "github", "branch": rama, "description": info.get("description"), "paths": rutas,
               "truncated": arbol.get("truncated", False), "languages": langs, "files": files},
              open(f, "w", encoding="utf-8"), ensure_ascii=False)
    return repo, f"{len(rutas)} rutas, {len(files)} archivos"


def codigo_de_aws_desktop_studio():
    """Añade el código fuente de aws-desktop-studio: ahí se ve qué servicios de AWS consulta de verdad."""
    f = os.path.join(OUT, "aws-desktop-studio.json")
    if not os.path.exists(f):
        return
    d = json.load(open(f, encoding="utf-8"))
    cands = [p for p in d["paths"] if re.search(r"\.(m?js|ts)$", p) and not re.search(r"(^|/)(test|tests|__tests__|dist|assets|vendor)/|\.test\.|\.spec\.", p)]
    for p in sorted(cands, key=lambda p: (p.count("/"), p))[:40]:
        t = raw("aws-desktop-studio", p, d["branch"])
        if t is not None:
            d["files"][p] = ["code", t]
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False)


def recoger_gitlab():
    """proyectos-aws-gitlab vive en GitLab: se lee con la API pública de GitLab."""
    f = os.path.join(OUT, "proyectos-aws-gitlab.json")
    if os.path.exists(f):
        return
    pid = urllib.parse.quote(GITLAB, safe="")
    rutas, pagina = [], 1
    while pagina < 60:
        d = json.loads(descargar(f"https://gitlab.com/api/v4/projects/{pid}/repository/tree?recursive=true&per_page=100&page={pagina}", 5_000_000) or "[]")
        if not d:
            break
        rutas += [x["path"] for x in d if x["type"] == "blob"]
        pagina += 1
    rutas = [p for p in rutas if not SKIP.search(p)]
    sel = re.compile(r"(\.tf$|(^|/)template\.ya?ml$|(^|/)\.gitlab-ci\.yml$|(^|/)package\.json$|(^|/)requirements[^/]*\.txt$|(^|/)Dockerfile[^/]*$|docker-compose[^/]*\.ya?ml$|(^|/)amplify\.yml$|(^|/)samconfig\.toml$|(^|/)README\.md$|(^|/)[a-z\-]+\.ya?ml$)")
    files = {}
    for p in sorted(rutas, key=lambda x: (x.count("/"), x)):
        if sel.search(p) and len(files) < 150:
            t = descargar(f"https://gitlab.com/api/v4/projects/{pid}/repository/files/{urllib.parse.quote(p, safe='')}/raw?ref=main")
            if t is None:
                continue
            tipo = "iac" if re.search(r"(\.tf$|template\.ya?ml$|\.gitlab-ci|amplify|samconfig)", p) else "manifest" if re.search(r"package\.json|requirements", p) else "docker" if re.search(r"Dockerfile|docker-compose", p) else "extra"
            files[p] = (tipo, t)
    json.dump({"repo": "proyectos-aws-gitlab", "platform": "gitlab", "url": f"https://gitlab.com/{GITLAB}", "branch": "main",
               "description": "GitLab → AWS", "paths": rutas, "truncated": False, "languages": {}, "files": files},
              open(f, "w", encoding="utf-8"), ensure_ascii=False)


def main():
    repos = [l.strip() for l in subprocess.run(["gh", "repo", "list", U, "--limit", "300", "--visibility", "public", "--source", "--json", "name", "--jq", ".[].name"],
                                                capture_output=True, text=True, encoding="utf-8").stdout.split("\n") if l.strip()]
    print(len(repos), "repositorios públicos propios")
    with cf.ThreadPoolExecutor(6) as ex:
        for r, msg in ex.map(recoger, repos):
            print(r, msg)
    codigo_de_aws_desktop_studio()
    recoger_gitlab()


if __name__ == "__main__":
    main()
