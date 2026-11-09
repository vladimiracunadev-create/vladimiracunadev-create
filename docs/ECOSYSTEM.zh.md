# 🗂️ 生态系统：产品、实验室、应用 AI、课程与科学计算

[← 返回档案](../README.zh.md)

**🌐** [Español](ECOSYSTEM.md) · [English](ECOSYSTEM.en.md) · [Português](ECOSYSTEM.pt.md) · [Italiano](ECOSYSTEM.it.md) · [Français](ECOSYSTEM.fr.md) · **简体中文** · [繁體中文](ECOSYSTEM.zh-TW.md) · [日本語](ECOSYSTEM.ja.md) · [한국어](ECOSYSTEM.ko.md) · [Türkçe](ECOSYSTEM.tr.md) · [Русский](ECOSYSTEM.ru.md) · [Tiếng Việt](ECOSYSTEM.vi.md) · [ไทย](ECOSYSTEM.th.md) · [Deutsch](ECOSYSTEM.de.md) · [Українська](ECOSYSTEM.uk.md) · [Polski](ECOSYSTEM.pl.md) · [العربية](ECOSYSTEM.ar.md) · [فارسی](ECOSYSTEM.fa.md) · [Bahasa Indonesia](ECOSYSTEM.id.md) · [Nederlands](ECOSYSTEM.nl.md) · [हिन्दी](ECOSYSTEM.hi.md) · [Ελληνικά](ECOSYSTEM.el.md)

本档案的实践成果集中在独立文档中：可下载安装的软件、工程实验室、应用 AI、完整技术课程与科学计算，以及账号中每个第三方项目 fork 的说明。

## 📦 真实分发的产品

这些软件可以下载、安装、使用 — 不只是 clone 代码。

