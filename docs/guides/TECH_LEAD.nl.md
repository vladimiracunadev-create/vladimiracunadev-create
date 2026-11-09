# 🛠️ Gids voor technische beoordeling

[← Waar te beginnen](../START_HERE.nl.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · **Nederlands** · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## In één regel

Je hoeft geen code te lezen om te beoordelen hoe ik denk: het volstaat te zien wat draait, wat getest wordt en wat als openstaand is aangemerkt.

## Vier routes van 10 minuten

| Route | Om te zien… | Hoe |
|---|---|---|
| **A. Observability en orkestratie** | Workflows, metrics, dashboards en guardrails over 20 cases en 18+ DB-engines | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Reproduceerbare infrastructuur** | Containerlabs in minuten draaiend | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Agents met getypte status** | 25 LangGraph-backends, DEMO/LIVE, bewijsketen | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Forensisch product in Rust** | Installers en binaries met checksums, zonder klonen | [RootCause-releases](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Controleerbare kwaliteitssignalen

| Signaal | Waar te kijken |
|---|---|
| Tests | GabySQL met 850 tests en een fuzzrun van 503,8 M queries zonder panics; Empresa Operativa Chile met 230 tests; Automa met 150 pytest |
| Toeleveringsketen | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, CycloneDX-SBOM en Scorecard, afhankelijk van de repo |
| Telemetrie | Nul in de forensische producten en in Empresa Operativa Chile, bij elke build gecontroleerd |
| Distributie | Releases met checksums en buildbewijs; commerciële ondertekening als openstaand aangemerkt |
| Eerlijkheid | Elke repo vermeldt zijn status en wat hij **niet** doet |

Alle cijfers met hun bron staan in [Verifieerbare status](../../README.nl.md#verifieerbare-status).

## Hoe ik ontwerp

- **Van model naar buiten:** eerst het domein, de interface als projectie.
- **Observability vanaf dag 1:** `/health`, `/ready`, `/metrics` en traceerbaarheid.
- **Echte veerkracht:** idempotentie, circuit breaker en gecontroleerde degradatie.
- **Polyglot door ontwerp:** taal en engine gekozen per use case.
- **DX eerst:** `doctor` en `smoke` per repo; als het niet makkelijk draait, deugt het niet als teambasis.

## Verder verdiepen

- [Technologiestack](../../README.nl.md#-technologiestack) gedetecteerd in de repos.
- [Bekijk het volledige ecosysteem](../ECOSYSTEM.nl.md): elk product met versie, tests en release.
- Forks van derden worden apart gehouden en tellen niet als eigen werk: [Forks van projecten van derden](../ECOSYSTEM.nl.md#forks).

## Volgende stap

Voor een architectuurreview of een technisch gesprek schrijf je naar [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
