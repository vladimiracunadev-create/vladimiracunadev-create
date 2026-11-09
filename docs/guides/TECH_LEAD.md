# 🛠️ Guía de evaluación técnica

[← Por dónde empezar](../START_HERE.md) · **Español** · [English](TECH_LEAD.en.md)

## En una línea

No hace falta leer código para evaluar cómo pienso: basta ver qué se puede ejecutar, qué se prueba y qué se declara como pendiente.

## Cuatro rutas de 10 minutos

| Ruta | Para ver… | Cómo |
|---|---|---|
| **A. Observabilidad y orquestación** | Workflows, métricas, dashboards y guardrails sobre 20 casos y 18+ motores de BD | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Infraestructura reproducible** | Laboratorios de contenedores levantados en minutos | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Agentes con estado tipado** | 25 backends LangGraph, DEMO/LIVE, cadena de custodia | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Producto forense en Rust** | Instaladores y binarios con checksums, sin clonar | [Releases de RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Señales de calidad que puedes verificar

| Señal | Dónde mirarla |
|---|---|
| Pruebas | GabySQL 850 tests y fuzz de 503,8 M de queries sin panics; Empresa Operativa Chile 230 pruebas; Automa 150 pytest |
| Cadena de suministro | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, SBOM CycloneDX y Scorecard según el repo |
| Telemetría | Cero en los productos forenses y en Empresa Operativa Chile, verificada en cada build |
| Distribución | Releases con checksums y evidencia de build; firmas comerciales declaradas como pendientes |
| Honestidad | Cada repo declara su estado y lo que **no** hace |

Todas las cifras con su fuente están en [Estado verificable](../../README.md#-estado-verificable).

## Cómo diseño

- **Del modelo hacia afuera:** el dominio primero, la interfaz es una proyección.
- **Observabilidad desde el día 1:** `/health`, `/ready`, `/metrics` y trazabilidad.
- **Resiliencia real:** idempotencia, circuit breaker y degradación controlada.
- **Políglota por diseño:** lenguaje y motor elegidos por caso de uso.
- **DX primero:** `doctor` y `smoke` por repo; si no se ejecuta fácil, no sirve como base de equipo.

## Dónde profundizar

- [Stack tecnológico](../../README.md#-stack-tecnológico) detectado en los repos.
- [Ecosistema completo](../ECOSYSTEM.md): cada producto con su versión, pruebas y release.
- Los forks de terceros están separados y no cuentan como obra propia: [ver forks](../ECOSYSTEM.md#forks).

## Siguiente paso

Si quieres una revisión de arquitectura o una conversación técnica, escribe a [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
