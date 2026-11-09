# 🛠️ Przewodnik oceny technicznej

[← Od czego zacząć](../START_HERE.pl.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · **Polski** · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## W jednym zdaniu

Nie musisz czytać kodu, by ocenić, jak myślę: wystarczy zobaczyć, co da się uruchomić, co jest testowane i co jest zadeklarowane jako otwarte.

## Cztery ścieżki po 10 minut

| Ścieżka | Aby zobaczyć… | Jak |
|---|---|---|
| **A. Obserwowalność i orkiestracja** | Przepływy, metryki, dashboardy i guardrails w 20 przypadkach i ponad 18 silnikach BD | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Powtarzalna infrastruktura** | Laboratoria kontenerowe uruchomione w minuty | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Agenci z typowanym stanem** | 25 backendów LangGraph, DEMO/LIVE, łańcuch dowodowy | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Produkt forensic w Rust** | Instalatory i binaria z sumami kontrolnymi, bez klonowania | [Wydania RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Sygnały jakości, które możesz zweryfikować

| Sygnał | Gdzie szukać |
|---|---|
| Testy | GabySQL z 850 testami i fuzzem 503,8 mln zapytań bez panik; Empresa Operativa Chile z 230 testami; Automa ze 150 pytest |
| Łańcuch dostaw | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, SBOM CycloneDX i Scorecard, zależnie od repo |
| Telemetria | Zero w produktach forensic i w Empresa Operativa Chile, weryfikowane przy każdym buildzie |
| Dystrybucja | Wydania z sumami kontrolnymi i dowodami buildu; podpisy komercyjne zadeklarowane jako oczekujące |
| Uczciwość | Każde repo deklaruje swój stan i czego **nie** robi |

Wszystkie liczby ze źródłem są w [Stan weryfikowalny](../../README.pl.md#stan-weryfikowalny).

## Jak projektuję

- **Od modelu na zewnątrz:** najpierw domena, interfejs jako projekcja.
- **Obserwowalność od pierwszego dnia:** `/health`, `/ready`, `/metrics` i śledzalność.
- **Realna odporność:** idempotentność, circuit breaker i kontrolowana degradacja.
- **Poliglota z założenia:** język i silnik dobrane do przypadku użycia.
- **DX przede wszystkim:** `doctor` i `smoke` w każdym repo; jeśli nie uruchamia się łatwo, nie nadaje się na bazę zespołu.

## Gdzie zgłębić temat

- [Stos technologiczny](../../README.pl.md#-stos-technologiczny) wykryty w repozytoriach.
- [Zobacz pełny ekosystem](../ECOSYSTEM.pl.md): każdy produkt z wersją, testami i wydaniem.
- Forki cudzych projektów są trzymane osobno i nie liczą się jako dzieło własne: [Forki projektów osób trzecich](../ECOSYSTEM.pl.md#forks).

## Następny krok

Aby omówić przegląd architektury lub rozmowę techniczną, napisz na [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
