# 🗂️ 생태계: 제품, 연구소, 응용 AI, 교육과정, 과학 컴퓨팅

[← 프로필로 돌아가기](../README.ko.md)

**🌐** [Español](ECOSYSTEM.md) · [English](ECOSYSTEM.en.md) · [Português](ECOSYSTEM.pt.md) · [Italiano](ECOSYSTEM.it.md) · [Français](ECOSYSTEM.fr.md) · [简体中文](ECOSYSTEM.zh.md) · [繁體中文](ECOSYSTEM.zh-TW.md) · [日本語](ECOSYSTEM.ja.md) · **한국어** · [Türkçe](ECOSYSTEM.tr.md) · [Русский](ECOSYSTEM.ru.md) · [Tiếng Việt](ECOSYSTEM.vi.md) · [ไทย](ECOSYSTEM.th.md) · [Deutsch](ECOSYSTEM.de.md) · [Українська](ECOSYSTEM.uk.md) · [Polski](ECOSYSTEM.pl.md) · [العربية](ECOSYSTEM.ar.md) · [فارسی](ECOSYSTEM.fa.md) · [Bahasa Indonesia](ECOSYSTEM.id.md) · [Nederlands](ECOSYSTEM.nl.md) · [हिन्दी](ECOSYSTEM.hi.md) · [Ελληνικά](ECOSYSTEM.el.md)

이 프로필의 실무 성과는 별도 문서에 모여 있습니다. 다운로드해 설치하는 소프트웨어, 엔지니어링 연구소, 응용 AI, 완전한 기술 교육과정, 과학 컴퓨팅, 그리고 계정에 있는 제3자 프로젝트 포크 각각에 대한 설명입니다.

## 📦Real Distribution을 통한 제품

다운로드 된 소프트웨어, 설치 및 사용 — 뿐만 아니라 복제.

