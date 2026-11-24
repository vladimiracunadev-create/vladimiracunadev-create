# 🔎 技术栈的来源

[← 返回档案](../README.zh.md)

**🌐** [Español](STACK_SOURCES.md) · [English](STACK_SOURCES.en.md) · [Português](STACK_SOURCES.pt.md) · [Italiano](STACK_SOURCES.it.md) · [Français](STACK_SOURCES.fr.md) · **简体中文** · [繁體中文](STACK_SOURCES.zh-TW.md) · [日本語](STACK_SOURCES.ja.md) · [한국어](STACK_SOURCES.ko.md) · [Türkçe](STACK_SOURCES.tr.md) · [Русский](STACK_SOURCES.ru.md) · [Tiếng Việt](STACK_SOURCES.vi.md) · [ไทย](STACK_SOURCES.th.md) · [Deutsch](STACK_SOURCES.de.md) · [Українська](STACK_SOURCES.uk.md) · [Polski](STACK_SOURCES.pl.md) · [العربية](STACK_SOURCES.ar.md) · [فارسی](STACK_SOURCES.fa.md) · [Bahasa Indonesia](STACK_SOURCES.id.md) · [Nederlands](STACK_SOURCES.nl.md) · [हिन्दी](STACK_SOURCES.hi.md) · [Ελληνικά](STACK_SOURCES.el.md)

本档案的技术栈来自这个账号公开仓库中实际存在的内容，而不是意向清单。本文说明什么算作证据、每个领域来自哪个仓库或哪个地方，以及哪些只是作者的声明。

## 纳入规则

1. **仅限自己的公开仓库。** 私有仓库和第三方项目的 fork 不计入。
2. **证据在仓库里。** 计入的是出现在代码、清单和锁文件、Docker/Compose、CI/CD 工作流、Terraform，或实验室、课程文档中的内容。课程文字里的顺带提及不算：Snowflake、BigQuery、Spark 和 Airflow 只作为课程内容出现，因此不在技术栈中。
3. **看使用，不看年限。** 出现在仓库里证明用过，并不等于声明有多少年的生产经验。
4. **声明的内容单独标注。** 无法通过公开仓库验证的内容会标为作者声明（见下文）。

## 每个领域的来源

