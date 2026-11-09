# 🛠️ Leitfaden zur technischen Bewertung

[← Wo anfangen](../START_HERE.de.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · **Deutsch** · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## In einer Zeile

Man muss keinen Code lesen, um zu beurteilen, wie ich denke: Es genügt zu sehen, was sich ausführen lässt, was getestet wird und was als offen ausgewiesen ist.

## Vier Routen zu je 10 Minuten

| Route | Zu sehen… | Wie |
|---|---|---|
| **A. Observability und Orchestrierung** | Workflows, Metriken, Dashboards und Guardrails über 20 Fälle und mehr als 18 DB-Engines | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Reproduzierbare Infrastruktur** | Container-Labore in Minuten gestartet | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Agenten mit typisiertem Zustand** | 25 LangGraph-Backends, DEMO/LIVE, Beweiskette | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Forensisches Produkt in Rust** | Installer und Binärdateien mit Checksummen, ohne Klonen | [RootCause-Releases](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Überprüfbare Qualitätssignale

| Signal | Wo nachsehen |
|---|---|
| Tests | GabySQL mit 850 Tests und einem Fuzz-Lauf über 503,8 Mio. Abfragen ohne Panics; Empresa Operativa Chile mit 230 Tests; Automa mit 150 pytest |
| Lieferkette | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, CycloneDX-SBOM und Scorecard, je nach Repo |
| Telemetrie | Null in den forensischen Produkten und in Empresa Operativa Chile, bei jedem Build geprüft |
| Distribution | Releases mit Checksummen und Build-Belegen; kommerzielle Signierung als offen ausgewiesen |
| Ehrlichkeit | Jedes Repo nennt seinen Status und was es **nicht** leistet |

Alle Zahlen mit Quelle stehen in [Nachprüfbarer Status](../../README.de.md#nachprüfbarer-status).

## Wie ich entwerfe

- **Vom Modell nach außen:** zuerst die Domäne, die Oberfläche als Projektion.
- **Observability ab Tag 1:** `/health`, `/ready`, `/metrics` und Nachvollziehbarkeit.
- **Echte Resilienz:** Idempotenz, Circuit Breaker und kontrollierte Degradation.
- **Polyglott per Design:** Sprache und Engine je nach Anwendungsfall.
- **DX zuerst:** `doctor` und `smoke` pro Repo; was sich nicht leicht ausführen lässt, taugt nicht als Team-Basis.

## Zum Vertiefen

- [Technologie-Stack](../../README.de.md#-technologie-stack), in den Repos erkannt.
- [Das vollständige Ökosystem ansehen](../ECOSYSTEM.de.md): jedes Produkt mit Version, Tests und Release.
- Forks von Dritten werden getrennt geführt und zählen nicht als eigene Arbeit: [Forks von Drittprojekten](../ECOSYSTEM.de.md#forks).

## Nächster Schritt

Für ein Architektur-Review oder ein technisches Gespräch schreiben Sie an [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
