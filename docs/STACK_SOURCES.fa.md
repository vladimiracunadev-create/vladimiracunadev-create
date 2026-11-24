# 🔎 پشتهٔ فناوری از کجا می‌آید

[← بازگشت به پروفایل](../README.fa.md)

**🌐** [Español](STACK_SOURCES.md) · [English](STACK_SOURCES.en.md) · [Português](STACK_SOURCES.pt.md) · [Italiano](STACK_SOURCES.it.md) · [Français](STACK_SOURCES.fr.md) · [简体中文](STACK_SOURCES.zh.md) · [繁體中文](STACK_SOURCES.zh-TW.md) · [日本語](STACK_SOURCES.ja.md) · [한국어](STACK_SOURCES.ko.md) · [Türkçe](STACK_SOURCES.tr.md) · [Русский](STACK_SOURCES.ru.md) · [Tiếng Việt](STACK_SOURCES.vi.md) · [ไทย](STACK_SOURCES.th.md) · [Deutsch](STACK_SOURCES.de.md) · [Українська](STACK_SOURCES.uk.md) · [Polski](STACK_SOURCES.pl.md) · [العربية](STACK_SOURCES.ar.md) · **فارسی** · [Bahasa Indonesia](STACK_SOURCES.id.md) · [Nederlands](STACK_SOURCES.nl.md) · [हिन्दी](STACK_SOURCES.hi.md) · [Ελληνικά](STACK_SOURCES.el.md)

پشتهٔ فناوری این پروفایل از چیزی می‌آید که در مخزن‌های عمومی این حساب وجود دارد، نه از فهرستی از نیت‌ها. این سند توضیح می‌دهد چه چیزی شاهد به‌شمار می‌آید، هر حوزه از کدام مخزن یا جا می‌آید و چه چیزی فقط اظهار نویسنده است.

## قواعد گنجاندن

1. **فقط مخزن‌های عمومیِ خودی.** مخزن‌های خصوصی و fork پروژه‌های دیگران حساب نمی‌شوند.
2. **شاهد در مخزن است.** آنچه در کد، manifest و lockfile، Docker/Compose، گردش‌کارهای CI/CD، Terraform یا مستندات یک آزمایشگاه یا برنامهٔ درسی ظاهر شود حساب می‌شود. اشارهٔ گذرا در متن یک دوره حساب نمی‌شود: Snowflake، BigQuery، Spark و Airflow فقط به‌عنوان محتوای دوره‌ها دیده می‌شوند و به همین دلیل در پشته نیستند.
3. **استفاده، نه سال.** حضور در یک مخزن شاهد استفاده است، نه ادعای سال‌ها تجربهٔ تولیدی.
4. **اظهارشده جدا می‌ماند.** آنچه از مخزن‌های عمومی قابل راستی‌آزمایی نیست به‌عنوان اظهار نویسنده علامت می‌خورد (در ادامه).

## هر حوزه از کجا می‌آید

