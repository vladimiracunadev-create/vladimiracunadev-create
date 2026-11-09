# 🗂️ Ekosistem: produk, laboratorium, AI terapan, dan komputasi ilmiah

[← Kembali ke profil](../README.id.md)

**🌐** [Español](ECOSYSTEM.md) · [English](ECOSYSTEM.en.md) · [Português](ECOSYSTEM.pt.md) · [Italiano](ECOSYSTEM.it.md) · [Français](ECOSYSTEM.fr.md) · [简体中文](ECOSYSTEM.zh.md) · [繁體中文](ECOSYSTEM.zh-TW.md) · [日本語](ECOSYSTEM.ja.md) · [한국어](ECOSYSTEM.ko.md) · [Türkçe](ECOSYSTEM.tr.md) · [Русский](ECOSYSTEM.ru.md) · [Tiếng Việt](ECOSYSTEM.vi.md) · [ไทย](ECOSYSTEM.th.md) · [Deutsch](ECOSYSTEM.de.md) · [Українська](ECOSYSTEM.uk.md) · [Polski](ECOSYSTEM.pl.md) · [العربية](ECOSYSTEM.ar.md) · [فارسی](ECOSYSTEM.fa.md) · **Bahasa Indonesia** · [Nederlands](ECOSYSTEM.nl.md) · [हिन्दी](ECOSYSTEM.hi.md) · [Ελληνικά](ECOSYSTEM.el.md)

Karya praktis profil ini ada di dokumen tersendiri: perangkat lunak yang diunduh dan dipasang, laboratorium rekayasa, AI terapan, dan komputasi ilmiah, beserta deskripsi setiap fork proyek pihak ketiga yang ada di akun.

## 📦Produk Dengan Distribusi Nyata

Perangkat lunak yang diunduh, terpasang, dan dipakai - tidak hanya dikloning.