| 产品 | 说明 | Stack | 交付 |
|---|---|---|---|
| [🔍 **RootCause Windows**](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) | 网络安全取证：任何异常资源失真都可能是威胁的最早信号。先诊断，再干预 | Rust 🦀 · ETW/WPR | **v0.19.0** · **16 releases** · **5 editions**: GUI · Portable · CLI · PowerShell · VS Code · [landing](https://vladimiracunadev-create.github.io/rootcause-windows-inspector/) |
| [📱 **RootCause Mobile**](https://github.com/vladimiracunadev-create/rootcause-mobile-inspector) | 移动端取证传感器：将每个 app 与自身基线比较，识别 stalkerware，并区分已授予权限和仅请求权限 | Flutter · Kotlin · Swift | **v0.8.0** · 可验证 Android APK · 5 languages · **zero telemetry** · [landing](https://vladimiracunadev-create.github.io/rootcause-mobile-inspector/) |
| [🍎 **RootCause macOS**](https://github.com/vladimiracunadev-create/rootcause-macos-inspector) | macOS 版本：`launchd` 持久化、Gatekeeper、SIP、FileVault、XProtect、TCC 权限、签名进程和网络邻居 — 每个面都与已知良好状态对比 | Rust 🦀 · macOS 13+ | **v0.1.0** · first published release · Apache-2.0 · [landing](https://vladimiracunadev-create.github.io/rootcause-macos-inspector/) |
| [🖥️ **RootCause Server**](https://github.com/vladimiracunadev-create/rootcause-server) | 服务器版本：把暴露面、访问尝试突增、同地址会话、关键文件完整性和传感器沉默关联成一句可执行结论 | Rust 🦀 · Windows · Linux · macOS | **v0.2.0** · **18 rules** with evidence and runbook · never executes actions on its own · local console · **no published release yet** · [landing](https://vladimiracunadev-create.github.io/rootcause-server/) |
| [🌐 **RootCause Web**](https://github.com/vladimiracunadev-create/rootcause-web-inspector) | 浏览器取证传感器：cookies、邮件会话、扩展、下载、权限，以及伪装真实窗口的网页 | JavaScript · MV3 extension | **v0.2.0** · no published release yet · panel on `127.0.0.1` · zero dependencies · zero telemetry verified in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-web-inspector/) |
| [₿ **RootCause Bitcoin Defense**](https://github.com/vladimiracunadev-create/rootcause-bitcoin-defense) | Bitcoin custody 的 watch-only 防御：盘点每把钥匙来源，与公开警告交叉检查，并用证据解释 root cause | JavaScript · Windows app · local panel | **v0.3.0** · **2 releases** · zero dependencies · never asks for seeds · verified in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-bitcoin-defense/) |
| [⛓️ **RootCause Blockchain Security**](https://github.com/vladimiracunadev-create/rootcause-blockchain-security) | 多链 watch-only 控制台：盘点 contracts、proxies、oracles、bridges、governance 和 dependencies，并生成 root-cause runbooks | JavaScript · Windows app · local panel | **v0.3.0** in repo · published release: `v0.1.0` · zero dependencies · never asks for private keys · verified in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-blockchain-security/) |
| [📷 **RootCause QR Inspector**](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) | 本地 Android app，用于行动前检查 QR：解释 26 个信号，区分事实和假设，导出脱敏证据 | Flutter · Dart | **v0.2.0** · **6 releases** · **163 tests** · Android APK published · verifiable SHA-256 · technical APK package signature; commercial/store signatures in progress · zero telemetry · [landing](https://vladimiracunadev-create.github.io/rootcause-qr-inspector/) |
| [🏢 **Empresa Operativa Chile**](https://github.com/vladimiracunadev-create/empresa-operativa-chile) | 陪伴 Chile SpA 从成立前到每月结账：带证据的设立、VAT carry-forward、F29 draft、immutable close 和 audit log。每条规则都有官方来源 | JavaScript · Rust · PWA | **v1.8.0** · Android · Windows · browser · **230 tests** · **0 production dependencies** · zero telemetry · [landing](https://vladimiracunadev-create.github.io/empresa-operativa-chile/) |
| [🔍 **Universal Code Scanner**](https://github.com/vladimiracunadev-create/universal-code-scanner) | QR 和条码读取器，**先解释再行动**：16 个本地 URL 风险信号和明确确认 | Flutter · Dart | **v1.1.0** · Android · iOS · macOS · PWA · encrypted history **AES-256-GCM** · [landing](https://vladimiracunadev-create.github.io/universal-code-scanner/) |
| [🗄️ **GabySQL**](https://github.com/vladimiracunadev-create/gabysql) | 嵌入式数据库：单个 `.db` 文件、WAL、cost-based optimizer、HTTP/JSON API | Rust 🦀 | Windows · macOS · Linux · [landing](https://vladimiracunadev-create.github.io/gabysql/) |
| [🤖 **Automa PC**](https://github.com/vladimiracunadev-create/automa-pc) | 本地编排器：JSON flows 打开真实窗口、与 DOM 交互并留下证据 | Python · Playwright · pywebview | **v0.3.0** · **27 flows** · published and verifiable installer · [landing](https://vladimiracunadev-create.github.io/automa-pc/) |
| [🏭 **AI Dataset Foundry**](https://github.com/vladimiracunadev-create/ai-dataset-foundry) | Local-first 数据集工厂：将 PDF、Word、web、Git、JSON、CSV 转成可审计数据集，用于 pretraining、fine-tuning、RAG 和 evaluation | Python | **v0.2.0** · Windows + offline Android · first published release · [landing](https://vladimiracunadev-create.github.io/ai-dataset-foundry/) |
| [☁️ **AWS Desktop Studio**](https://github.com/vladimiracunadev-create/aws-desktop-studio) | Local-first app，提供 15 个 AWS 资产集成、20 个教程、CLI/SSO 和默认只读；仍在开发中，并非通用访问 | JavaScript · Windows | **v0.1.1** · first published release · [landing](https://vladimiracunadev-create.github.io/aws-desktop-studio/) |
| [🧭 **Commerce OS**](https://github.com/vladimiracunadev-create/commerce-operating-system) | 商业运营概念演示：catalog、stock、CRM、orders、mock payments 和 traceability | JavaScript · Web · Windows · Android | **v0.3.0** · **3 releases** · no real money or real SII · [landing](https://vladimiracunadev-create.github.io/commerce-operating-system/) |
| [📄 **PDF Reader**](https://github.com/vladimiracunadev-create/pdf-reader-windows-android) | Android-first 本地只读阅读器：无裁剪缩放、可重开历史、分享到 WhatsApp、可设默认阅读器 | HTML · Web · Android · Windows | **v0.3.3** · signed APK · no accounts, sensitive permissions, or telemetry · [landing](https://vladimiracunadev-create.github.io/pdf-reader-windows-android/) |
| [🎙️ **Video Transcript Studio**](https://github.com/vladimiracunadev-create/video-transcript-studio) | 一个视频、播放列表或**整个 YouTube 频道**转带时间戳文本。不依赖原字幕：Whisper 在**你的电脑**识别音频，无 API、账户或密钥 | Python · PySide6 · FastAPI · faster-whisper | **v0.2.0** · Windows desktop + local panel `127.0.0.1` + CLI, **same queue** · MD · PDF · TXT · SRT · VTT · JSON · MP3 · OGG · **89 tests** · FFmpeg included · zero telemetry · [landing](https://vladimiracunadev-create.github.io/video-transcript-studio/) |
| [🎨 **ChofyAI Studio**](https://github.com/vladimiracunadev-create/chofyai-studio) | 本地创意 AI launcher：编排 Qwen3-TTS、whisper.cpp、FaceFusion、AceForge 和 ComfyUI | Tauri 2 · Rust · React | v0.5.1 · **5/5 tools with real inference** · macOS Apple Silicon · experimental Windows · **no published release yet** · [site](https://vladimiracunadev-create.github.io/chofyai-studio/) |
| [🦏 **Rhino Suite**](https://github.com/vladimiracunadev-create/rhino-suite) | 从零构建的办公套件：文档规则不依赖 DOM — HTML 只是投影 | Rust/WASM · Go · React 19 | Evolutionary monorepo by phases · [landing](https://vladimiracunadev-create.github.io/rhino-suite/) |
| [🎻 **My Violin Adventure**](https://github.com/vladimiracunadev-create/violin-adventure) | 儿童教育 app：chromatic tuner、基于音频时钟的精准 metronome、真实小提琴歌曲 | Tauri 2 · React · TS | **v1.3.0** · Windows · Android · Linux · macOS · PWA · [landing](https://vladimiracunadev-create.github.io/violin-adventure/) |
| [🎸 **My Guitar Adventure**](https://github.com/vladimiracunadev-create/guitarra-adventure) | 吉他兄弟项目：6 个世界 24 节课、6 弦调音器、无漂移 metronome、11 个真实吉他音符 | Tauri 2 · React · TS | **v1.0.0** · Windows · Android · Linux · macOS · iOS · PWA · no accounts, ads, or online dependency · [landing](https://vladimiracunadev-create.github.io/guitarra-adventure/) |
| [🧣 **Pañuelo al Viento**](https://github.com/vladimiracunadev-create/panuelo-al-viento-cueca-app) | 面向 10 岁以上的 cueca 学习：8 个级别 24 节课、72 个活动、六拍实验室（3+3 与 2+2+2）和可访问地面图。声明**补充而不是替代**教师和文化传承者 | Flutter · Dart | **v0.2.0** · Android 7+ · Windows 10/11 · APK · EXE · MSI · portable · **29 tests + 2 validators** · no camera, microphone, account, ads, or internet · [landing](https://vladimiracunadev-create.github.io/panuelo-al-viento-cueca-app/) |

## 🧪 工程实验室

| Repo | 展示内容 |
|---|---|
| [🐳 **Problem-Driven Systems Lab**](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) | **20 个真实问题**（load latency、N+1、retry storms、leaks、monolith、cache stampede、backpressure、zero-downtime migration、forgotten DLQ）以高保真故障注入，在 **7 个 stack** 中解决：PHP 8 · Python · Node.js · Java 21 · .NET 8 · **Go 1.23** · **Rust 1.83** · [landing](https://vladimiracunadev-create.github.io/problem-driven-systems-lab/) |
| [📆 **Social Bot Scheduler**](https://github.com/vladimiracunadev-create/social-bot-scheduler) | **v4.11.0** · **20 cases** source→n8n→receiver，覆盖 **18+ DB engines** —**19 operational**，逐一用 Docker 审计— **8-layer** audit、idempotency guardrails、circuit breaker、DLQ · [landing](https://vladimiracunadev-create.github.io/social-bot-scheduler/) |
| [🧰 **Microsistemas**](https://github.com/vladimiracunadev-create/microsistemas) | **13 个 PHP 诊断与现代化 microapps** · local read-only MCP server · 3-phase hardening · [landing](https://vladimiracunadev-create.github.io/microsistemas/) |
| [🧪 **Docker Labs**](https://github.com/vladimiracunadev-create/docker-labs) | **12 labs** on 4-service platform + automated `.exe` installer with launcher · [landing](https://vladimiracunadev-create.github.io/docker-labs/) |
| [🐳 **WSL Labs**](https://github.com/vladimiracunadev-create/wsl-labs) | **12 cases** on `wslc`, native WSL container engine — **without Docker Desktop** · [landing](https://vladimiracunadev-create.github.io/wsl-labs/) |
| [⚡ **Unikernel Labs**](https://github.com/vladimiracunadev-create/unikernel-labs) | “Docker Desktop for unikernels”：Windows control over Unikraft with WSL2 backend, `kraft` + QEMU/KVM · [landing](https://vladimiracunadev-create.github.io/unikernel-labs/) |
| [🧰 **QEMU/KVM Labs**](https://github.com/vladimiracunadev-create/qemu-kvm-labs) | **12 labs** real virtualization with QEMU, KVM, libvirt, cloud-init and `vm-manager` on Linux and WSL2 · [landing](https://vladimiracunadev-create.github.io/qemu-kvm-labs/) |
| [🛡️ **Sandbox Labs**](https://github.com/vladimiracunadev-create/sandbox-labs) | Linux isolation：在声明策略下运行第三方代码、文件和 business models，并**输出签名证据说明实际应用的控制** · **36 cases** in two families —15 technical and 21 capital-markets— · experimental and educational, *not a security product* · [landing](https://vladimiracunadev-create.github.io/sandbox-labs/) |
| [💳 **Universal Payments Engineering Lab**](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) | **28 payment families** in local self-explaining demo：states、ledger、reconciliation、security、implementation guides · [landing](https://vladimiracunadev-create.github.io/universal-payments-engineering-lab/) |
| [🕹️ **Decentraland Social Arcade**](https://github.com/vladimiracunadev-create/decentraland-social-arcade) | Native Decentraland social 3D experience：MVP + multi-game architecture with SDK7, ECS and TypeScript · Spanish docs · no payments or telemetry |
| [☁️ **AWS Projects**](https://github.com/vladimiracunadev-create/proyectos-aws) | Progressive cases，每个 case 增加一个 AWS service **以及**一个新的 GitHub Actions capability · SAA-C03 · DVA-C02 · SOA-C02 coverage |

## 🤖 应用 AI

| Repo | 展示内容 |
|---|---|
| [🤖 **LangGraph RealWorld**](https://github.com/vladimiracunadev-create/langgraph-realworld) | **25/25 operational backends** — typed state、conditional routes、NDJSON streaming、DEMO/LIVE mode、8 security layers、SHA-256 chain of custody |
| [🧭 **Operational AI Agents**](https://github.com/vladimiracunadev-create/operational-ai-agents) | **23 operational agents** for Claude Code and compatible runtimes：repo evolution、legacy modernization、curriculum design、portfolio publishing、security remediation、incident analysis · **69 deterministic evals** · 82 tests · zero-deps · Linux · macOS · Windows · [site](https://vladimiracunadev-create.github.io/operational-ai-agents/) |
| [🧠 **MCP + Ollama Local**](https://github.com/vladimiracunadev-create/mcp-ollama-local) | Local-first AI with MCP tools in sandbox · bind `127.0.0.1` · multilayer trust profile · honest about limits |
| [🧩 **Agentic Plugins Toolkit**](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) | **6 agentic plugins** installable in Claude Code, OpenAI/Codex, Copilot, Gemini and MCP from one source · **69 generated views without drift** · zero-deps · Linux · macOS · Windows · [site](https://vladimiracunadev-create.github.io/agentic-plugins-toolkit/) |
| [🧰 **Claude Skills Toolkit**](https://github.com/vladimiracunadev-create/claude-skills-toolkit) | **22 agentic skills** for Claude Code · security audits、Bitcoin custody、repo gates、coherence、Docker、docs · zero-deps · cross-platform |
| [🧰 **Codex Skills Toolkit**](https://github.com/vladimiracunadev-create/codex-skills-toolkit) | **19 agentic skills** for Codex：security and supply chain、preflight、functional flows、resilience and state、release evidence、Python/YAML/Markdown gates、versioning、dependencies、Docker、documents · Python-first · `pnpm` · Linux · macOS · Windows · [site](https://vladimiracunadev-create.github.io/codex-skills-toolkit/) |

<a id="curricula"></a>

## 📚 完整技术课程

这些是西班牙语顺序课程，每个仓库都明确声明状态和范围。21 个项目共 **14,550 classes**，由 [workflow](../.github/workflows/stats.yml) 从真实仓库结构或仓库内声明的可验证来源统计；徽章每周刷新，不是手写数字。

🧭 [**Lifelong Learning Ecosystem**](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem) 是一个联邦式学习导航器，通过可视化地图和[可访问的离线门户](https://vladimiracunadev-create.github.io/lifelong-learning-ecosystem/)连接 6 个领域的 30 条真实路径；它不计为额外课程项目。

| 项目 | 课程数 | 范围 |
|---|---:|---|
| [🔢 **Computational Mathematics**](https://github.com/vladimiracunadev-create/computational-mathematics-program) | 360 | From counting on fingers to reproducing a paper · **360 deterministic demonstrations verified in CI** · 1,080 notebooks · 489-term glossary · [site](https://vladimiracunadev-create.github.io/computational-mathematics-program/) |
| [🏦 **Finance and Banking**](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program) | 356 | 534 h · financial mathematics and IFRS → credit, risk, Basel III, open finance, DLT, stablecoins, MiCA · **27 个案例** · **298 项测试** · [site](https://vladimiracunadev-create.github.io/finance-and-banking-evolution-program/) |
| [🎮 **GameDev**](https://github.com/vladimiracunadev-create/modern-gamedev-program) | 352 | Math and C#/C++/GDScript → shaders、AI、multiplayer、VR/AR · Godot · Unity · Unreal · **10 Godot labs verified in CI** · [site](https://vladimiracunadev-create.github.io/modern-gamedev-program/) |
| [🛡️ **Cybersecurity**](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) | 370 | **v1.3.0** · 21 parts · foundations → Red Team、DFIR、cloud security、exploit dev、CTF、game security · mapped to **7 certifications** · offline Android/web app · [site](https://vladimiracunadev-create.github.io/modern-cybersecurity-program/) |
| [📈 **Marketing, Sales and Growth**](https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program) | 336 | 24 parts with operational definitions、measurement sheets、verifiable bibliography and Chilean regulatory context · **v1.6.0** · 1.29M words · 17 role paths · [site](https://vladimiracunadev-create.github.io/marketing-sales-growth-evolution-program/) |
| [🏢 **Business Creation**](https://github.com/vladimiracunadev-create/modern-business-creation-program) | 336 | Create and operate a real company in Chile：idea、incorporation、SII、operations、crisis、exit · 360 diagrams · 1,251-term glossary · 1,548-page manual · [site](https://vladimiracunadev-create.github.io/modern-business-creation-program/) |
| [🏛️ **Architecture and Built Environment**](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program) | 840 | 84 parts · 60 场综合课程 · 35 paths · 可追溯来源 · Markdown、offline reader、GitHub Pages · [site](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/) |
| [🇨🇱 **智利学校课程路径**](https://github.com/vladimiracunadev-create/chilean-school-learning-path) | 8,841 | 覆盖小学一年级至高中四年级 · **4,156 项跨学科整合活动** · **2,823 个学习目标** · MINEDUC 来源 · 无待处理提案，仍需专业人工复核 · [site](https://vladimiracunadev-create.github.io/chilean-school-learning-path/) |
| [🧭 **现代软件工程**](https://github.com/vladimiracunadev-create/modern-software-engineering-program) | 480 | 40 部分、8 个阶段 · 基础 → 产品、架构、安全、DevOps、SRE、SPEC、AI 与多智能体系统 · 编辑状态由仓库明确声明 · [site](https://vladimiracunadev-create.github.io/modern-software-engineering-program/) |
| [🎓 **Pedagogy and Learning Sciences**](https://github.com/vladimiracunadev-create/education-pedagogy-learning-sciences-program) | 300 | From how a person learns to how teachers are trained · 25 parts · **each class declares evidence state and limits** · literacy、methods、special needs、coexistence、cultural diversity · **v2.1.0** · [site](https://vladimiracunadev-create.github.io/education-pedagogy-learning-sciences-program/) |
| [☁️ **Multi-Cloud**](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) | 288 | AWS · Azure · GCP · Kubernetes · Terraform · SRE · FinOps · **1,288 hours** · 288 labs with JSON evidence · 1,032 sources · 2,884-page PDF manual · [site](https://vladimiracunadev-create.github.io/multi-cloud-engineering-program/) |
| [🎖️ **Executive Leadership**](https://github.com/vladimiracunadev-create/executive-leadership-founder-program) | 288 | From owning first outcome to leading a company and founding one：teams、KPI/OKR、finance、product、risk、board、M&A · [site](https://vladimiracunadev-create.github.io/executive-leadership-founder-program/) |
| [🐍 **Python Data Science**](https://github.com/vladimiracunadev-create/python-data-science-program) | 232 | Polars、ML+Optuna/SHAP、PyTorch/LLMs/LoRA、MLOps · native Windows app + Android APK · [site](https://vladimiracunadev-create.github.io/python-data-science-program/) |
| [🧠 **AI Evolution**](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program) | 184 | Symbolic → probabilistic → deep learning → LLMs、RAG、agents、safety、frontier · **v0.17.0** · **708 notebooks** · 148 foundational papers · offline Windows、Android、PWA apps · [site](https://vladimiracunadev-create.github.io/artificial-intelligence-evolution-program/) |
| [🌐 **Comparative Programming**](https://github.com/vladimiracunadev-create/polyglot-programming-labs) | 176 | One concept, **10 languages** verified in CI — **1,360 implementations** — plus **1,632 programs** in living legacy languages and atlas of **60 cards in 15 families** · [site](https://vladimiracunadev-create.github.io/polyglot-programming-labs/) |
| [🧩 **Frameworks Compared**](https://github.com/vladimiracunadev-create/framework-ecosystems-labs) | 149 | One executable contract against Express、FastAPI、Spring Boot、ASP.NET、Django、Rails、Laravel、React、Vue、Svelte and more · **70 节已构建课程** · **397 个 CI 验证案例** · **210 个 ISBN/DOI 来源** · [site](https://vladimiracunadev-create.github.io/framework-ecosystems-labs/) |
| [🗄️ **Databases**](https://github.com/vladimiracunadev-create/database-systems-labs) | 74 | **v3.0.0** · database engineering in 15 parts · 230 hours · 120 sources with ISBN/DOI/standard · same case solved in 27 engines · 150 pytest · [site](https://vladimiracunadev-create.github.io/database-systems-labs/) |
| [📐 **Psychometrics and Assessment**](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program) | 40 | How measurement instruments are built, scored, validated and audited · 8 parts · executable engine with **5 instruments and 344 items, 276 public-domain** · ✍️ **5/40** 已撰写 |
| [⛓️ **Blockchain**](https://github.com/vladimiracunadev-create/blockchain-learning-path) | 66 | **v0.15.0** · from zero to programmable financial infrastructure and on-chain analytics · **91 practices** and **508 tests** · Foundry and Slither in CI · [site](https://vladimiracunadev-create.github.io/blockchain-learning-path/) |
| [🧠 **Neural Network Training Labs**](https://github.com/vladimiracunadev-create/neural-network-training-labs) | 31 | 7 modules · ≈214 hours · **93 notebooks** —31 classes, 31 student versions, 31 solutions— · PyTorch · [study site](https://vladimiracunadev-create.github.io/neural-network-training-labs/) |
| [🕹️ **Machine Operator**](https://github.com/vladimiracunadev-create/machine-operator-program) | 451 | **41 training modules**, one per machine · **502 h 15 min** · systems、controls、physics、safety、simulation design with sources per class · *no executable simulator yet, and that is declared* |
| [🌌 **天文学、天体物理学、空间科学与航空航天工程**](https://github.com/vladimiracunadev-create/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program) | — | **规划中，不计入统计：**12 个领域、133 个模块共 2,077 节规划课程；其中 397 节已有正文，全部仍处于 E0 状态。独立培训，并非职业资格认证 · [网站](https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/)。 |

## 🔬 科学计算

| Repo | 展示内容 |
|---|---|
| [🧬 **Human Genome Labs**](https://github.com/vladimiracunadev-create/human-genome-labs) | 可复现基因组平台：typed `ScientificResult<T>` contracts、FASTA/GFF3/VCF、modules with **explicit maturity and evidence**。极端诚实：*不进行临床诊断* · [site](https://vladimiracunadev-create.github.io/human-genome-labs/) |

<a id="forks"></a>

## 🍴 第三方项目的 fork (52)

这些是保存在本账号中的他人项目的 fork。**它们不是我的原创作品**：功劳属于原作者，不计入本档案的任何数字，每条说明仅概括原项目自身的声明，并不意味着我提供支持、审计或拥有生产环境经验。说明依据原项目 · 2026-11-09。

### 🤖 编码代理与代理框架 (18)

| Fork | 原项目 | 语言 | 简介 |
|---|---|---|---|
| [**OpenHands**](https://github.com/vladimiracunadev-create/OpenHands) | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | TypeScript | AI 驱动的软件开发代理平台 |
| [**cline**](https://github.com/vladimiracunadev-create/cline) | [cline/cline](https://github.com/cline/cline) | TypeScript | 以 SDK、IDE 扩展或 CLI 形式提供的自主编码代理 |
| [**opencode**](https://github.com/vladimiracunadev-create/opencode) | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 开源编码代理 |
| [**qwen-code**](https://github.com/vladimiracunadev-create/qwen-code) | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | TypeScript | 面向终端的开源 AI 编码代理 |
| [**goose**](https://github.com/vladimiracunadev-create/goose) | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Rust | 可扩展代理，可用任意 LLM 安装、运行、编辑并测试代码 |
| [**pi**](https://github.com/vladimiracunadev-create/pi) | [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | 代理工具包：统一 LLM API、代理循环、TUI 与编码 CLI |
| [**hermes-agent**](https://github.com/vladimiracunadev-create/hermes-agent) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 与你共同成长的代理（NousResearch） |
| [**deepagents**](https://github.com/vladimiracunadev-create/deepagents) | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Python | “开箱即用”的代理框架（LangChain） |
| [**crewAI**](https://github.com/vladimiracunadev-create/crewAI) | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | 编排扮演角色的自主代理的框架 |
| [**agent-framework**](https://github.com/vladimiracunadev-create/agent-framework) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Python | 微软用于构建并部署代理与多代理工作流的框架，支持 Python 和 .NET |
| [**deepseek-harness**](https://github.com/vladimiracunadev-create/deepseek-harness) | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | TypeScript | DeepSeek 代理框架，一切皆插件 |
| [**agent-orchestrator**](https://github.com/vladimiracunadev-create/agent-orchestrator) | [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Go | 规划、运行并监督代理集群，从任务到合并 PR |
| [**orca**](https://github.com/vladimiracunadev-create/orca) | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 管理编码代理集群的工作区（桌面、移动与远程） |
| [**kander**](https://github.com/vladimiracunadev-create/kander) | [dualface/kander](https://github.com/dualface/kander) | Go | 看板，用隔离的 git worktree 和评审代理协调编码代理 |
| [**OpenBot**](https://github.com/vladimiracunadev-create/OpenBot) | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | TypeScript | AI 同事，各自拥有独立电脑；每个动作事前决定、事后记录 |
| [**browser-use**](https://github.com/vladimiracunadev-create/browser-use) | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | 让 AI 代理操作浏览器的 Python 库 |
| [**agent-desktop**](https://github.com/vladimiracunadev-create/agent-desktop) | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Rust | 面向 AI 代理的 computer use CLI |
| [**treg**](https://github.com/vladimiracunadev-create/treg) | [superdesigndev/treg](https://github.com/superdesigndev/treg) | Python | “面向代理工具的 OpenRouter” |

### 🧩 面向代理的技能、插件与工作流 (11)

| Fork | 原项目 | 语言 | 简介 |
|---|---|---|---|
| [**claude-plugins-official**](https://github.com/vladimiracunadev-create/claude-plugins-official) | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 由 Anthropic 管理的 Claude Code 优质插件官方目录 |
| [**agentic-awesome-skills**](https://github.com/vladimiracunadev-create/agentic-awesome-skills) | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | Python | 本地控制平面，用于发现、选择并验证大型 agentic 技能目录（CLI、本地 MCP、插件） |
| [**claude-review-all**](https://github.com/vladimiracunadev-create/claude-review-all) | [ncoevoet/claude-review-all](https://github.com/ncoevoet/claude-review-all) | Python | 面向 Claude Code 的多代理代码评审 |
| [**blender-skills**](https://github.com/vladimiracunadev-create/blender-skills) | [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | TypeScript | 面向编码代理的 Blender 专业技能，基于 MCP 的流水线 |
| [**diagram-design**](https://github.com/vladimiracunadev-create/diagram-design) | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 面向编码代理的编辑级图表设计（HTML + SVG） |
| [**elephant-goldfish-model**](https://github.com/vladimiracunadev-create/elephant-goldfish-model) | [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) | Python | Google 开放技能，用于借助 AI 代理设计与评审软件 |
| [**Claude-Code-Game-Studios**](https://github.com/vladimiracunadev-create/Claude-Code-Game-Studios) | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | 把 Claude Code 变成由协同代理组成的游戏工作室 |
| [**headcount**](https://github.com/vladimiracunadev-create/headcount) | [cbrock84/headcount](https://github.com/cbrock84/headcount) | Markdown | 像公司一样组织的代理体系：部门与可安装技能 |
| [**agentic-qe**](https://github.com/vladimiracunadev-create/agentic-qe) | [proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) | TypeScript | 开放的 QA/QE 平台，代理与技能覆盖软件全生命周期 |
| [**OpenExecutive**](https://github.com/vladimiracunadev-create/OpenExecutive) | [SenteLabsAI/OpenExecutive](https://github.com/SenteLabsAI/OpenExecutive) | Python | 虚拟管理团队：由 8 个专业 Claude 代理支撑的一位管理者形象 |
| [**n8n-mcp**](https://github.com/vladimiracunadev-create/n8n-mcp) | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | TypeScript | 让 Claude、Cursor 或 Windsurf 构建 n8n 工作流的 MCP 服务器 |

### 🛡️ 安全与软件分析 (8)

| Fork | 原项目 | 语言 | 简介 |
|---|---|---|---|
| [**raptor**](https://github.com/vladimiracunadev-create/raptor) | [gadievron/raptor](https://github.com/gadievron/raptor) | Python | 把 Claude Code 变成攻防兼备的安全代理 |
| [**Cybersecurity-Projects**](https://github.com/vladimiracunadev-create/Cybersecurity-Projects) | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | Go | 70 个由浅入深的网络安全项目 |
| [**SkillSpector**](https://github.com/vladimiracunadev-create/SkillSpector) | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Python | NVIDIA 的代理技能安全扫描器（提示注入、数据外泄、供应链） |
| [**Anthropic-Cybersecurity-Skills**](https://github.com/vladimiracunadev-create/Anthropic-Cybersecurity-Skills) | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | 数百个面向代理的网络安全技能，映射到 MITRE ATT&CK、NIST CSF 等框架 |
| [**security-audit-skill**](https://github.com/vladimiracunadev-create/security-audit-skill) | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | Cloudflare 的多阶段安全审计技能，结论经独立验证 |
| [**siteone-crawler**](https://github.com/vladimiracunadev-create/siteone-crawler) | [janreges/siteone-crawler](https://github.com/janreges/siteone-crawler) | Rust | 面向 SEO、安全、无障碍与性能的网站爬取与分析工具 |
| [**rea**](https://github.com/vladimiracunadev-create/rea) | [morluto/rea](https://github.com/morluto/rea) | TypeScript | 借助代理做逆向工程，从应用行为到原生二进制 |
| [**craft-anything**](https://github.com/vladimiracunadev-create/craft-anything) | [storytold/craft-anything](https://github.com/storytold/craft-anything) | Rust | 弄懂任何软件如何运作，并打造自己的软件 |

### 🧠 AI 模型与基础设施 (5)

| Fork | 原项目 | 语言 | 简介 |
|---|---|---|---|
| [**marin**](https://github.com/vladimiracunadev-create/marin) | [marin-community/marin](https://github.com/marin-community/marin) | Python | 面向基础模型研究与开发的开放框架 |
| [**prime-rl**](https://github.com/vladimiracunadev-create/prime-rl) | [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) | Python | 大规模代理式强化学习训练 |
| [**Olmo-core**](https://github.com/vladimiracunadev-create/Olmo-core) | [allenai/Olmo-core](https://github.com/allenai/Olmo-core) | Python | OLMo 生态系统的 PyTorch 基础模块 |
| [**DeepInfer**](https://github.com/vladimiracunadev-create/DeepInfer) | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | Python | 面向 DeepSeek 模型的高性能大规模推理框架 |
| [**heretic**](https://github.com/vladimiracunadev-create/heretic) | [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | 无需重新训练即可修改语言模型（审查、谄媚等） |

### 🏢 企业管理与平台 (6)

| Fork | 原项目 | 语言 | 简介 |
|---|---|---|---|
| [**erpnext**](https://github.com/vladimiracunadev-create/erpnext) | [frappe/erpnext](https://github.com/frappe/erpnext) | Python | 自由开源的 ERP |
| [**odoo**](https://github.com/vladimiracunadev-create/odoo) | [odoo/odoo](https://github.com/odoo/odoo) | Python | 开源企业应用 |
| [**mautic**](https://github.com/vladimiracunadev-create/mautic) | [mautic/mautic](https://github.com/mautic/mautic) | PHP | 开源营销自动化 |
| [**crm**](https://github.com/vladimiracunadev-create/crm) | [trycompai/crm](https://github.com/trycompai/crm) | TypeScript | 为 AI 代理设计的开源 CRM（Comp AI） |
| [**harness**](https://github.com/vladimiracunadev-create/harness) | [harness/harness](https://github.com/harness/harness) | Go | 端到端开发平台：代码管理、CI/CD、环境与制品库 |
| [**traccar**](https://github.com/vladimiracunadev-create/traccar) | [traccar/traccar](https://github.com/traccar/traccar) | Java | 开源 GPS 追踪平台，支持 200 多种设备协议 |

### 🎓 教育与参考 (4)

| Fork | 原项目 | 语言 | 简介 |
|---|---|---|---|
| [**computer-science**](https://github.com/vladimiracunadev-create/computer-science) | [ossu/computer-science](https://github.com/ossu/computer-science) | HTML | 免费计算机科学自学路径（OSSU） |
| [**math**](https://github.com/vladimiracunadev-create/math) | [ossu/math](https://github.com/ossu/math) | — | 免费数学自学路径（OSSU） |
| [**manim**](https://github.com/vladimiracunadev-create/manim) | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Python | 社区维护的数学动画 Python 框架 |
| [**asm-atari-2600**](https://github.com/vladimiracunadev-create/asm-atari-2600) | [johnidm/asm-atari-2600](https://github.com/johnidm/asm-atari-2600) | Assembly | Atari 2600 游戏汇编示例源码 |