| حوزه | منبع شاهد | کجا نگاه کنیم |
|---|---|---|
| زبان‌ها | آمار زبان‌های GitHub و manifest | Python · JavaScript · TypeScript · Rust · Go · Java · PHP · C# · Dart · Kotlin · Ruby → [vladimiracunadev-create](https://github.com/vladimiracunadev-create/?tab=repositories&type=source) · Zig · Elixir · Erlang · Crystal · Clojure · F# · Swift → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Solidity → [blockchain-learning-path](https://github.com/vladimiracunadev-create/blockchain-learning-path) · GDScript → [modern-gamedev-program](https://github.com/vladimiracunadev-create/modern-gamedev-program) · HCL → [multi-cloud-engineering-program](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) |
| چارچوب‌ها، محیط‌های اجرا و کتابخانه‌ها | آمار زبان‌های GitHub و manifest | FastAPI · Flask · Laravel · Symfony · React · Next.js → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Express · Django · Spring Boot · ASP.NET · Astro → [framework-ecosystems-labs](https://github.com/vladimiracunadev-create/framework-ecosystems-labs) · Flutter → [universal-code-scanner](https://github.com/vladimiracunadev-create/universal-code-scanner), [rootcause-qr-inspector](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) · Electron → [aws-desktop-studio](https://github.com/vladimiracunadev-create/aws-desktop-studio) · Rust → [rootcause-windows-inspector](https://github.com/vladimiracunadev-create/rootcause-windows-inspector), [gabysql](https://github.com/vladimiracunadev-create/gabysql) · TypeScript → [human-genome-labs](https://github.com/vladimiracunadev-create/human-genome-labs) · PyTorch · LoRA → [python-data-science-program](https://github.com/vladimiracunadev-create/python-data-science-program) |
| معماری‌های نرم‌افزار | کد و مستندات مخزن | Local-first → [empresa-operativa-chile](https://github.com/vladimiracunadev-create/empresa-operativa-chile), [ai-dataset-foundry](https://github.com/vladimiracunadev-create/ai-dataset-foundry) · Event-driven → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · Resilience → [problem-driven-systems-lab](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) · Ledger → [universal-payments-engineering-lab](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) · Plugins → [agentic-plugins-toolkit](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) · Agents → [langgraph-realworld](https://github.com/vladimiracunadev-create/langgraph-realworld), [operational-ai-agents](https://github.com/vladimiracunadev-create/operational-ai-agents) · Domain-first → [rhino-suite](https://github.com/vladimiracunadev-create/rhino-suite) · Micro-apps → [microsistemas](https://github.com/vladimiracunadev-create/microsistemas) · Embedded DB → [gabysql](https://github.com/vladimiracunadev-create/gabysql) · IaC → [proyectos-aws](https://github.com/vladimiracunadev-create/proyectos-aws) |
| پایگاه‌های داده | گردش‌کارها، Terraform و Docker/Compose | PostgreSQL · Redis · Elasticsearch → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · Supabase · Hasura → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) · 18+ → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler), [database-systems-labs](https://github.com/vladimiracunadev-create/database-systems-labs) · GabySQL → [gabysql](https://github.com/vladimiracunadev-create/gabysql) · Qdrant → [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets) |
| تحلیل داده و هوش تجاری (BI) | کد و مستندات مخزن | Power BI · DAX · Star schema → [social-bot-scheduler/analytics/powerbi](https://github.com/vladimiracunadev-create/social-bot-scheduler/tree/main/analytics/powerbi) (3 × .pbix) |
| ابر، کانتینر و DevOps | گردش‌کارها، Terraform و Docker/Compose | GitHub Actions → [proyectos-aws](https://github.com/vladimiracunadev-create/proyectos-aws) · GitLab CI → [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) · Terraform · Kubernetes · Azure · GCP → [multi-cloud-engineering-program](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) · Docker → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · WSL → [wsl-labs](https://github.com/vladimiracunadev-create/wsl-labs) |
| AWS: سرویس‌های استفاده‌شده (موارد روی GitLab CI) | موردها و پرس‌وجوهای واقعی | A–P → [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) · EC2 · RDS · VPC · Secrets Manager · CloudFormation · Cost Explorer → [aws-desktop-studio](https://github.com/vladimiracunadev-create/aws-desktop-studio) |
| مشاهده‌پذیری و پیام‌رسانی | گردش‌کارها، Terraform و Docker/Compose | Prometheus · Grafana · RabbitMQ → [docker-labs](https://github.com/vladimiracunadev-create/docker-labs) · Kafka · MQTT → [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) |
| هوش مصنوعی، عامل‌ها، مهارت‌ها و MCP | کد و مستندات مخزن | LangGraph → [langgraph-realworld](https://github.com/vladimiracunadev-create/langgraph-realworld) · Agents → [operational-ai-agents](https://github.com/vladimiracunadev-create/operational-ai-agents) · MCP · Ollama → [mcp-ollama-local](https://github.com/vladimiracunadev-create/mcp-ollama-local) · Skills → [claude-skills-toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit), [codex-skills-toolkit](https://github.com/vladimiracunadev-create/codex-skills-toolkit) · Plugins → [agentic-plugins-toolkit](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) · JSONL · RAG → [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets), [social-bot-scheduler](https://github.com/vladimiracunadev-create/social-bot-scheduler) |
| جریان توسعه AI-Assisted Development Flow | استقرارها و اظهار نویسنده | Claude Code · Codex → [claude-skills-toolkit](https://github.com/vladimiracunadev-create/claude-skills-toolkit), [codex-skills-toolkit](https://github.com/vladimiracunadev-create/codex-skills-toolkit) · VS Code → [rootcause-windows-inspector](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) · ChatGPT Plus · Antigravity · OpenCode |
| امنیت و زنجیرهٔ تأمین | گردش‌کارهای امنیتی | security.yml → [universal-api-orchestrator](https://github.com/vladimiracunadev-create/universal-api-orchestrator), [psychometrics-and-assessment-program](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program), [human-genome-labs](https://github.com/vladimiracunadev-create/human-genome-labs), [learning-path-datasets](https://github.com/vladimiracunadev-create/learning-path-datasets) · [modern-cybersecurity-program](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) |
| پلتفرم‌های هدف | خروجی‌های انتشار | Android · Windows · Web → [empresa-operativa-chile](https://github.com/vladimiracunadev-create/empresa-operativa-chile) · Windows · macOS · Linux · Android · PWA → [spherex-releases](https://github.com/vladimiracunadev-create/spherex-releases) |
| فناوری‌های انتشار | استقرارها و اظهار نویسنده | GitHub Pages → [vladimiracunadev-create.github.io](https://github.com/vladimiracunadev-create/vladimiracunadev-create.github.io) · Vercel → [spherex-releases](https://github.com/vladimiracunadev-create/spherex-releases) · Cloudflare · AWS |

## اظهار نویسنده (در مخزن‌های عمومی قابل راستی‌آزمایی نیست)

این موارد چون نویسنده از آن‌ها استفاده می‌کند در پشته هستند، اما هیچ مخزن عمومی به‌تنهایی آن‌ها را اثبات نمی‌کند:

- **Cloudflare** — کار شخصی.
- **ChatGPT Plus** (از ۲۰۲۳)، **Antigravity** و **OpenCode** — ابزارهای جریان توسعهٔ کمک‌گرفته از هوش مصنوعی.
- **AWS در وب‌سایت‌های عملیاتی مرتبط با GitLab** — آنچه به‌طور عمومی قابل راستی‌آزمایی است پروژهٔ [proyectos-aws-gitlab](https://gitlab.com/vladimir.acuna.dev-group/proyectos-aws-gitlab) است، نه آن وب‌سایت‌ها.

## چگونه بررسی کنیم

هر کسی می‌تواند بررسی را با GitHub CLI (`gh`) تکرار کند:

```bash
gh repo list vladimiracunadev-create --visibility public --source --limit 200
gh api repos/vladimiracunadev-create/<repo>/languages
gh search code "<tech>" --owner vladimiracunadev-create
```

## چگونه نگهداری می‌شود

- فناوری‌ها و نمودارشان از `scripts/stack_data.json` با `scripts/stack_graphic.py` تولید می‌شوند و عددهای پروفایل را گردش‌کار `stats.yml` محاسبه می‌کند.
- فناوری وقتی وارد پشته می‌شود که در یک مخزن عمومی (کد، manifest، گردش‌کار یا آزمایشگاه) ظاهر شود و وقتی خارج می‌شود که دیگر در هیچ‌کدام ظاهر نشود.

## محدودیت‌ها

- آمار زبان‌های GitHub فایل‌های تولیدشده و دادهٔ خام را هم می‌شمارد (به همین دلیل HTML سنگین است): نشان می‌دهد مخزن چه دارد، نه اینکه هر زبان را چقدر خوب می‌دانم.
- مخزن‌های خصوصی و کار برای مشتریان بخشی از این پشته نیستند و به‌عنوان شاهد به‌کار نمی‌روند.
