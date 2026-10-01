# Guida alla Contribuzione

**Lingue:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md)

Grazie per aver preso in considerazione un contributo a questo ecosistema. Poiché è progettato secondo i principi di **osservabilità**, **riproducibilità**, **qualità local-first** e **idempotenza**, manteniamo aspettative elevate sull'integrità del codice affinché questo portfolio continui a riflettere l'ingegneria moderna.

## Tipi di Contributo Richiesti

- 🐛 **Correzione di bug:** Risolvi i problemi identificati, preferibilmente aggiungendo un test automatico (`pytest`, ecc.) che dimostri la soluzione.
- 🚀 **Nuove funzionalità:** Miglioramenti architetturali e nuove integrazioni, ad esempio con n8n, Ollama o LangGraph.
- 📖 **Documentazione:** Maggiore chiarezza, traduzioni o diagrammi architetturali espliciti (Mermaid o draw.io).
- 🏗️ **Infrastruttura:** Miglioramenti ai flussi DevOps (Kubernetes, CI/CD, Makefile e configurazione PWA).

## Flusso di Lavoro (Git Flow)

Questo progetto usa un flusso standardizzato basato su branch di funzionalità:

1. **Crea un fork** del repository nel tuo account.
2. **Crea un branch** per la funzionalità o la correzione partendo dallo stato più recente di `main`:

   ```bash
   git checkout -b feature/nuova-magia-aws
   # oppure per le correzioni
   git checkout -b fix/auth-bypass
   ```

3. **Sviluppa** la modifica.
   - Segui l'approccio stabilito dal repository. Se usa `uv` per flussi Python ad alte prestazioni, non sostituirlo senza motivare il cambiamento.
   - Esegui i guardrail esistenti nel progetto.
4. **Crea un commit** delle modifiche. Usiamo i **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:`, ecc.):

   ```bash
   git commit -m "feat: implementare circuit breaker globale per le chiamate fallite"
   ```

5. **Esegui il push** del branch:

   ```bash
   git push origin feature/nuova-magia-aws
   ```

6. **Apri una Pull Request (PR)** verso il branch `main` di questo repository.

## Standard del Codice

- **Sviluppo guidato dai test (opzionale ma consigliato):** Includi i comandi per eseguire i test. Se il repository dispone di GitHub Actions con `mypy` o `bandit`, assicurati che le modifiche passino localmente (`make test`, `make lint` o gli script disponibili nell'ecosistema).
- **Docker-first:** Ogni dipendenza richiesta deve essere documentata e disponibile tramite `docker-compose.yml`, così da avviare l'architettura in meno di 60 secondi o evitare attriti inutili nella configurazione locale.
- **Documentazione obbligatoria:** Per una modifica importante, aggiorna il README e, quando applicabile, aggiungi un diagramma esplicativo.
