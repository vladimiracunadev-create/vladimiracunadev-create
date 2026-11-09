# Beitragsleitfaden

**Sprachen:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

Danke, dass Sie einen Beitrag zu diesem Ökosystem in Erwägung ziehen. Da es auf **Observability**, **Reproduzierbarkeit**, **Local-first-Qualität** und **Idempotenz** ausgelegt ist, stellen wir hohe Anforderungen an die Code-Integrität, damit dieses Portfolio ein Abbild moderner Ingenieurskunst bleibt.

## Beiträge, die wir begrüßen

- 🐛 **Fehlerbehebungen:** Beheben Sie erkannte Probleme, möglichst mit einem automatisierten Test (`pytest` usw.), der die Korrektur belegt.
- 🚀 **Neue Funktionen:** Architekturverbesserungen und neue Integrationen, zum Beispiel mit n8n, Ollama oder LangGraph.
- 📖 **Dokumentation:** Verständlichere Erklärungen, Übersetzungen oder explizite Architekturdiagramme (Mermaid oder draw.io).
- 🏗️ **Infrastruktur:** Verbesserungen an DevOps-Workflows (Kubernetes, CI/CD, Makefiles und PWA-Konfiguration).

## Arbeitsablauf (Git Flow)

Dieses Projekt nutzt einen standardisierten Feature-Branch-Workflow:

1. **Forken** Sie das Repository in Ihr Konto.
2. **Erstellen Sie einen Branch** für Ihr Feature oder Ihren Fix vom aktuellen `main`-Branch:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. **Entwickeln** Sie Ihre Änderung.
   - Folgen Sie dem etablierten Ansatz des Repositorys. Wenn es `uv` für leistungsstarke Python-Workflows verwendet, ersetzen Sie es nicht, ohne die Änderung zu begründen.
   - Führen Sie die vorhandenen Schutzmechanismen des Projekts aus.
4. **Committen** Sie Ihre Änderungen. Wir verwenden **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:` usw.):

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. **Pushen** Sie Ihren Branch:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. **Eröffnen Sie einen Pull Request (PR)** gegen den `main`-Branch dieses Repositorys.

## Code-Standards

- **Testgetriebene Entwicklung (optional, aber empfohlen):** Geben Sie die Befehle zum Ausführen Ihrer Tests an. Wenn das Repository GitHub Actions für `mypy` oder `bandit` hat, stellen Sie sicher, dass Ihre Änderungen lokal bestehen (`make test`, `make lint` oder die im Ökosystem verfügbaren Skripte).
- **Docker-first:** Jede benötigte Abhängigkeit muss dokumentiert und über `docker-compose.yml` verfügbar sein, damit die Architektur in weniger als 60 Sekunden startet oder unnötige lokale Einrichtungshürden vermieden werden.
- **Dokumentation ist Pflicht:** Aktualisieren Sie bei einer größeren Änderung das README und fügen Sie gegebenenfalls ein erklärendes Diagramm hinzu.
