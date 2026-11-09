# 🛠️ Technical evaluation guide

[← Start here](../START_HERE.en.md) · [Español](TECH_LEAD.md) · **English** · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## In one line

You don't need to read code to judge how I think: it is enough to see what can be run, what is tested and what is declared as pending.

## Four 10-minute routes

| Route | To see… | How |
|---|---|---|
| **A. Observability and orchestration** | Workflows, metrics, dashboards and guardrails across 20 cases and 18+ DB engines | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Reproducible infrastructure** | Container labs up in minutes | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Typed-state agents** | 25 LangGraph backends, DEMO/LIVE, chain of custody | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Forensic product in Rust** | Installers and binaries with checksums, no cloning | [RootCause releases](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Quality signals you can verify

| Signal | Where to look |
|---|---|
| Tests | GabySQL 850 tests and a 503.8 M-query fuzz run with no panics; Empresa Operativa Chile 230 tests; Automa 150 pytest |
| Supply chain | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, CycloneDX SBOM and Scorecard, depending on the repo |
| Telemetry | Zero in the forensic products and in Empresa Operativa Chile, verified on every build |
| Distribution | Releases with checksums and build evidence; commercial signing declared as pending |
| Honesty | Each repo states its status and what it does **not** do |

All figures with their source are in [Verifiable Status](../../README.en.md#-verifiable-status).

## How I design

- **Model outward:** domain first, interface as a projection.
- **Observability from day 1:** `/health`, `/ready`, `/metrics` and traceability.
- **Real resilience:** idempotency, circuit breaker and controlled degradation.
- **Polyglot by design:** language and engine chosen per use case.
- **DX first:** `doctor` and `smoke` per repo; if it does not run easily it is no good as a team base.

## Where to go deeper

- [Technology stack](../../README.en.md#-technology-stack) detected in the repos.
- [Full ecosystem](../ECOSYSTEM.en.md): each product with its version, tests and release.
- Third-party forks are kept apart and do not count as own work: [see forks](../ECOSYSTEM.en.md#forks).

## Next step

For an architecture review or a technical conversation, write to [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
