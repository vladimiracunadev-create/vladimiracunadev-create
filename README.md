# Arquitecto de Software | Full Stack Senior | Polyglot Engineer | Modernización y Escalabilidad
**PHP 8 · Python · Go · Node/TS · C# · Ruby · Rust · AWS · Docker · K8s · CI/CD · Observabilidad · IA aplicada (local-first + agentes)**

Diseño, construyo y escalo sistemas de producción: arquitectura, APIs, datos y automatización, con foco en **confiabilidad, performance, entrega continua** y **operación real**.

- 🧱 +16 años construyendo y operando software en entornos reales (incluye 14+ años en plataformas web educativas/psicométricas)
- ⚙️ Especialidad: performance, mantenibilidad, estabilidad, deuda técnica y continuidad operacional
- 🚀 Enfoque 2026: **Cloud + DevOps + polyglot persistence + repos reproducibles (docker-first) + observabilidad + multiplataforma (PWA/Capacitor) + agentes/IA local**
- ✅ Busco: roles Senior / Lead donde el perfil híbrido **Arquitectura + Delivery + Operación** sea una ventaja

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
- Ruta completa: *desde el workflow* → *métrica* → *dashboard* → *decisión*.

### 2) Resiliencia (guardrails) implementada, no solo hablada
- **Idempotencia** para evitar duplicados y spam.
- **Circuit breaker** + desvío controlado a DLQ cuando un proveedor se degrada.
- Troubleshooting orientado a "qué revisar primero" (n8n executions, logs, tablas de control).

### 3) Reproducibilidad y DX (Developer Experience) como diseño
- "Hub CLI" multi-OS (bash/powershell/python según repo).
- `doctor` para detectar puertos, Docker, dependencias.
- `smoke` para validar rápido que el sistema está sano.
- Launcher nativo en Go + instalador Windows (.exe) con release automation.
- Estructuras repetibles: docs, roadmap, security, changelog, contribución.

### 4) Cloud delivery profesional (no tutorial)
- Flujo `dev → PR → main` y despliegues reales con GitHub Actions / Amplify.
- **15 casos AWS** documentados en [GitLab monorepo](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) (11 completados, 4 proyectados).
- Tooling cloud: AWS CLI + Terraform + SAM + validaciones y checklist.
- Seguridad y gobernanza como parte del pipeline (no post-it).

### 5) Multiplataforma real (web + PWA + móvil/desktop)
- El portafolio está diseñado como **PWA instalable** y **Android/iOS ready** vía Capacitor.
- **6 idiomas** (ES, EN, PT, IT, FR, ZH) con 30+ PDFs generados por pipeline (CVs, portafolio, logros, recomendaciones).
- Guías profundas para build móvil (APK/IPA), troubleshooting y arquitectura.

### 6) IA aplicada con mentalidad de ingeniería
- Portal unificado con **4 casos operativos**: soporte omnicanal, screening RR.HH., onboarding, BI con SQL/charting.
- Agentes con **estado tipado** (TypedDict), **rutas condicionales**, **resiliencia**, y modo dual (offline demo + live).
- IA local para privacidad: chat local + tools MCP seguras + persistencia en SQLite + K8s ready.

### 7) Polyglot persistence y multi-lenguaje
- Matriz de **9 ejes de integración**: Python, Go, Node.js, PHP, Ruby, Rust, C#, Flask, Symfony.
- **12+ motores de datos**: MySQL, MariaDB, PostgreSQL, SQL Server, MongoDB, Cassandra, Redis, SQLite, DuckDB + más.
- Interoperabilidad real demostrada con métricas de cada combinación lenguaje×DB.

---

## ⭐ Evidencia rápida (repos clave del ecosistema)
> La idea no es "mirar código": es **ver cómo pienso**, cómo documento y cómo hago que todo sea ejecutable.

### 🔥 Cloud Portfolio (AWS + CI/CD + seguridad + flujo profesional)
**Repo:** https://github.com/vladimiracunadev-create/proyectos-aws
**Qué demuestra:** Deploy real + estándar profesional + security mindset + docs por perfil (reclutador/devops/seguridad).
**Demos públicas:** (ver README del repo)