| Produk | Apa itu | Stack | Pengiriman |
|---|---|---|---|
| [🔍 **RootCause Windows**](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) | Forensik Cybersecurity: setiap distorsi sumber daya yang aneh mungkin merupakan tanda pertama dari ancaman. Diagnoose first, intervents later | Rust🦀 ·ETW / WPR | **v0.19.0** · **16 rilis** · **5 edisi**GUI·Portabel·CLI·Shell PowerShell·Kode VS· [landing](https://vladimiracunadev-create.github.io/rootcause-windows-inspector/) |
| [📱 **RootCause Mobile**](https://github.com/vladimiracunadev-create/rootcause-mobile-inspector) | Saudara-saudara seluler: sebuah sensor forensik yang membandingkan setiap aplikasi terhadap dirinya sendiri, flag stalkerware, dan memisahkan hak pemberian dari yang hanya diminta | Flutter·Kotlin·Swift | **v0.8.0** ·Android APK dapat diverifikasi·5 bahasa· **nol telemetri** · [landing](https://vladimiracunadev-create.github.io/rootcause-mobile-inspector/) |
| [🍎 **RootCause macOS**](https://github.com/vladimiracunadev-create/rootcause-macos-inspector) | Edisi macOS:`launchd`Kegigihan, Gatekeeper, SIP, FileVault, XProtection, TCC permission, signed process, dan jaringan tetangga - setiap permukaan diperiksa terhadap negara-negara yang baik | Rust🦀 ·MaOS 13 + | **v0.1,0** ·rilis pertama yang diterbitkan·Apache -2.0· [landing](https://vladimiracunadev-create.github.io/rootcause-macos-inspector/) |
| [🖥️ **RootCause Server**](https://github.com/vladimiracunadev-create/rootcause-server) | Sibling server: menghubungkan apa yang tidak ada log melihat bersama - permukaan yang terkena, percobaan meledak, sesi yang diberikan ke alamat yang sama, integritas file kritis, dan sensor diam - dan mengubahnya menjadi satu kalimat yang dapat ditindaklanjuti | Rust🦀 ·Jendela·Linux·Mapos | **v0.2.0** · **18 aturan**dengan bukti dan buku panduan·tidak pernah mengeksekusi aksi sendiri·konsol lokal tanpa ketergantungan web· **belum ada rilis yang diterbitkan** · [landing](https://vladimiracunadev-create.github.io/rootcause-server/) |
| [🌐 **RootCause Web**](https://github.com/vladimiracunadev-create/rootcause-web-inspector) | Sensor forensik peramban: cookie, sesi email, ekstensi, pengunduhan, izin, dan halaman yang meniru jendela yang nyata | JavaScript·Ekstensi MV3 | **v0.2.0** ·belum ada rilis yang diterbitkan·panel hidup`127.0.0.1` ·ketergantungan nol·nol telemetri diverifikasi dalam CI· [landing](https://vladimiracunadev-create.github.io/rootcause-web-inspector/) |
| [₿ **RootCause Bitcoin Defense**](https://github.com/vladimiracunadev-create/rootcause-bitcoin-defense) | Pengawasan hanya untuk hak asuh Bitcoin: menginventori asal dari setiap kunci, lintas-memeriksa dengan peringatan yang diterbitkan, dan menjelaskan akar menyebabkan dengan bukti | JavaScript·Aplikasi Windows·panel lokal | **v0.3.0** · **2 rilis** ·ketergantungan nol·tidak pernah meminta benih·Diverifikasi dalam CI· [landing](https://vladimiracunadev-create.github.io/rootcause-bitcoin-defense/) |
| [⛓️ **RootCause Blockchain Security**](https://github.com/vladimiracunadev-create/rootcause-blockchain-security) | Jam rantai ganda - hanya konsol: inventory kontrak, proksi, oracles, jembatan, pemerintahan, dan ketergantungan, dan menghasilkan root - menyebabkan runbooks | JavaScript·Aplikasi Windows·panel lokal | **v0.3.0**dalam repositori·rilis diterbitkan:`v0.1.0` ·ketergantungan nol·tidak pernah meminta kunci privat·Diverifikasi dalam CI· [landing](https://vladimiracunadev-create.github.io/rootcause-blockchain-security/) |
| [📷 **RootCause QR Inspector**](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) | Aplikasi Android Lokal untuk memeriksa kode QR sebelum bertindak: menjelaskan 26 sinyal, memisahkan fakta dari hipotesis, dan ekspor bukti yang dihapus | Flutter·Dart | **v0.1,4** · **5 rilis** · **107 tes** ·published Android APK·diverifikasi SHA- 256·tanda tangan paket APK teknis; signature komersial / store sedang berlangsung·nol telemetri· [landing](https://vladimiracunadev-create.github.io/rootcause-qr-inspector/) |
| [🏢 **Empresa Operativa Chile**](https://github.com/vladimiracunadev-create/empresa-operativa-chile) | Memimpin SPA dari sebelum memasukkan ke setiap penutupan bulanan: memasukkan barang bukti, VAT carry- maju, F29 draft, dekat, dan audit log. Setiap peraturan menunjuk ke sumber resminya. | JavaScript·Rust·PWA | **v1.5,0** ·Android·Jendela·peramban· **158 tests** · **Ketergantungan produksi 0** ·nol telemetri· [landing](https://vladimiracunadev-create.github.io/empresa-operativa-chile/) |
| [🔍 **Universal Code Scanner**](https://github.com/vladimiracunadev-create/universal-code-scanner) | Pembaca QR dan Barcode yang**Meninterpretasikan sebelum bertindak**: 16 sinyal risiko URL lokal dan konfirmasi eksplisit | Flutter·Dart | **v1.0** ·Android·iOS·Mapos·PWA·riwayat terenkripsi**AES- 256- GCM** · [landing](https://vladimiracunadev-create.github.io/universal-code-scanner/) |
| [🗄️ **GabySQL**](https://github.com/vladimiracunadev-create/gabysql) | Basis data yang terbenamb: tunggal`.db`berkas, WAL, optimizer berbasis kost, HTTP / JSON API | Rust🦀 | Jendela·Mapos·Linux· [landing](https://vladimiracunadev-create.github.io/gabysql/) |
| [🤖 **Automa PC**](https://github.com/vladimiracunadev-create/automa-pc) | Organisasi lokal: JSON mengalir jendela asli yang terbuka, berinteraksi dengan DOM, dan meninggalkan bukti | Python·Dramawan·pywebview | **v0.3.0** · **27 arus** ·pemasang yang dapat diterbitkan dan diverifikasi· [landing](https://vladimiracunadev-create.github.io/automa-pc/) |
| [🏭 **AI Dataset Foundry**](https://github.com/vladimiracunadev-create/ai-dataset-foundry) | Pabrik pertama yang mengubah PDF, Word, Web, Git, JSON, dan CSV menjadi data yang dapat diaudit untuk pretraining, fine- tuning, RAG, dan evaluasi | Python | **v0.2.0** ·Windows + offline Android·rilis pertama yang diterbitkan· [landing](https://vladimiracunadev-create.github.io/ai-dataset-foundry/) |
| [☁️ **AWS Desktop Studio**](https://github.com/vladimiracunadev-create/aws-desktop-studio) | Aplikasi pertama locall- dengan 15% inventaris AWS, 20 tutorial, CLI / SSO, dan baca-saja baku; implementasi dalam proses, bukan akses universal | JavaScript·Jendela | **v0.1,1** ·rilis pertama yang diterbitkan· [landing](https://vladimiracunadev-create.github.io/aws-desktop-studio/) |
| [🧭 **Commerce OS**](https://github.com/vladimiracunadev-create/commerce-operating-system) | Demo konseptual guided dari operasi komersial: katalog, saham, CRM, perintah, pembayaran mock, dan traceabilitas | JavaScript·Web·Jendela·Android | **v0.3.0** · **2 rilis** ·tidak ada uang asli atau otoritas pajak Chilean integrasi· [landing](https://vladimiracunadev-create.github.io/commerce-operating-system/) |
| [📄 **PDF Reader**](https://github.com/vladimiracunadev-create/pdf-reader-windows-android) | Android--pertama pembaca lokal hanya-baca, dengan zum tidak-crop, reopenable sejarah, WhatsApp sharing, dan pilihan pembaca-default | HTML·Web·Android·Jendela | **v0.3.3** ·APK ditandatangani·tidak ada akun, izin sensitif, atau telemetri· [landing](https://vladimiracunadev-create.github.io/pdf-reader-windows-android/) |
| [🎙️ **Video Transcript Studio**](https://github.com/vladimiracunadev-create/video-transcript-studio) | Satu video, daftar putar, atau**seluruh kanal YouTube**untuk teks dengan penanda waktu. Ini tidak bergantung pada subtitel yang ada: Berbisik mengenali audio**di mesin Anda**, tanpa API, akun, atau kunci untuk mengkonfigurasi | Python·PySide6·FastAPI·Lebih cepat... Bisikan... | **v0.2.0** ·Desktop Windows + panel lokal hidup`127.0.0.1`+ CLI,**berbagi antrian yang sama** ·MD·PDF·TXT·SRT·VTT·JSON·MP3·OGG· **89 tes** ·bundled FFmpeg·nol telemetri· [landing](https://vladimiracunadev-create.github.io/video-transcript-studio/) |
| [🎨 **ChofyAI Studio**](https://github.com/vladimiracunadev-create/chofyai-studio) | Peluncur AI kreatif lokal: mendalangi Qwen3-TTS, bisikan-bisikan, FaceFasi, AceForge, dan ComfyUI | Tauri 2·Rust·Bereaksi | v0.5.1· **5 / 5 alat dengan inferensi nyata** ·Silikon MakOS Apple·Windows Eksperimen· **belum ada rilis yang diterbitkan** · [site](https://vladimiracunadev-create.github.io/chofyai-studio/) |
| [🦏 **Rhino Suite**](https://github.com/vladimiracunadev-create/rhino-suite) | Suite kantor dari awal: aturan dokumen tidak bergantung pada DOM - HTML hanya sebuah proyeksi | Rust / WASM·Pergi·Bereaksi 19 | Evolusi monorepo oleh fase· [landing](https://vladimiracunadev-create.github.io/rhino-suite/) |
| [🎻 **My Violin Adventure**](https://github.com/vladimiracunadev-create/violin-adventure) | Aplikasi pendidikan untuk anak-anak: tuner kromatik, audio-jam - akurat metronome, lagu-lagu dengan biola nyata | Tauri 2·Bereaksi·TS | **v1.3.0** ·Jendela·Android·Linux·Mapos·PWA· [landing](https://vladimiracunadev-create.github.io/violin-adventure/) |
| [🎸 **My Guitar Adventure**](https://github.com/vladimiracunadev-create/guitarra-adventure) | Saudara-string yang diplucked-: 24 pelajaran di 6 dunia, 6-string tuner, drift- gratis metronome, dan 11 catatan gitar nyata | Tauri 2·Bereaksi·TS | **v1.0.0** ·Jendela·Android·Linux·Mapos·iOS·PWA·tidak ada akun, iklan, atau ketergantungan online· [landing](https://vladimiracunadev-create.github.io/guitarra-adventure/) |
| [🧣 **Pañuelo al Viento**](https://github.com/vladimiracunadev-create/panuelo-al-viento-cueca-app) | Cueca dari usia 10: 24 kelas dalam 8 tingkat, 72 aktivitas, lab enam pulse (3 + 3 dan 2 + 2 + 2), dan diagram lantai yang dapat diakses. Ini menyatakan bahwa itu**pelengkap, tidak menggantikan**, guru dan pembawa budaya | Flutter·Dart | **v0.2.0** ·Android 7 +·Windows 10 / 11·APK·EXE·MSI·portabel· **29 tes + 2 validators** ·tidak ada kamera, mikrofon, akun, iklan, atau internet· [landing](https://vladimiracunadev-create.github.io/panuelo-al-viento-cueca-app/) |

## 🧪Laboratorium Teknik

| Repo | Apa yang menunjukkan |
|---|---|
| [🐳 **Problem-Driven Systems Lab**](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) | **20 masalah nyata**(latensi di bawah beban, N + 1, coba badai, kebocoran, monolith, stapede cache, backpresde, migrasi zero-downtime, dilupakan DLQ) dengan high- setia kegagalan disuntikkan, dipecahkan dalam**7 tumpukan**PHP 8·Python·Node.js·Java 21·- 8.· **Pergi 1.23** · **Rust 1.83** · [landing](https://vladimiracunadev-create.github.io/problem-driven-systems-lab/) |
| [📆 **Social Bot Scheduler**](https://github.com/vladimiracunadev-create/social-bot-scheduler) | **v4.10.0** · **20 kasus**sumber penerima sinyal berikut:**18 + mesin DB** —**19 operasional**, secara individual diaudit dengan Docker -**Lapisan 8**audit, idempotency guardrails, circuit breaker, and DLQ· [landing](https://vladimiracunadev-create.github.io/social-bot-scheduler/) |
| [🧰 **Microsistemas**](https://github.com/vladimiracunadev-create/microsistemas) | **12 diagnostik dan microapps modernisasi**untuk PHP·lokal baca-hanya server MCP·Hardening dalam 3 fase· [landing](https://vladimiracunadev-create.github.io/microsistemas/) |
| [🧪 **Docker Labs**](https://github.com/vladimiracunadev-create/docker-labs) | **13 laboratorium**pada platform 4- service + otomatis`.exe`installer dengan peluncur· [landing](https://vladimiracunadev-create.github.io/docker-labs/) |
| [🐳 **WSL Labs**](https://github.com/vladimiracunadev-create/wsl-labs) | **12 kasus**nyala`wslc`, mesin WSL kontainer asli -**tanpa Docker Desktop** · [landing](https://vladimiracunadev-create.github.io/wsl-labs/) |
| [⚡ **Unikernel Labs**](https://github.com/vladimiracunadev-create/unikernel-labs) | "Docker Desktop untuk unikernels": Kontrol Windows atas Unikraft dengan backend WSL2,`kraft`+ QEMU / KVM· [landing](https://vladimiracunadev-create.github.io/unikernel-labs/) |
| [🧰 **QEMU/KVM Labs**](https://github.com/vladimiracunadev-create/qemu-kvm-labs) | **12 laboratorium**dari virtualisasi nyata dengan QEMU, KVM, libvirt, cloud- init, dan`vm-manager`pada Linux dan WSL2· [landing](https://vladimiracunadev-create.github.io/qemu-kvm-labs/) |
| [🛡️ **Sandbox Labs**](https://github.com/vladimiracunadev-create/sandbox-labs) | Isolasi Linux: menjalankan kode pihak ketiga, berkas, dan model bisnis di bawah kebijakan yang dideklarasikan dan**memancarkan bukti yang ditandatangani yang mengontrol benar-benar diterapkan** · **36 kasus**dalam dua keluarga - 15 teknis dan 21 kapital- pasar -·mendeklarasikan eksperimental dan pendidikan, * Bukan produk keamanan *· [landing](https://vladimiracunadev-create.github.io/sandbox-labs/) |
| [💳 **Universal Payments Engineering Lab**](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) | **28 keluarga pembayaran**dalam demo penjelasan-lokal: Kondisi, buku besar, rekonsiliasi, keamanan, dan panduan implementasi· [landing](https://vladimiracunadev-create.github.io/universal-payments-engineering-lab/) |
| [🕹️ **Decentraland Social Arcade**](https://github.com/vladimiracunadev-create/decentraland-social-arcade) | Native Decentraland sosial 3D pengalaman: satu MVP dan multi- game arsitektur dengan SDK7, ECS, dan TypeScript·Dokumentasi Spanyol·tidak ada pembayaran atau telemetri |
| [☁️ **AWS Projects**](https://github.com/vladimiracunadev-create/proyectos-aws) | Kasus progresif di mana masing-masing menambahkan satu layanan AWS**dan**kemampuan baru dari GitHub Actions·SAA- C03·DVA- C02·C02 SOA- cakupan |

## 🤖AI Terapan

| Repo | Apa yang menunjukkan |
|---|---|
| [🤖 **LangGraph RealWorld**](https://github.com/vladimiracunadev-create/langgraph-realworld) | **25 / 25 backend operasional**- negara typed, rute kondisional, streaming NDJSON, mode DEMO / LIVE, 8 lapisan keamanan, SHA-256 rantai hak asuh |
| [🧭 **Operational AI Agents**](https://github.com/vladimiracunadev-create/operational-ai-agents) | **13 agen operasional**untuk Claude Code dan waktu-waktu jalan yang kompatibel: masing-masing menerima misi lengkap - evolusi repositori, modernisasi warisan, desain kurikulum, penerbitan portofolio, perbaikan keamanan, analisis insiden - di bawah kontrak yang dinyatakan, gerbang manusia, dan bukti yang dapat diverifikasi· **39 deterministik eval** ·34 tes·zero- deps (hanya stdlib)·Linux·Mapos·Jendela· [site](https://vladimiracunadev-create.github.io/operational-ai-agents/) |
| [🧠 **MCP + Ollama Local**](https://github.com/vladimiracunadev-create/mcp-ollama-local) | Local- pertama AI dengan alat MCP dalam sebuah sandbox· `127.0.0.1`bind·profil trust multilayer·jujur tentang batas |
| [🧩 **Agentic Plugins Toolkit**](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) | **6 plugin agentic**terinstall dalam Claude Code, OpenAI / Codex, Copilot, Gemini, dan MCP dari satu sumber:`repository-engineering`, `legacy-modernization`, `learning-program-studio`, `product-evolution`, `portfolio-governance`, dan`rootcause-response` · **69 tampilan yang dihasilkan tanpa drift**- setiap waktu berjalan menerima format dari kontrak yang sama -·zero- deps·Linux·Mapos·Jendela· [site](https://vladimiracunadev-create.github.io/agentic-plugins-toolkit/) |
| [🧰 **Claude Skills Toolkit**](https://github.com/vladimiracunadev-create/claude-skills-toolkit) | **15 Agnentic skills**untuk Claude Code· **keamanan**: 12-layer`security-audit`(OSV·KEV·EPSS·SAST·kontainer·rahasia) dan 14-stage`bitcoin-custody-audit` · **gerbang repo**: `pre-commit-guard`, `pre-push-guard`, `yaml-control`, `md-lint-fix`, `python-lint-guard` · **koherensi**: `repo-coherence-audit`, `version-bump`, `python-version-control`, `python-deps-pinning` · **Docker**: `docker-cleanup`, `docker-compose-doctor` · **docs**: `md-to-doc` ·zero- deps·platform-cross |
| [🧰 **Codex Skills Toolkit**](https://github.com/vladimiracunadev-create/codex-skills-toolkit) | **19 keahlian agnentic**untuk Codex: keamanan dan rantai pasokan, preflight, aliran fungsional, ketahanan dan negara, melepaskan bukti, Python / YAML / Markdown gerbang, versi, ketergantungan, Docker, dan dokumen·Pythagon- pertama· `pnpm` ·Linux·Mapos·Jendela· [site](https://vladimiracunadev-create.github.io/codex-skills-toolkit/) |

## 🔬Komputer Ilmiah

| Repo | Apa yang menunjukkan |
|---|---|
| [🧬 **Human Genome Labs**](https://github.com/vladimiracunadev-create/human-genome-labs) | Platform genomik reproduksif: diketik`ScientificResult<T>`kontrak, FASTA / GFF3 / VCF, modul dengan**Kedewasaan eksplisit dan bukti**Kejujuran radikal: * tidak melakukan diagnosis klinis *· [site](https://vladimiracunadev-create.github.io/human-genome-labs/) |

<a id="forks"></a>

## 🍴 Fork proyek pihak ketiga (52)

Ini adalah fork proyek milik orang lain yang disimpan di akun ini. **Bukan karya sendiri**: penghargaan milik penulis aslinya, tidak masuk ke angka mana pun di profil ini, dan setiap deskripsi merangkum apa yang dinyatakan proyek aslinya, tanpa menyiratkan dukungan, audit, atau pengalaman produksi saya sendiri. Deskripsi mengikuti proyek asli · 2026-11-09.

### 🤖 Agen pengodean dan framework agen (18)

| Fork | Proyek asli | Bahasa | Apa itu |
|---|---|---|---|
| [**OpenHands**](https://github.com/vladimiracunadev-create/OpenHands) | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | TypeScript | Platform agen untuk pengembangan perangkat lunak berbasis AI |
| [**cline**](https://github.com/vladimiracunadev-create/cline) | [cline/cline](https://github.com/cline/cline) | TypeScript | Agen pengodean otonom sebagai SDK, ekstensi IDE, atau CLI |
| [**opencode**](https://github.com/vladimiracunadev-create/opencode) | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | Agen pengodean sumber terbuka |
| [**qwen-code**](https://github.com/vladimiracunadev-create/qwen-code) | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | TypeScript | Agen pengodean AI sumber terbuka untuk terminal |
| [**goose**](https://github.com/vladimiracunadev-create/goose) | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Rust | Agen yang dapat diperluas untuk memasang, menjalankan, mengedit, dan menguji kode dengan LLM apa pun |
| [**pi**](https://github.com/vladimiracunadev-create/pi) | [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | Toolkit agen: API LLM terpadu, loop agen, TUI, dan CLI pengodean |
| [**hermes-agent**](https://github.com/vladimiracunadev-create/hermes-agent) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | Agen yang tumbuh bersama Anda (NousResearch) |
| [**deepagents**](https://github.com/vladimiracunadev-create/deepagents) | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Python | Harness agen «baterai sudah termasuk» (LangChain) |
| [**crewAI**](https://github.com/vladimiracunadev-create/crewAI) | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | Framework untuk mengorkestrasi agen otonom berperan |
| [**agent-framework**](https://github.com/vladimiracunadev-create/agent-framework) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Python | Framework Microsoft untuk membangun dan men-deploy agen dan alur kerja multi-agen di Python dan .NET |
| [**deepseek-harness**](https://github.com/vladimiracunadev-create/deepseek-harness) | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | TypeScript | Harness agen DeepSeek di mana semuanya adalah plugin |
| [**agent-orchestrator**](https://github.com/vladimiracunadev-create/agent-orchestrator) | [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Go | Merencanakan, menjalankan, dan mengawasi armada agen, dari tugas hingga PR yang digabung |
| [**orca**](https://github.com/vladimiracunadev-create/orca) | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | Ruang kerja untuk armada agen pengodean (desktop, seluler, dan jarak jauh) |
| [**kander**](https://github.com/vladimiracunadev-create/kander) | [dualface/kander](https://github.com/dualface/kander) | Go | Papan kanban yang mengoordinasikan agen pengodean dengan git worktree terisolasi dan agen peninjau |
| [**OpenBot**](https://github.com/vladimiracunadev-create/OpenBot) | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | TypeScript | Rekan kerja AI dengan komputer sendiri; setiap aksi diputuskan sebelumnya dan dicatat sesudahnya |
| [**browser-use**](https://github.com/vladimiracunadev-create/browser-use) | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | Pustaka Python untuk agen AI yang mengoperasikan browser |
| [**agent-desktop**](https://github.com/vladimiracunadev-create/agent-desktop) | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Rust | CLI computer use untuk agen AI |
| [**treg**](https://github.com/vladimiracunadev-create/treg) | [superdesigndev/treg](https://github.com/superdesigndev/treg) | Python | «OpenRouter untuk alat agen» |

### 🧩 Skill, plugin, dan alur kerja untuk agen (11)

| Fork | Proyek asli | Bahasa | Apa itu |
|---|---|---|---|
| [**claude-plugins-official**](https://github.com/vladimiracunadev-create/claude-plugins-official) | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | Direktori resmi plugin Claude Code berkualitas yang dikelola Anthropic |
| [**agentic-awesome-skills**](https://github.com/vladimiracunadev-create/agentic-awesome-skills) | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | Python | Control plane lokal untuk menemukan, memilih, dan memvalidasi katalog besar skill agentic (CLI, MCP lokal, plugin) |
| [**claude-review-all**](https://github.com/vladimiracunadev-create/claude-review-all) | [ncoevoet/claude-review-all](https://github.com/ncoevoet/claude-review-all) | Python | Tinjauan kode multi-agen untuk Claude Code |
| [**blender-skills**](https://github.com/vladimiracunadev-create/blender-skills) | [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | TypeScript | Skill Blender khusus untuk agen pengodean dengan pipeline berbasis MCP |
| [**diagram-design**](https://github.com/vladimiracunadev-create/diagram-design) | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | Desain diagram editorial (HTML + SVG) untuk agen pengodean |
| [**elephant-goldfish-model**](https://github.com/vladimiracunadev-create/elephant-goldfish-model) | [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) | Python | Skill terbuka Google untuk merancang dan meninjau perangkat lunak dengan agen AI |
| [**Claude-Code-Game-Studios**](https://github.com/vladimiracunadev-create/Claude-Code-Game-Studios) | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | Mengubah Claude Code menjadi studio gim dari agen yang terkoordinasi |
| [**headcount**](https://github.com/vladimiracunadev-create/headcount) | [cbrock84/headcount](https://github.com/cbrock84/headcount) | Markdown | Organisasi agen yang disusun seperti perusahaan: departemen dan skill yang dapat dipasang |
| [**agentic-qe**](https://github.com/vladimiracunadev-create/agentic-qe) | [proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) | TypeScript | Platform QA/QE terbuka dengan agen dan skill untuk seluruh siklus hidup perangkat lunak |
| [**OpenExecutive**](https://github.com/vladimiracunadev-create/OpenExecutive) | [SenteLabsAI/OpenExecutive](https://github.com/SenteLabsAI/OpenExecutive) | Python | Tim eksekutif virtual: satu sosok eksekutif yang didukung 8 agen Claude spesialis |
| [**n8n-mcp**](https://github.com/vladimiracunadev-create/n8n-mcp) | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | TypeScript | Server MCP agar Claude, Cursor, atau Windsurf membangun alur kerja n8n |

### 🛡️ Keamanan dan analisis perangkat lunak (8)

| Fork | Proyek asli | Bahasa | Apa itu |
|---|---|---|---|
| [**raptor**](https://github.com/vladimiracunadev-create/raptor) | [gadievron/raptor](https://github.com/gadievron/raptor) | Python | Mengubah Claude Code menjadi agen keamanan ofensif dan defensif |
| [**Cybersecurity-Projects**](https://github.com/vladimiracunadev-create/Cybersecurity-Projects) | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | Go | 70 proyek keamanan siber dari pemula hingga mahir |
| [**SkillSpector**](https://github.com/vladimiracunadev-create/SkillSpector) | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Python | Pemindai keamanan NVIDIA untuk skill agen (injeksi prompt, eksfiltrasi, rantai pasok) |
| [**Anthropic-Cybersecurity-Skills**](https://github.com/vladimiracunadev-create/Anthropic-Cybersecurity-Skills) | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | Ratusan skill keamanan siber untuk agen, dipetakan ke MITRE ATT&CK, NIST CSF, dan kerangka lain |
| [**security-audit-skill**](https://github.com/vladimiracunadev-create/security-audit-skill) | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | Skill Cloudflare untuk audit keamanan multi-fase dengan temuan yang diverifikasi independen |
| [**siteone-crawler**](https://github.com/vladimiracunadev-create/siteone-crawler) | [janreges/siteone-crawler](https://github.com/janreges/siteone-crawler) | Rust | Crawler dan penganalisis situs web untuk SEO, keamanan, aksesibilitas, dan performa |
| [**rea**](https://github.com/vladimiracunadev-create/rea) | [morluto/rea](https://github.com/morluto/rea) | TypeScript | Rekayasa balik dengan agen, dari perilaku aplikasi hingga biner native |
| [**craft-anything**](https://github.com/vladimiracunadev-create/craft-anything) | [storytold/craft-anything](https://github.com/storytold/craft-anything) | Rust | Memahami cara kerja perangkat lunak apa pun dan membangun milik sendiri |

### 🧠 Model AI dan infrastruktur (5)

| Fork | Proyek asli | Bahasa | Apa itu |
|---|---|---|---|
| [**marin**](https://github.com/vladimiracunadev-create/marin) | [marin-community/marin](https://github.com/marin-community/marin) | Python | Framework terbuka untuk riset dan pengembangan model fondasi |
| [**prime-rl**](https://github.com/vladimiracunadev-create/prime-rl) | [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) | Python | Pelatihan reinforcement learning agentik berskala besar |
| [**Olmo-core**](https://github.com/vladimiracunadev-create/Olmo-core) | [allenai/Olmo-core](https://github.com/allenai/Olmo-core) | Python | Blok bangunan PyTorch untuk ekosistem OLMo |
| [**DeepInfer**](https://github.com/vladimiracunadev-create/DeepInfer) | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | Python | Framework inferensi berkinerja tinggi berskala besar untuk model DeepSeek |
| [**heretic**](https://github.com/vladimiracunadev-create/heretic) | [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | Modifikasi model bahasa tanpa pelatihan ulang (sensor, sikap menjilat, dll.) |

### 🏢 Manajemen bisnis dan platform (6)

| Fork | Proyek asli | Bahasa | Apa itu |
|---|---|---|---|
| [**erpnext**](https://github.com/vladimiracunadev-create/erpnext) | [frappe/erpnext](https://github.com/frappe/erpnext) | Python | ERP bebas dan sumber terbuka |
| [**odoo**](https://github.com/vladimiracunadev-create/odoo) | [odoo/odoo](https://github.com/odoo/odoo) | Python | Aplikasi bisnis sumber terbuka |
| [**mautic**](https://github.com/vladimiracunadev-create/mautic) | [mautic/mautic](https://github.com/mautic/mautic) | PHP | Otomatisasi pemasaran sumber terbuka |
| [**crm**](https://github.com/vladimiracunadev-create/crm) | [trycompai/crm](https://github.com/trycompai/crm) | TypeScript | CRM sumber terbuka yang dirancang untuk agen AI (Comp AI) |
| [**harness**](https://github.com/vladimiracunadev-create/harness) | [harness/harness](https://github.com/harness/harness) | Go | Platform pengembang menyeluruh: kontrol kode sumber, CI/CD, lingkungan, dan registri artefak |
| [**traccar**](https://github.com/vladimiracunadev-create/traccar) | [traccar/traccar](https://github.com/traccar/traccar) | Java | Platform pelacakan GPS sumber terbuka, 200+ protokol perangkat |

### 🎓 Pendidikan dan referensi (4)

| Fork | Proyek asli | Bahasa | Apa itu |
|---|---|---|---|
| [**computer-science**](https://github.com/vladimiracunadev-create/computer-science) | [ossu/computer-science](https://github.com/ossu/computer-science) | HTML | Jalur belajar mandiri gratis Ilmu Komputer (OSSU) |
| [**math**](https://github.com/vladimiracunadev-create/math) | [ossu/math](https://github.com/ossu/math) | — | Jalur belajar mandiri gratis Matematika (OSSU) |
| [**manim**](https://github.com/vladimiracunadev-create/manim) | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Python | Framework Python komunitas untuk animasi matematika |
| [**asm-atari-2600**](https://github.com/vladimiracunadev-create/asm-atari-2600) | [johnidm/asm-atari-2600](https://github.com/johnidm/asm-atari-2600) | Assembly | Contoh kode sumber gim Atari 2600 dalam assembly |
