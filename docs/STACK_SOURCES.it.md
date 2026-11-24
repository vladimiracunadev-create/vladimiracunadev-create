# 🔎 Da dove nasce lo Stack tecnologico

[← Torna al profilo](../README.it.md)

**🌐** [Español](STACK_SOURCES.md) · [English](STACK_SOURCES.en.md) · [Português](STACK_SOURCES.pt.md) · **Italiano** · [Français](STACK_SOURCES.fr.md) · [简体中文](STACK_SOURCES.zh.md) · [繁體中文](STACK_SOURCES.zh-TW.md) · [日本語](STACK_SOURCES.ja.md) · [한국어](STACK_SOURCES.ko.md) · [Türkçe](STACK_SOURCES.tr.md) · [Русский](STACK_SOURCES.ru.md) · [Tiếng Việt](STACK_SOURCES.vi.md) · [ไทย](STACK_SOURCES.th.md) · [Deutsch](STACK_SOURCES.de.md) · [Українська](STACK_SOURCES.uk.md) · [Polski](STACK_SOURCES.pl.md) · [العربية](STACK_SOURCES.ar.md) · [فارسی](STACK_SOURCES.fa.md) · [Bahasa Indonesia](STACK_SOURCES.id.md) · [Nederlands](STACK_SOURCES.nl.md) · [हिन्दी](STACK_SOURCES.hi.md) · [Ελληνικά](STACK_SOURCES.el.md)

Lo Stack tecnologico del profilo nasce da ciò che c'è nei repository pubblici di questo account, non da un elenco di intenzioni. Questo documento spiega cosa conta come evidenza, da quale repository o luogo nasce ogni area e cosa è solo una dichiarazione dell'autore.

## Regole di inclusione

1. **Solo repository pubblici propri.** Non contano i repository privati né i fork di progetti di terzi.
2. **L'evidenza è nel repository.** Conta ciò che compare in codice, manifest e lockfile, Docker/Compose, workflow di CI/CD, Terraform o nella documentazione di un laboratorio o curriculum. Una menzione isolata nel testo di un corso non conta: Snowflake, BigQuery, Spark o Airflow compaiono solo come contenuto di corsi e per questo non sono nello Stack.
3. **Uso, non anni.** Comparire in un repository è evidenza d'uso, non un'affermazione di anni di esperienza produttiva.
4. **Il dichiarato resta a parte.** Ciò che non si può verificare dai repository pubblici è indicato come dichiarato dall'autore (più sotto).

## Da dove nasce ogni area

