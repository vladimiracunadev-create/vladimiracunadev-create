# 🗂️ Ecosistema: prodotti, laboratori, IA applicata, curricula e calcolo scientifico

[← Torna al profilo](../README.it.md)

**🌐** [Español](ECOSYSTEM.md) · [English](ECOSYSTEM.en.md) · [Português](ECOSYSTEM.pt.md) · **Italiano** · [Français](ECOSYSTEM.fr.md) · [简体中文](ECOSYSTEM.zh.md) · [繁體中文](ECOSYSTEM.zh-TW.md) · [日本語](ECOSYSTEM.ja.md) · [한국어](ECOSYSTEM.ko.md) · [Türkçe](ECOSYSTEM.tr.md) · [Русский](ECOSYSTEM.ru.md) · [Tiếng Việt](ECOSYSTEM.vi.md) · [ไทย](ECOSYSTEM.th.md) · [Deutsch](ECOSYSTEM.de.md) · [Українська](ECOSYSTEM.uk.md) · [Polski](ECOSYSTEM.pl.md) · [العربية](ECOSYSTEM.ar.md) · [فارسی](ECOSYSTEM.fa.md) · [Bahasa Indonesia](ECOSYSTEM.id.md) · [Nederlands](ECOSYSTEM.nl.md) · [हिन्दी](ECOSYSTEM.hi.md) · [Ελληνικά](ECOSYSTEM.el.md)

Il lavoro pratico del profilo vive in un documento a parte: software da scaricare e installare, laboratori di ingegneria, IA applicata e calcolo scientifico, più la descrizione di ogni fork di progetti di terzi presente nell'account.

## 📦 Prodotti Con Distribuzione Reale

Software che si scarica, si installa e si usa — non solo si clona.

