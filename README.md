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
- Flujo `dev → PR → main` y despliegues reales con GitHub Actions / Amplify.
- **15 casos AWS — 14 completados, 1 pendiente (Caso M · Resiliencia/Failover)** documentados en [GitLab monorepo](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab).
- Cobertura ~68% SAA-C03 · ~68% DVA-C02 · ~50% SOA-C02 (incluye Caso I · Bedrock + Claude Haiku 4.5 + Lambda + xray-sdk y Caso O · X-Ray distribuido).
- Tooling cloud: AWS CLI + Terraform + SAM + validaciones y checklist.
- Seguridad y gobernanza como parte del pipeline (no post-it).

### 5) Multiplataforma real (web + PWA + móvil/desktop)
- El portafolio está diseñado como **PWA instalable** y **Android/iOS ready** vía Capacitor.
- **6 idiomas** (ES, EN, PT, IT, FR, ZH) con 30+ PDFs generados por pipeline (CVs, portafolio, logros, recomendaciones).
- Guías profundas para build móvil (APK/IPA), troubleshooting y arquitectura.

### 6) IA aplicada con mentalidad de ingeniería
- Portal unificado con **10 backends operativos** sobre LangGraph + FastAPI: soporte omnicanal, screening RR.HH., onboarding, BI con SQL/charting y más (casos 01, 02, 03, 04, 05, 09, 10, 13, 19, 25).
- Agentes con **estado tipado** (TypedDict), **rutas condicionales**, **resiliencia**, OAuth2/OIDC opt-in y modo dual (offline demo + live).
- IA local para privacidad: chat local + tools MCP seguras + persistencia en SQLite + K8s ready.
- Workspace local-first (Trihorn Chat) para orquestación modular de LLMs sin nube obligatoria.

### 7) Polyglot persistence y multi-lenguaje
- Matriz de **9 ejes de integración**: Python, Go, Node.js, PHP, Ruby, Rust, C#, Flask, Symfony.
- **12+ motores de datos**: MySQL, MariaDB, PostgreSQL, SQL Server, MongoDB, Cassandra, Redis, SQLite, DuckDB + más.
- Interoperabilidad real demostrada con métricas de cada combinación lenguaje×DB.

### 8) Seguridad como pipeline (defense-in-depth, no checklist)
- Auditoría estándar de 8 capas: non-root containers, binding `127.0.0.1`, HTTP security headers, `grype --fail-build`, Trojan Source, nginx + TLS, `detect-secrets`, `pip-compile` + Dependabot.
- Hardening transversal: TruffleHog + Trivy + Bandit + pip-audit + Gitleaks + markdownlint según stack.
- SBOM generado en cada release · K8s NetworkPolicy + runtime isolation donde aplica.

---

## ⭐ Evidencia rápida (repos clave del ecosistema)
> La idea no es "mirar código": es **ver cómo pienso**, cómo documento y cómo hago que todo sea ejecutable.

### 🔥 Cloud Portfolio (AWS + CI/CD + seguridad + flujo profesional)
**Repo:** https://github.com/vladimiracunadev-create/proyectos-aws
**Mirror público (monorepo):** https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab
**Qué demuestra:** 14 casos AWS cerrados (de 15) con deploy real + estándar profesional + security mindset + docs por perfil (reclutador/devops/seguridad). Cobertura activa SAA-C03 · DVA-C02 · SOA-C02.

