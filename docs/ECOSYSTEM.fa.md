# 🗂️ اکوسیستم: محصولات، آزمایشگاه‌ها، هوش مصنوعی کاربردی، برنامه‌های آموزشی و محاسبات علمی

[← بازگشت به پروفایل](../README.fa.md)

**🌐** [Español](ECOSYSTEM.md) · [English](ECOSYSTEM.en.md) · [Português](ECOSYSTEM.pt.md) · [Italiano](ECOSYSTEM.it.md) · [Français](ECOSYSTEM.fr.md) · [简体中文](ECOSYSTEM.zh.md) · [繁體中文](ECOSYSTEM.zh-TW.md) · [日本語](ECOSYSTEM.ja.md) · [한국어](ECOSYSTEM.ko.md) · [Türkçe](ECOSYSTEM.tr.md) · [Русский](ECOSYSTEM.ru.md) · [Tiếng Việt](ECOSYSTEM.vi.md) · [ไทย](ECOSYSTEM.th.md) · [Deutsch](ECOSYSTEM.de.md) · [Українська](ECOSYSTEM.uk.md) · [Polski](ECOSYSTEM.pl.md) · [العربية](ECOSYSTEM.ar.md) · **فارسی** · [Bahasa Indonesia](ECOSYSTEM.id.md) · [Nederlands](ECOSYSTEM.nl.md) · [हिन्दी](ECOSYSTEM.hi.md) · [Ελληνικά](ECOSYSTEM.el.md)

کارهای عملی این پروفایل در سندی جداگانه آمده است: نرم‌افزارهایی که دانلود و نصب می‌شوند، آزمایشگاه‌های مهندسی، هوش مصنوعی کاربردی، برنامه‌های آموزشی فنی کامل و محاسبات علمی، به‌همراه توضیح هر fork از پروژه‌های اشخاص ثالث که در حساب وجود دارد.

## 📦محصولات با توزیع واقعی

نرم افزاری که دانلود، نصب و استفاده می شود - نه تنها کلون شده است.