| Prodotto | Cos'è | Stack | Consegna |
|---|---|---|---|
| [🔍 **RootCause Windows**](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) | Forense di cybersecurity: ogni distorsione anomala delle risorse può essere il primo indizio di una minaccia. Prima diagnosi, poi intervento | Rust 🦀 · ETW/WPR | **v0.19.0** · **16 release** · **5 edizioni**: GUI · Portable · CLI · PowerShell · VS Code · [landing](https://vladimiracunadev-create.github.io/rootcause-windows-inspector/) |
| [📱 **RootCause Mobile**](https://github.com/vladimiracunadev-create/rootcause-mobile-inspector) | Il fratello mobile: sensore forense che confronta ogni app con se stessa, segnala stalkerware e distingue permessi concessi da quelli solo richiesti | Flutter · Kotlin · Swift | **v0.8.0** · APK Android verificabile · 5 lingue · **telemetria zero** · [landing](https://vladimiracunadev-create.github.io/rootcause-mobile-inspector/) |
| [🍎 **RootCause macOS**](https://github.com/vladimiracunadev-create/rootcause-macos-inspector) | Edizione macOS: persistenza `launchd`, Gatekeeper, SIP, FileVault, XProtect, permessi TCC, processi firmati e vicini di rete — ogni superficie contro uno stato noto buono | Rust 🦀 · macOS 13+ | **v0.1.0** · prima release pubblicata · Apache-2.0 · [landing](https://vladimiracunadev-create.github.io/rootcause-macos-inspector/) |
| [🖥️ **RootCause Server**](https://github.com/vladimiracunadev-create/rootcause-server) | Il fratello server: correla superficie esposta, raffiche di accesso, sessione concessa allo stesso indirizzo, integrità di file critici e silenzio del sensore in una frase azionabile | Rust 🦀 · Windows · Linux · macOS | **v0.2.0** · **18 regole** con evidenza e runbook · non esegue azioni da solo · console locale senza dipendenze web · **ancora senza release pubblicata** · [landing](https://vladimiracunadev-create.github.io/rootcause-server/) |
| [🌐 **RootCause Web**](https://github.com/vladimiracunadev-create/rootcause-web-inspector) | Sensore forense del browser: cookie, sessioni email, estensioni, download, permessi e pagine che simulano una finestra reale | JavaScript · estensione MV3 | **v0.2.0** · ancora senza release pubblicata · pannello su `127.0.0.1` · zero dipendenze · telemetria zero verificata in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-web-inspector/) |
| [₿ **RootCause Bitcoin Defense**](https://github.com/vladimiracunadev-create/rootcause-bitcoin-defense) | Difesa watch-only per custodia Bitcoin: inventaria l'origine di ogni chiave, la incrocia con avvisi pubblicati e spiega la causa radice con evidenza | JavaScript · app Windows · pannello locale | **v0.3.0** · **2 release** · zero dipendenze · non chiede mai seed · verificato in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-bitcoin-defense/) |
| [⛓️ **RootCause Blockchain Security**](https://github.com/vladimiracunadev-create/rootcause-blockchain-security) | Console watch-only multi-chain: inventaria contratti, proxy, oracoli, bridge, governance e dipendenze, e genera runbook di causa radice | JavaScript · app Windows · pannello locale | **v0.3.0** nel repository · release pubblicata: `v0.1.0` · zero dipendenze · non chiede mai chiavi private · verificato in CI · [landing](https://vladimiracunadev-create.github.io/rootcause-blockchain-security/) |
| [📷 **RootCause QR Inspector**](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) | App Android locale per ispezionare QR prima di agire: spiega 26 segnali, separa fatti da ipotesi ed esporta evidenza redatta | Flutter · Dart | **v0.1.4** · **5 release** · **107 test** · APK Android pubblicato · SHA-256 verificabile · firma tecnica del pacchetto APK; firme commerciali/store in corso · telemetria zero · [landing](https://vladimiracunadev-create.github.io/rootcause-qr-inspector/) |
| [🏢 **Empresa Operativa Chile**](https://github.com/vladimiracunadev-create/empresa-operativa-chile) | Accompagna una SpA da prima della nascita alla chiusura mensile: costituzione con evidenza, IVA riportato, bozza F29, chiusura immutabile e audit log. Ogni regola ha fonte ufficiale | JavaScript · Rust · PWA | **v1.5.0** · Android · Windows · browser · **158 test** · **0 dipendenze di produzione** · telemetria zero · [landing](https://vladimiracunadev-create.github.io/empresa-operativa-chile/) |
| [🔍 **Universal Code Scanner**](https://github.com/vladimiracunadev-create/universal-code-scanner) | Lettore QR e barcode che **interpreta prima di agire**: 16 segnali locali di rischio URL e conferma esplicita | Flutter · Dart | **v1.1.0** · Android · iOS · macOS · PWA · cronologia cifrata **AES-256-GCM** · [landing](https://vladimiracunadev-create.github.io/universal-code-scanner/) |
| [🗄️ **GabySQL**](https://github.com/vladimiracunadev-create/gabysql) | Database embedded: file unico `.db`, WAL, ottimizzatore cost-based, API HTTP/JSON | Rust 🦀 | Windows · macOS · Linux · [landing](https://vladimiracunadev-create.github.io/gabysql/) |
| [🤖 **Automa PC**](https://github.com/vladimiracunadev-create/automa-pc) | Orchestratore locale: flow JSON che aprono finestre reali, interagiscono con il DOM e lasciano evidenza | Python · Playwright · pywebview | **v0.3.0** · **27 flow** · installer pubblicato e verificabile · [landing](https://vladimiracunadev-create.github.io/automa-pc/) |
| [🏭 **AI Dataset Foundry**](https://github.com/vladimiracunadev-create/ai-dataset-foundry) | Fabbrica local-first che converte PDF, Word, web, Git, JSON e CSV in dataset auditabili per pretraining, fine-tuning, RAG e valutazione | Python | **v0.2.0** · Windows + Android offline · prima release pubblicata · [landing](https://vladimiracunadev-create.github.io/ai-dataset-foundry/) |
| [☁️ **AWS Desktop Studio**](https://github.com/vladimiracunadev-create/aws-desktop-studio) | App local-first con 15 integrazioni di inventario AWS, 20 tutorial, CLI/SSO e lettura predefinita; implementazione in sviluppo, non accesso universale | JavaScript · Windows | **v0.1.1** · prima release pubblicata · [landing](https://vladimiracunadev-create.github.io/aws-desktop-studio/) |
| [🧭 **Commerce OS**](https://github.com/vladimiracunadev-create/commerce-operating-system) | Demo concettuale guidata di operazioni commerciali: catalogo, stock, CRM, ordini, pagamenti mock e tracciabilità | JavaScript · Web · Windows · Android | **v0.3.0** · **2 release** · senza denaro né SII reale · [landing](https://vladimiracunadev-create.github.io/commerce-operating-system/) |
| [📄 **PDF Reader**](https://github.com/vladimiracunadev-create/pdf-reader-windows-android) | Lettore Android-first locale e read-only, con zoom senza tagli, cronologia riapribile, condivisione WhatsApp e scelta come lettore predefinito | HTML · Web · Android · Windows | **v0.3.3** · APK firmato · zero account, permessi sensibili e telemetria · [landing](https://vladimiracunadev-create.github.io/pdf-reader-windows-android/) |
| [🎙️ **Video Transcript Studio**](https://github.com/vladimiracunadev-create/video-transcript-studio) | Un video, playlist o **canale YouTube completo** in testo con timestamp. Non dipende dai sottotitoli: Whisper riconosce l'audio **sul tuo computer**, senza API, account o chiavi | Python · PySide6 · FastAPI · faster-whisper | **v0.2.0** · desktop Windows + pannello locale `127.0.0.1` + CLI, **con la stessa coda** · MD · PDF · TXT · SRT · VTT · JSON · MP3 · OGG · **89 test** · FFmpeg incluso · telemetria zero · [landing](https://vladimiracunadev-create.github.io/video-transcript-studio/) |
| [🎨 **ChofyAI Studio**](https://github.com/vladimiracunadev-create/chofyai-studio) | Launcher locale di IA creativa: orchestra Qwen3-TTS, whisper.cpp, FaceFusion, AceForge e ComfyUI | Tauri 2 · Rust · React | v0.5.1 · **5/5 strumenti con inferenza reale** · macOS Apple Silicon · Windows sperimentale · **ancora senza release pubblicata** · [sito](https://vladimiracunadev-create.github.io/chofyai-studio/) |
| [🦏 **Rhino Suite**](https://github.com/vladimiracunadev-create/rhino-suite) | Suite office da zero: le regole del documento non dipendono dal DOM — HTML è solo una proiezione | Rust/WASM · Go · React 19 | Monorepo evolutivo per fasi · [landing](https://vladimiracunadev-create.github.io/rhino-suite/) |
| [🎻 **La Mia Avventura con il Violino**](https://github.com/vladimiracunadev-create/violin-adventure) | App educativa per bambini: accordatore cromatico, metronomo esatto sull'orologio audio, canzoni con violino reale | Tauri 2 · React · TS | **v1.3.0** · Windows · Android · Linux · macOS · PWA · [landing](https://vladimiracunadev-create.github.io/violin-adventure/) |
| [🎸 **La Mia Avventura con la Chitarra**](https://github.com/vladimiracunadev-create/guitarra-adventure) | Il fratello a corda pizzicata: 24 lezioni in 6 mondi, accordatore a 6 corde, metronomo senza deriva e 11 note reali di chitarra | Tauri 2 · React · TS | **v1.0.0** · Windows · Android · Linux · macOS · iOS · PWA · senza account, pubblicità o dipendenza online · [landing](https://vladimiracunadev-create.github.io/guitarra-adventure/) |
| [🧣 **Pañuelo al Viento**](https://github.com/vladimiracunadev-create/panuelo-al-viento-cueca-app) | La cueca dai 10 anni: 24 lezioni in 8 livelli, 72 attività, laboratorio di sei pulsazioni (3+3 e 2+2+2) e diagrammi di pavimento accessibili. Dichiara che **completa, non sostituisce**, docenti e cultori | Flutter · Dart | **v0.2.0** · Android 7+ · Windows 10/11 · APK · EXE · MSI · portable · **29 test + 2 validatori** · senza camera, microfono, account, pubblicità o internet · [landing](https://vladimiracunadev-create.github.io/panuelo-al-viento-cueca-app/) |

## 🧪 Laboratori Di Ingegneria

| Repo | Cosa dimostra |
|---|---|
| [🐳 **Problem-Driven Systems Lab**](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) | **20 problemi reali** (latenza sotto carico, N+1, retry storm, leak, monolite, cache stampede, backpressure, migrazione senza downtime, DLQ dimenticata) con guasti ad alta fedeltà, risolti in **7 stack**: PHP 8 · Python · Node.js · Java 21 · .NET 8 · **Go 1.23** · **Rust 1.83** · [landing](https://vladimiracunadev-create.github.io/problem-driven-systems-lab/) |
| [📆 **Social Bot Scheduler**](https://github.com/vladimiracunadev-create/social-bot-scheduler) | **v4.10.0** · **20 casi** sorgente→n8n→ricevitore su **18+ motori DB** —**19 operativi**, auditati uno a uno con Docker— audit a **8 livelli**, guardrail di idempotenza, circuit breaker e DLQ · [landing](https://vladimiracunadev-create.github.io/social-bot-scheduler/) |
| [🧰 **Microsistemas**](https://github.com/vladimiracunadev-create/microsistemas) | **12 microapp** di diagnosi e modernizzazione PHP · server MCP locale read-only · hardening in 3 fasi · [landing](https://vladimiracunadev-create.github.io/microsistemas/) |
| [🧪 **Docker Labs**](https://github.com/vladimiracunadev-create/docker-labs) | **13 lab** su piattaforma a 4 servizi + installer `.exe` automatizzato con launcher · [landing](https://vladimiracunadev-create.github.io/docker-labs/) |
| [🐳 **WSL Labs**](https://github.com/vladimiracunadev-create/wsl-labs) | **12 casi** su `wslc`, motore container nativo WSL — **senza Docker Desktop** · [landing](https://vladimiracunadev-create.github.io/wsl-labs/) |
| [⚡ **Unikernel Labs**](https://github.com/vladimiracunadev-create/unikernel-labs) | “Docker Desktop per unikernel”: controllo Windows su Unikraft con backend WSL2, `kraft` + QEMU/KVM · [landing](https://vladimiracunadev-create.github.io/unikernel-labs/) |
| [🧰 **QEMU/KVM Labs**](https://github.com/vladimiracunadev-create/qemu-kvm-labs) | **12 lab** di virtualizzazione reale con QEMU, KVM, libvirt, cloud-init e `vm-manager` su Linux e WSL2 · [landing](https://vladimiracunadev-create.github.io/qemu-kvm-labs/) |
| [🛡️ **Sandbox Labs**](https://github.com/vladimiracunadev-create/sandbox-labs) | Isolamento Linux: esegue codice, file e modelli business di terzi sotto policy dichiarate e **produce evidenza firmata dei controlli applicati davvero** · **36 casi** in due famiglie —15 tecnici e 21 capital market— · sperimentale ed educativo, *non un prodotto di sicurezza* · [landing](https://vladimiracunadev-create.github.io/sandbox-labs/) |
| [💳 **Universal Payments Engineering Lab**](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) | **28 famiglie** di pagamenti in una demo locale autoesplicativa: stati, ledger, riconciliazione, sicurezza e guide implementative · [landing](https://vladimiracunadev-create.github.io/universal-payments-engineering-lab/) |
| [🕹️ **Decentraland Social Arcade**](https://github.com/vladimiracunadev-create/decentraland-social-arcade) | Esperienza 3D sociale nativa Decentraland: un MVP e architettura multigioco con SDK7, ECS e TypeScript · documentazione in spagnolo · senza pagamenti né telemetria |
| [☁️ **Progetti AWS**](https://github.com/vladimiracunadev-create/proyectos-aws) | Casi progressivi dove ciascuno aggiunge un servizio AWS **e** una nuova capacità GitHub Actions · copertura SAA-C03 · DVA-C02 · SOA-C02 |

## 🤖 IA Applicata

| Repo | Cosa dimostra |
|---|---|
| [🤖 **LangGraph RealWorld**](https://github.com/vladimiracunadev-create/langgraph-realworld) | **25/25 backend operativi** — stato tipizzato, rotte condizionali, streaming NDJSON, modalità DEMO/LIVE, 8 livelli di sicurezza, chain of custody SHA-256 |
| [🧭 **Operational AI Agents**](https://github.com/vladimiracunadev-create/operational-ai-agents) | **13 agenti operativi** per Claude Code e runtime compatibili: missioni complete per evoluzione repo, modernizzazione legacy, design curricolare, portfolio, sicurezza e incidenti · **39 eval deterministici** · 34 test · zero-deps · Linux · macOS · Windows · [sito](https://vladimiracunadev-create.github.io/operational-ai-agents/) |
| [🧠 **MCP + Ollama Local**](https://github.com/vladimiracunadev-create/mcp-ollama-local) | IA local-first con tool MCP in sandbox · bind `127.0.0.1` · profilo di fiducia multilivello · onesto sui limiti |
| [🧩 **Agentic Plugins Toolkit**](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) | **6 plugin agentic** installabili in Claude Code, OpenAI/Codex, Copilot, Gemini e MCP da una fonte unica · **69 viste generate senza drift** · zero-deps · Linux · macOS · Windows · [sito](https://vladimiracunadev-create.github.io/agentic-plugins-toolkit/) |
| [🧰 **Claude Skills Toolkit**](https://github.com/vladimiracunadev-create/claude-skills-toolkit) | **15 skill agentic** per Claude Code · sicurezza, custodia Bitcoin, gate repo, coerenza, Docker e documentazione · zero-deps · multipiattaforma |
| [🧰 **Codex Skills Toolkit**](https://github.com/vladimiracunadev-create/codex-skills-toolkit) | **19 skill agentic** per Codex: sicurezza e supply chain, preflight, flussi funzionali, resilienza e stato, evidenza di release, gate Python/YAML/Markdown, versioni, dipendenze, Docker e documenti · Python-first · `pnpm` · Linux · macOS · Windows · [sito](https://vladimiracunadev-create.github.io/codex-skills-toolkit/) |

<a id="curricula"></a>

## 📚 Curricula Tecnici Completi

Programmi sequenziali in spagnolo, con stato e ambito dichiarati da ogni repository. I 21 programmi sommano **14.530 classi**, contate da [un workflow](../.github/workflows/stats.yml) sulla struttura reale o su una fonte verificabile dichiarata nel repository; il badge viene aggiornato ogni settimana e non è scritto a mano.

🧭 [**Lifelong Learning Ecosystem**](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem) è una bussola federata che collega 30 percorsi reali in 6 aree tramite mappe visuali e un [portale offline accessibile](https://vladimiracunadev-create.github.io/lifelong-learning-ecosystem/), senza essere contato come programma aggiuntivo.

| Programma | Classi | Ambito |
|---|---:|---|
| [🔢 **Matematica Computazionale**](https://github.com/vladimiracunadev-create/computational-mathematics-program) | 360 | Dal contare con le dita a riprodurre un paper · **360 dimostrazioni deterministiche verificate in CI** · 1.080 notebook · glossario di 489 termini · [sito](https://vladimiracunadev-create.github.io/computational-mathematics-program/) |
| [🏦 **Finanza e Banca**](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program) | 356 | 534 h · matematica finanziaria e IFRS → credito, rischio, Basilea III, open finance, DLT, stablecoin e MiCA · **27 casi** · **298 test** · [sito](https://vladimiracunadev-create.github.io/finance-and-banking-evolution-program/) |
| [🎮 **GameDev**](https://github.com/vladimiracunadev-create/modern-gamedev-program) | 352 | Matematica e C#/C++/GDScript → shader, IA, multiplayer, VR/AR · Godot · Unity · Unreal · **10 lab Godot verificati in CI** · [sito](https://vladimiracunadev-create.github.io/modern-gamedev-program/) |
| [🛡️ **Cybersecurity**](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) | 360 | **v1.3.0** · 20 parti · fondamenti → Red Team, DFIR, cloud security, exploit dev, CTF e game security · mappato a **7 certificazioni** · app offline Android/web · manuale PDF · [sito](https://vladimiracunadev-create.github.io/modern-cybersecurity-program/) |
| [📈 **Marketing, Vendite e Crescita**](https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program) | 336 | 24 parti con definizioni operative, schede di misurazione, bibliografia verificabile e contesto normativo cileno · **v1.6.0** · 1,29 M parole · 17 percorsi per ruolo · [sito](https://vladimiracunadev-create.github.io/marketing-sales-growth-evolution-program/) |
| [🏢 **Creazione d'Impresa**](https://github.com/vladimiracunadev-create/modern-business-creation-program) | 336 | Creare e operare un'impresa reale in Cile: idea, costituzione, SII, operazione, crisi e uscita · 360 diagrammi · glossario di 1.251 termini · manuale di 1.548 pagine · [sito](https://vladimiracunadev-create.github.io/modern-business-creation-program/) |
| [🏛️ **Architettura e Ambiente Costruito**](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program) | 830 | 83 parti · 60 sessioni integrative · 34 percorsi · fonti tracciabili · Markdown, lettore offline e GitHub Pages · [sito](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/) |
| [🇨🇱 **Percorso Scolastico Cileno**](https://github.com/vladimiracunadev-create/chilean-school-learning-path) | 8.841 | Dalla 1ª primaria alla 4ª superiore cilena · **4.156 esperienze trasversali integrate** · **2.823 obiettivi di apprendimento** · fonti MINEDUC · nessuna proposta in sospeso e revisione umana specializzata ancora necessaria · [sito](https://vladimiracunadev-create.github.io/chilean-school-learning-path/) |
| [🧭 **Ingegneria del software moderna**](https://github.com/vladimiracunadev-create/modern-software-engineering-program) | 480 | 40 parti e 8 fasi · fondamenti → prodotto, architettura, sicurezza, DevOps, SRE, SPEC, IA e sistemi multi-agente · stato editoriale dichiarato dal repository · [sito](https://vladimiracunadev-create.github.io/modern-software-engineering-program/) |
| [🎓 **Pedagogia e Scienze dell'Apprendimento**](https://github.com/vladimiracunadev-create/education-pedagogy-learning-sciences-program) | 300 | Come una persona impara e come si forma chi insegna · 25 parti · **ogni classe dichiara evidenza e limiti** · alfabetizzazione, metodologie comparate, bisogni educativi, convivenza, diversità culturale · glossario di 1.097 termini · 14 percorsi · **v2.1.0** · [sito](https://vladimiracunadev-create.github.io/education-pedagogy-learning-sciences-program/) |
| [☁️ **Multi-Cloud**](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) | 288 | AWS · Azure · GCP · Kubernetes · Terraform · SRE · FinOps · **1.288 ore** · 288 lab con evidenza JSON · 1.032 fonti · manuale PDF di 2.884 pagine · [sito](https://vladimiracunadev-create.github.io/multi-cloud-engineering-program/) |
| [🎖️ **Leadership Esecutiva**](https://github.com/vladimiracunadev-create/executive-leadership-founder-program) | 288 | Dal primo risultato alla direzione di un'azienda e alla fondazione della propria: team, KPI/OKR, finanza, prodotto, rischio, board e M&A · [sito](https://vladimiracunadev-create.github.io/executive-leadership-founder-program/) |
| [🐍 **Python Data Science**](https://github.com/vladimiracunadev-create/python-data-science-program) | 232 | Polars, ML+Optuna/SHAP, PyTorch/LLMs/LoRA, MLOps · app Windows nativa + APK Android · [sito](https://vladimiracunadev-create.github.io/python-data-science-program/) |
| [🧠 **Evoluzione dell'IA**](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program) | 184 | Simbolica → probabilistica → deep learning → LLM, RAG, agenti, sicurezza e frontiera · **v0.17.0** · **708 notebook** · 148 paper fondamentali · app offline Windows, Android e PWA · [sito](https://vladimiracunadev-create.github.io/artificial-intelligence-evolution-program/) |
| [🌐 **Programmazione Comparata**](https://github.com/vladimiracunadev-create/polyglot-programming-labs) | 176 | Un concetto, **10 linguaggi** verificati in CI — **1.360 implementazioni** — più **1.632 programmi** in linguaggi ancora vivi e atlas di **60 schede in 15 famiglie** · [sito](https://vladimiracunadev-create.github.io/polyglot-programming-labs/) |
| [🧩 **Framework Comparati**](https://github.com/vladimiracunadev-create/framework-ecosystems-labs) | 149 | Un contratto eseguibile contro Express, FastAPI, Spring Boot, ASP.NET, Django, Rails, Laravel, React, Vue, Svelte e altri · **70 classi costruite** · **397 casi verificati in CI** · **210 fonti** ISBN/DOI · [sito](https://vladimiracunadev-create.github.io/framework-ecosystems-labs/) |
| [🗄️ **Database**](https://github.com/vladimiracunadev-create/database-systems-labs) | 74 | **v3.0.0** · ingegneria database in 15 parti · 230 ore · 120 fonti con ISBN, DOI o standard · stesso caso in 27 motori · 150 pytest · [sito](https://vladimiracunadev-create.github.io/database-systems-labs/) |
| [📐 **Psicometria e Misurazione**](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program) | 40 | Come si costruisce, valuta, valida e audita uno strumento di misurazione · 8 parti · motore eseguibile con **5 strumenti e 344 item, 276 di pubblico dominio** |
| [⛓️ **Blockchain**](https://github.com/vladimiracunadev-create/blockchain-learning-path) | 66 | **v0.14.0** · da zero a infrastruttura finanziaria programmabile e analitica on-chain · **91 pratiche** e **363 test** · Foundry e Slither in CI · [sito](https://vladimiracunadev-create.github.io/blockchain-learning-path/) |
| [🧠 **Neural Network Training Labs**](https://github.com/vladimiracunadev-create/neural-network-training-labs) | 31 | 7 moduli · ≈214 ore · **93 notebook** —31 classi, 31 versioni studente e 31 soluzioni— · PyTorch · [sito di studio](https://vladimiracunadev-create.github.io/neural-network-training-labs/) |
| [🕹️ **Machine Operator**](https://github.com/vladimiracunadev-create/machine-operator-program) | 451 | **41 moduli formativi**, uno per macchina · **502 h 15 min** · sistemi, comandi, fisica, sicurezza e design di simulazione con fonti per classe · *nessun simulatore eseguibile ancora, e viene dichiarato* |

## 🔬 Calcolo Scientifico

| Repo | Cosa dimostra |
|---|---|
| [🧬 **Human Genome Labs**](https://github.com/vladimiracunadev-create/human-genome-labs) | Piattaforma riproducibile di genomica: contratti tipizzati `ScientificResult<T>`, FASTA/GFF3/VCF, moduli con **maturità ed evidenza esplicite**. Onestà radicale: *non effettua diagnosi clinica* · [sito](https://vladimiracunadev-create.github.io/human-genome-labs/) |

<a id="forks"></a>

## 🍴 Fork di progetti di terzi (52)

Sono fork di progetti altrui conservati in questo account. **Non sono opera propria**: il merito spetta agli autori originali, non rientrano in alcun numero di questo profilo e ogni descrizione riassume ciò che dichiara il progetto originale, senza implicare supporto, audit né esperienza produttiva propria. Descrizioni secondo il progetto originale · 2026-11-09.

### 🤖 Agenti di codice e framework per agenti (18)

| Fork | Progetto originale | Linguaggio | Che cos'è |
|---|---|---|---|
| [**OpenHands**](https://github.com/vladimiracunadev-create/OpenHands) | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | TypeScript | Piattaforma di agenti per lo sviluppo software guidato dall'IA |
| [**cline**](https://github.com/vladimiracunadev-create/cline) | [cline/cline](https://github.com/cline/cline) | TypeScript | Agente di codice autonomo come SDK, estensione IDE o CLI |
| [**opencode**](https://github.com/vladimiracunadev-create/opencode) | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | Agente di codice open source |
| [**qwen-code**](https://github.com/vladimiracunadev-create/qwen-code) | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | TypeScript | Agente di codice con IA open source per il terminale |
| [**goose**](https://github.com/vladimiracunadev-create/goose) | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Rust | Agente estensibile che installa, esegue, modifica e testa codice con qualsiasi LLM |
| [**pi**](https://github.com/vladimiracunadev-create/pi) | [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | Toolkit per agenti: API LLM unificata, ciclo dell'agente, TUI e CLI di codice |
| [**hermes-agent**](https://github.com/vladimiracunadev-create/hermes-agent) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | L'agente che cresce con te (NousResearch) |
| [**deepagents**](https://github.com/vladimiracunadev-create/deepagents) | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Python | Harness per agenti «batterie incluse» (LangChain) |
| [**crewAI**](https://github.com/vladimiracunadev-create/crewAI) | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | Framework per orchestrare agenti autonomi con ruoli |
| [**agent-framework**](https://github.com/vladimiracunadev-create/agent-framework) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Python | Framework Microsoft per creare e distribuire agenti e flussi multi-agente in Python e .NET |
| [**deepseek-harness**](https://github.com/vladimiracunadev-create/deepseek-harness) | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | TypeScript | Harness per agenti di DeepSeek in cui tutto è un plugin |
| [**agent-orchestrator**](https://github.com/vladimiracunadev-create/agent-orchestrator) | [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Go | Pianifica, esegue e supervisiona flotte di agenti, dal task alla PR unita |
| [**orca**](https://github.com/vladimiracunadev-create/orca) | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | Spazio di lavoro per una flotta di agenti di codice (desktop, mobile e remoto) |
| [**kander**](https://github.com/vladimiracunadev-create/kander) | [dualface/kander](https://github.com/dualface/kander) | Go | Kanban che coordina agenti di codice con git worktree isolati e agenti revisori |
| [**OpenBot**](https://github.com/vladimiracunadev-create/OpenBot) | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | TypeScript | Colleghi IA, ciascuno con il proprio computer; ogni azione è decisa prima e registrata dopo |
| [**browser-use**](https://github.com/vladimiracunadev-create/browser-use) | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | Libreria Python per agenti IA che usano il browser |
| [**agent-desktop**](https://github.com/vladimiracunadev-create/agent-desktop) | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Rust | CLI di computer use per agenti IA |
| [**treg**](https://github.com/vladimiracunadev-create/treg) | [superdesigndev/treg](https://github.com/superdesigndev/treg) | Python | «OpenRouter per gli strumenti degli agenti» |

### 🧩 Skill, plugin e flussi per agenti (11)

| Fork | Progetto originale | Linguaggio | Che cos'è |
|---|---|---|---|
| [**claude-plugins-official**](https://github.com/vladimiracunadev-create/claude-plugins-official) | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | Directory ufficiale, gestita da Anthropic, di plugin di qualità per Claude Code |
| [**agentic-awesome-skills**](https://github.com/vladimiracunadev-create/agentic-awesome-skills) | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | Python | Piano di controllo locale per scoprire, scegliere e validare un vasto catalogo di skill agentic (CLI, MCP locale, plugin) |
| [**claude-review-all**](https://github.com/vladimiracunadev-create/claude-review-all) | [ncoevoet/claude-review-all](https://github.com/ncoevoet/claude-review-all) | Python | Revisione del codice multi-agente per Claude Code |
| [**blender-skills**](https://github.com/vladimiracunadev-create/blender-skills) | [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | TypeScript | Skill specialistiche per Blender per agenti di codice, con pipeline basata su MCP |
| [**diagram-design**](https://github.com/vladimiracunadev-create/diagram-design) | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | Progettazione editoriale di diagrammi (HTML + SVG) per agenti di codice |
| [**elephant-goldfish-model**](https://github.com/vladimiracunadev-create/elephant-goldfish-model) | [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) | Python | Skill aperte di Google per progettare e rivedere software con agenti IA |
| [**Claude-Code-Game-Studios**](https://github.com/vladimiracunadev-create/Claude-Code-Game-Studios) | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | Trasforma Claude Code in uno studio di videogiochi di agenti coordinati |
| [**headcount**](https://github.com/vladimiracunadev-create/headcount) | [cbrock84/headcount](https://github.com/cbrock84/headcount) | Markdown | Organizzazione di agenti strutturata come un'azienda: reparti e skill installabili |
| [**agentic-qe**](https://github.com/vladimiracunadev-create/agentic-qe) | [proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) | TypeScript | Piattaforma aperta di QA/QE con agenti e skill per l'intero ciclo di vita del software |
| [**OpenExecutive**](https://github.com/vladimiracunadev-create/OpenExecutive) | [SenteLabsAI/OpenExecutive](https://github.com/SenteLabsAI/OpenExecutive) | Python | Team esecutivo virtuale: una figura dirigente sostenuta da 8 agenti Claude specialisti |
| [**n8n-mcp**](https://github.com/vladimiracunadev-create/n8n-mcp) | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | TypeScript | Server MCP per far costruire flussi n8n a Claude, Cursor o Windsurf |

### 🛡️ Sicurezza e analisi del software (8)

| Fork | Progetto originale | Linguaggio | Che cos'è |
|---|---|---|---|
| [**raptor**](https://github.com/vladimiracunadev-create/raptor) | [gadievron/raptor](https://github.com/gadievron/raptor) | Python | Trasforma Claude Code in un agente di sicurezza offensiva e difensiva |
| [**Cybersecurity-Projects**](https://github.com/vladimiracunadev-create/Cybersecurity-Projects) | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | Go | 70 progetti di cybersecurity, da principiante ad avanzato |
| [**SkillSpector**](https://github.com/vladimiracunadev-create/SkillSpector) | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Python | Scanner di sicurezza NVIDIA per skill di agenti (prompt injection, esfiltrazione, supply chain) |
| [**Anthropic-Cybersecurity-Skills**](https://github.com/vladimiracunadev-create/Anthropic-Cybersecurity-Skills) | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | Centinaia di skill di cybersecurity per agenti, mappate su MITRE ATT&CK, NIST CSF e altri framework |
| [**security-audit-skill**](https://github.com/vladimiracunadev-create/security-audit-skill) | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | Skill di Cloudflare per audit di sicurezza multifase con risultati verificati in modo indipendente |
| [**siteone-crawler**](https://github.com/vladimiracunadev-create/siteone-crawler) | [janreges/siteone-crawler](https://github.com/janreges/siteone-crawler) | Rust | Crawler e analizzatore di siti web per SEO, sicurezza, accessibilità e prestazioni |
| [**rea**](https://github.com/vladimiracunadev-create/rea) | [morluto/rea](https://github.com/morluto/rea) | TypeScript | Reverse engineering con agenti, dal comportamento di un'app ai binari nativi |
| [**craft-anything**](https://github.com/vladimiracunadev-create/craft-anything) | [storytold/craft-anything](https://github.com/storytold/craft-anything) | Rust | Capire come funziona qualsiasi software e costruire il proprio |

### 🧠 Modelli di IA e infrastruttura (5)

| Fork | Progetto originale | Linguaggio | Che cos'è |
|---|---|---|---|
| [**marin**](https://github.com/vladimiracunadev-create/marin) | [marin-community/marin](https://github.com/marin-community/marin) | Python | Framework aperto per la ricerca e lo sviluppo di modelli di base |
| [**prime-rl**](https://github.com/vladimiracunadev-create/prime-rl) | [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) | Python | Addestramento per rinforzo agentico su larga scala |
| [**Olmo-core**](https://github.com/vladimiracunadev-create/Olmo-core) | [allenai/Olmo-core](https://github.com/allenai/Olmo-core) | Python | Blocchi costruttivi PyTorch per l'ecosistema OLMo |
| [**DeepInfer**](https://github.com/vladimiracunadev-create/DeepInfer) | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | Python | Framework di inferenza ad alte prestazioni e su larga scala per i modelli DeepSeek |
| [**heretic**](https://github.com/vladimiracunadev-create/heretic) | [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | Modifica di modelli linguistici senza riaddestramento (censura, piaggeria, ecc.) |

### 🏢 Gestione aziendale e piattaforme (6)

| Fork | Progetto originale | Linguaggio | Che cos'è |
|---|---|---|---|
| [**erpnext**](https://github.com/vladimiracunadev-create/erpnext) | [frappe/erpnext](https://github.com/frappe/erpnext) | Python | ERP libero e open source |
| [**odoo**](https://github.com/vladimiracunadev-create/odoo) | [odoo/odoo](https://github.com/odoo/odoo) | Python | App aziendali open source |
| [**mautic**](https://github.com/vladimiracunadev-create/mautic) | [mautic/mautic](https://github.com/mautic/mautic) | PHP | Marketing automation open source |
| [**crm**](https://github.com/vladimiracunadev-create/crm) | [trycompai/crm](https://github.com/trycompai/crm) | TypeScript | CRM open source pensato per gli agenti IA (Comp AI) |
| [**harness**](https://github.com/vladimiracunadev-create/harness) | [harness/harness](https://github.com/harness/harness) | Go | Piattaforma di sviluppo completa: controllo del codice, CI/CD, ambienti e registri di artefatti |
| [**traccar**](https://github.com/vladimiracunadev-create/traccar) | [traccar/traccar](https://github.com/traccar/traccar) | Java | Piattaforma di tracciamento GPS open source, oltre 200 protocolli di dispositivi |

### 🎓 Formazione e riferimento (4)

| Fork | Progetto originale | Linguaggio | Che cos'è |
|---|---|---|---|
| [**computer-science**](https://github.com/vladimiracunadev-create/computer-science) | [ossu/computer-science](https://github.com/ossu/computer-science) | HTML | Percorso gratuito di autoapprendimento in Informatica (OSSU) |
| [**math**](https://github.com/vladimiracunadev-create/math) | [ossu/math](https://github.com/ossu/math) | — | Percorso gratuito di autoapprendimento in Matematica (OSSU) |
| [**manim**](https://github.com/vladimiracunadev-create/manim) | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Python | Framework Python della community per animazioni matematiche |
| [**asm-atari-2600**](https://github.com/vladimiracunadev-create/asm-atari-2600) | [johnidm/asm-atari-2600](https://github.com/johnidm/asm-atari-2600) | Assembly | Codice sorgente di esempio di giochi per Atari 2600 in assembly |