### 📆 Social Bot Scheduler v4.x (n8n + Polyglot Persistence + Observabilidad + Guardrails)
**Repo:** https://github.com/vladimiracunadev-create/social-bot-scheduler
**Qué demuestra:** Orquestación real con 9 ejes de integración (Python/Go/Node/PHP/Ruby/Rust/C#/Flask/Symfony), polyglot persistence (12+ DBs), observabilidad industrial (Prometheus/Grafana), idempotencia/circuit breaker, seguridad (Trivy/Gitleaks/K8s NetworkPolicy + runtime isolation).

### 🧪 Docker Labs v1.5.0 (infra y stacks "levanta en 60s" + K8s ready)
**Repo:** https://github.com/vladimiracunadev-create/docker-labs
**Qué demuestra:** 12 labs integrados con centro de control unificado (port 9090), Inventory Core API, Operations Portal, Platform Gateway. Launcher nativo en Go, instalador Windows automatizado, ruta de observabilidad (Prometheus/Grafana), manifiestos K8s.

### 🧰 Microsistemas (Developer Productivity Suite: 11 herramientas + MCP server)
**Repo:** https://github.com/vladimiracunadev-create/microsistemas
**Qué demuestra:** 11 herramientas modulares incluyendo KatasMultiLang (195 comparaciones / 67 tecnologías), CicdLibrary (192 patrones CI/CD), AWS Assistant Pro, servidor MCP Python para integración con IA. Hardening en 3 fases (TruffleHog + Trivy + Dependabot + markdownlint) y SBOM en cada release. Hub CLI con diagnóstico y smoke testing.

### 🤖 LangGraph RealWorld v4.2.0 (25 casos · 10 backends operativos)
**Repo:** https://github.com/vladimiracunadev-create/langgraph-realworld
**Qué demuestra:** 25 casos empresariales con **10 backends operativos** (01, 02, 03, 04, 05, 09, 10, 13, 19, 25): soporte omnicanal, HR screening + calendario, onboarding, BI SQL/charting. Estado tipado (TypedDict), modo dual offline/live, OAuth2/OIDC opt-in, LangSmith opt-in, `/health`/`/ready`/`/metrics`, reverse proxy nginx + TLS, CI por caso. Auditoría de 8 capas de seguridad.

### 🧠 MCP + Ollama Local (IA local: FastAPI + tools MCP seguras + SQLite + K8s)
**Repo:** https://github.com/vladimiracunadev-create/mcp-ollama-local
**Qué demuestra:** IA aplicada con privacidad y arquitectura clara: persistencia SQLite, tools sandbox, tests, manifiestos k8s. Security & Trust Profile activo (Bandit + pip-audit + secret scanning).

### 🤖 Trihorn Chat v0.10.1 (Industrial AI Orchestrator · local-first)
**Repo:** https://github.com/vladimiracunadev-create/trihorn-chat
**Qué demuestra:** Workspace técnico modular para orquestación de LLMs, gestión de conocimiento y automatización de tareas de ingeniería. Corre 100% en `localhost`, sin nube obligatoria. CI backend + frontend, Security Scan, Dependabot, manuales separados (usuario / técnico), auto-compactación y UI minimalista.

### 🔩 FerreMarket (POS Cloud + Marketplace · Node 20 · PostgreSQL · Redis · BullMQ)
**Repo:** https://github.com/vladimiracunadev-create/ferremarket
**Qué demuestra:** Sistema POS cloud + marketplace para ferreterías con punto de venta físico, inventario unificado y e-commerce integrado. Node 20 · Express 4.22 · PostgreSQL 16 · Redis 7.2 · BullMQ · JWT · Docker Compose · OpenTelemetry. CI + Security Scan + Health Check como workflows separados.

### 🤖 Flujo Autónomo (Orquestador local Windows · JSON declarativo · Playwright · SQLite)
**Repo:** https://github.com/vladimiracunadev-create/flujo-autonomo-repo
**Qué demuestra:** Control local de tareas y acciones efectivas sobre Windows: abre ventanas reales, llena formularios, captura escritorio y DOM, audita el equipo. Flujos declarativos en JSON · scheduler · OCR/visión · UI dry-run · Python 3.10+ con `uv` · 79 tests pytest · CI + Security + Workflow security.

### 🗄️ GabySQL (Base de datos embebida en Rust · multiplataforma · single-file `.db` + WAL)
**Repo:** https://github.com/vladimiracunadev-create/gabysql
**Qué demuestra:** Motor de base de datos embebido escrito en Rust pensado como producto base serio: storage claro, formato en disco entendible, durabilidad por WAL y CI multi-OS (Windows/Linux/macOS). Superficie SQL `CREATE`/`INSERT`/`SELECT`/`WHERE PK`/`LIMIT/OFFSET`, API HTTP/JSON y admin web liviano.

### 🌐 Web/Portafolio (PWA + 6 idiomas + Capacitor + documentación profunda)
**Repo:** https://github.com/vladimiracunadev-create/vladimiracunadev-create.github.io
**Web:** https://vladimiracunadev-create.github.io/
**Qué demuestra:** Portafolio profesional en 6 idiomas (ES/EN/PT/IT/FR/ZH), 30+ PDFs generados por pipeline Python, PWA instalable, CV Data API JSON estática, guías de build móvil/desktop.

### ⚡ Unikernel Labs · Control Center
**Repo:** https://github.com/vladimiracunadev-create/unikernel-labs
**Qué demuestra:** Suite profesional para operar servicios Unikraft en Windows con backend WSL2. Control total vía Dashboard Node.js y Launcher WinForms en localhost. Arquitectura de alto rendimiento y orquestación unikernel.

### 🍎 ChofyAI Studio · macOS Local AI Launcher (Fase 4)
**Repo:** https://github.com/vladimiracunadev-create/chofyai-studio
**Qué demuestra:** Lanzador de escritorio para macOS Apple Silicon que centraliza e instala herramientas de IA local (Qwen3-TTS, whisper.cpp, FaceFusion, AceForge). Tauri + Rust + React. Fase 4: disco dual, zona de módulos, stats, empaquetado ad-hoc, soporte `uv`.

### 🐳 Problem-Driven Systems Lab (Docker-first · 12 casos · UI integrada)
**Repo:** https://github.com/vladimiracunadev-create/problem-driven-systems-lab
**Qué demuestra:** 12 casos reales de sistemas distribuidos Docker-first con **UI nativa integrada** (no solo "API JSON ciega"). Patrones profesionales (Adapter, Strangler, Circuit Breaker) sobre cuellos de botella reales en runtime PHP, con scaffolds en Node.js, Python, Java y .NET. Observabilidad Prometheus :9091 + Grafana :3001. Catálogo en `shared/catalog/cases.json`.

### 📊 Python Data Science Bootcamp (Docencia · Notebooks · App Desktop · Android Expo)
**Repo:** https://github.com/vladimiracunadev-create/python-data-science-bootcamp
**Qué demuestra:** Bootcamp con 31 clases · notebooks interactivos · datasets reales · App Desktop Windows (Edge WebView2) · App Android (Expo) · PDFs generados. Diseñado para principiantes y transición profesional hacia análisis de datos.

### 🏛️ Portales operativos (PHP modular · Docker · GitHub Actions)
Cuatro portales verticales construidos como referencia de modernización legacy y verticalización de dominio:

- **[portal-empresarial](https://github.com/vladimiracunadev-create/portal-empresarial)** — Gestión completa para crear una empresa: plan de negocio, constitución legal, finanzas, equipo, pipeline de clientes e hitos.
- **[portal-bienestar](https://github.com/vladimiracunadev-create/portal-bienestar)** — Portal de empleabilidad para CV, documentos laborales, redes profesionales y bolsas de trabajo. PHP · MariaDB · Docker · GitHub Actions.
- **[portal-educativo](https://github.com/vladimiracunadev-create/portal-educativo)** — Software educativo para el aula chilena: evaluaciones, libro de notas, planificaciones MINEDUC y módulo psicoeducativo.
- **[portal-tecnologia](https://github.com/vladimiracunadev-create/portal-tecnologia)** — Plataforma vertical de tecnología.

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

<sub>Última actualización: 2026-05-02</sub>
