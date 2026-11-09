# 🛠️ 技術評估指南

[← 從哪裡開始](../START_HERE.zh-TW.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · **繁體中文** · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## 一句話

不需要閱讀程式碼就能判斷我如何思考：只需看哪些可以執行、哪些經過測試、哪些被聲明為待辦。

## 四條 10 分鐘路線

| 路線 | 查看… | 方法 |
|---|---|---|
| **A. 可觀測性與編排** | 涵蓋 20 個案例與 18 種以上資料庫引擎的工作流程、指標、儀表板與護欄 | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. 可重現的基礎設施** | 幾分鐘內啟動的容器實驗室 | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. 型別化狀態的代理** | 25 個 LangGraph 後端、DEMO/LIVE、證據保管鏈 | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Rust 鑑識產品** | 附校驗碼的安裝檔與二進位檔，無需複製 | [RootCause 發行](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## 你可以核實的品質訊號

| 訊號 | 在哪裡看 |
|---|---|
| 測試 | GabySQL 850 項測試，以及 5.038 億次查詢的模糊測試且無 panic；Empresa Operativa Chile 230 項測試；Automa 150 項 pytest |
| 供應鏈 | 視儲存庫而定，使用 CodeQL、Semgrep、Bandit、Trivy、Grype、Gitleaks、TruffleHog、CycloneDX SBOM 與 Scorecard |
| 遙測 | 鑑識類產品與 Empresa Operativa Chile 為零，每次建置都會核驗 |
| 散布 | 附校驗碼與建置證據的發行；商業簽章聲明為待辦 |
| 誠實 | 每個儲存庫都會說明自身狀態以及它**不做**什麼 |

所有附來源的數據見[可核實狀態](../../README.zh-TW.md#可核實狀態)。

## 我如何設計

- **由模型向外：**先有領域，介面只是其投影。
- **從第一天起的可觀測性：**`/health`、`/ready`、`/metrics` 與可追溯性。
- **真正的韌性：**冪等、斷路器與受控降級。
- **多語言是設計使然：**依使用情境選擇語言與引擎。
- **DX 優先：**每個儲存庫都有 `doctor` 與 `smoke`；如果無法輕鬆執行，就不適合作為團隊基礎。

## 深入了解

- 在各儲存庫中偵測到的[技術堆疊](../../README.zh-TW.md#-技術堆疊)。
- [查看完整生態系統](../ECOSYSTEM.zh-TW.md)：每個產品都有版本、測試與發行。
- 第三方 fork 另行存放，不計入自有作品：[第三方專案的 fork](../ECOSYSTEM.zh-TW.md#forks)。

## 下一步

如需架構審查或技術交流，請寫信至 [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com)。
