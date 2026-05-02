# Arquitecto de Soluciones | Legacy Modernization Architect | Senior Full-Stack · AI Automation Architect
**PHP 8 · Python · Go · Node/TS · C# · Ruby · Rust · AWS · Terraform · K8s · n8n · LangGraph/MCP · CI/CD · FinOps · Observabilidad · IA aplicada**

[![Portfolio](https://img.shields.io/badge/🌐_Portfolio_en_vivo-vladimiracunadev--create.github.io-0366d6?style=for-the-badge)](https://vladimiracunadev-create.github.io/)
[![GitHub](https://img.shields.io/badge/GitHub-vladimiracunadev--create-24292f?style=for-the-badge&logo=github)](https://github.com/vladimiracunadev-create)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Vladimir_Acuña-0a66c2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/vladimir-acu%C3%B1a-valdebenito-11924a29/)

Arquitectura, modernización, automatización e IA aplicada a proyectos reales. Diseño, construyo y opero sistemas de producción con foco en **confiabilidad, performance, entrega continua** y **criterio técnico propio**.

- 🧱 +16 años construyendo y operando software en entornos reales (incluye 14+ años en plataformas web educativas/psicométricas)
- ⚙️ Especialidad: performance, mantenibilidad, estabilidad, deuda técnica y continuidad operacional
- 🚀 Enfoque 2026: **Cloud + DevOps + polyglot persistence + repos reproducibles (docker-first) + observabilidad + multiplataforma (PWA/Capacitor) + agentes/IA local**
- ✅ Busco: roles donde el perfil **Arquitecto + Full-Stack + AI Automation** sea una ventaja real — no un genérico

---

## 🧭 Qué encontrarás en ESTE GitHub (no es "un repo", es un sistema)
Este perfil está construido como un portafolio verificable:

- **Demos reproducibles** (clonas, ejecutas, validas)
- **Tooling estandarizado** (Makefiles + "Hub CLI" + doctor/smoke)
- **Defensa en profundidad** (secret scanning, policies, killed practices)
- **Observabilidad** (métricas + dashboards + trazabilidad)
- **Documentación profunda** (reclutador / novato / devops / seguridad, según repo)
- **Multiplataforma** (web → PWA → móvil/desktop via Capacitor, cuando aplica)
- **Internacionalización** (portafolio disponible en 6 idiomas: ES, EN, PT, IT, FR, ZH)

---

## 🆕 Avances consolidados (lo que mejoré recientemente y ya quedó como estándar)
### 1) Observabilidad que se siente "de producción"
- Stack Prometheus/Grafana + métricas accionables (salud del flujo, fallos, estrés interno).
- Dashboards pensados para eliminar la "caja negra" típica de integraciones.
- Endpoints estándar `/health`, `/ready`, `/metrics` por servicio + logging JSON estructurado.
- Ruta completa: *desde el workflow* → *métrica* → *dashboard* → *decisión*.

### 2) Resiliencia (guardrails) implementada, no solo hablada
- **Idempotencia** para evitar duplicados y spam.
- **Circuit breaker** + desvío controlado a DLQ cuando un proveedor se degrada.
- Patrones `Adapter`, `Strangler` y `Circuit Breaker` aplicados a cuellos de botella reales.
- Troubleshooting orientado a "qué revisar primero" (n8n executions, logs, tablas de control).

### 3) Reproducibilidad y DX (Developer Experience) como diseño
- "Hub CLI" multi-OS (bash/powershell/python según repo).
- `doctor` para detectar puertos, Docker, dependencias.
- `smoke` para validar rápido que el sistema está sano.
- Launcher nativo en Go + instalador Windows (.exe) con release automation.
- Estructuras repetibles: docs, roadmap, security, changelog, contribución.

### 4) Cloud delivery profesional (no tutorial)
- Flujo `dev → PR → main` con despliegues reales: AWS Amplify (multi-branch) y GitHub Actions deploy a S3 con OIDC.
- **Journey GitHub Actions × AWS**: cada caso introduce un servicio AWS nuevo y una capacidad de Actions que no existía antes (paths filter, OIDC federation, environments + approvals, matrix strategy, reusable workflows, GHCR, cron, multi-region, GitOps).
- Cobertura activa de objetivos **SAA-C03 · DVA-C02 · SOA-C02** mapeada caso a caso.
- Tooling: AWS CLI · Terraform · SAM · TruffleHog · detect-secrets · wiki sync.
- Seguridad y gobernanza como parte del pipeline (no post-it): OIDC sin credenciales largas, secret scanning, environments con aprobaciones.

### 5) Multiplataforma real (web + PWA + móvil/desktop)
- El portafolio está diseñado como **PWA instalable** y **Android/iOS ready** vía Capacitor.
- **6 idiomas** (ES, EN, PT, IT, FR, ZH) con 30+ PDFs generados por pipeline (CVs, portafolio, logros, recomendaciones).
- Guías profundas para build móvil (APK/IPA), troubleshooting y arquitectura.

### 6) IA aplicada con mentalidad de ingeniería
- **10 backends operativos** sobre LangGraph + FastAPI (casos 01, 02, 03, 04, 05, 09, 10, 13, 19, 25): soporte omnicanal, screening RR.HH. + calendario, onboarding, BI con SQL/charting, analista de documentos.
- Agentes con **estado tipado** (TypedDict), **rutas condicionales**, **resiliencia**, OAuth2/OIDC opt-in, LangSmith opt-in y modo dual (DEMO offline / LIVE).
- IA local con privacidad completa: chat web local (FastAPI + Ollama) + tools MCP en sandbox `data/sandbox` + persistencia SQLite, bind `127.0.0.1`, sin nube obligatoria.
- Servidor MCP de solo lectura para Claude Desktop integrado en la suite de microsistemas (read-only knowledge bridge).

### 7) Polyglot persistence y multi-lenguaje
- **9 casos de integración real** con stacks completos emisor → puente n8n → receptor → DB: Python↔PHP/MySQL, Python↔Go/MariaDB, Go↔Node/PostgreSQL, Node↔FastAPI/SQLite, Laravel↔React/MongoDB, Go↔Symfony/Redis, Rust↔Ruby/Cassandra, .NET↔Flask/SQL Server, Python↔FastAPI/DuckDB.
- **20+ contenedores** orquestados con **11 patrones arquitectónicos**: microservicios, event-driven, mediador, idempotencia, circuit breaker, DLQ, persistencia políglota, observabilidad opt-in, supply-chain hardening, edge proxy con TLS, runtime isolation.
- Interoperabilidad real demostrada con métricas de cada combinación lenguaje × DB.

### 8) Seguridad como pipeline (defense-in-depth, no checklist)
- Auditoría estándar de 8 capas: non-root containers, binding `127.0.0.1`, HTTP security headers, `grype --fail-build`, Trojan Source, nginx + TLS, `detect-secrets`, `pip-compile` + Dependabot.
- Hardening transversal: TruffleHog + Trivy + Bandit + pip-audit + Gitleaks + markdownlint según stack.
- SBOM generado en cada release · K8s NetworkPolicy + runtime isolation donde aplica.

---

## ⭐ Evidencia rápida (repos clave del ecosistema)
> La idea no es "mirar código": es **ver cómo pienso**, cómo documento y cómo hago que todo sea ejecutable.

### 🔥 Cloud Portfolio · GitHub Actions Journey × AWS
**Repo:** https://github.com/vladimiracunadev-create/proyectos-aws
**Qué demuestra:** **11 casos progresivos** donde cada uno introduce un servicio AWS nuevo *y* una capacidad de GitHub Actions que no existía antes. Fase 1 operativa con demos vivas — caso 01 (Amplify multi-branch: [main](https://main.d3r1wuymolxagh.amplifyapp.com/) · [dev](https://dev.d20m8tc0banvg.amplifyapp.com/)) y caso 02 (S3 + paths filter). Fases 2-5 mapeadas: CloudFront + OIDC, Environments + Approvals, Lambda + API Gateway, DynamoDB + Matrix, Reusable Workflows, Containers + GHCR, FinOps + Cron, Multi-región + DR, EKS + GitOps. Cobertura **DVA-C02 · SAA-C03 · SOA-C02** mapeada caso a caso. Pipeline con TruffleHog + detect-secrets + wiki sync.

### 📆 Social Bot Scheduler v4.2.0 · Security Hardened
**Repo:** https://github.com/vladimiracunadev-create/social-bot-scheduler
**Qué demuestra:** Matriz tecnológica con **9 casos de integración** (Python↔PHP, Python↔Go, Go↔Node, Node↔FastAPI, Laravel↔React, Go↔Symfony, Rust↔Ruby, .NET↔Flask, Python↔FastAPI) puenteados por n8n, **20+ contenedores**, **11 patrones arquitectónicos** y **9 motores de DB** (MySQL · MariaDB · PostgreSQL · SQLite · MongoDB · Redis · Cassandra · SQL Server · DuckDB). Auditoría de **8 capas** (contenedor, red, credenciales, servidor web, herramientas, autenticación, CI/CD, supply chain): bind `127.0.0.1`, non-root, HTTP security headers (CSP, HSTS, Permissions-Policy), Caddy edge proxy + TLS + Basic Auth, Trivy + pip-audit + Gitleaks + Trojan Source detection, Dependabot para 11 ecosistemas. Observabilidad opt-in (Prometheus + Grafana en `--profile observability`).

### 🧪 Docker Labs v1.5.0 · Plataforma Docker Modular
**Repo:** https://github.com/vladimiracunadev-create/docker-labs
**Qué demuestra:** **13 labs operativos** organizados en plataforma de 4 servicios (Control Center `:9090` Node.js, Inventory Core API `:8000` Python+PostgreSQL, Operations Portal `:8083` Node+MongoDB+Nginx, Platform Gateway `:8085` Nginx) + 9 labs independientes (Node, PHP/LAMP, Python Flask, Redis, RabbitMQ, Prometheus+Grafana, Go, Elasticsearch, Jenkins LTS). **Instalador `.exe` automatizado para Windows** (workflow `build-windows-installer`), launcher con browser auto-open. CI con smoke tests por lab, docs separadas por audiencia (Beginner Guide, User Manual, Technical Specs, Recruiter Guide).

### 🧰 Microsistemas v3.x · Developer Productivity Suite
**Repo:** https://github.com/vladimiracunadev-create/microsistemas
**Landing:** https://vladimiracunadev-create.github.io/microsistemas/
**Qué demuestra:** **12 microapps web** para diagnóstico, soporte, DevOps, aprendizaje y modernización PHP. Doble modo de uso: stack Docker (`make up` listo en 30 s) o XAMPP local. Incluye KatasMultiLang (195 comparaciones / 67 tecnologías), CicdLibrary (192 patrones CI/CD), AWS Assistant Pro, **servidor MCP local de solo lectura** para Claude Desktop. Hardening en **3 fases** (infraestructura + aplicación + supply-chain): CSRF, rate limiting, TruffleHog, Trivy, Dependabot, markdownlint, SBOM por release. Hub CLI unificado con diagnóstico y smoke testing.

### 🤖 LangGraph RealWorld v4.2.0 · 25 casos · 10 backends operativos
**Repo:** https://github.com/vladimiracunadev-create/langgraph-realworld
**Qué demuestra:** Portafolio de **25 casos empresariales** con **10 backends 100% operativos** (01, 02, 03, 04, 05, 09, 10, 13, 19, 25) — incluye Caso 05 (Analista de Documentos) elevado a OPERATIVO en v4.2.0, soporte omnicanal, HR screening + calendario, onboarding, BI SQL/charting. Estado tipado (TypedDict), modo dual DEMO/LIVE, OAuth2/OIDC opt-in, LangSmith opt-in, endpoints `/health` `/ready` `/metrics` con latencia y errores por servicio, reverse proxy nginx + TLS, logging JSON estructurado, CI por caso. Auditoría de **8 capas** de seguridad: non-root, `127.0.0.1`, HTTP headers, `grype --fail-build`, Trojan Source, nginx TLS, detect-secrets, pip-compile + Dependabot. 15 casos restantes son scaffolds documentados.

### 🧠 MCP + Ollama Local · IA local-first con sandbox MCP
**Repo:** https://github.com/vladimiracunadev-create/mcp-ollama-local
**Qué demuestra:** Web local (FastAPI + Uvicorn, Python 3.13) + chat con Ollama vía `httpx` + bridge MCP por `stdio` con tools acotadas a `data/sandbox`. Persistencia en SQLite, despliegue en local, Docker o K8s. Bind `127.0.0.1:8000`, CORS configurable, API key opcional (`X-API-Key`), rate limiting en memoria, contenedor non-root. **Security & Trust Profile multi-capa**: `ci.yml` (Ruff + Pytest), `security.yml` (Bandit + pip-audit), `codeql.yml` (code scanning semántico), `semgrep.yml` (reglas locales), `supply-chain.yml` (SBOM CycloneDX + firma de release), `scorecard.yml` (señal pública), Dependabot. Honesto sobre límites (no es multi-usuario, no RBAC).

### 🌐 Web/Portafolio v2.2.0 · PWA · 6 idiomas · Lighthouse 100
**Repo:** https://github.com/vladimiracunadev-create/vladimiracunadev-create.github.io
**Web:** https://vladimiracunadev-create.github.io/
**Qué demuestra:** SPA estática profesional en **6 idiomas** (ES/EN/PT/IT/FR/ZH) con sistema de 3 vistas (Reclutador / Normal / Profundo), **30+ PDFs** generados por pipeline Python (CV ATS + CV Reclutador + Portafolio + Carta de Recomendación + Declaración de Logros, todos × 6 idiomas), **PWA instalable** con manifest + service worker, **CV Data API JSON estática** en `api/v1/` (6 endpoints sin servidor), wrapper Capacitor para Android/iOS, **Lighthouse 100**.

### ⚡ Unikernel Labs · Control Center v1.0.0
**Repo:** https://github.com/vladimiracunadev-create/unikernel-labs
**Qué demuestra:** Capa de control Windows sobre runtime Linux real para operar servicios **Unikraft**: Dashboard Node.js (REST API en `localhost:9091`), Launcher WinForms .NET y backend WSL2 con `kraft` + QEMU/KVM. Catálogo único en `labs.config.json` (sincronizado al launcher), 8 labs (de `01-hello-world` a `08-kraft-cloud-track`), arranque real validado de `nginx-runtime` en `localhost:8080`. Workflow de build automatizado para instalador `.exe` de Windows + instalación silenciosa.

### 🍎 ChofyAI Studio · macOS Local AI Launcher · Fase 4
**Repo:** https://github.com/vladimiracunadev-create/chofyai-studio
**Qué demuestra:** Lanzador de escritorio para macOS Apple Silicon (**Tauri + Rust + React**) que centraliza e instala herramientas de IA local: **Qwen3-TTS**, **whisper.cpp**, **FaceFusion**, **AceForge**. Fase 4 entregada: disco dual, zona de módulos con instalación/actualización individual, panel de stats, empaquetado ad-hoc para distribución, soporte `uv` como acelerador opcional para tools Python.

### 🐳 Problem-Driven Systems Lab · 12 casos · multi-stack OPERATIVO
**Repo:** https://github.com/vladimiracunadev-create/problem-driven-systems-lab
**Qué demuestra:** **12 problemas reales de ingeniería** (latencia bajo carga, N+1, observabilidad pobre, retry storms, fugas de memoria, pipelines frágiles, modernización del monolito, extracción crítica, integraciones inestables, sobre-arquitectura, reportes bloqueantes, single point of knowledge) con fallos de alta fidelidad inyectados — no simulaciones abstractas. **Stack PHP 100% OPERATIVO** con UI nativa interactiva (los 12 casos detectan `Accept` de browser y devuelven dashboards), **stack Python 100% OPERATIVO** (12 casos en stdlib pura, autocontenidos), **caso 03 también OPERATIVO en Node.js**. Scaffolds documentados para Java, .NET y Node.js (casos 01-02, 04-12). Patrones profesionales: **Adapter, Strangler, Circuit Breaker**. Compose por lenguaje (`compose.root.yml` PHP · `compose.python.yml` · `compose.portal.yml`), Prometheus `:9091` + Grafana `:3001` + portal `:8080`. Catálogo único en [`shared/catalog/cases.json`](https://github.com/vladimiracunadev-create/problem-driven-systems-lab/blob/main/shared/catalog/cases.json).

### 📊 Python Data Science Bootcamp v1.1.0 · Material docente multiplataforma
**Repo:** https://github.com/vladimiracunadev-create/python-data-science-bootcamp
**Qué demuestra:** Bootcamp con **31 clases** (expansión v1.1.0 · 2026-04-29), notebooks Jupyter interactivos, datasets reales y entorno local configurable. Distribución multiplataforma: **App Desktop Windows** con Edge WebView2, **App Android** con Expo, **PDFs generados** desde el material docente. Diseñado para principiantes y transición profesional hacia análisis de datos.

---

## ⚡ "Si tengo 10 minutos para evaluarte" (rutas de prueba)
### Ruta A — Observabilidad + orquestación real (mi favorita)
```bash
git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git
cd social-bot-scheduler
# Sigue README: HUB + doctor + levantar stack
```
Qué vas a ver: workflows + métricas + dashboards + guardrails.

### Ruta B — Infra reproducible en minutos
```bash
git clone https://github.com/vladimiracunadev-create/docker-labs.git
cd docker-labs
make up-dashboard
# dashboard local (ver README del repo)
```

### Ruta C — IA local con arquitectura clara
```bash
git clone https://github.com/vladimiracunadev-create/mcp-ollama-local.git
cd mcp-ollama-local
# Sigue README (FastAPI + Ollama + SQLite + tools MCP)
```

### Ruta D — Agentes industriales con estado tipado
```bash
git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git
cd langgraph-realworld
# Cualquiera de los 10 backends operativos: 01, 02, 03, 04, 05, 09, 10, 13, 19, 25
```

---

## 🧠 Aprendizajes convertidos en "estándar de repos"
Lo que repetí y reforcé al crecer los commits del portafolio:

- **DX primero**: si no se ejecuta fácil, no sirve como demo ni como base de equipo.
- **Observabilidad no es opcional**: métricas y trazabilidad desde el día 1.
- **Seguridad como pipeline**: secret scanning, checklist, prácticas prohibidas (killed), SBOM por release.
- **Resiliencia**: idempotencia + circuit breaker + "degradación controlada".
- **Polyglot por diseño**: lenguajes y bases de datos elegidos por caso de uso, no por moda.
- **Docs por audiencia**: reclutador / devops / seguridad / estudiante (cuando aplica).

---

## ✅ Alcance profesional real (3 capas, atado a evidencia)

### 🎯 Identidad principal
- **Arquitecto de Soluciones / Solutions Architect** — diseño de sistemas modulares, escalables y con criterio evolutivo
- **Legacy Modernization Architect** — experiencia real en evolución de legacy (PHP 5.x→8.x, SQL, refactor incremental sin cortar operación)
- **Senior Full-Stack Developer / Tech Lead** — arquitectura + ejecución + estándares en plataformas reales (14+ años)
- **AI Automation Architect** — sistemas agénticos con LangGraph/MCP, flujos n8n con guardrails, IA aplicada con validación humana

### ↗ Expansión natural — cargos asumibles con fuerza
- **AI Orchestration Engineer** — agentes con estado tipado, rutas condicionales, resiliencia (LangGraph, FastAPI, MCP)
- **AI Automation Engineer** — orquestación de workflows reales con n8n, Python, circuit breaker e idempotencia
- **Solutions Engineer** — demos y PoCs verificables, comunicación técnico-negocio, requisitos y arquitectura orientada a cliente
- **Technical Product Builder** — construcción end-to-end: arquitectura, desarrollo, operación y entrega con criterio de producto
- **Consultor de Transformación Digital** — diagnóstico, plan evolutivo y ejecución de modernización en organizaciones con legacy real
- **Product Operations Técnico** — continuidad y evolución de plataformas con observabilidad, reducción de fricción y mejora continua

### ⚙️ Alcance complementario (respaldado por experiencia directa)
- Platform Engineer / IDP · DevOps / CI-CD Engineer · Cloud / AWS Engineer
- SRE orientado a aplicaciones · Automation Engineer · Relator Técnico / Technical Trainer
- Consultor Técnico-Comercial (puente TI–negocio)

> *Perfil híbrido verificable: Arquitectura + Delivery + Operación + IA aplicada. No es un listado de aspiraciones — cada punto tiene evidencia en este GitHub.*

---

## 🤖 Flujo de desarrollo asistido por IA (en uso activo)

| Herramienta | Uso principal |
|---|---|
| **Claude Code** | Revisión arquitectónica, implementación y documentación técnica |
| **ChatGPT Plus** | Análisis, arquitectura, iteración y documentación (desde 2023) |
| **Codex** | Generación y refactorización de código |
| **Antigravity** | Aceleración de flujos de desarrollo y automatización |
| **VS Code / OpenCode** | Entornos de desarrollo con asistencia IA integrada |

> *Combino criterio técnico propio, validación humana y dirección arquitectónica. La IA amplifica capacidad, velocidad y alcance — no reemplaza experiencia.*

---

## 📌 Disponibilidad
**Abierto a**: Senior Full-Stack / Arquitectura / Modernización de legado / Platform-IDP / SRE apps / DevOps pragmático / Automatización / AI Automation
**Modalidad**: Remoto / Híbrido (según proyecto)

---

## 📬 Contacto
- LinkedIn: https://www.linkedin.com/in/vladimir-acu%C3%B1a-valdebenito-11924a29/
- Web: https://vladimiracunadev-create.github.io/
- GitLab: https://gitlab.com/vladimir.acuna.dev-group/vladimir.acuna.dev-group
- Email: vladimir.acuna.dev@gmail.com

---

## 📚 Documentación del Proyecto

Como parte de los estándares de este ecosistema, la documentación detallada se divide en:
- [📘 Guía de Instalación y Despliegue (INSTALL.md)](INSTALL.md)
- [📜 Historial de Cambios (CHANGELOG.md)](CHANGELOG.md)
- [🤝 Guía de Contribución (CONTRIBUTING.md)](CONTRIBUTING.md)
- [🛡️ Política de Seguridad (SECURITY.md)](SECURITY.md)
- [⚖️ Código de Conducta (CODE_OF_CONDUCT.md)](CODE_OF_CONDUCT.md)

---

<sub>Última actualización: 2026-05-02 · README sincronizado con el estado real verificado de cada repositorio público.</sub>