| Product | What it is | Stack | Delivery |
|---|---|---|---|
| [🔍 **RootCause Windows**](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) | Cybersecurity forensics: every anomalous resource distortion may be the first sign of a threat. Diagnose first, intervene later | Rust 🦀 · ETW/WPR | **v0.19.0** · **16 releases** · **5 editions**: GUI · Portable · CLI · PowerShell · VS Code · [landing](https://vladimiracunadev-create.github.io/rootcause-windows-inspector/) |
| [📱 **RootCause Mobile**](https://github.com/vladimiracunadev-create/rootcause-mobile-inspector) | The mobile sibling: a forensic sensor that compares each app against itself, flags stalkerware, and separates granted permissions from merely requested ones | Flutter · Kotlin · Swift | **v0.8.0** · verifiable Android APK · 5 languages · **zero telemetry** · [landing](https://vladimiracunadev-create.github.io/rootcause-mobile-inspector/) |
| [🍎 **RootCause macOS**](https://github.com/vladimiracunadev-create/rootcause-macos-inspector) | نسخه macOS`launchd`پایداری، دروازه بان، SIP، FileVault، X protection، TCC مجوزهای، فرایندهای امضا شده و همسایگان شبکه - هر سطح در برابر یک حالت شناخته شده بررسی می شود | Rust🦀 ·macOS 13+ | **v0.1.0** ·اولین انتشار منتشر شده·Apache-2.0· [landing](https://vladimiracunadev-create.github.io/rootcause-macos-inspector/) |
| [🖥️ **RootCause Server**](https://github.com/vladimiracunadev-create/rootcause-server) | The server sibling: correlates what no single log sees together — exposed surface, access-attempt bursts, a session granted to that same address, critical file integrity, and sensor silence — and turns it into one actionable sentence | Rust 🦀 · Windows · Linux · macOS | **v0.2.0** · **18 rules** with evidence and runbook · never executes actions on its own · local console without web dependencies · **no published release yet** · [landing](https://vladimiracunadev-create.github.io/rootcause-server/) |
| [🌐 **RootCause Web**](https://github.com/vladimiracunadev-create/rootcause-web-inspector) | Browser forensic sensor: cookies, email sessions, extensions, downloads, permissions, and pages that imitate a real window | JavaScript · MV3 extension | **v0.2.0** · no published release yet · panel on `127.0.0.1` · zero dependencies · zero telemetry verified in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-web-inspector/) |
| [₿ **RootCause Bitcoin Defense**](https://github.com/vladimiracunadev-create/rootcause-bitcoin-defense) | Watch-only defense for Bitcoin custody: inventories the origin of each key, cross-checks it with published warnings, and explains root cause with evidence | JavaScript · Windows app · local panel | **v0.3.0** · **2 releases** · zero dependencies · never asks for seeds · verified in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-bitcoin-defense/) |
| [⛓️ **RootCause Blockchain Security**](https://github.com/vladimiracunadev-create/rootcause-blockchain-security) | Multi-chain watch-only console: inventories contracts, proxies, oracles, bridges, governance, and dependencies, and generates root-cause runbooks | JavaScript · Windows app · local panel | **v0.3.0** in the repository · published release: `v0.1.0` · zero dependencies · never asks for private keys · verified in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-blockchain-security/) |
| [📷 **RootCause QR Inspector**](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) | برنامه محلی آندروید برای بررسی کدهای QR قبل از عمل: توضیح می دهد 26 سیگنال، جدا کردن حقایق از فرضیه ها و صادرات شواهد قرمز | Flutter·دارت | **v0.2.0** · **6 انتشار** · **163 تست** ·Android APK منتشر شده·قابل اعتماد بودن SHA-256·امضای بسته فنی: امضاهای تجاری / فروشگاه در پیشرفت·عدم تقارن صفر· [landing](https://vladimiracunadev-create.github.io/rootcause-qr-inspector/) |
| [🏢 **Empresa Operativa Chile**](https://github.com/vladimiracunadev-create/empresa-operativa-chile) | Guides a SpA from before incorporation to each monthly close: incorporation with evidence, VAT carry-forward, F29 draft, immutable close, and audit log. Every rule points to its official source | JavaScript · Rust · PWA | **v1.8.0** · Android · Windows · browser · **230 tests** · **0 production dependencies** · zero telemetry · [landing](https://vladimiracunadev-create.github.io/empresa-operativa-chile/) |
| [🔍 **Universal Code Scanner**](https://github.com/vladimiracunadev-create/universal-code-scanner) | QR and barcode reader that **interprets before acting**: 16 local URL risk signals and explicit confirmation | Flutter · Dart | **v1.1.0** · Android · iOS · macOS · PWA · encrypted history **AES-256-GCM** · [landing](https://vladimiracunadev-create.github.io/universal-code-scanner/) |
| [🗄️ **GabySQL**](https://github.com/vladimiracunadev-create/gabysql) | Embedded database: single `.db` file, WAL, cost-based optimizer, HTTP/JSON API | Rust 🦀 | Windows · macOS · Linux · [landing](https://vladimiracunadev-create.github.io/gabysql/) |
| [🤖 **Automa PC**](https://github.com/vladimiracunadev-create/automa-pc) | Local orchestrator: JSON flows that open real windows, interact with the DOM, and leave evidence | Python · Playwright · pywebview | **v0.3.0** · **27 flows** · published and verifiable installer · [landing](https://vladimiracunadev-create.github.io/automa-pc/) |
| [🏭 **AI Dataset Foundry**](https://github.com/vladimiracunadev-create/ai-dataset-foundry) | Local-first factory that turns PDF, Word, web, Git, JSON, and CSV into auditable datasets for pretraining, fine-tuning, RAG, and evaluation | Python | **v0.2.0** · Windows + offline Android · first published release · [landing](https://vladimiracunadev-create.github.io/ai-dataset-foundry/) |
| [☁️ **AWS Desktop Studio**](https://github.com/vladimiracunadev-create/aws-desktop-studio) | Local-first app with 15 AWS inventory integrations, 20 tutorials, CLI/SSO, and read-only defaults; implementation in progress, not universal access | JavaScript · Windows | **v0.1.1** · first published release · [landing](https://vladimiracunadev-create.github.io/aws-desktop-studio/) |
| [🧭 **Commerce OS**](https://github.com/vladimiracunadev-create/commerce-operating-system) | Guided conceptual demo of commercial operations: catalog, stock, CRM, orders, mock payments, and traceability | JavaScript · Web · Windows · Android | **v0.3.0** · **3 releases** · no real money or Chilean tax authority integration · [landing](https://vladimiracunadev-create.github.io/commerce-operating-system/) |
| [📄 **PDF Reader**](https://github.com/vladimiracunadev-create/pdf-reader-windows-android) | Android-first local read-only reader, with no-crop zoom, reopenable history, WhatsApp sharing, and default-reader selection | HTML · Web · Android · Windows | **v0.3.3** · signed APK · no accounts, sensitive permissions, or telemetry · [landing](https://vladimiracunadev-create.github.io/pdf-reader-windows-android/) |
| [🎙️ **Video Transcript Studio**](https://github.com/vladimiracunadev-create/video-transcript-studio) | One video, playlist, or **entire YouTube channel** to text with timestamps. It does not rely on existing subtitles: Whisper recognizes audio **on your machine**, with no API, account, or key to configure | Python · PySide6 · FastAPI · faster-whisper | **v0.2.0** · Windows desktop + local panel on `127.0.0.1` + CLI, **sharing the same queue** · MD · PDF · TXT · SRT · VTT · JSON · MP3 · OGG · **89 tests** · bundled FFmpeg · zero telemetry · [landing](https://vladimiracunadev-create.github.io/video-transcript-studio/) |
| [🎨 **ChofyAI Studio**](https://github.com/vladimiracunadev-create/chofyai-studio) | Local creative AI launcher: orchestrates Qwen3-TTS, whisper.cpp, FaceFusion, AceForge, and ComfyUI | Tauri 2 · Rust · React | v0.5.1 · **5/5 tools with real inference** · macOS Apple Silicon · experimental Windows · **no published release yet** · [site](https://vladimiracunadev-create.github.io/chofyai-studio/) |
| [🦏 **Rhino Suite**](https://github.com/vladimiracunadev-create/rhino-suite) | Office suite from scratch: document rules do not depend on the DOM — HTML is only a projection | Rust/WASM · Go · React 19 | Evolutionary monorepo by phases · [landing](https://vladimiracunadev-create.github.io/rhino-suite/) |
| [🎻 **My Violin Adventure**](https://github.com/vladimiracunadev-create/violin-adventure) | Educational app for children: chromatic tuner, audio-clock-accurate metronome, songs with real violin | Tauri 2 · React · TS | **v1.3.0** · Windows · Android · Linux · macOS · PWA · [landing](https://vladimiracunadev-create.github.io/violin-adventure/) |
| [🎸 **My Guitar Adventure**](https://github.com/vladimiracunadev-create/guitarra-adventure) | The plucked-string sibling: 24 lessons in 6 worlds, 6-string tuner, drift-free metronome, and 11 real guitar notes | Tauri 2 · React · TS | **v1.0.0** · Windows · Android · Linux · macOS · iOS · PWA · no accounts, ads, or online dependency · [landing](https://vladimiracunadev-create.github.io/guitarra-adventure/) |
| [🧣 **Pañuelo al Viento**](https://github.com/vladimiracunadev-create/panuelo-al-viento-cueca-app) | Cueca از سن 10: 24 کلاس در 8 سطح، 72 فعالیت، آزمایشگاه شش پالس (3+3 و 2+2)، و نمودار کف قابل دسترس است. می گوید که**مکمل ها، نه جایگزین**معلمان و صاحبان فرهنگ | Flutter·دارت | **v0.2.0** ·Android 7+·ویندوز 10/11·دانلود بازی APK·EXE·MSI·قابل حمل· **29 تست + 2 اعتبار سنجی** ·هیچ دوربین، میکروفون، حساب، تبلیغات یا اینترنت· [landing](https://vladimiracunadev-create.github.io/panuelo-al-viento-cueca-app/) |

## 🧪آزمایشگاه های مهندسی

| Repo | آنچه که نشان می دهد |
|---|---|
| [🐳 **Problem-Driven Systems Lab**](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) | **20 real problems** (latency under load, N+1, retry storms, leaks, monoliths, cache stampede, backpressure, zero-downtime migration, forgotten DLQ) with high-fidelity injected failures, solved in **7 stacks**: PHP 8 · Python · Node.js · Java 21 · .NET 8 · **Go 1.23** · **Rust 1.83** · [landing](https://vladimiracunadev-create.github.io/problem-driven-systems-lab/) |
| [📆 **Social Bot Scheduler**](https://github.com/vladimiracunadev-create/social-bot-scheduler) | **v4.11.0** · **20 مورد**منبع: n8n**18+ موتورهای DB** —**19 عملیات عملیاتی**به صورت جداگانه با Docker حسابرسی می شود.**8 لایه**حسابرسی، محافظان، شکستن مدار و DLQ· [landing](https://vladimiracunadev-create.github.io/social-bot-scheduler/) |
| [🧰 **Microsistemas**](https://github.com/vladimiracunadev-create/microsistemas) | **13 میکروکارهای تشخیصی و مدرن سازی**PHP·محلی Read- Only MCP server·سخت شدن در 3 مرحله· [landing](https://vladimiracunadev-create.github.io/microsistemas/) |
| [🧪 **Docker Labs**](https://github.com/vladimiracunadev-create/docker-labs) | **12 آزمایشگاه**در یک پلت فرم 4service + خودکار`.exe`نصب کننده با Launcher· [landing](https://vladimiracunadev-create.github.io/docker-labs/) |
| [🐳 **WSL Labs**](https://github.com/vladimiracunadev-create/wsl-labs) | **12 مورد**در`wslc`موتور ظروف بومی WSL –**بدون Docker Desktop** · [landing](https://vladimiracunadev-create.github.io/wsl-labs/) |
| [⚡ **Unikernel Labs**](https://github.com/vladimiracunadev-create/unikernel-labs) | "Docker Desktop for Unikernels" : کنترل ویندوز بر UniDSM با WSL2 backend`kraft`QEMU / KVM· [landing](https://vladimiracunadev-create.github.io/unikernel-labs/) |
| [🧰 **QEMU/KVM Labs**](https://github.com/vladimiracunadev-create/qemu-kvm-labs) | **12 آزمایشگاه**مجازی سازی واقعی با QEMU، KVM، libvirt، Cloud-init و`vm-manager`در لینوکس و WSL2· [landing](https://vladimiracunadev-create.github.io/qemu-kvm-labs/) |
| [🛡️ **Sandbox Labs**](https://github.com/vladimiracunadev-create/sandbox-labs) | انزوای لینوکس: اجرای کد شخص ثالث، فایل ها و مدل های تجاری تحت سیاست های اعلام شده و**گزارش های امضا شده که در واقع کنترل ها اعمال می شوند** · **۳۶ مورد**در دو خانواده – ۱۵ بازار فنی و ۲۱ سرمایه –·گواهی تجربی و آموزشی، * نه یک محصول امنیتی *· [landing](https://vladimiracunadev-create.github.io/sandbox-labs/) |
| [💳 **Universal Payments Engineering Lab**](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) | **28 خانواده پرداخت**در یک دموی محلی خود توضیحی: دولت ها، کللی، آشتی، امنیت و راهنماهای پیاده سازی· [landing](https://vladimiracunadev-create.github.io/universal-payments-engineering-lab/) |
| [🕹️ **Decentraland Social Arcade**](https://github.com/vladimiracunadev-create/decentraland-social-arcade) | تجربه بومی Decentraland Social 3D: یک MVP و یک معماری چند بازی با SDK7، ECS و TypeScript·مستند اسپانیایی·پرداخت یا تلهومتر |
| [☁️ **AWS Projects**](https://github.com/vladimiracunadev-create/proyectos-aws) | موارد پیشرفته که هر یک از آنها یک سرویس AWS را اضافه می کند**و**قابلیت جدید GitHub Actions·SAA-C03·DVA-C02·پوشش SOA-C02 |

## 🤖کاربردی AI

| Repo | آنچه که نشان می دهد |
|---|---|
| [🤖 **LangGraph RealWorld**](https://github.com/vladimiracunadev-create/langgraph-realworld) | **25/25 بازگشت عملیاتی**- حالت نوع، مسیرهای مشروط، جریان NDJSON، حالت DEMO / LIVE، 8 لایه امنیتی، زنجیره نگهداری SHA-256 |
| [🧭 **Operational AI Agents**](https://github.com/vladimiracunadev-create/operational-ai-agents) | **23 operational agents** for Claude Code and compatible runtimes: each receives a complete mission —repository evolution, legacy modernization, curriculum design, portfolio publishing, security remediation, incident analysis— under a declared contract, human gates, and verifiable evidence · **69 deterministic evals** · 82 tests · zero-deps (stdlib only) · Linux · macOS · Windows · [site](https://vladimiracunadev-create.github.io/operational-ai-agents/) |
| [🧠 **MCP + Ollama Local**](https://github.com/vladimiracunadev-create/mcp-ollama-local) | Local-first AI with MCP tools in a sandbox · `127.0.0.1` bind · multilayer trust profile · honest about its limits |
| [🧩 **Agentic Plugins Toolkit**](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) | **6 agentic plugins** installable in Claude Code, OpenAI/Codex, Copilot, Gemini, and MCP from one source: `repository-engineering`, `legacy-modernization`, `learning-program-studio`, `product-evolution`, `portfolio-governance`, and `rootcause-response` · **69 generated views without drift** —each runtime receives its format from the same contract— · zero-deps · Linux · macOS · Windows · [site](https://vladimiracunadev-create.github.io/agentic-plugins-toolkit/) |
| [🧰 **Claude Skills Toolkit**](https://github.com/vladimiracunadev-create/claude-skills-toolkit) | **22 agentic skills** for Claude Code · **security**: 12-layer `security-audit` (OSV · KEV · EPSS · SAST · container · secrets) and 14-stage `bitcoin-custody-audit` · **repo gates**: `pre-commit-guard`, `pre-push-guard`, `yaml-control`, `md-lint-fix`, `python-lint-guard` · **coherence**: `repo-coherence-audit`, `version-bump`, `python-version-control`, `python-deps-pinning` · **Docker**: `docker-cleanup`, `docker-compose-doctor` · **docs**: `md-to-doc` · zero-deps · cross-platform |
| [🧰 **Codex Skills Toolkit**](https://github.com/vladimiracunadev-create/codex-skills-toolkit) | **19 agentic skills** for Codex: security and supply chain, preflight, functional flows, resilience and state, release evidence, Python/YAML/Markdown gates, versioning, dependencies, Docker, and documents · Python-first · `pnpm` · Linux · macOS · Windows · [site](https://vladimiracunadev-create.github.io/codex-skills-toolkit/) |

<a id="curricula"></a>

## 📚ویژگی های فنی کامل

برنامه های اکتشافی در اسپانیایی، با وضعیت و محدوده اعلام شده توسط هر مخزن. 21 برنامه اضافه شده به**14550 کلاس**شمارش شده توسط[a workflow](../.github/workflows/stats.yml)از ساختار مخزن واقعی یا یک منبع قابل راستی که در مخزن اعلام شده است؛ نشان هر هفته تازه می شود و توسط دست نوشته نمی شود.

🧭 [**Lifelong Learning Ecosystem**](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem)یک قطب نمای تغذیه شده است که 30 مسیر واقعی را در 6 ناحیه از طریق نقشه های بصری و یک قطب نمای بصری متصل می کند.[accessible offline portal](https://vladimiracunadev-create.github.io/lifelong-learning-ecosystem/)این به عنوان یک برنامه اضافی شمرده نمی شود.

| Program | Classes | Scope |
|---|---:|---|
| [🔢 **Computational Mathematics**](https://github.com/vladimiracunadev-create/computational-mathematics-program) | 360 | از شمارش روی انگشتان تا بازتولید یک کاغذ· **360 تظاهرات قاطع تایید شده در CI** ·1080 نوت بوک·۴۸۹- واژه نامه· [site](https://vladimiracunadev-create.github.io/computational-mathematics-program/) |
| [🏦 **Finance and Banking**](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program) | 356 | 534 h·ریاضیات مالی و IFRS اعتبار، ریسک، بازل III، امور مالی باز، DLT، ثابت کوین ها و MiCA· **27 مورد** · **تست های 298** · [site](https://vladimiracunadev-create.github.io/finance-and-banking-evolution-program/) |
| [🎮 **GameDev**](https://github.com/vladimiracunadev-create/modern-gamedev-program) | 352 | Mathematics and C#/C++/GDScript → shaders, AI, multiplayer, VR/AR · Godot · Unity · Unreal · **10 Godot labs verified in CI** (301 checks) · [site](https://vladimiracunadev-create.github.io/modern-gamedev-program/) |
| [🛡️ **Cybersecurity**](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) | 370 | **v1.3.0** ·21 قسمت·بنیادهای Red Team، DFIR، امنیت ابر، بهره برداری از dev، CTF و امنیت بازی·نقشه برداری برای**7 گواهینامه** ·برنامه Android / Web·PDF Manual·CI، امنیت و صفحات تایید شده· [site](https://vladimiracunadev-create.github.io/modern-cybersecurity-program/) |
| [📈 **Marketing, Sales, and Growth**](https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program) | 336 | 24 بخش با تعاریف عملیاتی، ورق های اندازه گیری، بی اعتبار بودن واقعی، و زمینه تنظیم مقررات شیلی· **v1.6.0** ·1.29M کلمات·17 مسیر مبتنی بر نقش· [site](https://vladimiracunadev-create.github.io/marketing-sales-growth-evolution-program/) |
| [🏢 **Business Creation**](https://github.com/vladimiracunadev-create/modern-business-creation-program) | 336 | ایجاد و کار یک شرکت واقعی در شیلی: از ایده به مشارکت، اقتدار مالیاتی، عملیات، بحران و خروج·360 نمودار·1،251-termary·1،548 صفحه راهنمای· [site](https://vladimiracunadev-create.github.io/modern-business-creation-program/) |
| [🏛️ **Architecture and Built Environment**](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program) | 840 | 84 قسمت·60 جلسه ی یکپارچه·35 مسیر·منابع قابل ردیابی·مارک معکوس، خواننده آفلاین و صفحات GitHub· [site](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/) |
| [🇨🇱 **Chilean School Learning Path**](https://github.com/vladimiracunadev-create/chilean-school-learning-path) | 8,841 | درجه 1 -12· **۴،۱۵ تجربه برنامه های درسی یکپارچه** · **2823 اهداف یادگیری** ·منابع ذهنی·هیچ پیشنهادی و بررسی تخصصی انسانی هنوز در انتظار نیست· [site](https://vladimiracunadev-create.github.io/chilean-school-learning-path/) |
| [🧭 **Modern Software Engineering**](https://github.com/vladimiracunadev-create/modern-software-engineering-program) | 480 | 40 قسمت و 8 مرحله·پایه ها، محصول، معماری، امنیت، DevOps، SRE، SPEC، AI و سیستم های چند عاملی·وضعیت سرمقاله اعلام شده توسط مخزن· [site](https://vladimiracunadev-create.github.io/modern-software-engineering-program/) |
| [🎓 **Pedagogy and Learning Sciences**](https://github.com/vladimiracunadev-create/education-pedagogy-learning-sciences-program) | 300 | از چگونگی یادگیری یک فرد به چگونگی آموزش معلمان·25 قسمت· **هر کلاسی وضعیت و محدودیت های خود را اعلام می کند.** ·سواد اولیه، روش های مقایسه ای، نیازهای آموزشی خاص، همزیستی، تنوع فرهنگی و شواهد بین المللی·1097-termary, 325 Dias و 60-active Class bank·14 مسیر شغلی با نقش·LMS-Exportable· **v2.1.0** · [site](https://vladimiracunadev-create.github.io/education-pedagogy-learning-sciences-program/) |
| [☁️ **Multi-Cloud**](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) | 288 | AWS·Azure·GCP·Kubernetes·سازنده : Terraform·SRE·FinOps· **1،288 ساعت** ·288 آزمایشگاه با شواهد JSON·1032 منابع ردیابی·2884 صفحه راهنمای PDF· [site](https://vladimiracunadev-create.github.io/multi-cloud-engineering-program/) |
| [🎖️ **Executive Leadership**](https://github.com/vladimiracunadev-create/executive-leadership-founder-program) | 288 | از داشتن اولین نتیجه خود برای رهبری یک شرکت و تاسیس خود: تیم ها، KPI /OKR، امور مالی، محصول، خطر، هیئت مدیره و M&A·24 مورد، 96 آزمایشگاه و 39 قالب· [site](https://vladimiracunadev-create.github.io/executive-leadership-founder-program/) |
| [🐍 **Python Data Science**](https://github.com/vladimiracunadev-create/python-data-science-program) | 232 | Polars، ML+Optuna/SHAP، PyTorch/LLMs/LoRA، MLOps·برنامه های ویندوز بومی + Android APK· [site](https://vladimiracunadev-create.github.io/python-data-science-program/) |
| [🧠 **AI Evolution**](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program) | 184 | نماد → یادگیری عمیق → LLM ها، RAG، عوامل، ایمنی و مرز· **v0.17.0** · **708 دفترچه** · **148 مقاله بنیادی** ·برنامه های آفلاین ویندوز، Android و PWA· [site](https://vladimiracunadev-create.github.io/artificial-intelligence-evolution-program/) |
| [🌐 **Comparative Programming**](https://github.com/vladimiracunadev-create/polyglot-programming-labs) | 176 | یک مفهوم،**10 زبان**تایید شده در CI -**1،360 پیاده سازی**- به علاوه**1،750 برنامه**در زبان های زنده (COBOL، Fortran، Ada، RPG، MUMPS ...) و alas of of the**60 کارت در 15 خانواده** ·v1.1.0· [site](https://vladimiracunadev-create.github.io/polyglot-programming-labs/) |
| [🧩 **Frameworks Compared**](https://github.com/vladimiracunadev-create/framework-ecosystems-labs) | 149 | یک قرارداد اجرایی، بدون آداپتور، در برابر Express، FastAPI، Spring Boot، ASP.NET، Django، Rails، Laravel، React، Vue، Svelte و بیشتر·12 قسمت· **70 کلاس ساخت** · **397 مورد تایید در CI** · **منابع ISBN/DOI** · [site](https://vladimiracunadev-create.github.io/framework-ecosystems-labs/) |
| [🗄️ **Databases**](https://github.com/vladimiracunadev-create/database-systems-labs) | 74 | **v3.0.0** ·مهندسی پایگاه داده در 15 بخش·230 ساعت· **منبع قابل اثبات برای هر ادعایی**120 منبع با ISBN، DEC یا استاندارد·همان مورد در 27 موتور حل شد·306- بلند مدت·150 pytest· [site](https://vladimiracunadev-create.github.io/database-systems-labs/) |
| [📐 **Psychometrics and Assessment**](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program) | 40 | چگونه یک ابزار اندازه گیری ساخته شده، به ثمر رسانده، معتبر و حسابرسی شده است·8 قسمت·موتور اجرایی با**5 ابزار و 344 آیتم، 276 Public-domain** · ✍️ **5/40** نوشته‌شده |
| [⛓️ **Blockchain**](https://github.com/vladimiracunadev-create/blockchain-learning-path) | 66 | **v0.15.0** ·از صفر تا زیرساخت های مالی قابل برنامه ریزی و تجزیه و تحلیل های زنجیره ای· **91 شیوه**و**508 تست** ·قراردادهای با Foundry (تحریم و عایق) و تجزیه و تحلیل استاتیک Slither در CI·برنامه های آفلاین با باز کردن باینری و شمارش محتویات آن تایید شده است· [site](https://vladimiracunadev-create.github.io/blockchain-learning-path/) |
| [🧠 **Neural Network Training Labs**](https://github.com/vladimiracunadev-create/neural-network-training-labs) | 31 | 7 ماژول·≈ساعت ≈· **93 دفترچه یادداشت**- 31 کلاس، 31 نسخه دانشجویی و 31 راه حل -·سوالات، نقشه های بصری، شیوه ها و ارزیابی با داده های عمومی واقعی·PyTorch· [study site](https://vladimiracunadev-create.github.io/neural-network-training-labs/) |
| [🕹️ **Machine Operator**](https://github.com/vladimiracunadev-create/machine-operator-program) | 451 | **41 ماژول آموزش**یک در هر ماشین· **502 h 15 دقیقه** ·سیستم ها، کنترل ها، فیزیک، ایمنی و طراحی شبیه سازی با منابع در هر کلاس·* هنوز هم شبیه ساز اجرایی نیست و این گونه اعلام می شود |

🌌 **در حال برنامه‌ریزی، خارج از شمارش:** [نجوم، اخترفیزیک، علوم فضایی و مهندسی هوافضا](https://github.com/vladimiracunadev-create/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program) — ۲٬۰۷۷ درس برنامه‌ریزی‌شده در ۱۲ حوزه و ۱۳۳ بلوک؛ برای ۳۹۷ درس متن نوشته شده و همه هنوز در وضعیت E0 هستند. آموزش مستقل، نه مجوز حرفه‌ای · [سایت](https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/).

## 🔬محاسبات علمی

| Repo | آنچه که نشان می دهد |
|---|---|
| [🧬 **Human Genome Labs**](https://github.com/vladimiracunadev-create/human-genome-labs) | پلتفرم genomics Reroducible: Typed`ScientificResult<T>`قراردادها، FASTA / GFF / VCF، ماژول ها با**بلوغ و شواهد صریح**صداقت رادیکال: * تشخیص بالینی انجام نمی دهد *· [site](https://vladimiracunadev-create.github.io/human-genome-labs/) |

<a id="forks"></a>

## 🍴 forkهای پروژه‌های اشخاص ثالث (52)

این‌ها forkهایی از پروژه‌های دیگران هستند که در این حساب نگهداری می‌شوند. **کار خودم نیستند**: اعتبار آن‌ها متعلق به نویسندگان اصلی است، در هیچ رقمی از این پروفایل به حساب نمی‌آیند و هر توضیح فقط آنچه را پروژهٔ اصلی خودش اعلام کرده خلاصه می‌کند، بدون آنکه به معنای پشتیبانی، ممیزی یا تجربهٔ عملیاتی من باشد. توضیحات بر پایهٔ پروژهٔ اصلی · 2026-11-09.

### 🤖 عامل‌های کدنویسی و چارچوب‌های عامل (18)

| Fork | پروژهٔ اصلی | زبان | چیست |
|---|---|---|---|
| [**OpenHands**](https://github.com/vladimiracunadev-create/OpenHands) | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | TypeScript | پلتفرم عامل برای توسعهٔ نرم‌افزار مبتنی بر هوش مصنوعی |
| [**cline**](https://github.com/vladimiracunadev-create/cline) | [cline/cline](https://github.com/cline/cline) | TypeScript | عامل کدنویسی خودمختار به‌صورت SDK، افزونهٔ IDE یا CLI |
| [**opencode**](https://github.com/vladimiracunadev-create/opencode) | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | عامل کدنویسی متن‌باز |
| [**qwen-code**](https://github.com/vladimiracunadev-create/qwen-code) | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | TypeScript | عامل کدنویسی هوش مصنوعی متن‌باز برای ترمینال |
| [**goose**](https://github.com/vladimiracunadev-create/goose) | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Rust | عامل توسعه‌پذیر که با هر LLM کد را نصب، اجرا، ویرایش و آزمایش می‌کند |
| [**pi**](https://github.com/vladimiracunadev-create/pi) | [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | جعبه‌ابزار عامل: API یکپارچهٔ LLM، حلقهٔ عامل، TUI و CLI کدنویسی |
| [**hermes-agent**](https://github.com/vladimiracunadev-create/hermes-agent) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | عاملی که همراه شما رشد می‌کند (NousResearch) |
| [**deepagents**](https://github.com/vladimiracunadev-create/deepagents) | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Python | مهار عامل «با همهٔ امکانات» (LangChain) |
| [**crewAI**](https://github.com/vladimiracunadev-create/crewAI) | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | چارچوب برای هماهنگی عامل‌های خودمختار نقش‌دار |
| [**agent-framework**](https://github.com/vladimiracunadev-create/agent-framework) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Python | چارچوب مایکروسافت برای ساخت و استقرار عامل‌ها و گردش‌کارهای چندعاملی با Python و .NET |
| [**deepseek-harness**](https://github.com/vladimiracunadev-create/deepseek-harness) | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | TypeScript | مهار عامل DeepSeek که در آن همه‌چیز افزونه است |
| [**agent-orchestrator**](https://github.com/vladimiracunadev-create/agent-orchestrator) | [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Go | برنامه‌ریزی، اجرا و نظارت بر ناوگان عامل‌ها، از وظیفه تا PR ادغام‌شده |
| [**orca**](https://github.com/vladimiracunadev-create/orca) | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | فضای کار برای ناوگانی از عامل‌های کدنویسی (دسکتاپ، موبایل و راه دور) |
| [**kander**](https://github.com/vladimiracunadev-create/kander) | [dualface/kander](https://github.com/dualface/kander) | Go | تخته کانبان که عامل‌های کدنویسی را با git worktree جداگانه و عامل‌های بازبین هماهنگ می‌کند |
| [**OpenBot**](https://github.com/vladimiracunadev-create/OpenBot) | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | TypeScript | همکاران هوش مصنوعی که هر یک رایانهٔ خود را دارند؛ هر اقدام پیش از انجام تصمیم‌گیری و پس از آن ثبت می‌شود |
| [**browser-use**](https://github.com/vladimiracunadev-create/browser-use) | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | کتابخانهٔ Python برای عامل‌های هوش مصنوعی که مرورگر را کنترل می‌کنند |
| [**agent-desktop**](https://github.com/vladimiracunadev-create/agent-desktop) | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Rust | CLI استفادهٔ رایانه (computer use) برای عامل‌های هوش مصنوعی |
| [**treg**](https://github.com/vladimiracunadev-create/treg) | [superdesigndev/treg](https://github.com/superdesigndev/treg) | Python | «OpenRouter برای ابزارهای عامل» |

### 🧩 مهارت‌ها، افزونه‌ها و گردش‌کارها برای عامل‌ها (11)

| Fork | پروژهٔ اصلی | زبان | چیست |
|---|---|---|---|
| [**claude-plugins-official**](https://github.com/vladimiracunadev-create/claude-plugins-official) | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | فهرست رسمی افزونه‌های باکیفیت Claude Code با مدیریت Anthropic |
| [**agentic-awesome-skills**](https://github.com/vladimiracunadev-create/agentic-awesome-skills) | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | Python | صفحهٔ کنترل محلی برای کشف، انتخاب و اعتبارسنجی فهرست بزرگی از مهارت‌های agentic (CLI، MCP محلی، افزونه‌ها) |
| [**claude-review-all**](https://github.com/vladimiracunadev-create/claude-review-all) | [ncoevoet/claude-review-all](https://github.com/ncoevoet/claude-review-all) | Python | بازبینی کد چندعاملی برای Claude Code |
| [**blender-skills**](https://github.com/vladimiracunadev-create/blender-skills) | [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | TypeScript | مهارت‌های تخصصی Blender برای عامل‌های کدنویسی با خط لولهٔ مبتنی بر MCP |
| [**diagram-design**](https://github.com/vladimiracunadev-create/diagram-design) | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | طراحی نمودار سبک نشریه (HTML + SVG) برای عامل‌های کدنویسی |
| [**elephant-goldfish-model**](https://github.com/vladimiracunadev-create/elephant-goldfish-model) | [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) | Python | مهارت‌های باز Google برای طراحی و بازبینی نرم‌افزار با عامل‌های هوش مصنوعی |
| [**Claude-Code-Game-Studios**](https://github.com/vladimiracunadev-create/Claude-Code-Game-Studios) | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | Claude Code را به استودیوی بازی از عامل‌های هماهنگ تبدیل می‌کند |
| [**headcount**](https://github.com/vladimiracunadev-create/headcount) | [cbrock84/headcount](https://github.com/cbrock84/headcount) | Markdown | سازمان عامل‌ها با ساختار یک شرکت: بخش‌ها و مهارت‌های قابل نصب |
| [**agentic-qe**](https://github.com/vladimiracunadev-create/agentic-qe) | [proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) | TypeScript | پلتفرم باز QA/QE با عامل‌ها و مهارت‌ها برای کل چرخهٔ عمر نرم‌افزار |
| [**OpenExecutive**](https://github.com/vladimiracunadev-create/OpenExecutive) | [SenteLabsAI/OpenExecutive](https://github.com/SenteLabsAI/OpenExecutive) | Python | تیم اجرایی مجازی: یک شخصیت اجرایی با پشتیبانی ۸ عامل تخصصی Claude |
| [**n8n-mcp**](https://github.com/vladimiracunadev-create/n8n-mcp) | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | TypeScript | سرور MCP تا Claude، Cursor یا Windsurf گردش‌کارهای n8n بسازند |

### 🛡️ امنیت و تحلیل نرم‌افزار (8)

| Fork | پروژهٔ اصلی | زبان | چیست |
|---|---|---|---|
| [**raptor**](https://github.com/vladimiracunadev-create/raptor) | [gadievron/raptor](https://github.com/gadievron/raptor) | Python | Claude Code را به عامل امنیت تهاجمی و تدافعی تبدیل می‌کند |
| [**Cybersecurity-Projects**](https://github.com/vladimiracunadev-create/Cybersecurity-Projects) | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | Go | ۷۰ پروژهٔ امنیت سایبری از مقدماتی تا پیشرفته |
| [**SkillSpector**](https://github.com/vladimiracunadev-create/SkillSpector) | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Python | اسکنر امنیتی NVIDIA برای مهارت‌های عامل (تزریق پرامپت، نشت داده، زنجیرهٔ تأمین) |
| [**Anthropic-Cybersecurity-Skills**](https://github.com/vladimiracunadev-create/Anthropic-Cybersecurity-Skills) | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | صدها مهارت امنیت سایبری برای عامل‌ها، نگاشت‌شده به MITRE ATT&CK، NIST CSF و چارچوب‌های دیگر |
| [**security-audit-skill**](https://github.com/vladimiracunadev-create/security-audit-skill) | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | مهارت Cloudflare برای ممیزی امنیتی چندمرحله‌ای با یافته‌های تأییدشدهٔ مستقل |
| [**siteone-crawler**](https://github.com/vladimiracunadev-create/siteone-crawler) | [janreges/siteone-crawler](https://github.com/janreges/siteone-crawler) | Rust | خزنده و تحلیلگر وب‌سایت برای سئو، امنیت، دسترس‌پذیری و کارایی |
| [**rea**](https://github.com/vladimiracunadev-create/rea) | [morluto/rea](https://github.com/morluto/rea) | TypeScript | مهندسی معکوس با عامل‌ها، از رفتار برنامه تا باینری‌های بومی |
| [**craft-anything**](https://github.com/vladimiracunadev-create/craft-anything) | [storytold/craft-anything](https://github.com/storytold/craft-anything) | Rust | فهمیدن چگونگی کار هر نرم‌افزار و ساختن نرم‌افزار خودتان |

### 🧠 مدل‌های هوش مصنوعی و زیرساخت (5)

| Fork | پروژهٔ اصلی | زبان | چیست |
|---|---|---|---|
| [**marin**](https://github.com/vladimiracunadev-create/marin) | [marin-community/marin](https://github.com/marin-community/marin) | Python | چارچوب باز برای پژوهش و توسعهٔ مدل‌های پایه |
| [**prime-rl**](https://github.com/vladimiracunadev-create/prime-rl) | [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) | Python | آموزش یادگیری تقویتی عاملی در مقیاس بزرگ |
| [**Olmo-core**](https://github.com/vladimiracunadev-create/Olmo-core) | [allenai/Olmo-core](https://github.com/allenai/Olmo-core) | Python | بلوک‌های سازندهٔ PyTorch برای اکوسیستم OLMo |
| [**DeepInfer**](https://github.com/vladimiracunadev-create/DeepInfer) | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | Python | چارچوب استنتاج پرکارایی و در مقیاس بزرگ برای مدل‌های DeepSeek |
| [**heretic**](https://github.com/vladimiracunadev-create/heretic) | [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | تغییر مدل‌های زبانی بدون بازآموزی (سانسور، چاپلوسی و غیره) |

### 🏢 مدیریت کسب‌وکار و پلتفرم‌ها (6)

| Fork | پروژهٔ اصلی | زبان | چیست |
|---|---|---|---|
| [**erpnext**](https://github.com/vladimiracunadev-create/erpnext) | [frappe/erpnext](https://github.com/frappe/erpnext) | Python | ERP آزاد و متن‌باز |
| [**odoo**](https://github.com/vladimiracunadev-create/odoo) | [odoo/odoo](https://github.com/odoo/odoo) | Python | برنامه‌های کسب‌وکار متن‌باز |
| [**mautic**](https://github.com/vladimiracunadev-create/mautic) | [mautic/mautic](https://github.com/mautic/mautic) | PHP | خودکارسازی بازاریابی متن‌باز |
| [**crm**](https://github.com/vladimiracunadev-create/crm) | [trycompai/crm](https://github.com/trycompai/crm) | TypeScript | CRM متن‌باز طراحی‌شده برای عامل‌های هوش مصنوعی (Comp AI) |
| [**harness**](https://github.com/vladimiracunadev-create/harness) | [harness/harness](https://github.com/harness/harness) | Go | پلتفرم توسعهٔ سرتاسری: مدیریت کد، CI/CD، محیط‌ها و رجیستری مصنوعات |
| [**traccar**](https://github.com/vladimiracunadev-create/traccar) | [traccar/traccar](https://github.com/traccar/traccar) | Java | پلتفرم ردیابی GPS متن‌باز با بیش از ۲۰۰ پروتکل دستگاه |

### 🎓 آموزش و مرجع (4)

| Fork | پروژهٔ اصلی | زبان | چیست |
|---|---|---|---|
| [**computer-science**](https://github.com/vladimiracunadev-create/computer-science) | [ossu/computer-science](https://github.com/ossu/computer-science) | HTML | مسیر رایگان خودآموزی علوم کامپیوتر (OSSU) |
| [**math**](https://github.com/vladimiracunadev-create/math) | [ossu/math](https://github.com/ossu/math) | — | مسیر رایگان خودآموزی ریاضیات (OSSU) |
| [**manim**](https://github.com/vladimiracunadev-create/manim) | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Python | چارچوب Python جامعه‌محور برای انیمیشن‌های ریاضی |
| [**asm-atari-2600**](https://github.com/vladimiracunadev-create/asm-atari-2600) | [johnidm/asm-atari-2600](https://github.com/johnidm/asm-atari-2600) | Assembly | کد منبع نمونهٔ بازی‌های Atari 2600 به زبان اسمبلی |