### 📆 Social Bot Scheduler v4.x (n8n + Polyglot Persistence + Observabilidad + Guardrails)
**Repo:** https://github.com/vladimiracunadev-create/social-bot-scheduler
**Qué demuestra:** Orquestación real con 9 ejes de integración (Python/Go/Node/PHP/Ruby/Rust/C#/Flask/Symfony), polyglot persistence (12+ DBs), observabilidad industrial (Prometheus/Grafana), idempotencia/circuit breaker, seguridad (Trivy/Gitleaks/K8s NetworkPolicy).

### 🧪 Docker Labs v1.4 (infra y stacks "levanta en 60s" + K8s ready)
**Repo:** https://github.com/vladimiracunadev-create/docker-labs
**Qué demuestra:** 12 labs integrados con centro de control unificado (port 9090), Inventory Core API, Operations Portal, Platform Gateway. Launcher nativo en Go, instalador Windows automatizado, ruta de observabilidad (Prometheus/Grafana), manifiestos K8s.

### 🧰 Microsistemas (Developer Productivity Suite: 11 herramientas + MCP server)
**Repo:** https://github.com/vladimiracunadev-create/microsistemas
**Qué demuestra:** 11 herramientas modulares incluyendo KatasMultiLang (195 comparaciones / 67 tecnologías), CicdLibrary (192 patrones CI/CD), AWS Assistant Pro, servidor MCP Python para integración con IA. Hub CLI con diagnóstico y smoke testing.

### 🤖 LangGraph RealWorld (25 casos: agentes con estado tipado + resiliencia)
**Repo:** https://github.com/vladimiracunadev-create/langgraph-realworld
**Qué demuestra:** Portal unificado con 4 casos operativos (soporte omnicanal, HR screening, onboarding, BI SQL/charting), contratos de estado tipado (TypedDict), modo dual offline/live, health/readiness endpoints, CI por casos.

### 🧠 MCP + Ollama Local (IA local: FastAPI + tools MCP seguras + SQLite + K8s)
**Repo:** https://github.com/vladimiracunadev-create/mcp-ollama-local
**Qué demuestra:** IA aplicada con privacidad y arquitectura clara: persistencia, tools sandbox, tests, k8s.

### 🌐 Web/Portafolio (PWA + 6 idiomas + Capacitor + documentación profunda)
**Repo:** https://github.com/vladimiracunadev-create/vladimiracunadev-create.github.io
**Web:** https://vladimiracunadev-create.github.io/
**Qué demuestra:** Portafolio profesional en 6 idiomas (ES/EN/PT/IT/FR/ZH), 30+ PDFs generados por pipeline Python, PWA instalable, guías de build móvil/desktop.

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

---

## 🧠 Aprendizajes convertidos en "estándar de repos"
Lo que repetí y reforcé al crecer los commits del portafolio:

- **DX primero**: si no se ejecuta fácil, no sirve como demo ni como base de equipo.
- **Observabilidad no es opcional**: métricas y trazabilidad desde el día 1.
- **Seguridad como pipeline**: secret scanning, checklist, prácticas prohibidas (killed).
- **Resiliencia**: idempotencia + circuit breaker + "degradación controlada".
- **Polyglot por diseño**: lenguajes y bases de datos elegidos por caso de uso, no por moda.
- **Docs por audiencia**: reclutador / devops / seguridad / estudiante (cuando aplica).

---

## ✅ Roles donde encajo (ampliado, pero atado a evidencia)
- Arquitecto de Software / Solutions Architect (modernización, escalabilidad, delivery)
- Full-Stack Senior / Tech Lead (arquitectura + ejecución + estándares)
- Modernization Architect (legacy real: PHP 5.x→8.x, SQL, refactor incremental)
- Platform Engineer / IDP (plantillas, pipelines, entornos reproducibles, DX)
- SRE orientado a aplicaciones (observabilidad, performance, resiliencia, incident response)
- DevOps pragmático (CI/CD, costos, guardrails, despliegues en AWS)
- Automation Engineer (n8n/workflows, integración multi-sistema, polyglot)
- Solutions Engineer / Pre-Sales técnico (PoCs, demos verificables, puente TI–negocio)

---

## 📌 Disponibilidad
**Abierto a**: Senior Full-Stack / Arquitectura / Modernización de legado / Platform-IDP / SRE apps / DevOps pragmático / Automatización
**Modalidad**: Remoto / Híbrido (según proyecto)

---

## 📬 Contacto
- LinkedIn: https://www.linkedin.com/in/vladimir-acu%C3%B1a-valdebenito-11924a29/
- Web: https://vladimiracunadev-create.github.io/
- GitLab: https://gitlab.com/vladimir.acuna.dev-group/vladimir.acuna.dev-group
- Email: vladimir.acuna.dev@gmail.com




## 📚 Documentación del Proyecto

Como parte de los estándares de este ecosistema, la documentación detallada se divide en:
- [📘 Guía de Instalación y Despliegue (INSTALL.md)](INSTALL.md)
- [📜 Historial de Cambios (CHANGELOG.md)](CHANGELOG.md)
- [🤝 Guía de Contribución (CONTRIBUTING.md)](CONTRIBUTING.md)
- [🛡️ Política de Seguridad (SECURITY.md)](SECURITY.md)
- [⚖️ Código de Conducta (CODE_OF_CONDUCT.md)](CODE_OF_CONDUCT.md)
