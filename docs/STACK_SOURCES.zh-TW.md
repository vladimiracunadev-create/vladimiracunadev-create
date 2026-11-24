# 🔎 技術棧的來源

[← 返回檔案](../README.zh-TW.md)

**🌐** [Español](STACK_SOURCES.md) · [English](STACK_SOURCES.en.md) · [Português](STACK_SOURCES.pt.md) · [Italiano](STACK_SOURCES.it.md) · [Français](STACK_SOURCES.fr.md) · [简体中文](STACK_SOURCES.zh.md) · **繁體中文** · [日本語](STACK_SOURCES.ja.md) · [한국어](STACK_SOURCES.ko.md) · [Türkçe](STACK_SOURCES.tr.md) · [Русский](STACK_SOURCES.ru.md) · [Tiếng Việt](STACK_SOURCES.vi.md) · [ไทย](STACK_SOURCES.th.md) · [Deutsch](STACK_SOURCES.de.md) · [Українська](STACK_SOURCES.uk.md) · [Polski](STACK_SOURCES.pl.md) · [العربية](STACK_SOURCES.ar.md) · [فارسی](STACK_SOURCES.fa.md) · [Bahasa Indonesia](STACK_SOURCES.id.md) · [Nederlands](STACK_SOURCES.nl.md) · [हिन्दी](STACK_SOURCES.hi.md) · [Ελληνικά](STACK_SOURCES.el.md)

本檔案的技術棧來自這個賬號公開倉庫中實際存在的內容，而不是意向清單。本文說明什麼算作證據、每個領域來自哪個倉庫或哪個地方，以及哪些只是作者的宣告。

## 納入規則

1. **僅限自己的公開倉庫。** 私有倉庫和第三方專案的 fork 不計入。
2. **證據在倉庫裡。** 計入的是出現在程式碼、清單和鎖檔案、Docker/Compose、CI/CD 工作流、Terraform，或實驗室、課程文件中的內容。課程文字裡的順帶提及不算：Snowflake、BigQuery、Spark 和 Airflow 只作為課程內容出現，因此不在技術棧中。
3. **看使用，不看年限。** 出現在倉庫裡證明用過，並不等於宣告有多少年的生產經驗。
4. **宣告的內容單獨標註。** 無法透過公開倉庫驗證的內容會標為作者宣告（見下文）。

## 每個領域的來源

