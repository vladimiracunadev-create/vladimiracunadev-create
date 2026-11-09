# Bijdragegids

**Talen:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

Bedankt dat je overweegt bij te dragen aan dit ecosysteem. Omdat het is ontworpen rond **observability**, **reproduceerbaarheid**, **local-first kwaliteit** en **idempotentie**, stellen we hoge eisen aan de integriteit van de code, zodat dit portfolio een afspiegeling blijft van moderne engineering.

## Bijdragen die we verwelkomen

- 🐛 **Bugfixes:** Los vastgestelde problemen op, bij voorkeur met een geautomatiseerde test (`pytest`, enz.) die de oplossing bewijst.
- 🚀 **Nieuwe functies:** Architectuurverbeteringen en nieuwe integraties, bijvoorbeeld met n8n, Ollama of LangGraph.
- 📖 **Documentatie:** Duidelijkere uitleg, vertalingen of expliciete architectuurdiagrammen (Mermaid of draw.io).
- 🏗️ **Infrastructuur:** Verbeteringen aan DevOps-workflows (Kubernetes, CI/CD, Makefiles en PWA-configuratie).

## Werkwijze (Git Flow)

Dit project gebruikt een gestandaardiseerde feature-branch-werkwijze:

1. **Fork** de repository naar je account.
2. **Maak een branch** voor je feature of fix vanaf de nieuwste `main`-branch:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. **Ontwikkel** je wijziging.
   - Volg de gevestigde aanpak van de repository. Als die `uv` gebruikt voor hoogwaardige Python-workflows, vervang het dan niet zonder de wijziging te motiveren.
   - Voer de bestaande vangrails van het project uit.
4. **Commit** je wijzigingen. We gebruiken **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:`, enz.):

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. **Push** je branch:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. **Open een Pull Request (PR)** tegen de `main`-branch van deze repository.

## Codestandaarden

- **Testgedreven ontwikkeling (optioneel maar aanbevolen):** Voeg opdrachten toe om je tests uit te voeren. Heeft de repository GitHub Actions voor `mypy` of `bandit`, zorg dan dat je wijzigingen lokaal slagen (`make test`, `make lint` of de scripts in het ecosysteem).
- **Docker-first:** Elke vereiste afhankelijkheid moet gedocumenteerd en beschikbaar zijn via `docker-compose.yml`, zodat de architectuur in minder dan 60 seconden start of onnodige lokale installatiehobbels worden vermeden.
- **Documentatie is verplicht:** Werk bij een grote wijziging de README bij en voeg waar nuttig een verklarend diagram toe.