| Area | Fonte dell'evidenza | Dove guardare |
|---|---|---|
| Linguaggi | Statistiche dei linguaggi di GitHub e manifest | Python · JavaScript · TypeScript · Rust · Go · Java · PHP · C# · Dart · Kotlin · Ruby → [vladimiracunadev-create](https://github.com/vladimiracunadev-create/?tab=repositories&type=source) · Zig · Elixir · Erlang · Crystal · Clojure · F# · Swift → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Solidity → [blockchain-learning-path](https://github.com/vladimiracunadev-create/blockchain-learning-path) · GDScript → [modern-gamedev-program](https://github.com/vladimiracunadev-create/modern-gamedev-program) · HCL → [multi-cloud-engineering-program](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) |
| Framework, runtime e librerie | Statistiche dei linguaggi di GitHub e manifest | FastAPI · Flask · Laravel · Symfony · React · Next.js → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Express · Django · Spring Boot · ASP.NET · Astro → [framework-ecosystems-labs](https://github.com/vladimiracunadev-create/framework-ecosystems-labs) · Flutter → [universal-code-scanner](https://github.com/vladimiracunadev-create/universal-code-scanner), [rootcause-qr-inspector](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) · Electron → [aws-desktop-studio](https://github.com/vladimiracunadev-create/aws-desktop-studio) · Rust → [rootcause-windows-inspector](https://github.com/vladimiracunadev-create/rootcause-windows-inspector), [gabysql](https://github.com/vladimiracunadev-create/gabysql) · TypeScript → [human-genome-labs](https://github.com/vladimiracunadev-create/human-genome-labs) · PyTorch · LoRA → [python-data-science-program](https://github.com/vladimiracunadev-create/python-data-science-program) |
| Architetture software | Codice e documentazione del repository | Local-first → [empresa-operativa-chile](https://github.com/vladimiracunadev-create/empresa-operativa-chile), [ai-dataset-foundry](https://github.com/vladimiracunadev-create/ai-dataset-foundry) · Event-driven → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Resilience → [problem-driven-systems-lab](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) · Ledger → [universal-payments-engineering-lab](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) · Plugins → [agentic-plugins-toolkit](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) · Agents → [langgraph-realworld](https://github.com/vladimiracunadev-create/langgraph-realworld), [operational-ai-agents](https://github.com/vladimiracunadev-create/operational-ai-agents) · Domain-first → [rhino-suite](https://github.com/vladimiracunadev-create/rhino-suite) · Micro-apps → [microsistemas](https://github.com/vladimiracunadev-create/microsistemas) · Embedded DB → [gabysql](https://github.com/vladimiracunadev-create/gabysql) · IaC → [proyectos-aws](https://github.com/vladimiracunadev-create/proyectos-aws) |
| Database | Workflow, Terraform e Docker/Compose | PostgreSQL · Redis · Elasticsearch → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · Supabase · Hasura → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · 18+ → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler), [database-systems-labs](https://github.com/vladimiracunadev-create/database-systems-labs) · GabySQL → [gabysql](https://github.com/vladimiracunadev-create/gabysql) · Qdrant → [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets) |
| Analisi dei dati e BI | Codice e documentazione del repository | Power BI · DAX · Star schema → [social-bot-scheduler/analytics/powerbi](https://github.com/vladimiracunadev-create/social-bot-scheduler/tree/main/analytics/powerbi) (3 × .pbix) |
| Cloud, container e DevOps | Workflow, Terraform e Docker/Compose | GitHub Actions → [proyectos-aws](https://github.com/vladimiracunadev-create/proyectos-aws) · GitLab CI → [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) · Terraform · Kubernetes · Azure · GCP → [multi-cloud-engineering-program](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) · Docker → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · WSL → [wsl-labs](https://github.com/vladimiracunadev-create/wsl-labs) |
| AWS: servizi usati (casi su GitLab CI) | Casi e interrogazioni reali | A–P → [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) · EC2 · RDS · VPC · Secrets Manager · CloudFormation · Cost Explorer → [aws-desktop-studio](https://github.com/vladimiracunadev-create/aws-desktop-studio) |
| Osservabilità e messaggistica | Workflow, Terraform e Docker/Compose | Prometheus · Grafana · RabbitMQ → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · Kafka · MQTT → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) |
| IA, agenti, skill e MCP | Codice e documentazione del repository | LangGraph → [langgraph-realworld](https://github.com/vladimiracunadev-create/langgraph-realworld) · Agents → [operational-ai-agents](https://github.com/vladimiracunadev-create/operational-ai-agents) · MCP · Ollama → [mcp-ollama-local](https://github.com/vladimiracunadev-create/mcp-ollama-local) · Skills → [claude-skills-toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit), [codex-skills-toolkit](https://github.com/vladimiracunadev-create/codex-skills-toolkit) · Plugins → [agentic-plugins-toolkit](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) · JSONL · RAG → [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets), [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) |
| Flusso Di Sviluppo Assistito Da IA | Distribuzioni e dichiarazione dell'autore | Claude Code · Codex → [claude-skills-toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit), [codex-skills-toolkit](https://github.com/vladimiracunadev-create/codex-skills-toolkit) · VS Code → [rootcause-windows-inspector](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) · ChatGPT Plus · Antigravity · OpenCode |
| Sicurezza e supply chain | Workflow di sicurezza | security.yml → [universal-api-orchestrator](https://github.com/vladimiracunadev-create/universal-api-orchestrator), [psychometrics-and-assessment-program](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program), [human-genome-labs](https://github.com/vladimiracunadev-create/human-genome-labs), [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets) · [modern-cybersecurity-program](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) |
| Piattaforme di destinazione | Artefatti delle release | Android · Windows · Web → [empresa-operativa-chile](https://github.com/vladimiracunadev-create/empresa-operativa-chile) · Windows · macOS · Linux · Android · PWA → [spherex-releases](https://github.com/vladimiracunadev-create/spherex-releases) |
| Tecnologie di pubblicazione | Distribuzioni e dichiarazione dell'autore | GitHub Pages → [vladimiracunadev-create.github.io](https://github.com/vladimiracunadev-create/vladimiracunadev-create.github.io) · Vercel → [spherex-releases](https://github.com/vladimiracunadev-create/spherex-releases) · Cloudflare · AWS |

## Dichiarato dall'autore (non verificabile nei repository pubblici)

Questi elementi sono nello Stack perché l'autore li usa, ma nessun repository pubblico li dimostra da solo:

- **Cloudflare** — lavoro personale.
- **ChatGPT Plus** (dal 2023), **Antigravity** e **OpenCode** — strumenti del flusso di sviluppo assistito dall'IA.
- **AWS in siti operativi legati a GitLab** — ciò che è verificabile in pubblico è il progetto [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab), non quei siti.

## Come verificarlo

Chiunque può ripetere la verifica con la CLI di GitHub (`gh`):

```bash
gh repo list vladimiracunadev-create --visibility public --source --limit 200
gh api repos/vladimiracunadev-create/<repo>/languages
gh search code "<tech>" --owner vladimiracunadev-create
```

## Come viene mantenuto

- Le tecnologie e il loro grafico sono generati da `scripts/stack_data.json` con `scripts/stack_graphic.py`; le cifre del profilo le calcola il workflow `stats.yml`.
- Una tecnologia entra nello Stack quando compare in un repository pubblico (codice, manifest, workflow o laboratorio) ed esce se smette di comparire in tutti.

## Limiti

- Le statistiche dei linguaggi di GitHub contano file generati e di dati (per questo l'HTML pesa tanto): servono a sapere cosa c'è in un repository, non quanto conosco ogni linguaggio.
- I repository privati e il lavoro per i clienti non fanno parte di questo Stack né sono usati come evidenza.
