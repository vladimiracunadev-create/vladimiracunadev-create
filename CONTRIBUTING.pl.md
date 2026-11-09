# Przewodnik współpracy

**Języki:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

Dziękujemy za rozważenie wkładu w ten ekosystem. Ponieważ został zaprojektowany wokół **obserwowalności**, **powtarzalności**, **jakości local-first** i **idempotentności**, stawiamy wysokie wymagania integralności kodu, aby to portfolio pozostało odzwierciedleniem nowoczesnej inżynierii.

## Wkład, który mile widzimy

- 🐛 **Poprawki błędów:** Rozwiązuj zidentyfikowane problemy, najlepiej z automatycznym testem (`pytest` itp.), który potwierdza poprawkę.
- 🚀 **Nowe funkcje:** Ulepszenia architektury i nowe integracje, na przykład z n8n, Ollama lub LangGraph.
- 📖 **Dokumentacja:** Jaśniejsze wyjaśnienia, tłumaczenia lub jawne diagramy architektury (Mermaid lub draw.io).
- 🏗️ **Infrastruktura:** Usprawnienia przepływów DevOps (Kubernetes, CI/CD, Makefile i konfiguracja PWA).

## Przepływ pracy (Git Flow)

Ten projekt stosuje ustandaryzowany przepływ z gałęziami funkcjonalnymi:

1. **Sforkuj** repozytorium na swoje konto.
2. **Utwórz gałąź** dla swojej funkcji lub poprawki na podstawie najnowszej gałęzi `main`:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. **Rozwijaj** swoją zmianę.
   - Trzymaj się ustalonego podejścia repozytorium. Jeśli używa `uv` do wydajnych przepływów Pythona, nie zastępuj go bez uzasadnienia zmiany.
   - Uruchom istniejące zabezpieczenia projektu.
4. **Zatwierdź** zmiany (commit). Używamy **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:` itd.):

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. **Wypchnij** (push) swoją gałąź:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. **Otwórz Pull Request (PR)** do gałęzi `main` tego repozytorium.

## Standardy kodu

- **Programowanie sterowane testami (opcjonalne, ale zalecane):** Podaj polecenia uruchamiania testów. Jeśli repozytorium ma GitHub Actions dla `mypy` lub `bandit`, upewnij się, że zmiany przechodzą lokalnie (`make test`, `make lint` lub skrypty dostępne w ekosystemie).
- **Docker-first:** Każda wymagana zależność musi być udokumentowana i dostępna przez `docker-compose.yml`, aby architektura uruchamiała się w mniej niż 60 sekund lub w inny sposób unikała zbędnych kłopotów z lokalną konfiguracją.
- **Dokumentacja jest wymagana:** Przy większej zmianie zaktualizuj README i, jeśli to zasadne, dodaj diagram wyjaśniający.
