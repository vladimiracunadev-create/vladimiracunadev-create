# 🔎 Откуда берётся технологический стек

[← Назад к профилю](../README.ru.md)

**🌐** [Español](STACK_SOURCES.md) · [English](STACK_SOURCES.en.md) · [Português](STACK_SOURCES.pt.md) · [Italiano](STACK_SOURCES.it.md) · [Français](STACK_SOURCES.fr.md) · [简体中文](STACK_SOURCES.zh.md) · [繁體中文](STACK_SOURCES.zh-TW.md) · [日本語](STACK_SOURCES.ja.md) · [한국어](STACK_SOURCES.ko.md) · [Türkçe](STACK_SOURCES.tr.md) · **Русский** · [Tiếng Việt](STACK_SOURCES.vi.md) · [ไทย](STACK_SOURCES.th.md) · [Deutsch](STACK_SOURCES.de.md) · [Українська](STACK_SOURCES.uk.md) · [Polski](STACK_SOURCES.pl.md) · [العربية](STACK_SOURCES.ar.md) · [فارسی](STACK_SOURCES.fa.md) · [Bahasa Indonesia](STACK_SOURCES.id.md) · [Nederlands](STACK_SOURCES.nl.md) · [हिन्दी](STACK_SOURCES.hi.md) · [Ελληνικά](STACK_SOURCES.el.md)

Технологический стек профиля берётся из того, что есть в публичных репозиториях этого аккаунта, а не из списка намерений. Этот документ объясняет, что считается доказательством, из какого репозитория или места берётся каждая область и что является лишь заявлением автора.

## Правила включения

1. **Только собственные публичные репозитории.** Приватные репозитории и форки чужих проектов не учитываются.
2. **Доказательство находится в репозитории.** Учитывается то, что есть в коде, манифестах и lock-файлах, Docker/Compose, CI/CD-воркфлоу, Terraform или в документации лаборатории либо учебной программы. Случайное упоминание в тексте курса не считается: Snowflake, BigQuery, Spark и Airflow встречаются только как содержание курсов, поэтому их нет в стеке.
3. **Использование, а не годы.** Присутствие в репозитории — свидетельство использования, а не утверждение о годах производственного опыта.
4. **Заявленное отделено.** То, что нельзя проверить по публичным репозиториям, помечено как заявленное автором (ниже).

## Откуда берётся каждая область

