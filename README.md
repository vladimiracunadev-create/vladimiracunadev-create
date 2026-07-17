# Arquitecto de Soluciones | Legacy Modernization Architect | Senior Full-Stack · AI Automation Architect
**PHP 8 · Python · Go · Node/TS · Java 21 · .NET 8 · C# · Ruby · Rust · Dart/Flutter · WASM · AWS · Terraform · K8s · n8n · LangGraph/MCP · CI/CD · FinOps · Observabilidad · IA aplicada**

[![Portfolio](https://img.shields.io/badge/🌐_Portfolio_en_vivo-vladimiracunadev--create.github.io-0366d6?style=for-the-badge)](https://vladimiracunadev-create.github.io/)
[![GitHub](https://img.shields.io/badge/GitHub-vladimiracunadev--create-24292f?style=for-the-badge&logo=github)](https://github.com/vladimiracunadev-create)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Vladimir_Acuña-0a66c2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/vladimir-acu%C3%B1a-valdebenito-11924a29/)

Arquitectura, modernización, automatización e IA aplicada a proyectos reales. Diseño, construyo y opero sistemas de producción con foco en **confiabilidad, performance, entrega continua** y **criterio técnico propio**.

- 🧱 +16 años construyendo y operando software en entornos reales (incluye 14+ años en plataformas web educativas/psicométricas)
- ⚙️ Especialidad: performance, mantenibilidad, estabilidad, deuda técnica y continuidad operacional
- 🚀 Enfoque 2026: **Cloud + DevOps + polyglot persistence + repos reproducibles (docker-first) + observabilidad + multiplataforma (PWA/Capacitor/Flutter) + agentes/IA local + seguridad forense (Windows/móvil) + computación científica + currículos técnicos completos + auditoría multi-capa + trust profile (CodeQL · Semgrep · SBOM CycloneDX · Scorecard) + distribución como producto (instaladores `.exe`/`.msi`/`.apk` automatizados)**
- ✅ Busco: roles donde el perfil **Arquitecto + Full-Stack + AI Automation** sea una ventaja real — no un genérico

---

## 🧭 Qué encontrarás en ESTE GitHub (no es "un repo", es un sistema)
Este perfil está construido como un portafolio verificable:

- **Demos reproducibles** (clonas, ejecutas, validas)
- **Tooling estandarizado** (Makefiles + "Hub CLI" + doctor/smoke)
- **Defensa en profundidad** (secret scanning, policies, killed practices)
- **Observabilidad** (métricas + dashboards + trazabilidad)
- **Documentación profunda** (reclutador / novato / devops / seguridad, según repo)
- **Multiplataforma** (web → PWA → móvil/desktop via Capacitor/Flutter/Tauri, cuando aplica)
- **Internacionalización** (portafolio disponible en 6 idiomas: ES, EN, PT, IT, FR, ZH)
- **Productos con distribución real** — instaladores `.exe`/`.msi` (Windows), `.dmg` (macOS) y `.apk` (Android) con build y firma automatizados (docker-labs, unikernel-labs, automa-pc, rootcause, gabysql, chofyai-studio)
- **Seguridad forense** — sensores de diagnóstico agnóstico de amenazas para Windows (Rust) y Android/iOS (Flutter), telemetría cero
- **Computación científica** — plataforma reproducible de genómica con contratos tipados y madurez explícita por módulo
- **Currículos técnicos completos** — programas de estudio secuenciales (ciberseguridad, gamedev, data science) con reto verificable por clase
- **Honestidad técnica explícita** — distinción visible entre `OPERATIVO`, `DOCUMENTADO/SCAFFOLD` y `PLANIFICADO` (problem-driven-systems-lab, langgraph-realworld y modern-gamedev-program lo declaran tabularmente)
- **MCP local read-only** — bridge para Claude Desktop integrado tanto en `microsistemas` como en `mcp-ollama-local` (IA con contexto de repo, sin enviar datos a la nube)

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
- Launcher nativo (Go/.NET/WinForms) + instalador Windows (.exe/.msi) con release automation.
- Estructuras repetibles: docs, roadmap, security, changelog, contribución.

### 4) Cloud delivery profesional (no tutorial)
- Flujo `dev → PR → main` con despliegues reales: AWS Amplify (multi-branch) y GitHub Actions deploy a S3 con OIDC.
- **Journey GitHub Actions × AWS**: cada caso introduce un servicio AWS nuevo y una capacidad de Actions que no existía antes (paths filter, OIDC federation, environments + approvals, matrix strategy, reusable workflows, GHCR, cron, multi-region, GitOps).
- Cobertura activa de objetivos **SAA-C03 · DVA-C02 · SOA-C02** mapeada caso a caso.
- Tooling: AWS CLI · Terraform · SAM · TruffleHog · detect-secrets · wiki sync.
- Seguridad y gobernanza como parte del pipeline (no post-it): OIDC sin credenciales largas, secret scanning, environments con aprobaciones.

### 5) Multiplataforma real (web + PWA + móvil/desktop)
- El portafolio está diseñado como **PWA instalable** y **Android/iOS ready** vía Capacitor (APK release v2.3.0 publicado).
- **6 idiomas** (ES, EN, PT, IT, FR, ZH) con 30+ PDFs generados por pipeline (CVs, portafolio, logros, recomendaciones).
- **4 vistas paralelas** (Reclutador por defecto · Normal · Profundo · Freelance) con `VIEW_SCHEMA` migration para resetear `localStorage` viejo al introducir nuevas vistas.
- Apps móviles nativas más allá del wrapper: **RootCause Mobile** (Flutter, Android/iOS con colectores Kotlin/Swift) y **python-data-science-program** (app Android Expo).

### 6) IA aplicada con mentalidad de ingeniería
- **25/25 backends operativos (cobertura 100%, v4.15.0)** sobre LangGraph + FastAPI (casos 01–25): soporte omnicanal, screening RR.HH. + calendario, onboarding, BI con SQL/charting, analista de documentos, RAG, agentes multi-step, planificadores y más.
- **AI-orchestrated local automation** con **Automa PC Orchestrator v0.3.0** (27 flows operativos, 150 pytest tests, Playwright + pywebview, instalador firmado) y **RootCause Windows Inspector v0.19.0** (Rust + ETW/WPR, 5 ediciones: GUI · Portable · CLI · PowerShell · VS Code).
- Agentes con **estado tipado** (TypedDict), **rutas condicionales**, **resiliencia**, OAuth2/OIDC opt-in, LangSmith opt-in y modo dual (DEMO offline / LIVE).
- IA local con privacidad completa: chat web local (FastAPI + Ollama) + tools MCP en sandbox `data/sandbox` + persistencia SQLite, bind `127.0.0.1`, sin nube obligatoria.
- Servidor MCP de solo lectura para Claude Desktop integrado en la suite de microsistemas (read-only knowledge bridge).

### 7) Polyglot persistence y multi-lenguaje
- **19 casos de integración real** (19/20 operativos) con stacks completos emisor → puente n8n → receptor → DB, verificados end-to-end uno a uno con Docker.
- **20+ contenedores** orquestados con **11 patrones arquitectónicos**: microservicios, event-driven, mediador, idempotencia, circuit breaker, DLQ, persistencia políglota, observabilidad opt-in, supply-chain hardening, edge proxy con TLS, runtime isolation.
- **18+ motores de bases de datos** distintos (relacionales, NoSQL, grafos, vectorial, series temporales, streaming) con métricas por combinación lenguaje × DB.

### 8) Seguridad como pipeline (defense-in-depth, no checklist)
- Auditoría estándar de 8 capas: non-root containers, binding `127.0.0.1`, HTTP security headers, `grype --fail-build`, Trojan Source, nginx + TLS, `detect-secrets`, `pip-compile` + Dependabot.
- Hardening transversal: TruffleHog + Trivy + Bandit + pip-audit + Gitleaks + markdownlint según stack.
- SBOM generado en cada release · K8s NetworkPolicy + runtime isolation donde aplica.
- **Seguridad forense como producto**: sensores que detectan distorsiones anómalas de recursos (indicio temprano de amenaza) en Windows y móvil, agnósticos de firma, con evidencia exportable y telemetría cero.

### 9) Distribución como producto (no "clona y suerte")
- Instaladores firmados y builds cross-platform automatizados: `.exe`/`.msi` (Windows), `.dmg` (macOS), `.apk` (Android), Scoop manifests + `SHA256SUMS` por release.
- Landing pages dedicadas por producto (automa-pc, rootcause, gabysql, chofyai-studio, microsistemas) desplegadas en GitHub Pages.
- Supply-chain hardening con migración npm → **pnpm v11** + verificación SHA-512 de lockfile en los repos Node/TS.

---

## ⭐ Evidencia rápida (repos clave del ecosistema)
> La idea no es "mirar código": es **ver cómo pienso**, cómo documento y cómo hago que todo sea ejecutable.

### 🔥 Cloud Portfolio · GitHub Actions Journey × AWS
**Repo:** https://github.com/vladimiracunadev-create/proyectos-aws
**Qué demuestra:** **11 casos progresivos** donde cada uno introduce un servicio AWS nuevo *y* una capacidad de GitHub Actions que no existía antes. Fase 1 operativa con demos vivas — caso 01 (Amplify multi-branch: [main](https://main.d3r1wuymolxagh.amplifyapp.com/) · [dev](https://dev.d20m8tc0banvg.amplifyapp.com/)) y caso 02 (S3 + paths filter). Fases 2-5 mapeadas: CloudFront + OIDC, Environments + Approvals, Lambda + API Gateway, DynamoDB + Matrix, Reusable Workflows, Containers + GHCR, FinOps + Cron, Multi-región + DR, EKS + GitOps. Cobertura **DVA-C02 · SAA-C03 · SOA-C02** mapeada caso a caso. Pipeline con TruffleHog + detect-secrets + wiki sync.

### 📆 Social Bot Scheduler v4.9.1 · 19 casos · 18+ motores de BD
**Repo:** https://github.com/vladimiracunadev-create/social-bot-scheduler
**Qué demuestra:** Matriz tecnológica con **19 casos de integración** (**19/20 operativos**) puenteados por n8n, cada uno verificado end-to-end con Docker (persistencia real por motor), **20+ contenedores**, **11 patrones arquitectónicos** y **18+ motores de bases de datos** (relacionales, NoSQL, grafos, vectorial, series temporales, streaming). Master Dashboard con detección automática OFFLINE/READY, contadores en vivo y badges de RAM por caso. Auditoría de **8 capas** (contenedor, red, credenciales, servidor web, herramientas, autenticación, CI/CD, supply chain): bind `127.0.0.1`, non-root, HTTP security headers (CSP, HSTS, Permissions-Policy), Caddy edge proxy + TLS + Basic Auth, Trivy + pip-audit + Gitleaks + Trojan Source detection, Dependabot multi-ecosistema. Observabilidad opt-in (Prometheus + Grafana en `--profile observability`). **v4.9.x** consolida la auditoría Docker de los 19 casos + migración npm → **pnpm v11** en el runtime Node.

### 🤖 LangGraph RealWorld v4.15.0 · 25/25 backends operativos · cobertura 100%
**Repo:** https://github.com/vladimiracunadev-create/langgraph-realworld
**Qué demuestra:** Portafolio de **25 casos empresariales** con **25/25 backends 100% operativos** (casos 01–25, sin omisiones) — soporte omnicanal, HR screening + calendario, onboarding, BI SQL/charting, RAG, agentes multi-step, analista de documentos, planificadores y más. Estado tipado (TypedDict), modo dual DEMO/LIVE, **streaming NDJSON**, OAuth2/OIDC opt-in, LangSmith opt-in, endpoints `/health` `/ready` `/metrics` con latencia y errores por servicio, reverse proxy nginx + TLS, logging JSON estructurado, CI extendido a los 25 casos. Auditoría de **8 capas** de seguridad + **cadena de custodia SHA-256** + release v4.15 de hardening adversarial (4 critical fixes inline, `shared/lgrw_common/` como fuente canónica, `python-jose` → `joserfc`). Python 3.11 · FastAPI · Docker · pytest · uv opcional.

### 🔍 RootCause · Windows Inspector v0.19.0 · Diagnóstico forense en Rust (5 ediciones)
**Repo:** https://github.com/vladimiracunadev-create/rootcause-windows-inspector
**Landing:** https://vladimiracunadev-create.github.io/rootcause-windows-inspector/
**Qué demuestra:** Software forense de ciberseguridad para **Windows 10/11** escrito en **Rust 🦀 (edition 2024)**. Parte de una idea: **cualquier distorsión anómala de recursos —CPU, disco, memoria, red, procesos, autoarranque, servicios— puede ser el primer indicio de una amenaza** (malware activo, persistencia, exfiltración, binario secuestrado, control de seguridad apagado). Vigila de forma **agnóstica**, correlaciona señales en incidentes y **explica la causa raíz con evidencia** — complementa al antivirus/EDR, no lo reemplaza. **5 ediciones publicadas** por release: GUI Desktop (`RootCause-Setup.exe`), Portable .zip, **CLI single-binary** (`rootcause.exe`), módulo PowerShell (`.psm1`), extensión VS Code (`.vsix`). Stack ETW + WPR, **SHA256SUMS** + manifest Scoop por release, **19+ releases tagueadas** (v0.5.0 → v0.19.0, incluye tab de red: equipos cercanos / red conocida). Filosofía: *diagnóstico primero, intervención después*. Telemetría: cero.

### 📱 RootCause · Mobile Inspector v0.2.0 · Sensor forense Android/iOS (Flutter)
**Repo:** https://github.com/vladimiracunadev-create/rootcause-mobile-inspector
**Qué demuestra:** El hermano móvil de RootCause Windows — sensor forense de diagnóstico para **Android e iOS** construido con **Flutter** (lógica compartida en Dart + colectores nativos en **Kotlin y Swift**). Hereda la misma razón de existir: toda distorsión anómala de recursos del dispositivo (memoria, almacenamiento, batería, red, **superficie de permisos**) puede ser el primer indicio de una amenaza. Motor de reglas local, tendencia temporal + desviación estándar, cercanía BLE, detección de indicadores root/jailbreak y apps con permisos peligrosos. Todo se queda en el dispositivo: **cero telemetría, cero red saliente**. **APK firmado** publicado en Releases, español por defecto con toggle de idioma persistente, CI + release-android automatizados.

### 🤖 Automa · PC Orchestrator v0.3.0 · Orquestador local Windows (Playwright + pywebview + PyInstaller)
**Repo:** https://github.com/vladimiracunadev-create/automa-pc
**Landing:** https://vladimiracunadev-create.github.io/automa-pc/
**Qué demuestra:** Orquestador local de **acciones efectivas sobre Windows**. **27 flows operativos** declarativos en JSON que **abren ventanas reales**, **interactúan con DOM**, **capturan evidencia** y **dejan trazabilidad**. Panel local en `127.0.0.1` (**pywebview + PyInstaller**), stack **Python 3.10+ + Playwright** (headless y visible), **SQLite** para historial, OCR/visión, **uv** packaging, **150 pytest tests**, **instalador Windows firmado** (`Automa-Setup-v0.3.0.exe`). Local-first, sin servicios en la nube. Cubre el espacio "más allá de un scheduler" — pasa de reporte pasivo a operación activa sobre el equipo.

### 🗄️ GabySQL v0.2.0 + Modeler v0.1.0 · Base de datos embebida en Rust (single-file · WAL · HTTP/JSON · edge)
**Repo:** https://github.com/vladimiracunadev-create/gabysql
**Landing:** https://vladimiracunadev-create.github.io/gabysql/
**Qué demuestra:** Motor de base de datos embebido escrito en **Rust 🦀** (Fase 3 cerrada). **Archivo único `.db`** (formato propietario con WAL para integridad), **API HTTP/JSON** + **admin web liviano** + **GabyModeler desktop GUI v0.1.0** (Windows .exe/.msi). Superficie SQL amplia (JOINs ANSI, CTEs recursivas, window functions, triggers, procedures, PL/pgSQL, RLS, GRANT/REVOKE), **cost-based query optimizer** con estadísticas persistentes, **SAVEPOINT/ROLLBACK TO**, sesiones HTTP cross-request (ORMs pueden mantener transacción a través de N requests). **828 tests verdes** (integration + server E2E + proptest), **fuzz parser con 503.8M queries random / 1h limpia / 0 panics**. Builds cross-platform: Windows (.exe + .msi + .zip), macOS arm64, Linux x86_64. Demuestra dominio de Rust para systems programming y diseño de storage engines.

### 🧰 Microsistemas v3.x · Developer Productivity Suite
**Repo:** https://github.com/vladimiracunadev-create/microsistemas
**Landing:** https://vladimiracunadev-create.github.io/microsistemas/
**Qué demuestra:** **12 microapps web** para diagnóstico, soporte, DevOps, aprendizaje y modernización PHP. Doble modo de uso: stack Docker (`make up` listo en 30 s) o XAMPP local. Incluye KatasMultiLang (195 comparaciones / 67 tecnologías), CicdLibrary (192 patrones CI/CD), AWS Assistant Pro, **servidor MCP local de solo lectura** para Claude Desktop. Hardening en **3 fases** (infraestructura + aplicación + supply-chain): CSRF, rate limiting, TruffleHog, Trivy, Dependabot, markdownlint, SBOM por release. Hub CLI unificado con diagnóstico y smoke testing.

### 🧪 Docker Labs v1.5.0 · Plataforma Docker Modular
**Repo:** https://github.com/vladimiracunadev-create/docker-labs
**Qué demuestra:** **13 labs operativos** organizados en plataforma de 4 servicios (Control Center `:9090` Node.js, Inventory Core API `:8000` Python+PostgreSQL, Operations Portal `:8083` Node+MongoDB+Nginx, Platform Gateway `:8085` Nginx) + 9 labs independientes (Node, PHP/LAMP, Python Flask, Redis, RabbitMQ, Prometheus+Grafana, Go, Elasticsearch, Jenkins LTS). **Instalador `.exe` automatizado para Windows** (workflow `build-windows-installer`), launcher con browser auto-open. CI con smoke tests por lab, docs separadas por audiencia (Beginner Guide, User Manual, Technical Specs, Recruiter Guide).

### 🐳 WSL Labs · WSL Container Center v0.4.1 (sin Docker Desktop)
**Repo:** https://github.com/vladimiracunadev-create/wsl-labs
**Qué demuestra:** Centro de control de contenedores sobre **`wslc`**, el motor de contenedores nativo de WSL (WSL ≥ 2.9) — el equivalente WSL de un panel Docker, **sin Docker Desktop**. **12 casos reales** portados de `docker-labs` con imágenes propias, Panel Node.js (`:9092`) que construye/levanta/detiene/supervisa contenedores, Launcher Windows (Go `.exe`), fuente única de verdad en `containers.config.json`. v0.4.x agrega límites de recursos, volúmenes persistentes y guía de portabilidad. Build Windows + docs + dashboard automatizados en CI.

### ⚡ Unikernel Labs · Control Center v2.0.0
**Repo:** https://github.com/vladimiracunadev-create/unikernel-labs
**Qué demuestra:** "Docker Desktop para unikernels" — capa de control Windows sobre runtime Linux real para operar servicios **Unikraft**: Dashboard Node.js (REST API en `localhost:9091`), Launcher WinForms .NET y backend WSL2 con `kraft` + QEMU/KVM. Catálogo único en `labs.config.json` (sincronizado al launcher), 8 labs (de `01-hello-world` a `08-kraft-cloud-track`), arranque real validado de servicios en localhost. **v2.0.0** con hardening de workflows, Pages y cobertura de tests Node. Workflow de build automatizado para instalador `.exe` de Windows + instalación silenciosa.

### 🧠 MCP + Ollama Local · IA local-first con sandbox MCP
**Repo:** https://github.com/vladimiracunadev-create/mcp-ollama-local
**Qué demuestra:** Web local (FastAPI + Uvicorn, Python 3.13) + chat con Ollama vía `httpx` + bridge MCP por `stdio` con tools acotadas a `data/sandbox`. Persistencia en SQLite, despliegue en local, Docker o K8s. Bind `127.0.0.1:8000`, CORS configurable, API key opcional (`X-API-Key`), rate limiting en memoria, contenedor non-root. **Security & Trust Profile multi-capa**: `ci.yml` (Ruff + Pytest), `security.yml` (Bandit + pip-audit), `codeql.yml` (code scanning semántico), `semgrep.yml` (reglas locales), `supply-chain.yml` (SBOM CycloneDX + firma de release), `scorecard.yml` (señal pública), Actions y base images pineadas por hash. Honesto sobre límites (no es multi-usuario, no RBAC).

### 🍎 ChofyAI Studio v0.5.1 · macOS Apple Silicon + Windows experimental + NVIDIA GPU
**Repo:** https://github.com/vladimiracunadev-create/chofyai-studio
**Landing:** https://vladimiracunadev-create.github.io/chofyai-studio/
**Qué demuestra:** Lanzador de escritorio para **IA local creativa** validado en **macOS Apple Silicon** con soporte experimental **Windows + NVIDIA GPU** (**Tauri 2 + Rust + React**). Orquesta 5 herramientas: **Qwen3-TTS**, **whisper.cpp**, **FaceFusion**, **AceForge** y **ComfyUI** (5/5 inferencia real). Descargas guiadas de modelos con progreso, settings UI (model/output/cache dirs), automated .dmg releases, **pnpm migration + SHA-512 lockfile verification**, soporte `uv` como acelerador opcional para tools Python.

### 🐳 Problem-Driven Systems Lab · 12 casos · 5 stacks (PHP 8 · Python · Node · Java 21 · .NET 8)
**Repo:** https://github.com/vladimiracunadev-create/problem-driven-systems-lab
**Qué demuestra:** **12 problemas reales de ingeniería** (latencia bajo carga, N+1, observabilidad pobre, retry storms, fugas de memoria, pipelines frágiles, modernización del monolito, extracción crítica, integraciones inestables, sobre-arquitectura, reportes bloqueantes, single point of knowledge) con fallos de alta fidelidad inyectados — no simulaciones abstractas. Resuelto en **5 stacks**: PHP 8, Python, Node.js, **Java 21** (`ConcurrentHashMap`, `CompletableFuture.orTimeout`, `Semaphore`, record types) y **.NET 8** (`ConcurrentDictionary`, `CancellationTokenSource`, `SemaphoreSlim`). **Stack PHP 100% OPERATIVO** con UI nativa interactiva (Dashboards Interactivos según `Accept` de browser), **stack Python 100% OPERATIVO** (12 casos en stdlib pura). Patrones profesionales: **Adapter, Strangler, Circuit Breaker, LRU, Cancellation**. Compose por lenguaje, Prometheus `:9091` + Grafana `:3001` + portal `:8080`. Plan **AWS_MIGRATION.md** con 3 rutas (ECS Fargate · Lambda · EKS), costos reales estimados y mapping explícito de cómo AWS mitiga cada hallazgo de `SECURITY.md`.

### 🦏 Rhino Suite v0.7.0 (Fase 2.5) · Suite ofimática desde el modelo (Rust/WASM + Go + React)
**Repo:** https://github.com/vladimiracunadev-create/rhino-suite
**Qué demuestra:** Suite ofimática web y de escritorio **construida desde cero**, con un principio central: *las reglas del documento no dependen del DOM, de React ni del SO — el HTML es solo una proyección del estado vivo*. Monorepo evolutivo donde cada fase conserva las anteriores y **migra sus formatos automáticamente** (schema interno v5). Motor documental en **Rust → WebAssembly** (`wasm-bindgen`) con respaldo TypeScript compatible, **API Go** (`net/http`) para cuentas/sesión/permisos, frontend **React 19 + TypeScript**, persistencia atómica + IndexedDB local. Fase 2.5: editor funcional dentro de una unidad de archivos con cuentas y compartición. Hoja de cálculo, presentaciones, PDF, colaboración en tiempo real y escritorio llegan en fases posteriores sin romper lo anterior.

### 🧬 Human Genome Labs v1.0.0 · Plataforma científica reproducible (TypeScript)
**Repo:** https://github.com/vladimiracunadev-create/human-genome-labs
**Demo:** https://vladimiracunadev-create.github.io/human-genome-labs/
**Qué demuestra:** Plataforma científica **evolutiva, reproducible y educativa** para genética molecular y genómica. **Núcleo TypeScript verificable** (secuencias, traducción, ORF, variantes, G-cuádruplex, estadísticas), contratos comunes `ScientificResult<T>` y coordenadas genómicas 0-based half-open, lectores **FASTA / GFF3 / VCF**, perfiles de organismo, **registro de módulos con madurez y evidencia explícitas**, CLI científica + laboratorio web (PWA) + juego educativo. Node ≥ 22 · pnpm 11 · TypeScript 5.9. Honestidad radical: *no realiza diagnóstico clínico; las predicciones computacionales no equivalen a evidencia funcional*. Demuestra diseño de dominio complejo con contratos tipados y criterios de promoción de madurez.

### 🧰 Claude Skills Toolkit v0.2.0 · 10 skills agentic para Claude Code (Python · Cross-platform · Zero-deps)
**Repo:** https://github.com/vladimiracunadev-create/claude-skills-toolkit
**Qué demuestra:** **10 skills agentic** productivos para Claude Code. **security-audit** corre 12 capas — OSV / CISA KEV / EPSS / GHSA / PyPA / RustSec / Bandit SAST / trivy + grype container scan / gitleaks + detect-secrets / zizmor (GitHub Actions) / hadolint (Dockerfile) / typosquat heurístico — genera reporte Markdown y opcionalmente PR de bump con auto-merge. **yaml-control** valida YAML + actionlint. **md-lint-fix** auto-corrige MD024/040/031/etc. con contexto. **docker-cleanup** wipea contenedores/imágenes/volúmenes/redes/build cache. **docker-compose-doctor** diagnostica `compose*.yml`. **pre-commit-guard** + **pre-push-guard** orquestan validadores antes de commit/push. **python-version-control** audita drift de versión Python. **repo-coherence-audit** reconcilia docs↔repo contra fuentes de verdad. **web-snap** captura screenshots en Windows. Zero-deps por defecto y cross-platform (Linux 🐧 · macOS 🍎 · Windows 🪟).

### 📚 Python Data Science Program v3.8.0 · 232 clases · 9 partes · Windows nativo (PySide6+Qt) + Android (Expo)
**Repo:** https://github.com/vladimiracunadev-create/python-data-science-program
**Qué demuestra:** Programa avanzado de Data Science y ML en **9 partes y 232 clases**: Python + Polars, **ML clásico** + Optuna/SHAP, **Deep Learning** (PyTorch, LLMs, LoRA/DPO/vLLM, MCP, agentes, multimodal, SDXL, JAX), **estadística inferencial + causalidad**, **MLOps**, **ingeniería de datos**, **recomendadores**, **ética/fairness** y **capstones**. Distribución multiplataforma: **Laboratorio Flask interactivo** + **kernel Jupyter real**, **app de escritorio Windows nativa** (**PySide6 + Qt + kernel Jupyter**) y **app Android** (**Expo SDK 51**). 232 PDFs + 232 PPTX generados, instalador `.exe` (Inno Setup) publicado.

### 🛡️ Modern Cybersecurity Program · 340 clases · 19 partes · fundamentos → experto
**Repo:** https://github.com/vladimiracunadev-create/modern-cybersecurity-program
**Qué demuestra:** El currículo de ciberseguridad más completo en español — **340 clases numeradas en 19 partes**, de redes, criptografía y Linux hasta Red Team, DFIR, cloud security, exploit development y seguridad de IA. Cada clase es una carpeta con objetivo, resultados verificables, laboratorio guiado con herramientas reales, ejercicios, reto con criterio de aceptación, errores comunes (síntoma → causa → solución) y FAQ. Mapeo a **7 certificaciones** (Security+, PenTest+, CySA+, OSCP, CISSP, BTL1, SANS) con 86–92% de cobertura. Manual completo en PDF, GitHub Pages, énfasis explícito en uso ético y legal. Laboratorios Docker + retos CTF.

### 🎮 Modern GameDev Program · 292 clases · 18 partes · fundamentos → profesional
**Repo:** https://github.com/vladimiracunadev-create/modern-gamedev-program
**Sitio:** https://vladimiracunadev-create.github.io/modern-gamedev-program/
**Qué demuestra:** El programa de desarrollo de videojuegos más completo en español — **292 clases en 18 partes** (verificadas: 292 carpetas de clase), de matemáticas, C#/C++/GDScript y game loops a motores 2D/3D, shaders, IA de juegos, multijugador, VR/AR, optimización y publicación. Motores **Godot · Unity · Unreal**. Honestidad de verificación tabulada: los **6 laboratorios Godot** los importa/arranca/prueba la CI en cada push (badge Labs); el código dentro de los README es material revisado a mano pero no ejecutado en CI. Cada clase termina en **reto verificable con criterio de aceptación**.

### 🕹️ Machine Operator Program · Base documental de simulación de máquinas
**Repo:** https://github.com/vladimiracunadev-create/machine-operator-program
**Qué demuestra:** Biblioteca de cursos técnicos para pilotar, conducir y navegar máquinas (motos, autos, buses, grúas, buques, aeronaves, naves espaciales + naves de ficción). Cada máquina se documenta como curso completo e interconectado: historia, características funcionales, mecánica en profundidad, mandos, principios físicos, entornos, reglamentos (foco en ley chilena) y diseño de simulación. Honestidad explícita: *aún no hay simulador ejecutable — esto es la base documental que cualquiera necesitaría antes de existir* (el proyecto se renombró de "Multisimulador" para no prometer software inexistente). CI de validación de documentación + verificación de enlaces.

### 🌐 Web/Portafolio v2.3.0 · PWA · 6 idiomas · 4 vistas (Reclutador / Normal / Profundo / Freelance)
**Repo:** https://github.com/vladimiracunadev-create/vladimiracunadev-create.github.io
**Web:** https://vladimiracunadev-create.github.io/
**Qué demuestra:** SPA estática profesional en **6 idiomas** (ES/EN/PT/IT/FR/ZH) con **4 vistas** (Reclutador por defecto · Normal · Profundo · Freelance — curaduría para clientes que evalúan contratación por proyecto), **30+ PDFs** generados por pipeline Python (CV ATS + CV Reclutador + Portafolio + Carta de Recomendación + Declaración de Logros, todos × 6 idiomas), **sección #productos** con cards descargables (landing + .exe/.zip/.apk), **PWA instalable** con service worker v7 (network-first `cache: no-cache`), **CV Data API JSON estática** en `api/v1/` (6 endpoints sin servidor), wrapper Capacitor para Android/iOS, **APK v2.3.0** firmado y publicado, **Lighthouse 100**.

---

## ⚡ "Si tengo 10 minutos para evaluarte" (rutas de prueba)
### Ruta A — Observabilidad + orquestación real (mi favorita)
```bash
git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git
cd social-bot-scheduler
# Sigue README: HUB + doctor + levantar stack (19 casos, 18+ motores de BD)
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
# Cualquiera de los 25 backends operativos (cobertura 100%): casos 01-25
```

### Ruta E — Producto forense en Rust (sin clonar, directo al release)
```text
# Descarga el instalador o el binario CLI desde:
# https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases
# 5 ediciones: GUI · Portable · CLI · PowerShell · VS Code — verifica SHA256SUMS
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
- **Honestidad sobre el estado del producto**: cada caso se etiqueta `OPERATIVO`, `DOCUMENTADO/SCAFFOLD` o `PLANIFICADO`. No hay maquillaje — el lector sabe qué levanta y qué todavía no. Incluso el nombre de un repo se cambia (`Multisimulador` → `machine-operator-program`) para no prometer software que aún no existe.
- **Trust profile, no "security marketing"**: los badges son señales, no la evidencia. Cada repo declara explícitamente sus *límites* (lo que NO hace) además de sus controles.
- **Producto > repo**: cuando aplica, el repo entrega instalador firmado, launcher con browser auto-open, landing page y workflow de build automatizado — no un README con `docker compose up` y nada más.
- **Del modelo hacia afuera**: el estado vivo no es el DOM ni la UI (Rhino Suite); el dominio se diseña primero y la interfaz es una proyección — lo mismo aplica a los contratos tipados de Human Genome Labs.

---

## ✅ Alcance profesional real (3 capas, atado a evidencia)

### 🎯 Identidad principal
- **Arquitecto de Soluciones / Solutions Architect** — diseño de sistemas modulares, escalables y con criterio evolutivo
- **Legacy Modernization Architect** — experiencia real en evolución de legacy (PHP 5.x→8.x, SQL, refactor incremental sin cortar operación)
- **Senior Full-Stack Developer / Tech Lead** — arquitectura + ejecución + estándares en plataformas reales (14+ años)
- **AI Automation Architect** — sistemas agénticos con LangGraph/MCP, flujos n8n con guardrails, IA aplicada con validación humana

### ↗ Expansión natural — cargos asumibles con fuerza
- **AI Orchestration Engineer** — agentes con estado tipado, rutas condicionales, resiliencia (LangGraph v4.15.0 · **25/25 backends operativos (cobertura 100%)** · 8 capas de seguridad · cadena de custodia SHA-256 · OAuth2/OIDC + LangSmith opt-in)
- **AI Automation Engineer** — orquestación de workflows reales con n8n, Python, circuit breaker e idempotencia (social-bot-scheduler v4.9 · 19 casos de integración · 18+ motores de BD · Caddy edge proxy + TLS) + automatización de escritorio (automa-pc v0.3.0 · 27 flows · 150 tests)
- **Systems / Rust Engineer** — programación de sistemas y storage engines (gabysql: 828 tests, fuzz 503.8M queries, WAL, query optimizer) + herramientas forenses de bajo nivel (rootcause Windows en Rust/ETW, 5 ediciones)
- **Mobile Engineer (Flutter)** — app forense Android/iOS con colectores nativos Kotlin/Swift, motor de reglas local, distribución APK firmada (rootcause-mobile v0.2.0)
- **Solutions Engineer** — demos y PoCs verificables, comunicación técnico-negocio, requisitos y arquitectura orientada a cliente
- **Technical Product Builder** — construcción end-to-end: arquitectura, desarrollo, operación y entrega con criterio de producto (instaladores Windows `.exe`/`.msi`, `.dmg` macOS, `.apk` Android — automatizados y firmados)
- **Technical Trainer / Educador técnico** — **currículos técnicos completos**: **modern-cybersecurity-program** (340 clases · 19 partes · mapeo a 7 certificaciones), **modern-gamedev-program** (292 clases · 18 partes · Godot/Unity/Unreal), **python-data-science-program v3.8.0** (232 clases · 9 partes · app Desktop Windows + Android) — cada clase con laboratorio guiado y reto verificable
- **Consultor de Transformación Digital** — diagnóstico, plan evolutivo y ejecución de modernización en organizaciones con legacy real
- **Product Operations Técnico** — continuidad y evolución de plataformas con observabilidad, reducción de fricción y mejora continua

### ⚙️ Alcance complementario (respaldado por experiencia directa)
- Platform Engineer / IDP · DevOps / CI-CD Engineer · Cloud / AWS Engineer
- SRE orientado a aplicaciones · Automation Engineer
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

<sub>Última actualización: 2026-07-16 · README sincronizado con el estado real verificado de cada repositorio público.</sub>
