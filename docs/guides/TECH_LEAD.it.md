# 🛠️ Guida alla valutazione tecnica

[← Da dove iniziare](../START_HERE.it.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · **Italiano** · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## In una riga

Non serve leggere codice per capire come ragiono: basta vedere cosa si può eseguire, cosa viene testato e cosa è dichiarato in sospeso.

## Quattro percorsi da 10 minuti

| Percorso | Per vedere… | Come |
|---|---|---|
| **A. Osservabilità e orchestrazione** | Workflow, metriche, dashboard e guardrail su 20 casi e oltre 18 motori di DB | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Infrastruttura riproducibile** | Laboratori di container attivi in pochi minuti | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Agenti con stato tipizzato** | 25 backend LangGraph, DEMO/LIVE, catena di custodia | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Prodotto forense in Rust** | Installer e binari con checksum, senza clonare | [Release di RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Segnali di qualità verificabili

| Segnale | Dove guardare |
|---|---|
| Test | GabySQL con 850 test e fuzz da 503,8 M di query senza panic; Empresa Operativa Chile con 230 test; Automa con 150 pytest |
| Supply chain | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, SBOM CycloneDX e Scorecard, secondo il repository |
| Telemetria | Zero nei prodotti forensi e in Empresa Operativa Chile, verificata a ogni build |
| Distribuzione | Release con checksum ed evidenza di build; firme commerciali dichiarate come in sospeso |
| Onestà | Ogni repository dichiara il proprio stato e ciò che **non** fa |

Tutte le cifre con la loro fonte sono in [Stato Verificabile](../../README.it.md#-stato-verificabile).

## Come progetto

- **Dal modello verso l'esterno:** prima il dominio, l'interfaccia come proiezione.
- **Osservabilità dal primo giorno:** `/health`, `/ready`, `/metrics` e tracciabilità.
- **Resilienza reale:** idempotenza, circuit breaker e degrado controllato.
- **Poliglotta per design:** linguaggio e motore scelti per caso d'uso.
- **DX prima di tutto:** `doctor` e `smoke` per repository; se non si esegue facilmente, non serve come base di team.

## Per approfondire

- [Stack tecnologico](../../README.it.md#-stack-tecnologico) rilevato nei repository.
- [Vedi l'ecosistema completo](../ECOSYSTEM.it.md): ogni prodotto con versione, test e release.
- I fork di terzi restano separati e non contano come opera propria: [Fork di progetti di terzi](../ECOSYSTEM.it.md#forks).

## Passo successivo

Per una revisione di architettura o una conversazione tecnica, scrivi a [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
