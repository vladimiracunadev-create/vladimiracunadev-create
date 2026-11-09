# 🗂️ 生態系統：產品、實驗室、應用 AI、課程與科學運算

[← 返回檔案](../README.zh-TW.md)

**🌐** [Español](ECOSYSTEM.md) · [English](ECOSYSTEM.en.md) · [Português](ECOSYSTEM.pt.md) · [Italiano](ECOSYSTEM.it.md) · [Français](ECOSYSTEM.fr.md) · [简体中文](ECOSYSTEM.zh.md) · **繁體中文** · [日本語](ECOSYSTEM.ja.md) · [한국어](ECOSYSTEM.ko.md) · [Türkçe](ECOSYSTEM.tr.md) · [Русский](ECOSYSTEM.ru.md) · [Tiếng Việt](ECOSYSTEM.vi.md) · [ไทย](ECOSYSTEM.th.md) · [Deutsch](ECOSYSTEM.de.md) · [Українська](ECOSYSTEM.uk.md) · [Polski](ECOSYSTEM.pl.md) · [العربية](ECOSYSTEM.ar.md) · [فارسی](ECOSYSTEM.fa.md) · [Bahasa Indonesia](ECOSYSTEM.id.md) · [Nederlands](ECOSYSTEM.nl.md) · [हिन्दी](ECOSYSTEM.hi.md) · [Ελληνικά](ECOSYSTEM.el.md)

本檔案的實作成果集中在獨立文件中：可下載安裝的軟體、工程實驗室、應用 AI 與科學運算，以及帳號中每個第三方專案 fork 的說明。

## 📦具有實際分佈的產品

軟體被下載,安裝,使用——不僅被克隆.