| Product | What it is | Stack | Delivery |
|---|---|---|---|
| [🔍 **RootCause Windows**](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) | Cybersecurity forensics: every anomalous resource distortion may be the first sign of a threat. Diagnose first, intervene later | Rust 🦀 · ETW/WPR | **v0.19.0** · **16 releases** · **5 editions**: GUI · Portable · CLI · PowerShell · VS Code · [landing](https://vladimiracunadev-create.github.io/rootcause-windows-inspector/) |
| [📱 **RootCause Mobile**](https://github.com/vladimiracunadev-create/rootcause-mobile-inspector) | 모바일 사이블링: 자체에 대한 각 응용 프로그램을 비교하는 법의 센서, 플래그 스토커웨어, 그리고 별도의 권한은 단지 요청한 것들 | 팟캐스트·팟캐스트·퀵메뉴 | **0.0.0 다운로드** ·APK를 다운로드·5 개 언어· **0개의 telemetry** · [landing](https://vladimiracunadev-create.github.io/rootcause-mobile-inspector/) |
| [🍎 **RootCause macOS**](https://github.com/vladimiracunadev-create/rootcause-macos-inspector) | macOS 판:`launchd`지속, Gatekeeper, SIP, FileVault, XProtect, TCC 권한, 서명 프로세스 및 네트워크 이웃 - 알려진 좋은 상태에 대해 모든 표면 검사 | 뚱 베어🦀 ·맥 OS 13+ | **₢ 킹** ·첫 번째 출판된 출시·아파치 2.0· [landing](https://vladimiracunadev-create.github.io/rootcause-macos-inspector/) |
| [🖥️ **RootCause Server**](https://github.com/vladimiracunadev-create/rootcause-server) | 서버 sibling: 단일 로그가 함께 볼 수 없는 상관관계 - 노출된 표면, 액세스 권한 파열, 동일한 주소, 중요 파일 무결성 및 센서 침묵에 부여된 세션, 그리고 하나의 행동 가능한 문장으로 전환 | 뚱 베어🦀 ·윈도우·리눅스·맥 OS | **v0.2.0의** · **18 규칙**증거와 runbook으로·자신의 행동을 결코 실행하지·웹 의존성없이 로컬 콘솔· **아직 공개되지 않음** · [landing](https://vladimiracunadev-create.github.io/rootcause-server/) |
| [🌐 **RootCause Web**](https://github.com/vladimiracunadev-create/rootcause-web-inspector) | Browser forensic sensor: cookies, email sessions, extensions, downloads, permissions, and pages that imitate a real window | JavaScript · MV3 extension | **v0.2.0** · no published release yet · panel on `127.0.0.1` · zero dependencies · zero telemetry verified in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-web-inspector/) |
| [₿ **RootCause Bitcoin Defense**](https://github.com/vladimiracunadev-create/rootcause-bitcoin-defense) | Watch-only defense for Bitcoin custody: inventories the origin of each key, cross-checks it with published warnings, and explains root cause with evidence | JavaScript · Windows app · local panel | **v0.3.0** · **2 releases** · zero dependencies · never asks for seeds · verified in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-bitcoin-defense/) |
| [⛓️ **RootCause Blockchain Security**](https://github.com/vladimiracunadev-create/rootcause-blockchain-security) | Multi-chain watch-only console: inventories contracts, proxies, oracles, bridges, governance, and dependencies, and generates root-cause runbooks | JavaScript · Windows app · local panel | **v0.3.0** in the repository · published release: `v0.1.0` · zero dependencies · never asks for private keys · verified in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-blockchain-security/) |
| [📷 **RootCause QR Inspector**](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) | 행동하기 전에 QR 코드를 검사하는 로컬 안드로이드 앱 : 26 신호를 설명하고, 저하로부터 사실 분리하고, 적정 증거를 수출 | 팟캐스트·팟캐스트 | **v0.2.0** · **6개의 출시** · **163 테스트** ·안드로이드 APK를 게시·verifiable SHA-256를·기술 APK 패키지 서명; 진행중인 상업 / 상점 서명·0개의 telemetry· [landing](https://vladimiracunadev-create.github.io/rootcause-qr-inspector/) |
| [🏢 **Empresa Operativa Chile**](https://github.com/vladimiracunadev-create/empresa-operativa-chile) | Guides a SpA from before incorporation to each monthly close: incorporation with evidence, VAT carry-forward, F29 draft, immutable close, and audit log. Every rule points to its official source | JavaScript · Rust · PWA | **v1.8.0** · Android · Windows · browser · **230 tests** · **0 production dependencies** · zero telemetry · [landing](https://vladimiracunadev-create.github.io/empresa-operativa-chile/) |
| [🔍 **Universal Code Scanner**](https://github.com/vladimiracunadev-create/universal-code-scanner) | QR and barcode reader that **interprets before acting**: 16 local URL risk signals and explicit confirmation | Flutter · Dart | **v1.1.0** · Android · iOS · macOS · PWA · encrypted history **AES-256-GCM** · [landing](https://vladimiracunadev-create.github.io/universal-code-scanner/) |
| [🗄️ **GabySQL**](https://github.com/vladimiracunadev-create/gabysql) | 임베디드 데이터베이스: 단일`.db`파일, WAL, 비용 기반 최적화기, HTTP / JSON API | 뚱 베어🦀 | 윈도우·맥 OS·리눅스· [landing](https://vladimiracunadev-create.github.io/gabysql/) |
| [🤖 **Automa PC**](https://github.com/vladimiracunadev-create/automa-pc) | Local Orchestrator: JSON은 실제 창을 열고 DOM과 상호 작용하며, 증거를 남깁니다. | 팟캐스트·팟캐스트·pywebview의 장점 | **0.0.1 다운로드** · **27의 교류** ·출판 및 검증 가능한 설치· [landing](https://vladimiracunadev-create.github.io/automa-pc/) |
| [🏭 **AI Dataset Foundry**](https://github.com/vladimiracunadev-create/ai-dataset-foundry) | PDF, Word, 웹, Git, JSON 및 CSV를 사전 훈련, 미세 조정, RAG 및 평가를위한 감사 데이터 세트로 전환하는 로컬 최초의 공장 | 팟캐스트 | **v0.2.0의** ·Windows + 오프라인 Android·첫 번째 출판된 출시· [landing](https://vladimiracunadev-create.github.io/ai-dataset-foundry/) |
| [☁️ **AWS Desktop Studio**](https://github.com/vladimiracunadev-create/aws-desktop-studio) | Local-first app with 15 AWS inventory integrations, 20 tutorials, CLI/SSO, and read-only defaults; implementation in progress, not universal access | JavaScript · Windows | **v0.1.1** · first published release · [landing](https://vladimiracunadev-create.github.io/aws-desktop-studio/) |
| [🧭 **Commerce OS**](https://github.com/vladimiracunadev-create/commerce-operating-system) | Guided conceptual demo of commercial operations: catalog, stock, CRM, orders, mock payments, and traceability | JavaScript · Web · Windows · Android | **v0.3.0** · **3 releases** · no real money or Chilean tax authority integration · [landing](https://vladimiracunadev-create.github.io/commerce-operating-system/) |
| [📄 **PDF Reader**](https://github.com/vladimiracunadev-create/pdf-reader-windows-android) | Android-first local read-only reader, with no-crop zoom, reopenable history, WhatsApp sharing, and default-reader selection | HTML · Web · Android · Windows | **v0.3.3** · signed APK · no accounts, sensitive permissions, or telemetry · [landing](https://vladimiracunadev-create.github.io/pdf-reader-windows-android/) |
| [🎙️ **Video Transcript Studio**](https://github.com/vladimiracunadev-create/video-transcript-studio) | 한 비디오, 재생 목록, 또는**전체 YouTube 채널**타임스탬프와 텍스트. 기존 자막에 의존하지 않습니다. Whisper는 오디오를 인식**당신의 기계에**, API, 계정, 또는 구성하는 열쇠 없이 | 팟캐스트·PySide6의 특징·빠른 API·빠른 위스키 | **v0.2.0의** ·Windows 데스크톱 + 로컬 패널`127.0.0.1`+ CLI,**같은 큐를 공유** ·담당자: Mr. s. com·PDF 파일·TXT의·RSS 피드·VTT 소개·의논하기·MP3의·의 OGG· **89 시험** ·묶인 FFmpeg·0개의 telemetry· [landing](https://vladimiracunadev-create.github.io/video-transcript-studio/) |
| [🎨 **ChofyAI Studio**](https://github.com/vladimiracunadev-create/chofyai-studio) | Local Creative AI launcher: 관현악 Qwen3-TTS, whisper.cpp, FaceFusion, AceForge, ComfyUI | 타우리 2·뚱 베어·퀵메뉴 | 0.0.1 다운로드· **5/5 실제 inference 도구** ·macOS 애플 실리콘·실험적인 Windows· **아직 공개되지 않음** · [site](https://vladimiracunadev-create.github.io/chofyai-studio/) |
| [🦏 **Rhino Suite**](https://github.com/vladimiracunadev-create/rhino-suite) | 스크래치의 오피스 스위트: 문서 규칙은 DOM에 의존하지 않습니다 — HTML은 단지 투영입니다 | 녹/WASM·으로·반응 19 | 진화 monorepo 단계별· [landing](https://vladimiracunadev-create.github.io/rhino-suite/) |
| [🎻 **My Violin Adventure**](https://github.com/vladimiracunadev-create/violin-adventure) | Educational app for children: chromatic tuner, audio-clock-accurate metronome, songs with real violin | Tauri 2 · React · TS | **v1.3.0** · Windows · Android · Linux · macOS · PWA · [landing](https://vladimiracunadev-create.github.io/violin-adventure/) |
| [🎸 **My Guitar Adventure**](https://github.com/vladimiracunadev-create/guitarra-adventure) | The plucked-string sibling: 24 lessons in 6 worlds, 6-string tuner, drift-free metronome, and 11 real guitar notes | Tauri 2 · React · TS | **v1.0.0** · Windows · Android · Linux · macOS · iOS · PWA · no accounts, ads, or online dependency · [landing](https://vladimiracunadev-create.github.io/guitarra-adventure/) |
| [🧣 **Pañuelo al Viento**](https://github.com/vladimiracunadev-create/panuelo-al-viento-cueca-app) | Cueca from age 10: 24 classes in 8 levels, 72 activities, six-pulse lab (3+3 and 2+2+2), and accessible floor diagrams. It states that it **complements, not replaces**, teachers and culture bearers | Flutter · Dart | **v0.2.0** · Android 7+ · Windows 10/11 · APK · EXE · MSI · portable · **29 tests + 2 validators** · no camera, microphone, account, ads, or internet · [landing](https://vladimiracunadev-create.github.io/panuelo-al-viento-cueca-app/) |

## 🧪엔지니어링 연구소

| 의논하기 | 어떤 의미 |
|---|---|
| [🐳 **Problem-Driven Systems Lab**](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) | **20 실제 문제**(부하, N+1의 재기 폭풍, 누출, 모놀리, 캐시 스탬프, backpressure, 0-downtime 마이그레이션, 잊어 DLQ) 높은-피델리 인젝트 실패, 해결**7개의 더미**: PHP 8·팟캐스트·Node.js를 사용하려면·Java 21의·.NET 8의· **1.23로 이동** · **녹 1.83** · [landing](https://vladimiracunadev-create.github.io/problem-driven-systems-lab/) |
| [📆 **Social Bot Scheduler**](https://github.com/vladimiracunadev-create/social-bot-scheduler) | **v4.11.0** · **20 건**source→n8n→receiver에**18+ DB 엔진** —**19 운영**, 독수리로 개별적으로 감사-**8 층**감사, 불투명 난간, 회로 차단기 및 DLQ· [landing](https://vladimiracunadev-create.github.io/social-bot-scheduler/) |
| [🧰 **Microsistemas**](https://github.com/vladimiracunadev-create/microsistemas) | **13 진단과 현대화 microapps**PHP에 대한·로컬 읽기 전용 MCP 서버·3 단계의 경화· [landing](https://vladimiracunadev-create.github.io/microsistemas/) |
| [🧪 **Docker Labs**](https://github.com/vladimiracunadev-create/docker-labs) | **12 실험실**4대 서비스 플랫폼 + 자동화`.exe`launcher와 설치· [landing](https://vladimiracunadev-create.github.io/docker-labs/) |
| [🐳 **WSL Labs**](https://github.com/vladimiracunadev-create/wsl-labs) | **12 cases** on `wslc`, the native WSL container engine — **without Docker Desktop** · [landing](https://vladimiracunadev-create.github.io/wsl-labs/) |
| [⚡ **Unikernel Labs**](https://github.com/vladimiracunadev-create/unikernel-labs) | “다중한 데스크톱”: WSL2 백엔드를 가진 Unikraft에 Windows 통제,`kraft`+ QEMU/KVM의· [landing](https://vladimiracunadev-create.github.io/unikernel-labs/) |
| [🧰 **QEMU/KVM Labs**](https://github.com/vladimiracunadev-create/qemu-kvm-labs) | **12 실험실**QEMU, KVM, libvirt, 클라우드 init, 및 실제 가상화의`vm-manager`리눅스 및 WSL2· [landing](https://vladimiracunadev-create.github.io/qemu-kvm-labs/) |
| [🛡️ **Sandbox Labs**](https://github.com/vladimiracunadev-create/sandbox-labs) | Linux isolation: 선언된 정책과 밑에 제삼자 부호, 파일 및 사업 모형을 실행하십시오**실제로 적용되는 통제의 서명한 증거** · **36 건**2개의 가족 —15명의 기술 및 21개의 자본 시장—·실험 및 교육 선언, * 보안 제품 *· [landing](https://vladimiracunadev-create.github.io/sandbox-labs/) |
| [💳 **Universal Payments Engineering Lab**](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) | **28 결제 가족**로컬 자체 설명 데모: 상태, ledger, 재건축, 보안, 구현 가이드· [landing](https://vladimiracunadev-create.github.io/universal-payments-engineering-lab/) |
| [🕹️ **Decentraland Social Arcade**](https://github.com/vladimiracunadev-create/decentraland-social-arcade) | Native Decentraland 소셜 3D 경험: MVP와 SDK7, ECS, TypeScript를 가진 멀티게임 아키텍처·English 한국어·지불 또는 원격 측정 |
| [☁️ **AWS Projects**](https://github.com/vladimiracunadev-create/proyectos-aws) | Progressive cases where each one adds one AWS service **and** a new GitHub Actions capability · SAA-C03 · DVA-C02 · SOA-C02 coverage |

## 🤖응용 AI

| 의논하기 | 어떤 의미 |
|---|---|
| [🤖 **LangGraph RealWorld**](https://github.com/vladimiracunadev-create/langgraph-realworld) | **25/25 운영한 후원**— 유형 상태, 조건 경로, NDJSON 스트리밍, DEMO/LIVE 모드, 8 보안 레이어, custody의 SHA-256 체인 |
| [🧭 **Operational AI Agents**](https://github.com/vladimiracunadev-create/operational-ai-agents) | **23 운영 대리인**Claude Code 및 호환 실행 시간: 각은 완전한 임무를받습니다. - 구조 진화, 유산 현대화, 커리큘럼 디자인, 포트폴리오 출판, 보안 구제, 사건 분석 - 선언 계약, 인간 문 및 검증 가능한 증거· **69개의 신중한 evals** ·82 테스트·0-deps (stdlib 전용)·리눅스·맥 OS·윈도우· [site](https://vladimiracunadev-create.github.io/operational-ai-agents/) |
| [🧠 **MCP + Ollama Local**](https://github.com/vladimiracunadev-create/mcp-ollama-local) | 샌드박스의 MCP 도구와 현지 최초의 AI· `127.0.0.1`팟캐스트·다중층 신뢰 프로필·그 한계에 대해 정직 |
| [🧩 **Agentic Plugins Toolkit**](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) | **6개의 대리인 플러그인**Claude Code, OpenAI/Codex, Copilot, Gemini 및 MCP에서 설치 가능:`repository-engineering`, `legacy-modernization`, `learning-program-studio`, `product-evolution`, `portfolio-governance`, 및`rootcause-response` · **69 생성된 조회 수 없이 drift**—각 실행 시간은 같은 계약에서 형식을받습니다.·0-deps의·리눅스·맥 OS·윈도우· [site](https://vladimiracunadev-create.github.io/agentic-plugins-toolkit/) |
| [🧰 **Claude Skills Toolkit**](https://github.com/vladimiracunadev-create/claude-skills-toolkit) | **22 agentic skills** for Claude Code · **security**: 12-layer `security-audit` (OSV · KEV · EPSS · SAST · container · secrets) and 14-stage `bitcoin-custody-audit` · **repo gates**: `pre-commit-guard`, `pre-push-guard`, `yaml-control`, `md-lint-fix`, `python-lint-guard` · **coherence**: `repo-coherence-audit`, `version-bump`, `python-version-control`, `python-deps-pinning` · **Docker**: `docker-cleanup`, `docker-compose-doctor` · **docs**: `md-to-doc` · zero-deps · cross-platform |
| [🧰 **Codex Skills Toolkit**](https://github.com/vladimiracunadev-create/codex-skills-toolkit) | **19 에이전트 기술**Codex: 보안 및 공급망, 선명하고 기능적인 흐름, 탄력 및 상태, 방출 증거, Python/YAML/Markdown 문, 판결, 종결, 도크러 및 문서·Python-first(펄스)· `pnpm` ·리눅스·맥 OS·윈도우· [site](https://vladimiracunadev-create.github.io/codex-skills-toolkit/) |

<a id="curricula"></a>

## 📚완전한 기술 교육과정

스페인어의 순차적 프로그램, 상태 및 범위는 각 저장소에 의해 선언. 21개의 프로그램 추가**14,550 클래스**, 으로 계산[a workflow](../.github/workflows/stats.yml)실제 저장소 구조 또는 저장소에 선언 된 검증 가능한 소스에서; 배지는 매주 새로 고침하고 손으로 작성되지 않습니다.

🧭 [**Lifelong Learning Ecosystem**](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem) is a federated compass connecting 30 real paths across 6 areas through visual maps and an [accessible offline portal](https://vladimiracunadev-create.github.io/lifelong-learning-ecosystem/); it is not counted as an additional program.

| 의 특징 | 의 특징 | 의논하기 |
|---|---:|---|
| [🔢 **Computational Mathematics**](https://github.com/vladimiracunadev-create/computational-mathematics-program) | 360 | 손가락에 넣기에서 종이를 재생· **360개의 신중한 시연** ·1,080 노트북·489-term 광택· [site](https://vladimiracunadev-create.github.io/computational-mathematics-program/) |
| [🏦 **Finance and Banking**](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program) | 356 | 534 시간·금융 수학 및 IFRS → 신용, 위험, Basel III, 개방 금융, DLT, Stablecoins 및 MiCA· **27 건의 사례** · **298 테스트** · [site](https://vladimiracunadev-create.github.io/finance-and-banking-evolution-program/) |
| [🎮 **GameDev**](https://github.com/vladimiracunadev-create/modern-gamedev-program) | 352 | 수학 및 C # / C++ / GDScript → 쉐이더, AI, 멀티플레이어, VR / AR·혜진·뚱 베어·뚱 베어· **CI에서 확인 된 10 Godot 실험실**(301건)· [site](https://vladimiracunadev-create.github.io/modern-gamedev-program/) |
| [🛡️ **Cybersecurity**](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) | 370 | **₢ 킹** ·21 부품·기초 → Red Team, DFIR, 클라우드 보안, 분산, CTF 및 게임 보안·지도로**7 인증** ·오프라인 Android/웹 앱·PDF 설명서·CI, 보안 및 페이지 확인· [site](https://vladimiracunadev-create.github.io/modern-cybersecurity-program/) |
| [📈 **Marketing, Sales, and Growth**](https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program) | 336 | 운영 정의, 측정 시트, 검증 가능한 생물학적, 칠레 규제 상황에 24 부품· **0.0.0.0 다운로드** ·1.29M 단어·17개의 역할 기반 경로· [site](https://vladimiracunadev-create.github.io/marketing-sales-growth-evolution-program/) |
| [🏢 **Business Creation**](https://github.com/vladimiracunadev-create/modern-business-creation-program) | 336 | 칠레에서 실제 회사를 만들고 운영합니다. 설립, 세금 기관, 운영, 위기 및 출구에 대한 아이디어에서·360도·1,251 용어 광택·1,548 페이지 설명서· [site](https://vladimiracunadev-create.github.io/modern-business-creation-program/) |
| [🏛️ **Architecture and Built Environment**](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program) | 840 | 84 부품·60개의 통합 세션·35 경로·추적 가능한 소스·Markdown, 오프라인 리더, GitHub 페이지· [site](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/) |
| [🇨🇱 **Chilean School Learning Path**](https://github.com/vladimiracunadev-create/chilean-school-learning-path) | 8,841 | 학년 1-12· **4,156 통합 크로스 컬리어** · **2,823 학습 목표** ·MINEDUC 소스·공개 제안 및 전문 인적 검토는 여전히 종료· [site](https://vladimiracunadev-create.github.io/chilean-school-learning-path/) |
| [🧭 **Modern Software Engineering**](https://github.com/vladimiracunadev-create/modern-software-engineering-program) | 480 | 40 부품 및 8 단계·기초 → 제품, 건축, 안전, DevOps, SRE, SPEC, AI 및 다중 시약 체계·repository에 의해 선언 된 편집 상태· [site](https://vladimiracunadev-create.github.io/modern-software-engineering-program/) |
| [🎓 **Pedagogy and Learning Sciences**](https://github.com/vladimiracunadev-create/education-pedagogy-learning-sciences-program) | 300 | 선생님이 훈련하는 방법을 배우는 방법·25 부품· **각 클래스는 증거 국가와 한계를 선언합니다.** ·초기의 문학, 비교 방법, 특정 교육 요구, 협동, 문화 다양성, 국제 증거·1,097-term 광택, 325 다이어그램 및 60-activity 교실 은행·14 역할에 의한 경력 경로·LMS 호환· **₢ 킹** · [site](https://vladimiracunadev-create.github.io/education-pedagogy-learning-sciences-program/) |
| [☁️ **Multi-Cloud**](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) | 288 | AWS 지원·는·GCP(주)·쿠버네티스·의 특징·₢ 킹·핀 핑· **1,288 시간** ·288 JSON 증거와 실험실·1,032 추적 소스·2,884 페이지 PDF 설명서· [site](https://vladimiracunadev-create.github.io/multi-cloud-engineering-program/) |
| [🎖️ **Executive Leadership**](https://github.com/vladimiracunadev-create/executive-leadership-founder-program) | 288 | 회사를 선도하고 자신만의 팀을 이끌고, KPI/OKR, 금융, 제품, 위험, 보드 및 M&A를 자체적으로 관리하여·24건, 96건, 39건· [site](https://vladimiracunadev-create.github.io/executive-leadership-founder-program/) |
| [🐍 **Python Data Science**](https://github.com/vladimiracunadev-create/python-data-science-program) | 232 | 극, ML + Optuna / SHAP, PyTorch / LLMs / LoRA, MLOps·기본 Windows 앱 + Android APK· [site](https://vladimiracunadev-create.github.io/python-data-science-program/) |
| [🧠 **AI Evolution**](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program) | 184 | 심볼 → probabilistic → 깊은 학습 → LLMs, RAG, 대리인, 안전, 및 국경· **v0.17.0의** · **708 노트북** · **148 기초지** ·오프라인 Windows, Android 및 PWA 앱· [site](https://vladimiracunadev-create.github.io/artificial-intelligence-evolution-program/) |
| [🌐 **Comparative Programming**](https://github.com/vladimiracunadev-create/polyglot-programming-labs) | 176 | 1개의 개념,**10 개 언어**CI에서 확인하기 —**1,360 구현**- 더하기**1,632 프로그램**아직도 살고있는 언어 (COBOL, Fortran, Ada, RPG, MUMPS...)과 아틀라스의**15개 가족 60개 카드** ·₢ 킹· [site](https://vladimiracunadev-create.github.io/polyglot-programming-labs/) |
| [🧩 **Frameworks Compared**](https://github.com/vladimiracunadev-create/framework-ecosystems-labs) | 149 | 어댑터가 없는 한 실행 가능한 계약, Express, FastAPI, Spring Boot, ASP.NET, Django, Rails, Laravel, React, Vue, Svelte 등·12 부품· **70 내장 클래스** · **397건 CI에서 확인된 경우** · **210 ISBN/DOI 소스** · [site](https://vladimiracunadev-create.github.io/framework-ecosystems-labs/) |
| [🗄️ **Databases**](https://github.com/vladimiracunadev-create/database-systems-labs) | 74 | **0.0.0.0의** ·15개 부품 엔지니어링·230시간· **모든 청구에 대한 검증 가능한 소스**: ISBN, DOI, 또는 표준 120 소스·27 엔진에서 해결되는 동일한 케이스·306-term 광택·150 파이트· [site](https://vladimiracunadev-create.github.io/database-systems-labs/) |
| [📐 **Psychometrics and Assessment**](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program) | 40 | 측정 계기가 내장되어 있고, 평가되고, 검증되고, 감사·8개 부품·실행 가능한 엔진**5개 상품 및 344개 상품, 276개 공공주** · ✍️ **5/40** 작성됨 |
| [⛓️ **Blockchain**](https://github.com/vladimiracunadev-create/blockchain-learning-path) | 66 | **v0.15.0** · from zero to programmable financial infrastructure and on-chain analytics · **91 practices** and **508 tests** · contracts with Foundry (fuzzing and invariants) and Slither static analysis in CI · offline apps verified by opening the binary and counting its contents · [site](https://vladimiracunadev-create.github.io/blockchain-learning-path/) |
| [🧠 **Neural Network Training Labs**](https://github.com/vladimiracunadev-create/neural-network-training-labs) | 31 | 7개의 단위·≈214 시간· **93 노트북**—31 클래스, 31 학생 버전, 31 솔루션—·질문, 시각지도, 관행 및 실제 자료로 평가·핑크· [study site](https://vladimiracunadev-create.github.io/neural-network-training-labs/) |
| [🕹️ **Machine Operator**](https://github.com/vladimiracunadev-create/machine-operator-program) | 451 | **41 교육 모듈**, 기계 당 하나· **502 h 15 분** ·시스템, 제어, 물리, 안전, 및 클래스 당 소스와 시뮬레이션 디자인·* 아직 실행할 수 없는 시뮬레이터, 그리고 그것은 그 way* 선언됩니다 |
| [🌌 **천문학, 천체물리학, 우주과학, 항공우주공학**](https://github.com/vladimiracunadev-create/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program) | — | **계획 중, 집계 제외:** 12개 영역, 133개 블록에 걸친 2,077개 계획 수업. 397개는 본문이 작성되었으며 모두 아직 E0 상태입니다. 독립 교육이며 직업 자격이 아닙니다 · [사이트](https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/). |

## 🔬과학 컴퓨팅

| 의논하기 | 어떤 의미 |
|---|---|
| [🧬 **Human Genome Labs**](https://github.com/vladimiracunadev-create/human-genome-labs) | Reproducible genomics 플랫폼: 유형`ScientificResult<T>`계약, FASTA/GFF3/VCF의 단위**명시적 성숙과 증거**. Radical 정직: * 그것은 임상 진단*를 실행하지 않습니다· [site](https://vladimiracunadev-create.github.io/human-genome-labs/) |

<a id="forks"></a>

## 🍴 제3자 프로젝트의 포크 (52)

이 계정에 보관된 타인 프로젝트의 포크입니다. **제 자체 작업물이 아닙니다**. 공로는 원저자에게 있으며, 이 프로필의 어떤 수치에도 포함되지 않고, 각 설명은 원 프로젝트가 스스로 밝힌 내용을 요약한 것으로 지원, 감사 또는 제 운영 경험을 뜻하지 않습니다. 설명은 원 프로젝트 기준 · 2026-11-09.

### 🤖 코딩 에이전트와 에이전트 프레임워크 (18)

| 포크 | 원 프로젝트 | 언어 | 설명 |
|---|---|---|---|
| [**OpenHands**](https://github.com/vladimiracunadev-create/OpenHands) | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | TypeScript | AI 기반 소프트웨어 개발을 위한 에이전트 플랫폼 |
| [**cline**](https://github.com/vladimiracunadev-create/cline) | [cline/cline](https://github.com/cline/cline) | TypeScript | SDK, IDE 확장, CLI로 쓰는 자율 코딩 에이전트 |
| [**opencode**](https://github.com/vladimiracunadev-create/opencode) | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 오픈소스 코딩 에이전트 |
| [**qwen-code**](https://github.com/vladimiracunadev-create/qwen-code) | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | TypeScript | 터미널용 오픈소스 AI 코딩 에이전트 |
| [**goose**](https://github.com/vladimiracunadev-create/goose) | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Rust | 어떤 LLM으로든 코드를 설치·실행·편집·테스트하는 확장형 에이전트 |
| [**pi**](https://github.com/vladimiracunadev-create/pi) | [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | 에이전트 툴킷: 통합 LLM API, 에이전트 루프, TUI, 코딩 CLI |
| [**hermes-agent**](https://github.com/vladimiracunadev-create/hermes-agent) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 사용자와 함께 성장하는 에이전트 (NousResearch) |
| [**deepagents**](https://github.com/vladimiracunadev-create/deepagents) | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Python | "배터리 포함" 에이전트 하네스 (LangChain) |
| [**crewAI**](https://github.com/vladimiracunadev-create/crewAI) | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | 역할을 가진 자율 에이전트를 오케스트레이션하는 프레임워크 |
| [**agent-framework**](https://github.com/vladimiracunadev-create/agent-framework) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Python | Python과 .NET으로 에이전트와 멀티 에이전트 워크플로를 구축·배포하는 Microsoft 프레임워크 |
| [**deepseek-harness**](https://github.com/vladimiracunadev-create/deepseek-harness) | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | TypeScript | 모든 것이 플러그인인 DeepSeek 에이전트 하네스 |
| [**agent-orchestrator**](https://github.com/vladimiracunadev-create/agent-orchestrator) | [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Go | 작업부터 병합된 PR까지 에이전트 함대를 계획·실행·감독 |
| [**orca**](https://github.com/vladimiracunadev-create/orca) | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 코딩 에이전트 함대를 다루는 작업 공간 (데스크톱, 모바일, 원격) |
| [**kander**](https://github.com/vladimiracunadev-create/kander) | [dualface/kander](https://github.com/dualface/kander) | Go | 격리된 git worktree와 리뷰어 에이전트로 코딩 에이전트를 조율하는 칸반 보드 |
| [**OpenBot**](https://github.com/vladimiracunadev-create/OpenBot) | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | TypeScript | 각자 자기 컴퓨터를 가진 AI 동료. 모든 행동은 사전에 결정되고 사후에 기록됨 |
| [**browser-use**](https://github.com/vladimiracunadev-create/browser-use) | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | 브라우저를 조작하는 AI 에이전트용 Python 라이브러리 |
| [**agent-desktop**](https://github.com/vladimiracunadev-create/agent-desktop) | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Rust | AI 에이전트용 computer use CLI |
| [**treg**](https://github.com/vladimiracunadev-create/treg) | [superdesigndev/treg](https://github.com/superdesigndev/treg) | Python | "에이전트 도구용 OpenRouter" |

### 🧩 에이전트용 스킬, 플러그인, 워크플로 (11)

| 포크 | 원 프로젝트 | 언어 | 설명 |
|---|---|---|---|
| [**claude-plugins-official**](https://github.com/vladimiracunadev-create/claude-plugins-official) | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | Anthropic이 관리하는 고품질 Claude Code 플러그인 공식 디렉터리 |
| [**agentic-awesome-skills**](https://github.com/vladimiracunadev-create/agentic-awesome-skills) | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | Python | 대규모 agentic 스킬 카탈로그를 찾고 선택하고 검증하는 로컬 컨트롤 플레인 (CLI, 로컬 MCP, 플러그인) |
| [**claude-review-all**](https://github.com/vladimiracunadev-create/claude-review-all) | [ncoevoet/claude-review-all](https://github.com/ncoevoet/claude-review-all) | Python | Claude Code용 멀티 에이전트 코드 리뷰 |
| [**blender-skills**](https://github.com/vladimiracunadev-create/blender-skills) | [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | TypeScript | 코딩 에이전트용 Blender 전문 스킬, MCP 기반 파이프라인 |
| [**diagram-design**](https://github.com/vladimiracunadev-create/diagram-design) | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 코딩 에이전트용 에디토리얼 다이어그램 디자인 (HTML + SVG) |
| [**elephant-goldfish-model**](https://github.com/vladimiracunadev-create/elephant-goldfish-model) | [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) | Python | AI 에이전트로 소프트웨어를 설계·검토하는 Google의 오픈 스킬 |
| [**Claude-Code-Game-Studios**](https://github.com/vladimiracunadev-create/Claude-Code-Game-Studios) | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | Claude Code를 협업하는 에이전트로 구성된 게임 스튜디오로 변환 |
| [**headcount**](https://github.com/vladimiracunadev-create/headcount) | [cbrock84/headcount](https://github.com/cbrock84/headcount) | Markdown | 회사처럼 구성한 에이전트 조직: 부서와 설치 가능한 스킬 |
| [**agentic-qe**](https://github.com/vladimiracunadev-create/agentic-qe) | [proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) | TypeScript | 소프트웨어 전체 수명주기를 에이전트와 스킬로 지원하는 오픈 QA/QE 플랫폼 |
| [**OpenExecutive**](https://github.com/vladimiracunadev-create/OpenExecutive) | [SenteLabsAI/OpenExecutive](https://github.com/SenteLabsAI/OpenExecutive) | Python | 가상 경영진 팀: 8개의 전문 Claude 에이전트가 뒷받침하는 한 명의 경영자 페르소나 |
| [**n8n-mcp**](https://github.com/vladimiracunadev-create/n8n-mcp) | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | TypeScript | Claude, Cursor, Windsurf가 n8n 워크플로를 만들 수 있게 하는 MCP 서버 |

### 🛡️ 보안 및 소프트웨어 분석 (8)

| 포크 | 원 프로젝트 | 언어 | 설명 |
|---|---|---|---|
| [**raptor**](https://github.com/vladimiracunadev-create/raptor) | [gadievron/raptor](https://github.com/gadievron/raptor) | Python | Claude Code를 공격·방어 보안 에이전트로 변환 |
| [**Cybersecurity-Projects**](https://github.com/vladimiracunadev-create/Cybersecurity-Projects) | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | Go | 초급부터 고급까지 70개의 사이버 보안 프로젝트 |
| [**SkillSpector**](https://github.com/vladimiracunadev-create/SkillSpector) | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Python | 에이전트 스킬용 NVIDIA 보안 스캐너 (프롬프트 인젝션, 유출, 공급망) |
| [**Anthropic-Cybersecurity-Skills**](https://github.com/vladimiracunadev-create/Anthropic-Cybersecurity-Skills) | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | MITRE ATT&CK, NIST CSF 등에 매핑된 에이전트용 사이버 보안 스킬 수백 개 |
| [**security-audit-skill**](https://github.com/vladimiracunadev-create/security-audit-skill) | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 독립 검증된 결과를 내는 다단계 보안 감사용 Cloudflare 스킬 |
| [**siteone-crawler**](https://github.com/vladimiracunadev-create/siteone-crawler) | [janreges/siteone-crawler](https://github.com/janreges/siteone-crawler) | Rust | SEO, 보안, 접근성, 성능을 위한 웹사이트 크롤러 및 분석기 |
| [**rea**](https://github.com/vladimiracunadev-create/rea) | [morluto/rea](https://github.com/morluto/rea) | TypeScript | 에이전트로 하는 리버스 엔지니어링. 앱 동작부터 네이티브 바이너리까지 |
| [**craft-anything**](https://github.com/vladimiracunadev-create/craft-anything) | [storytold/craft-anything](https://github.com/storytold/craft-anything) | Rust | 어떤 소프트웨어든 작동 원리를 이해하고 나만의 것을 만들기 |

### 🧠 AI 모델과 인프라 (5)

| 포크 | 원 프로젝트 | 언어 | 설명 |
|---|---|---|---|
| [**marin**](https://github.com/vladimiracunadev-create/marin) | [marin-community/marin](https://github.com/marin-community/marin) | Python | 파운데이션 모델 연구·개발을 위한 오픈 프레임워크 |
| [**prime-rl**](https://github.com/vladimiracunadev-create/prime-rl) | [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) | Python | 대규모 에이전트형 강화학습 훈련 |
| [**Olmo-core**](https://github.com/vladimiracunadev-create/Olmo-core) | [allenai/Olmo-core](https://github.com/allenai/Olmo-core) | Python | OLMo 생태계를 위한 PyTorch 구성 요소 |
| [**DeepInfer**](https://github.com/vladimiracunadev-create/DeepInfer) | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | Python | DeepSeek 모델용 고성능 대규모 추론 프레임워크 |
| [**heretic**](https://github.com/vladimiracunadev-create/heretic) | [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | 재학습 없이 언어 모델 수정 (검열, 아첨 등) |

### 🏢 기업 경영과 플랫폼 (6)

| 포크 | 원 프로젝트 | 언어 | 설명 |
|---|---|---|---|
| [**erpnext**](https://github.com/vladimiracunadev-create/erpnext) | [frappe/erpnext](https://github.com/frappe/erpnext) | Python | 자유 오픈소스 ERP |
| [**odoo**](https://github.com/vladimiracunadev-create/odoo) | [odoo/odoo](https://github.com/odoo/odoo) | Python | 오픈소스 비즈니스 앱 |
| [**mautic**](https://github.com/vladimiracunadev-create/mautic) | [mautic/mautic](https://github.com/mautic/mautic) | PHP | 오픈소스 마케팅 자동화 |
| [**crm**](https://github.com/vladimiracunadev-create/crm) | [trycompai/crm](https://github.com/trycompai/crm) | TypeScript | AI 에이전트를 위해 설계된 오픈소스 CRM (Comp AI) |
| [**harness**](https://github.com/vladimiracunadev-create/harness) | [harness/harness](https://github.com/harness/harness) | Go | 소스 관리, CI/CD, 환경, 아티팩트 레지스트리를 갖춘 종단 간 개발 플랫폼 |
| [**traccar**](https://github.com/vladimiracunadev-create/traccar) | [traccar/traccar](https://github.com/traccar/traccar) | Java | 오픈소스 GPS 추적 플랫폼, 200개 이상의 장치 프로토콜 |

### 🎓 교육과 참고 자료 (4)

| 포크 | 원 프로젝트 | 언어 | 설명 |
|---|---|---|---|
| [**computer-science**](https://github.com/vladimiracunadev-create/computer-science) | [ossu/computer-science](https://github.com/ossu/computer-science) | HTML | 컴퓨터 과학 무료 독학 경로 (OSSU) |
| [**math**](https://github.com/vladimiracunadev-create/math) | [ossu/math](https://github.com/ossu/math) | — | 수학 무료 독학 경로 (OSSU) |
| [**manim**](https://github.com/vladimiracunadev-create/manim) | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Python | 수학 애니메이션용 커뮤니티 Python 프레임워크 |
| [**asm-atari-2600**](https://github.com/vladimiracunadev-create/asm-atari-2600) | [johnidm/asm-atari-2600](https://github.com/johnidm/asm-atari-2600) | Assembly | 어셈블리로 작성된 Atari 2600 게임 샘플 소스 코드 |