| Область | Источник доказательства | Где смотреть |
|---|---|---|
| Языки | Статистика языков GitHub и манифесты | Python · JavaScript · TypeScript · Rust · Go · Java · PHP · C# · Dart · Kotlin · Ruby → [vladimiracunadev-create](https://github.com/vladimiracunadev-create/?tab=repositories&type=source) · Zig · Elixir · Erlang · Crystal · Clojure · F# · Swift → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Solidity → [blockchain-learning-path](https://github.com/vladimiracunadev-create/blockchain-learning-path) · GDScript → [modern-gamedev-program](https://github.com/vladimiracunadev-create/modern-gamedev-program) · HCL → [multi-cloud-engineering-program](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) |
| Фреймворки, среды выполнения и библиотеки | Статистика языков GitHub и манифесты | FastAPI · Flask · Laravel · Symfony · React · Next.js → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Express · Django · Spring Boot · ASP.NET · Astro → [framework-ecosystems-labs](https://github.com/vladimiracunadev-create/framework-ecosystems-labs) · Flutter → [universal-code-scanner](https://github.com/vladimiracunadev-create/universal-code-scanner), [rootcause-qr-inspector](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) · Electron → [aws-desktop-studio](https://github.com/vladimiracunadev-create/aws-desktop-studio) · Rust → [rootcause-windows-inspector](https://github.com/vladimiracunadev-create/rootcause-windows-inspector), [gabysql](https://github.com/vladimiracunadev-create/gabysql) · TypeScript → [human-genome-labs](https://github.com/vladimiracunadev-create/human-genome-labs) · PyTorch · LoRA → [python-data-science-program](https://github.com/vladimiracunadev-create/python-data-science-program) |
| Архитектуры ПО | Код и документация репозитория | Local-first → [empresa-operativa-chile](https://github.com/vladimiracunadev-create/empresa-operativa-chile), [ai-dataset-foundry](https://github.com/vladimiracunadev-create/ai-dataset-foundry) · Event-driven → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Resilience → [problem-driven-systems-lab](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) · Ledger → [universal-payments-engineering-lab](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) · Plugins → [agentic-plugins-toolkit](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) · Agents → [langgraph-realworld](https://github.com/vladimiracunadev-create/langgraph-realworld), [operational-ai-agents](https://github.com/vladimiracunadev-create/operational-ai-agents) · Domain-first → [rhino-suite](https://github.com/vladimiracunadev-create/rhino-suite) · Micro-apps → [microsistemas](https://github.com/vladimiracunadev-create/microsistemas) · Embedded DB → [gabysql](https://github.com/vladimiracunadev-create/gabysql) · IaC → [proyectos-aws](https://github.com/vladimiracunadev-create/proyectos-aws) |
| Базы данных | Воркфлоу, Terraform и Docker/Compose | PostgreSQL · Redis · Elasticsearch → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · Supabase · Hasura → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · 18+ → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler), [database-systems-labs](https://github.com/vladimiracunadev-create/database-systems-labs) · GabySQL → [gabysql](https://github.com/vladimiracunadev-create/gabysql) · Qdrant → [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets) |
| Аналитика данных и BI | Код и документация репозитория | Power BI · DAX · Star schema → [social-bot-scheduler/analytics/powerbi](https://github.com/vladimiracunadev-create/social-bot-scheduler/tree/main/analytics/powerbi) (3 × .pbix) |
| Облако, контейнеры и DevOps | Воркфлоу, Terraform и Docker/Compose | GitHub Actions → [proyectos-aws](https://github.com/vladimiracunadev-create/proyectos-aws) · GitLab CI → [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) · Terraform · Kubernetes · Azure · GCP → [multi-cloud-engineering-program](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) · Docker → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · WSL → [wsl-labs](https://github.com/vladimiracunadev-create/wsl-labs) |
| AWS: используемые сервисы (кейсы в GitLab CI) | Реальные кейсы и запросы | A–P → [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) · EC2 · RDS · VPC · Secrets Manager · CloudFormation · Cost Explorer → [aws-desktop-studio](https://github.com/vladimiracunadev-create/aws-desktop-studio) |
| Наблюдаемость и обмен сообщениями | Воркфлоу, Terraform и Docker/Compose | Prometheus · Grafana · RabbitMQ → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · Kafka · MQTT → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) |
| ИИ, агенты, навыки и MCP | Код и документация репозитория | LangGraph → [langgraph-realworld](https://github.com/vladimiracunadev-create/langgraph-realworld) · Agents → [operational-ai-agents](https://github.com/vladimiracunadev-create/operational-ai-agents) · MCP · Ollama → [mcp-ollama-local](https://github.com/vladimiracunadev-create/mcp-ollama-local) · Skills → [claude-skills-toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit), [codex-skills-toolkit](https://github.com/vladimiracunadev-create/codex-skills-toolkit) · Plugins → [agentic-plugins-toolkit](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) · JSONL · RAG → [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets), [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) |
| Поток развития с помощью ИИ | Развёртывания и заявление автора | Claude Code · Codex → [claude-skills-toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit), [codex-skills-toolkit](https://github.com/vladimiracunadev-create/codex-skills-toolkit) · VS Code → [rootcause-windows-inspector](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) · ChatGPT Plus · Antigravity · OpenCode |
| Безопасность и цепочка поставок | Воркфлоу безопасности | security.yml → [universal-api-orchestrator](https://github.com/vladimiracunadev-create/universal-api-orchestrator), [psychometrics-and-assessment-program](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program), [human-genome-labs](https://github.com/vladimiracunadev-create/human-genome-labs), [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets) · [modern-cybersecurity-program](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) |
| Целевые платформы | Артефакты релизов | Android · Windows · Web → [empresa-operativa-chile](https://github.com/vladimiracunadev-create/empresa-operativa-chile) · Windows · macOS · Linux · Android · PWA → [spherex-releases](https://github.com/vladimiracunadev-create/spherex-releases) |
| Технологии публикации | Развёртывания и заявление автора | GitHub Pages → [vladimiracunadev-create.github.io](https://github.com/vladimiracunadev-create/vladimiracunadev-create.github.io) · Vercel → [spherex-releases](https://github.com/vladimiracunadev-create/spherex-releases) · Cloudflare · AWS |

## Заявлено автором (не проверяется по публичным репозиториям)

Эти пункты есть в стеке, потому что автор их использует, но ни один публичный репозиторий не доказывает их сам по себе:

- **Cloudflare** — личная работа.
- **ChatGPT Plus** (с 2023 года), **Antigravity** и **OpenCode** — инструменты процесса разработки с помощью ИИ.
- **AWS на рабочих сайтах, связанных с GitLab** — публично проверяем проект [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab), а не сами сайты.

## Как проверить

Любой может повторить проверку с помощью GitHub CLI (`gh`):

```bash
gh repo list vladimiracunadev-create --visibility public --source --limit 200
gh api repos/vladimiracunadev-create/<repo>/languages
gh search code "<tech>" --owner vladimiracunadev-create
```

## Как это поддерживается

- Технологии и их график генерируются из `scripts/stack_data.json` скриптом `scripts/stack_graphic.py`; цифры профиля считает воркфлоу `stats.yml`.
- Технология попадает в стек, когда появляется в публичном репозитории (код, манифест, воркфлоу или лаборатория), и выбывает, если нигде больше не встречается.

## Ограничения

- Статистика языков GitHub учитывает сгенерированные файлы и файлы данных (поэтому HTML весит так много): она показывает, что есть в репозитории, а не насколько хорошо я знаю каждый язык.
- Приватные репозитории и работа для клиентов не входят в этот стек и не используются как доказательство.