| 產品 | 是什麼來著? | 堆疊 | 交付 |
|---|---|---|---|
| [🔍 **RootCause Windows**](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) | 網路安全法證:每一次異常的資源扭曲,都可能是威脅的第一個跡象. 先診斷,後干預 | 鏽🦀 ·ETW/WPR 電子資料交換系統 | **0.19.0 維基百科中的相關條目: 維基百科** · **16次釋出** · **5個版本**: 圖形介面·可移植·國家學習水平·電殼·VS 程式碼· [landing](https://vladimiracunadev-create.github.io/rootcause-windows-inspector/) |
| [📱 **RootCause Mobile**](https://github.com/vladimiracunadev-create/rootcause-mobile-inspector) | 移動兄弟:一個法證感測器,將每個應用程式與自己進行比較,標出跟蹤器的旗子,並將所授予的許可與僅要求的許可分開。 | 小蝶 , 蝶 , 蝶 , 蝶 , 蝶 , 蝶·科特林語Name·輕取 | **以0.8.0計** ·可核查的Android APK·5種語言· **零遙測** · [landing](https://vladimiracunadev-create.github.io/rootcause-mobile-inspector/) |
| [🍎 **RootCause macOS**](https://github.com/vladimiracunadev-create/rootcause-macos-inspector) | macOS 版 :`launchd`持續、守門、SIP、FileVault、XProtect、TCC許可權、簽名程序和網路鄰居——每個表面都對照已知的良好狀態檢查 | 鏽🦀 ·macOS 13+ 常規 | **單位:千分之一** ·首次釋出·阿帕奇-2.0 維基月球線上解說-阿帕奇-2.0· [landing](https://vladimiracunadev-create.github.io/rootcause-macos-inspector/) |
| [🖥️ **RootCause Server**](https://github.com/vladimiracunadev-create/rootcause-server) | 伺服器兄弟關係:將沒有單一日誌所看到的東西聯絡起來——曝光的表面、訪問的嘗試、給予同一地址的會話、關鍵檔案完整性和感測器的沉默——並將其變成一個可操作的句子 | 鏽🦀 ·視窗·連結·macOS 系統 | **以0.2.0計** · **18 第 條**證據和記錄·從未單獨執行動作·本地控制檯, 不含網路依賴性· **目前尚未釋出** · [landing](https://vladimiracunadev-create.github.io/rootcause-server/) |
| [🌐 **RootCause Web**](https://github.com/vladimiracunadev-create/rootcause-web-inspector) | 瀏覽器法證感測器: cookie, 電子郵件會話, 擴充套件, 下載, 許可權, 以及模模擬實視窗的頁面 | Java 指令碼·MV3 擴充套件 | **以0.2.0計** ·目前尚未釋出·面板開口`127.0.0.1` ·零依賴關係·在 CI 中驗證的零遙測· [landing](https://vladimiracunadev-create.github.io/rootcause-web-inspector/) |
| [₿ **RootCause Bitcoin Defense**](https://github.com/vladimiracunadev-create/rootcause-bitcoin-defense) | 僅監視Bitcoin監管的辯護:盤點每把鑰匙的來源,用公佈的警告進行交叉核對,用證據解釋根源 | Java 指令碼·視窗應用程式·本地面板 | **維基月球0.3.0** · **2次釋出** ·零依賴關係·永遠不要要求種子·已核實的 CI· [landing](https://vladimiracunadev-create.github.io/rootcause-bitcoin-defense/) |
| [⛓️ **RootCause Blockchain Security**](https://github.com/vladimiracunadev-create/rootcause-blockchain-security) | 多鏈只監視控制檯:庫存合同、代理、甲骨文、橋樑、治理和依賴性,生成根源執行本 | Java 指令碼·視窗應用程式·本地面板 | **維基月球0.3.0**儲存器中·已釋出發行 :`v0.1.0` ·零依賴關係·從未要求私鑰·已核實的 CI· [landing](https://vladimiracunadev-create.github.io/rootcause-blockchain-security/) |
| [📷 **RootCause QR Inspector**](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) | 用於檢查 QR 程式碼的本地Android app 操作前: 解釋 26 個訊號, 將事實與假說區分開來, 並輸出被編輯的證據 | 小蝶 , 蝶 , 蝶 , 蝶 , 蝶 , 蝶·達特 | **v0.2.0** · **6次釋出** · **163次測試** ·已出版的Android APK·可核查的SHA-256·APK 成套技術簽名;商業/儲存簽名正在進行·零遙測· [landing](https://vladimiracunadev-create.github.io/rootcause-qr-inspector/) |
| [🏢 **Empresa Operativa Chile**](https://github.com/vladimiracunadev-create/empresa-operativa-chile) | 將註冊前的證券交易指南改為每月關閉:附有證據的註冊、增值稅結轉、F29草案、不可改變的關閉和審計記錄。 每一個規則都指向它的官方來源 | Java 指令碼·鏽·太平洋婦女協會 | **v1.8.0** ·機器人·視窗·瀏覽器· **217次試驗** · **0個生產依賴** ·零遙測· [landing](https://vladimiracunadev-create.github.io/empresa-operativa-chile/) |
| [🔍 **Universal Code Scanner**](https://github.com/vladimiracunadev-create/universal-code-scanner) | QR 和條碼讀取器**行動前的翻譯**: 16個本地URL風險訊號並明確確認 | 小蝶 , 蝶 , 蝶 , 蝶 , 蝶 , 蝶·達特 | **維基百科中的相關條目: 維基語錄連結:名人名言 - 分類** ·機器人·iOS 系統·macOS 系統·太平洋婦女協會·加密歷史**AES-256-GCM 導彈** · [landing](https://vladimiracunadev-create.github.io/universal-code-scanner/) |
| [🗄️ **GabySQL**](https://github.com/vladimiracunadev-create/gabysql) | 嵌入式資料庫:單`.db`檔案, WAL, 基於成本的最佳化器, HTTP/ JSON API | 鏽🦀 | 視窗·macOS 系統·連結· [landing](https://vladimiracunadev-create.github.io/gabysql/) |
| [🤖 **Automa PC**](https://github.com/vladimiracunadev-create/automa-pc) | 本地管絃樂器:JSON 流出開啟真實視窗,與 DOM 互動,留下證據 | 蟒蛇·劇作家·pywebview 頁面檢視 | **維基月球0.3.0** · **27個流動** ·已公佈和可核查的安裝器· [landing](https://vladimiracunadev-create.github.io/automa-pc/) |
| [🏭 **AI Dataset Foundry**](https://github.com/vladimiracunadev-create/ai-dataset-foundry) | 本地第一工廠,將PDF、Word、Web、Git、JSON和CSV轉化為可審計的資料集,用於預訓、微調、RAG和評價 | 蟒蛇 | **以0.2.0計** ·Windows + 離線Android 軟體·首次釋出· [landing](https://vladimiracunadev-create.github.io/ai-dataset-foundry/) |
| [☁️ **AWS Desktop Studio**](https://github.com/vladimiracunadev-create/aws-desktop-studio) | 本地第一應用程式,包含15個AWS庫存整合,20個教程,CLI/SSO,以及只讀預設;執行中,沒有普及 | Java 指令碼·視窗 | **編號為0.1.1** ·首次釋出· [landing](https://vladimiracunadev-create.github.io/aws-desktop-studio/) |
| [🧭 **Commerce OS**](https://github.com/vladimiracunadev-create/commerce-operating-system) | 商業業務的引導概念示範:目錄、庫存、客戶關係管理、訂單、模擬付款和可追蹤性 | Java 指令碼·網頁·視窗·機器人 | **維基月球0.3.0** · **2次釋出** ·沒有任何實收資金或智利稅務當局的一體化· [landing](https://vladimiracunadev-create.github.io/commerce-operating-system/) |
| [📄 **PDF Reader**](https://github.com/vladimiracunadev-create/pdf-reader-windows-android) | Android- 第一臺本地只讀讀取器, 其無剪輯縮放, 可重開歷史、 WhatsApp 共享以及預設讀取器選擇 | HTML 語言·網頁·機器人·視窗 | **0.3.3 資料** ·已簽名的APK·沒有賬戶、敏感許可權或遙測· [landing](https://vladimiracunadev-create.github.io/pdf-reader-windows-android/) |
| [🎙️ **Video Transcript Studio**](https://github.com/vladimiracunadev-create/video-transcript-studio) | 影片、播放列表或**整個YouTube頻道**以時間戳來文字。 它不依賴現有的字幕: 低聲識別音訊**訣竟**,沒有 API、賬戶或金鑰來配置 | 蟒蛇·雙管6·FastAPI 軟體·快速低聲 | **以0.2.0計** ·視窗桌面+ 本地面板在`127.0.0.1`+CLI, + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +**共享相同的佇列** ·貨幣·個人檔案·自動除錯·特別審判庭·虛擬TT·傑森,你好嗎?·MP3 調變解調器·歐格· **89次測試** ·捆綁的FFmpeg 軟體·零遙測· [landing](https://vladimiracunadev-create.github.io/video-transcript-studio/) |
| [🎨 **ChofyAI Studio**](https://github.com/vladimiracunadev-create/chofyai-studio) | 本地創意AI發射裝置:管弦樂團 Qune3-TTS,低語.cpp,FaceFusion,AceForge,和ComfyUI | 陶里語 2·鏽·反應 | 5.1 以內· **5/5 工具,並有真實的推論** ·macOS 蘋果矽·實驗視窗· **目前尚未釋出** · [site](https://vladimiracunadev-create.github.io/chofyai-studio/) |
| [🦏 **Rhino Suite**](https://github.com/vladimiracunadev-create/rhino-suite) | 從頭開始的辦公套件:文件規則不依賴於 DOM —— HTML 僅僅是一個投影 | 粗口/瓦斯米·去吧,我們走·反應 19 | 按相位演化的單重力· [landing](https://vladimiracunadev-create.github.io/rhino-suite/) |
| [🎻 **My Violin Adventure**](https://github.com/vladimiracunadev-create/violin-adventure) | 兒童教育應用:花色調奏器、錄音鍾精確的節拍器、有真琴的歌曲 | 陶里語 2·反應·TS 調製 | **編號: 1.3.0** ·視窗·機器人·連結·macOS 系統·太平洋婦女協會· [landing](https://vladimiracunadev-create.github.io/violin-adventure/) |
| [🎸 **My Guitar Adventure**](https://github.com/vladimiracunadev-create/guitarra-adventure) | 接弦的弟弟: 6個世界的24個課,6個弦調奏者,無漂流的節奏, 和11個真正的吉他音符 | 陶里語 2·反應·TS 調製 | **單曲 1. 0.0** ·視窗·機器人·連結·macOS 系統·iOS 系統·太平洋婦女協會·沒有賬戶、廣告或線上依賴· [landing](https://vladimiracunadev-create.github.io/guitarra-adventure/) |
| [🧣 **Pañuelo al Viento**](https://github.com/vladimiracunadev-create/panuelo-al-viento-cueca-app) | 10歲的Cueca:8級24個班級,72個活動,6個脈衝實驗室(3+3和2+2+2),以及可訪問的地平圖. 宣告如下:**補充,而不是替換**教師和文化傳承者 | 小蝶 , 蝶 , 蝶 , 蝶 , 蝶 , 蝶·達特 | **以0.2.0計** ·7+號機器人·Windows 10/11 視窗 10/11·APK 自動交換·EXE 資料·模里西斯·行動式· **29個測試+2個驗證器** ·沒有相機、麥克風、賬戶、廣告或網際網路· [landing](https://vladimiracunadev-create.github.io/panuelo-al-viento-cueca-app/) |

## 🧪工程實驗室

| 重播( R) | 所顯示的 |
|---|---|
| [🐳 **Problem-Driven Systems Lab**](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) | **20個真正的問題**(負載下緯度,N+1,重試風暴,出洩,單層,快取被印出,回壓,零下行遷移,被遺忘 DLQ) 具有高純度注入出故障,解入.**7個堆**: 首頁8·蟒蛇·節點.js·爪哇島21·.NET 8 資料· **衝出1.23** · **粗口1.83 號** · [landing](https://vladimiracunadev-create.github.io/problem-driven-systems-lab/) |
| [📆 **Social Bot Scheduler**](https://github.com/vladimiracunadev-create/social-bot-scheduler) | **以4.10.0計** · **20個案件**來源=n8n=收件者**18+ DB 發動機** —**19起業務**,個人審計 與多克 -**8層**審計、一手護欄、斷路器和DLQ· [landing](https://vladimiracunadev-create.github.io/social-bot-scheduler/) |
| [🧰 **Microsistemas**](https://github.com/vladimiracunadev-create/microsistemas) | **12個診斷和現代化微型應用程式**用於最高階·本地只讀的 MCP 伺服器·分三個階段進行硬化· [landing](https://vladimiracunadev-create.github.io/microsistemas/) |
| [🧪 **Docker Labs**](https://github.com/vladimiracunadev-create/docker-labs) | **13個實驗室**4個服務平臺+自動`.exe`裝有發射裝置的安裝器· [landing](https://vladimiracunadev-create.github.io/docker-labs/) |
| [🐳 **WSL Labs**](https://github.com/vladimiracunadev-create/wsl-labs) | **12個案件**開啟`wslc`,本地WSL集裝箱發動機——**不掛起子桌面** · [landing](https://vladimiracunadev-create.github.io/wsl-labs/) |
| [⚡ **Unikernel Labs**](https://github.com/vladimiracunadev-create/unikernel-labs) | “單核管的容器桌面” : 使用 WSL2 後端控制 Unikraft 的 Windows 控制器,`kraft`+ QEMU/KVM· [landing](https://vladimiracunadev-create.github.io/unikernel-labs/) |
| [🧰 **QEMU/KVM Labs**](https://github.com/vladimiracunadev-create/qemu-kvm-labs) | **12個實驗室**與QEMU、KVM、libvirt、雲-init以及`vm-manager`有關 Linux 和 WSL2 的· [landing](https://vladimiracunadev-create.github.io/qemu-kvm-labs/) |
| [🛡️ **Sandbox Labs**](https://github.com/vladimiracunadev-create/sandbox-labs) | Linux 隔離: 執行第三方程式碼、檔案, 以及宣佈的政策下的商務模式**簽發了實際適用控制措施的簽名證據** · **36個案件**15個技術市場和21個資本市場,·* 已申報為實驗和教育產品,* 不是安全產品*· [landing](https://vladimiracunadev-create.github.io/sandbox-labs/) |
| [💳 **Universal Payments Engineering Lab**](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) | **28個支付家庭**當地自我解釋演示:狀態、分類賬、對賬、安全和執行指南· [landing](https://vladimiracunadev-create.github.io/universal-payments-engineering-lab/) |
| [🕹️ **Decentraland Social Arcade**](https://github.com/vladimiracunadev-create/decentraland-social-arcade) | 原生的Decentraliand 社交 三維體驗:一個MVP和多遊戲架構,並配有 SDK7, ECS, 和 TypeScript·西班牙文文件·無付款或遙測 |
| [☁️ **AWS Projects**](https://github.com/vladimiracunadev-create/proyectos-aws) | Progressive cases where each one adds one AWS service **and** a new GitHub Actions capability · SAA-C03 · DVA-C02 · SOA-C02 coverage |

## 🤖應用AI

| 重播( R) | 所顯示的 |
|---|---|
| [🤖 **LangGraph RealWorld**](https://github.com/vladimiracunadev-create/langgraph-realworld) | **25/25 業務後端**——打出狀態,有條件的路線,NDJSON流線,DEMO/LIVE模式,8個安全層,SHA-256 監管鏈 |
| [🧭 **Operational AI Agents**](https://github.com/vladimiracunadev-create/operational-ai-agents) | **13個業務代理**克勞德密碼和相容執行時間:每個系統都收到一個完整的任務——儲存器演變、遺產現代化、課程設計、組合出版、安全補救、事件分析——根據申報的合同、人口和可核查的證據· **39個確定性評估** ·34個測試·零潛入( 僅限Stdlib)·連結·macOS 系統·視窗· [site](https://vladimiracunadev-create.github.io/operational-ai-agents/) |
| [🧠 **MCP + Ollama Local**](https://github.com/vladimiracunadev-create/mcp-ollama-local) | 沙盒中帶有 MCP 工具的本地首個AI· `127.0.0.1`繫結·多層信任配置·誠實地說,這是有限度的, |
| [🧩 **Agentic Plugins Toolkit**](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) | **6個代理外掛**可從一個來源在克洛德碼、OpenAI/Codex、副駕駛、雙子座和MCP中安裝:`repository-engineering`, `legacy-modernization`, `learning-program-studio`, `product-evolution`, `portfolio-governance`,以及`rootcause-response` · **69個生成的不漂移的檢視**——每次執行時間都從同一份合同中收到其格式.·零讀取·連結·macOS 系統·視窗· [site](https://vladimiracunadev-create.github.io/agentic-plugins-toolkit/) |
| [🧰 **Claude Skills Toolkit**](https://github.com/vladimiracunadev-create/claude-skills-toolkit) | **22個代理技能**克勞德程式碼· **安保服務**: 12 層`security-audit`維也納(OSV)·開源軟體國際化之簡體中文組·電子軟體系統·薩斯德·容器·保密)和14階段`bitcoin-custody-audit` · **重置閘門**: `pre-commit-guard`, `pre-push-guard`, `yaml-control`, `md-lint-fix`, `python-lint-guard` · **一致性**: `repo-coherence-audit`, `version-bump`, `python-version-control`, `python-deps-pinning` · **掛起點**: `docker-cleanup`, `docker-compose-doctor` · **文件**: `md-to-doc` ·零讀取·跨平臺 |
| [🧰 **Codex Skills Toolkit**](https://github.com/vladimiracunadev-create/codex-skills-toolkit) | **19個代理技能**用於編碼:安全和供應鏈、飛行前、功能流動、復原力和狀態、釋放證據、Python/YAML/Markdown門、版本、依賴、Docker和檔案·蟒蛇第一號· `pnpm` ·連結·macOS 系統·視窗· [site](https://vladimiracunadev-create.github.io/codex-skills-toolkit/) |

<a id="curricula"></a>

🌌 **規劃中，不計入統計：**[天文學、天體物理學、太空科學與航空太空工程](https://github.com/vladimiracunadev-create/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program)——12 個領域、133 個模組共 2,077 堂規劃課程；其中 397 堂已有正文，全部仍處於 E0 狀態。獨立培訓，並非職業資格認證 · [網站](https://vladimiracunadev-create.github.io/astronomy-astrophysics-space-sciences-aerospace-engineering-learning-program/)。

## 📚完成技術課程

西班牙語序列程式,每個儲存器都宣告狀態和範圍. 21個方案加起來是:**14 550個班級**,計算為[a workflow](../.github/workflows/stats.yml),從真正的暫存器結構或暫存器中宣告的可核查源;徽章每週重新整理一次,不由手寫.

🧭 [**Lifelong Learning Ecosystem**](https://github.com/vladimiracunadev-create/lifelong-learning-ecosystem)是一個聯邦指南針,透過視覺地圖和影象圖連線6個地區的30個真實路徑[accessible offline portal](https://vladimiracunadev-create.github.io/lifelong-learning-ecosystem/);不計為附加程式。

| 程式 | 類 | 範圍 |
|---|---:|---|
| [🔢 **Computational Mathematics**](https://github.com/vladimiracunadev-create/computational-mathematics-program) | 360 | 從依靠手指到複製出紙· **360起在CI核實的決定性示威** ·1 080個筆記本·489個術語表· [site](https://vladimiracunadev-create.github.io/computational-mathematics-program/) |
| [🏦 **Finance and Banking**](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program) | 356 | 534小時·金融數學和《國際財務報告準則》 ——信貸、風險、巴塞爾三號、公開金融、DLT、穩定幣和MICA· **27個案件** · **298次測試** · [site](https://vladimiracunadev-create.github.io/finance-and-banking-evolution-program/) |
| [🎮 **GameDev**](https://github.com/vladimiracunadev-create/modern-gamedev-program) | 352 | 數學和C#/C++/GDScript → 陰影器,AI,多人遊戲,VR/AR·哥多特語·團結·虛幻· **在CI中核實的10個戈多實驗室**(301次檢查)· [site](https://vladimiracunadev-create.github.io/modern-gamedev-program/) |
| [🛡️ **Cybersecurity**](https://github.com/vladimiracunadev-create/modern-cybersecurity-program) | 360 | **編號: 1.3.0** ·20個部分·– 紅色團隊,DFIR,雲安全,開發dev,CTF,和遊戲安全·對映到**7份證書** ·離線Android/web app·PDF 手冊·核實了CI、安保和網頁· [site](https://vladimiracunadev-create.github.io/modern-cybersecurity-program/) |
| [📈 **Marketing, Sales, and Growth**](https://github.com/vladimiracunadev-create/marketing-sales-growth-evolution-program) | 336 | 24個部分,包括業務定義、計量單、可核查的參考書目和智利的監管背景· **千分之一.6.0 千分之一.** ·1.29M字數·17個基於角色的路徑· [site](https://vladimiracunadev-create.github.io/marketing-sales-growth-evolution-program/) |
| [🏢 **Business Creation**](https://github.com/vladimiracunadev-create/modern-business-creation-program) | 336 | 在智利建立和經營一家真正的公司:從想法到成立、稅務當局、業務、危機和退出·360 個圖表·1 251個任期詞彙表·1 548頁手冊· [site](https://vladimiracunadev-create.github.io/modern-business-creation-program/) |
| [🏛️ **Architecture and Built Environment**](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program) | 830 | 83個編·60屆綜合會議·34道路徑·可追蹤來源·下行、離線閱讀器和 GitHub Pages· [site](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/) |
| [🇨🇱 **Chilean School Learning Path**](https://github.com/vladimiracunadev-create/chilean-school-learning-path) | 8,841 | 1至12年級· **4 156次綜合跨課程經驗** · **2 823個學習目標** ·聯剛特派團的訊息來源·尚未提出待決提案和尚未進行專門人力審查· [site](https://vladimiracunadev-create.github.io/chilean-school-learning-path/) |
| [🧭 **Modern Software Engineering**](https://github.com/vladimiracunadev-create/modern-software-engineering-program) | 480 | 40個部分和8個階段·基礎 → 產品、建築、安全、DevOps、SRE、SPEC、AI和多代理系統·資料庫宣佈的編輯地位· [site](https://vladimiracunadev-create.github.io/modern-software-engineering-program/) |
| [🎓 **Pedagogy and Learning Sciences**](https://github.com/vladimiracunadev-create/education-pedagogy-learning-sciences-program) | 300 | 從一個人如何學習到如何培訓教師·25個部分· **每一類都宣告其證據狀態和限度** ·早期識字、比較方法、具體教育需要、共處、文化多樣性和國際證據·1 097個定期詞彙表、325個圖表和60個活動課堂庫·按角色分列的14個職業道路·LMS 可出口· **維基百科中的相關條目: 維基語錄連結:名人名言 - 分類** · [site](https://vladimiracunadev-create.github.io/education-pedagogy-learning-sciences-program/) |
| [☁️ **Multi-Cloud**](https://github.com/vladimiracunadev-create/multi-cloud-engineering-program) | 288 | 自動取款機·阿蘇雷·GCP 常規·庫伯涅斯·地表·塞爾維亞·財務操作· **1 288小時** ·288個有JSON證據的實驗室·1 032個來源·2 884頁PDF手冊· [site](https://vladimiracunadev-create.github.io/multi-cloud-engineering-program/) |
| [🎖️ **Executive Leadership**](https://github.com/vladimiracunadev-create/executive-leadership-founder-program) | 288 | 從擁有第一個結果到領導一個公司和建立自己的團隊:團隊、KPI/OKR、金融、產品、風險、板子和併購·24個病例、96個實驗室和39個模板· [site](https://vladimiracunadev-create.github.io/executive-leadership-founder-program/) |
| [🐍 **Python Data Science**](https://github.com/vladimiracunadev-create/python-data-science-program) | 232 | 極地,ML+Optuna/SHAP,PyTorch/LLMS/LORA,MLOps·本地 Windows 應用程式 + Android APK· [site](https://vladimiracunadev-create.github.io/python-data-science-program/) |
| [🧠 **AI Evolution**](https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program) | 184 | 典型的 / 機率的 / 深層學習 / 法學碩士、 研究與培訓、代理、安全和邊境· **0.17.0 億** · **708個筆記本** · **148份基礎檔案** ·離線的 Windows, Android, 和 PWA 應用程式· [site](https://vladimiracunadev-create.github.io/artificial-intelligence-evolution-program/) |
| [🌐 **Comparative Programming**](https://github.com/vladimiracunadev-create/polyglot-programming-labs) | 176 | 有個概念**10種語言**由CI核實 -**1 360項執行**+ 加上**1 632個方案**以活語言(COBOL、Fortran、Ada、RPG、MUPS......)和地圖集**15個家庭的60張卡片** ·維基百科中的相關條目: 維基語錄連結:名人名言 - 分類· [site](https://vladimiracunadev-create.github.io/polyglot-programming-labs/) |
| [🧩 **Frameworks Compared**](https://github.com/vladimiracunadev-create/framework-ecosystems-labs) | 149 | 一份沒有介面卡的可執行合同,針對快遞、快活API、斯普林布特、ASP.NET、Django、Rails、Laravel、React、Vue、Svelte等·12個部分· **70個建築班級** · **397起在CI核實的案件** · **210 ISBN/DOI來源 網際網路檔案館的存檔,存檔日期2013-03-02.** · [site](https://vladimiracunadev-create.github.io/framework-ecosystems-labs/) |
| [🗄️ **Databases**](https://github.com/vladimiracunadev-create/database-systems-labs) | 74 | **單曲3. 0.0** ·15個部分的資料庫工程·230小時· **每項索賠的可核實來源**:120 有ISBN,DOI,或標準來源.·27個引擎破了同樣的案子·306個術語表·150個火試· [site](https://vladimiracunadev-create.github.io/database-systems-labs/) |
| [📐 **Psychometrics and Assessment**](https://github.com/vladimiracunadev-create/psychometrics-and-assessment-program) | 40 | 衡量工具如何構建、打分、驗證和審計·8個部分·可執行引擎, 使用**5項文書和344項,276項公共領域** |
| [⛓️ **Blockchain**](https://github.com/vladimiracunadev-create/blockchain-learning-path) | 66 | **v0.15.0** ·從零到可程式設計的金融基礎設施和鏈上分析· **91個做法**財務報告和已審計財務報表**508次測試** ·與開業公司(模糊和變化不定)和CI的Slither靜態分析的合同·開啟二進位制並計數其內容的離線應用程式· [site](https://vladimiracunadev-create.github.io/blockchain-learning-path/) |
| [🧠 **Neural Network Training Labs**](https://github.com/vladimiracunadev-create/neural-network-training-labs) | 31 | 7 modules · ≈214 hours · **93 notebooks** —31 classes, 31 student versions, and 31 solutions— · questions, visual maps, practices, and assessment with real public data · PyTorch · [study site](https://vladimiracunadev-create.github.io/neural-network-training-labs/) |
| [🕹️ **Machine Operator**](https://github.com/vladimiracunadev-create/machine-operator-program) | 451 | **41個培訓單元**,每臺一臺機器· **502小時15分鐘** ·系統、控制、物理、安全和模擬設計,每類源·*還沒有可執行模擬器,而且它被宣佈為這樣* |

## 🔬科學計算

| 重播( R) | 所顯示的 |
|---|---|
| [🧬 **Human Genome Labs**](https://github.com/vladimiracunadev-create/human-genome-labs) | 複製基因組學平臺:已打入`ScientificResult<T>`合同,FASTA/GFF3/VCF,模組與**明確到期和證據**. 絕對誠實:*它不進行臨床診斷*· [site](https://vladimiracunadev-create.github.io/human-genome-labs/) |

<a id="forks"></a>

## 🍴 第三方專案的 fork (52)

這些是保存在本帳號中的他人專案 fork。**它們不是我的原創作品**：功勞屬於原作者，不計入本檔案的任何數字，每則說明僅概述原專案自身的聲明，並不代表我提供支援、稽核或具備正式環境經驗。說明依據原專案 · 2026-11-09。

### 🤖 編碼代理與代理框架 (18)

| Fork | 原專案 | 語言 | 簡介 |
|---|---|---|---|
| [**OpenHands**](https://github.com/vladimiracunadev-create/OpenHands) | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | TypeScript | AI 驅動的軟體開發代理平台 |
| [**cline**](https://github.com/vladimiracunadev-create/cline) | [cline/cline](https://github.com/cline/cline) | TypeScript | 以 SDK、IDE 擴充或 CLI 形式提供的自主編碼代理 |
| [**opencode**](https://github.com/vladimiracunadev-create/opencode) | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 開源編碼代理 |
| [**qwen-code**](https://github.com/vladimiracunadev-create/qwen-code) | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | TypeScript | 面向終端機的開源 AI 編碼代理 |
| [**goose**](https://github.com/vladimiracunadev-create/goose) | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Rust | 可擴充代理，可用任意 LLM 安裝、執行、編輯並測試程式碼 |
| [**pi**](https://github.com/vladimiracunadev-create/pi) | [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | 代理工具包：統一 LLM API、代理迴圈、TUI 與編碼 CLI |
| [**hermes-agent**](https://github.com/vladimiracunadev-create/hermes-agent) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | 與你一同成長的代理（NousResearch） |
| [**deepagents**](https://github.com/vladimiracunadev-create/deepagents) | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Python | 「開箱即用」的代理框架（LangChain） |
| [**crewAI**](https://github.com/vladimiracunadev-create/crewAI) | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | 編排扮演角色之自主代理的框架 |
| [**agent-framework**](https://github.com/vladimiracunadev-create/agent-framework) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Python | 微軟用於建構並部署代理與多代理工作流程的框架，支援 Python 與 .NET |
| [**deepseek-harness**](https://github.com/vladimiracunadev-create/deepseek-harness) | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | TypeScript | DeepSeek 代理框架，一切皆外掛 |
| [**agent-orchestrator**](https://github.com/vladimiracunadev-create/agent-orchestrator) | [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Go | 規劃、執行並監督代理叢集，從任務到合併 PR |
| [**orca**](https://github.com/vladimiracunadev-create/orca) | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 管理編碼代理叢集的工作區（桌面、行動與遠端） |
| [**kander**](https://github.com/vladimiracunadev-create/kander) | [dualface/kander](https://github.com/dualface/kander) | Go | 看板，以隔離的 git worktree 與審查代理協調編碼代理 |
| [**OpenBot**](https://github.com/vladimiracunadev-create/OpenBot) | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | TypeScript | AI 同事，各自擁有獨立電腦；每個動作事前決定、事後記錄 |
| [**browser-use**](https://github.com/vladimiracunadev-create/browser-use) | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | 讓 AI 代理操作瀏覽器的 Python 函式庫 |
| [**agent-desktop**](https://github.com/vladimiracunadev-create/agent-desktop) | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Rust | 面向 AI 代理的 computer use CLI |
| [**treg**](https://github.com/vladimiracunadev-create/treg) | [superdesigndev/treg](https://github.com/superdesigndev/treg) | Python | 「面向代理工具的 OpenRouter」 |

### 🧩 面向代理的技能、外掛與工作流程 (11)

| Fork | 原專案 | 語言 | 簡介 |
|---|---|---|---|
| [**claude-plugins-official**](https://github.com/vladimiracunadev-create/claude-plugins-official) | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | 由 Anthropic 管理的 Claude Code 優質外掛官方目錄 |
| [**agentic-awesome-skills**](https://github.com/vladimiracunadev-create/agentic-awesome-skills) | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | Python | 本機控制平面，用於探索、選擇並驗證大型 agentic 技能目錄（CLI、本機 MCP、外掛） |
| [**claude-review-all**](https://github.com/vladimiracunadev-create/claude-review-all) | [ncoevoet/claude-review-all](https://github.com/ncoevoet/claude-review-all) | Python | 面向 Claude Code 的多代理程式碼審查 |
| [**blender-skills**](https://github.com/vladimiracunadev-create/blender-skills) | [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | TypeScript | 面向編碼代理的 Blender 專業技能，以 MCP 驅動的流程 |
| [**diagram-design**](https://github.com/vladimiracunadev-create/diagram-design) | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 面向編碼代理的編輯級圖表設計（HTML + SVG） |
| [**elephant-goldfish-model**](https://github.com/vladimiracunadev-create/elephant-goldfish-model) | [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) | Python | Google 開放技能，用於借助 AI 代理設計與審查軟體 |
| [**Claude-Code-Game-Studios**](https://github.com/vladimiracunadev-create/Claude-Code-Game-Studios) | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | 把 Claude Code 變成由協同代理組成的遊戲工作室 |
| [**headcount**](https://github.com/vladimiracunadev-create/headcount) | [cbrock84/headcount](https://github.com/cbrock84/headcount) | Markdown | 像公司一樣組織的代理體系：部門與可安裝技能 |
| [**agentic-qe**](https://github.com/vladimiracunadev-create/agentic-qe) | [proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) | TypeScript | 開放的 QA/QE 平台，代理與技能涵蓋軟體全生命週期 |
| [**OpenExecutive**](https://github.com/vladimiracunadev-create/OpenExecutive) | [SenteLabsAI/OpenExecutive](https://github.com/SenteLabsAI/OpenExecutive) | Python | 虛擬管理團隊：由 8 個專業 Claude 代理支撐的一位管理者形象 |
| [**n8n-mcp**](https://github.com/vladimiracunadev-create/n8n-mcp) | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | TypeScript | 讓 Claude、Cursor 或 Windsurf 建立 n8n 工作流程的 MCP 伺服器 |

### 🛡️ 資安與軟體分析 (8)

| Fork | 原專案 | 語言 | 簡介 |
|---|---|---|---|
| [**raptor**](https://github.com/vladimiracunadev-create/raptor) | [gadievron/raptor](https://github.com/gadievron/raptor) | Python | 把 Claude Code 變成攻防兼備的資安代理 |
| [**Cybersecurity-Projects**](https://github.com/vladimiracunadev-create/Cybersecurity-Projects) | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | Go | 70 個由淺入深的資安專案 |
| [**SkillSpector**](https://github.com/vladimiracunadev-create/SkillSpector) | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Python | NVIDIA 的代理技能資安掃描器（提示注入、資料外洩、供應鏈） |
| [**Anthropic-Cybersecurity-Skills**](https://github.com/vladimiracunadev-create/Anthropic-Cybersecurity-Skills) | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | 數百個面向代理的資安技能，對應 MITRE ATT&CK、NIST CSF 等框架 |
| [**security-audit-skill**](https://github.com/vladimiracunadev-create/security-audit-skill) | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | Cloudflare 的多階段資安稽核技能，結論經獨立驗證 |
| [**siteone-crawler**](https://github.com/vladimiracunadev-create/siteone-crawler) | [janreges/siteone-crawler](https://github.com/janreges/siteone-crawler) | Rust | 面向 SEO、資安、無障礙與效能的網站爬取與分析工具 |
| [**rea**](https://github.com/vladimiracunadev-create/rea) | [morluto/rea](https://github.com/morluto/rea) | TypeScript | 藉由代理進行逆向工程，從應用程式行為到原生二進位檔 |
| [**craft-anything**](https://github.com/vladimiracunadev-create/craft-anything) | [storytold/craft-anything](https://github.com/storytold/craft-anything) | Rust | 弄懂任何軟體如何運作，並打造自己的軟體 |

### 🧠 AI 模型與基礎設施 (5)

| Fork | 原專案 | 語言 | 簡介 |
|---|---|---|---|
| [**marin**](https://github.com/vladimiracunadev-create/marin) | [marin-community/marin](https://github.com/marin-community/marin) | Python | 面向基礎模型研究與開發的開放框架 |
| [**prime-rl**](https://github.com/vladimiracunadev-create/prime-rl) | [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) | Python | 大規模代理式強化學習訓練 |
| [**Olmo-core**](https://github.com/vladimiracunadev-create/Olmo-core) | [allenai/Olmo-core](https://github.com/allenai/Olmo-core) | Python | OLMo 生態系統的 PyTorch 基礎模組 |
| [**DeepInfer**](https://github.com/vladimiracunadev-create/DeepInfer) | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | Python | 面向 DeepSeek 模型的高效能大規模推論框架 |
| [**heretic**](https://github.com/vladimiracunadev-create/heretic) | [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | 無需重新訓練即可修改語言模型（審查、諂媚等） |

### 🏢 企業管理與平台 (6)

| Fork | 原專案 | 語言 | 簡介 |
|---|---|---|---|
| [**erpnext**](https://github.com/vladimiracunadev-create/erpnext) | [frappe/erpnext](https://github.com/frappe/erpnext) | Python | 自由開源的 ERP |
| [**odoo**](https://github.com/vladimiracunadev-create/odoo) | [odoo/odoo](https://github.com/odoo/odoo) | Python | 開源企業應用 |
| [**mautic**](https://github.com/vladimiracunadev-create/mautic) | [mautic/mautic](https://github.com/mautic/mautic) | PHP | 開源行銷自動化 |
| [**crm**](https://github.com/vladimiracunadev-create/crm) | [trycompai/crm](https://github.com/trycompai/crm) | TypeScript | 為 AI 代理設計的開源 CRM（Comp AI） |
| [**harness**](https://github.com/vladimiracunadev-create/harness) | [harness/harness](https://github.com/harness/harness) | Go | 端到端開發平台：程式碼管理、CI/CD、環境與製品庫 |
| [**traccar**](https://github.com/vladimiracunadev-create/traccar) | [traccar/traccar](https://github.com/traccar/traccar) | Java | 開源 GPS 追蹤平台，支援 200 多種裝置協定 |

### 🎓 教育與參考 (4)

| Fork | 原專案 | 語言 | 簡介 |
|---|---|---|---|
| [**computer-science**](https://github.com/vladimiracunadev-create/computer-science) | [ossu/computer-science](https://github.com/ossu/computer-science) | HTML | 免費電腦科學自學路徑（OSSU） |
| [**math**](https://github.com/vladimiracunadev-create/math) | [ossu/math](https://github.com/ossu/math) | — | 免費數學自學路徑（OSSU） |
| [**manim**](https://github.com/vladimiracunadev-create/manim) | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Python | 社群維護的數學動畫 Python 框架 |
| [**asm-atari-2600**](https://github.com/vladimiracunadev-create/asm-atari-2600) | [johnidm/asm-atari-2600](https://github.com/johnidm/asm-atari-2600) | Assembly | Atari 2600 遊戲組合語言範例原始碼 |