| 領域 | 證據來源 | 檢視位置 |
|---|---|---|
| 程式語言 | GitHub 語言統計和清單 | Python · JavaScript · TypeScript · Rust · Go · Java · PHP · C# · Dart · Kotlin · Ruby → [vladimiracunadev-create](https://github.com/vladimiracunadev-create/?tab=repositories&type=source) · Zig · Elixir · Erlang · Crystal · Clojure · F# · Swift → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Solidity → [blockchain-learning-path](https://github.com/vladimiracunadev-create/blockchain-learning-path) · GDScript → [modern-gamedev-program](https://github.com/vladimiracunadev-create/modern-gamedev-program) · HCL → [multi-cloud-engineering-program](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) |
| 框架、執行環境與函式庫 | GitHub 語言統計和清單 | FastAPI · Flask · Laravel · Symfony · React · Next.js → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Express · Django · Spring Boot · ASP.NET · Astro → [framework-ecosystems-labs](https://github.com/vladimiracunadev-create/framework-ecosystems-labs) · Flutter → [universal-code-scanner](https://github.com/vladimiracunadev-create/universal-code-scanner), [rootcause-qr-inspector](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) · Electron → [aws-desktop-studio](https://github.com/vladimiracunadev-create/aws-desktop-studio) · Rust → [rootcause-windows-inspector](https://github.com/vladimiracunadev-create/rootcause-windows-inspector), [gabysql](https://github.com/vladimiracunadev-create/gabysql) · TypeScript → [human-genome-labs](https://github.com/vladimiracunadev-create/human-genome-labs) · PyTorch · LoRA → [python-data-science-program](https://github.com/vladimiracunadev-create/python-data-science-program) |
| 軟體架構 | 倉庫程式碼和文件 | Local-first → [empresa-operativa-chile](https://github.com/vladimiracunadev-create/empresa-operativa-chile), [ai-dataset-foundry](https://github.com/vladimiracunadev-create/ai-dataset-foundry) · Event-driven → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Resilience → [problem-driven-systems-lab](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) · Ledger → [universal-payments-engineering-lab](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) · Plugins → [agentic-plugins-toolkit](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) · Agents → [langgraph-realworld](https://github.com/vladimiracunadev-create/langgraph-realworld), [operational-ai-agents](https://github.com/vladimiracunadev-create/operational-ai-agents) · Domain-first → [rhino-suite](https://github.com/vladimiracunadev-create/rhino-suite) · Micro-apps → [microsistemas](https://github.com/vladimiracunadev-create/microsistemas) · Embedded DB → [gabysql](https://github.com/vladimiracunadev-create/gabysql) · IaC → [proyectos-aws](https://github.com/vladimiracunadev-create/proyectos-aws) |
| 資料庫 | 工作流、Terraform 和 Docker/Compose | PostgreSQL · Redis · Elasticsearch → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · Supabase · Hasura → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · 18+ → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler), [database-systems-labs](https://github.com/vladimiracunadev-create/database-systems-labs) · GabySQL → [gabysql](https://github.com/vladimiracunadev-create/gabysql) · Qdrant → [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets) |
| 資料分析與商業智慧（BI） | 倉庫程式碼和文件 | Power BI · DAX · Star schema → [social-bot-scheduler/analytics/powerbi](https://github.com/vladimiracunadev-create/social-bot-scheduler/tree/main/analytics/powerbi) (3 × .pbix) |
| 雲端、容器與 DevOps | 工作流、Terraform 和 Docker/Compose | GitHub Actions → [proyectos-aws](https://github.com/vladimiracunadev-create/proyectos-aws) · GitLab CI → [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) · Terraform · Kubernetes · Azure · GCP → [multi-cloud-engineering-program](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) · Docker → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · WSL → [wsl-labs](https://github.com/vladimiracunadev-create/wsl-labs) |
| AWS：已使用的服務（GitLab CI 案例） | 真實案例和查詢 | A–P → [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) · EC2 · RDS · VPC · Secrets Manager · CloudFormation · Cost Explorer → [aws-desktop-studio](https://github.com/vladimiracunadev-create/aws-desktop-studio) |
| 可觀測性與訊息 | 工作流、Terraform 和 Docker/Compose | Prometheus · Grafana · RabbitMQ → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · Kafka · MQTT → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) |
| AI、代理、技能與 MCP | 倉庫程式碼和文件 | LangGraph → [langgraph-realworld](https://github.com/vladimiracunadev-create/langgraph-realworld) · Agents → [operational-ai-agents](https://github.com/vladimiracunadev-create/operational-ai-agents) · MCP · Ollama → [mcp-ollama-local](https://github.com/vladimiracunadev-create/mcp-ollama-local) · Skills → [claude-skills-toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit), [codex-skills-toolkit](https://github.com/vladimiracunadev-create/codex-skills-toolkit) · Plugins → [agentic-plugins-toolkit](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) · JSONL · RAG → [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets), [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) |
| AI-輔助發展流動 | 部署和作者宣告 | Claude Code · Codex → [claude-skills-toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit), [codex-skills-toolkit](https://github.com/vladimiracunadev-create/codex-skills-toolkit) · VS Code → [rootcause-windows-inspector](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) · ChatGPT Plus · Antigravity · OpenCode |
| 資安與供應鏈 | 安全工作流 | security.yml → [universal-api-orchestrator](https://github.com/vladimiracunadev-create/universal-api-orchestrator), [psychometrics-and-assessment-program](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program), [human-genome-labs](https://github.com/vladimiracunadev-create/human-genome-labs), [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets) · [modern-cybersecurity-program](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) |
| 目標平台 | 釋出產物 | Android · Windows · Web → [empresa-operativa-chile](https://github.com/vladimiracunadev-create/empresa-operativa-chile) · Windows · macOS · Linux · Android · PWA → [spherex-releases](https://github.com/vladimiracunadev-create/spherex-releases) |
| 釋出技術 | 部署和作者宣告 | GitHub Pages → [vladimiracunadev-create.github.io](https://github.com/vladimiracunadev-create/vladimiracunadev-create.github.io) · Vercel → [spherex-releases](https://github.com/vladimiracunadev-create/spherex-releases) · Cloudflare · AWS |

## 作者宣告（無法在公開倉庫中驗證）

這些內容在技術棧中是因為作者在使用，但沒有任何公開倉庫能單獨證明它們：

- **Cloudflare** — 個人工作。
- **ChatGPT Plus**（自 2023 年起）、**Antigravity** 和 **OpenCode** — AI 輔助開發流程中的工具。
- **與 GitLab 相關的運營網站上的 AWS** — 可公開驗證的是專案 [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab)，而不是這些網站。

## 如何驗證

任何人都可以用 GitHub CLI（`gh`）重複驗證：

```bash
gh repo list vladimiracunadev-create --visibility public --source --limit 200
gh api repos/vladimiracunadev-create/<repo>/languages
gh search code "<tech>" --owner vladimiracunadev-create
```

## 如何維護

- 技術棧及其圖表由 `scripts/stack_data.json` 透過 `scripts/stack_graphic.py` 生成；檔案中的數字由 `stats.yml` 工作流計算。
- 技術出現在某個公開倉庫（程式碼、清單、工作流或實驗室）時進入技術棧，不再出現在任何倉庫時移出。

## 侷限

- GitHub 的語言統計會計入生成檔案和資料檔案（所以 HTML 佔比很大）：它只說明倉庫裡有什麼，不代表我對每種語言有多熟悉。
- 私有倉庫和客戶工作不屬於這個技術棧，也不作為證據。