| 领域 | 证据来源 | 查看位置 |
|---|---|---|
| 编程语言 | GitHub 语言统计和清单 | Python · JavaScript · TypeScript · Rust · Go · Java · PHP · C# · Dart · Kotlin · Ruby → [vladimiracunadev-create](https://github.com/vladimiracunadev-create/?tab=repositories&type=source) · Zig · Elixir · Erlang · Crystal · Clojure · F# · Swift → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Solidity → [blockchain-learning-path](https://github.com/vladimiracunadev-create/blockchain-learning-path) · GDScript → [modern-gamedev-program](https://github.com/vladimiracunadev-create/modern-gamedev-program) · HCL → [multi-cloud-engineering-program](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) |
| 框架、运行时与库 | GitHub 语言统计和清单 | FastAPI · Flask · Laravel · Symfony · React · Next.js → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Express · Django · Spring Boot · ASP.NET · Astro → [framework-ecosystems-labs](https://github.com/vladimiracunadev-create/framework-ecosystems-labs) · Flutter → [universal-code-scanner](https://github.com/vladimiracunadev-create/universal-code-scanner), [rootcause-qr-inspector](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) · Electron → [aws-desktop-studio](https://github.com/vladimiracunadev-create/aws-desktop-studio) · Rust → [rootcause-windows-inspector](https://github.com/vladimiracunadev-create/rootcause-windows-inspector), [gabysql](https://github.com/vladimiracunadev-create/gabysql) · TypeScript → [human-genome-labs](https://github.com/vladimiracunadev-create/human-genome-labs) · PyTorch · LoRA → [python-data-science-program](https://github.com/vladimiracunadev-create/python-data-science-program) |
| 软件架构 | 仓库代码和文档 | Local-first → [empresa-operativa-chile](https://github.com/vladimiracunadev-create/empresa-operativa-chile), [ai-dataset-foundry](https://github.com/vladimiracunadev-create/ai-dataset-foundry) · Event-driven → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Resilience → [problem-driven-systems-lab](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) · Ledger → [universal-payments-engineering-lab](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) · Plugins → [agentic-plugins-toolkit](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) · Agents → [langgraph-realworld](https://github.com/vladimiracunadev-create/langgraph-realworld), [operational-ai-agents](https://github.com/vladimiracunadev-create/operational-ai-agents) · Domain-first → [rhino-suite](https://github.com/vladimiracunadev-create/rhino-suite) · Micro-apps → [microsistemas](https://github.com/vladimiracunadev-create/microsistemas) · Embedded DB → [gabysql](https://github.com/vladimiracunadev-create/gabysql) · IaC → [proyectos-aws](https://github.com/vladimiracunadev-create/proyectos-aws) |
| 数据库 | 工作流、Terraform 和 Docker/Compose | PostgreSQL · Redis · Elasticsearch → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · Supabase · Hasura → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · 18+ → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler), [database-systems-labs](https://github.com/vladimiracunadev-create/database-systems-labs) · GabySQL → [gabysql](https://github.com/vladimiracunadev-create/gabysql) · Qdrant → [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets) |
| 数据分析与商业智能（BI） | 仓库代码和文档 | Power BI · DAX · Star schema → [social-bot-scheduler/analytics/powerbi](https://github.com/vladimiracunadev-create/social-bot-scheduler/tree/main/analytics/powerbi) (3 × .pbix) |
| 云、容器与 DevOps | 工作流、Terraform 和 Docker/Compose | GitHub Actions → [proyectos-aws](https://github.com/vladimiracunadev-create/proyectos-aws) · GitLab CI → [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) · Terraform · Kubernetes · Azure · GCP → [multi-cloud-engineering-program](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) · Docker → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · WSL → [wsl-labs](https://github.com/vladimiracunadev-create/wsl-labs) |
| AWS：已使用的服务（GitLab CI 案例） | 真实案例和查询 | A–P → [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) · EC2 · RDS · VPC · Secrets Manager · CloudFormation · Cost Explorer → [aws-desktop-studio](https://github.com/vladimiracunadev-create/aws-desktop-studio) |
| 可观测性与消息 | 工作流、Terraform 和 Docker/Compose | Prometheus · Grafana · RabbitMQ → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · Kafka · MQTT → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) |
| AI、代理、技能与 MCP | 仓库代码和文档 | LangGraph → [langgraph-realworld](https://github.com/vladimiracunadev-create/langgraph-realworld) · Agents → [operational-ai-agents](https://github.com/vladimiracunadev-create/operational-ai-agents) · MCP · Ollama → [mcp-ollama-local](https://github.com/vladimiracunadev-create/mcp-ollama-local) · Skills → [claude-skills-toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit), [codex-skills-toolkit](https://github.com/vladimiracunadev-create/codex-skills-toolkit) · Plugins → [agentic-plugins-toolkit](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) · JSONL · RAG → [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets), [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) |
| AI 辅助开发流程 | 部署和作者声明 | Claude Code · Codex → [claude-skills-toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit), [codex-skills-toolkit](https://github.com/vladimiracunadev-create/codex-skills-toolkit) · VS Code → [rootcause-windows-inspector](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) · ChatGPT Plus · Antigravity · OpenCode |
| 安全与供应链 | 安全工作流 | security.yml → [universal-api-orchestrator](https://github.com/vladimiracunadev-create/universal-api-orchestrator), [psychometrics-and-assessment-program](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program), [human-genome-labs](https://github.com/vladimiracunadev-create/human-genome-labs), [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets) · [modern-cybersecurity-program](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) |
| 目标平台 | 发布产物 | Android · Windows · Web → [empresa-operativa-chile](https://github.com/vladimiracunadev-create/empresa-operativa-chile) · Windows · macOS · Linux · Android · PWA → [spherex-releases](https://github.com/vladimiracunadev-create/spherex-releases) |
| 发布技术 | 部署和作者声明 | GitHub Pages → [vladimiracunadev-create.github.io](https://github.com/vladimiracunadev-create/vladimiracunadev-create.github.io) · Vercel → [spherex-releases](https://github.com/vladimiracunadev-create/spherex-releases) · Cloudflare · AWS |

## 作者声明（无法在公开仓库中验证）

这些内容在技术栈中是因为作者在使用，但没有任何公开仓库能单独证明它们：

- **Cloudflare** — 个人工作。
- **ChatGPT Plus**（自 2023 年起）、**Antigravity** 和 **OpenCode** — AI 辅助开发流程中的工具。
- **与 GitLab 相关的运营网站上的 AWS** — 可公开验证的是项目 [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab)，而不是这些网站。

## 如何验证

任何人都可以用 GitHub CLI（`gh`）重复验证：

```bash
gh repo list vladimiracunadev-create --visibility public --source --limit 200
gh api repos/vladimiracunadev-create/<repo>/languages
gh search code "<tech>" --owner vladimiracunadev-create
```

## 如何维护

- 技术栈及其图表由 `scripts/stack_data.json` 通过 `scripts/stack_graphic.py` 生成；档案中的数字由 `stats.yml` 工作流计算。
- 技术出现在某个公开仓库（代码、清单、工作流或实验室）时进入技术栈，不再出现在任何仓库时移出。

## 局限

- GitHub 的语言统计会计入生成文件和数据文件（所以 HTML 占比很大）：它只说明仓库里有什么，不代表我对每种语言有多熟悉。
- 私有仓库和客户工作不属于这个技术栈，也不作为证据。
