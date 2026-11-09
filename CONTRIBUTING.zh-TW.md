# 貢獻指南

**語言：** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

感謝您考慮為這個生態系統做出貢獻。由於它以**可觀測性**、**可重現性**、**local-first 品質**與**冪等性**為核心設計，我們對程式碼完整性抱持高標準，讓這份作品集持續反映現代工程實務。

## 我們歡迎的貢獻

- 🐛 **修復錯誤：**解決已確認的問題，最好附上能證明修復有效的自動化測試（`pytest` 等）。
- 🚀 **新功能：**架構改進與新的整合，例如與 n8n、Ollama 或 LangGraph 的整合。
- 📖 **文件：**更清楚的說明、翻譯，或明確的架構圖（Mermaid 或 draw.io）。
- 🏗️ **基礎設施：**改進 DevOps 工作流程（Kubernetes、CI/CD、Makefile 與 PWA 設定）。

## 工作流程（Git Flow）

本專案採用標準化的功能分支工作流程：

1. 將儲存庫 **Fork** 到您的帳號。
2. 從最新的 `main` 分支為您的功能或修復**建立分支**：

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. **開發**您的變更。
   - 遵循儲存庫既有的作法。若其使用 `uv` 處理高效能 Python 工作流程，除非您能說明理由，否則請勿取代。
   - 執行專案既有的防護檢查。
4. **提交**（commit）您的變更。我們使用 **Conventional Commits**（`feat:`、`fix:`、`docs:`、`chore:` 等）：

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. **推送**（push）您的分支：

   ```bash
   git push origin feature/new-aws-magic
   ```

6. 對本儲存庫的 `main` 分支**開啟 Pull Request（PR）**。

## 程式碼標準

- **測試驅動開發（選用但建議）：**附上執行測試的指令。若儲存庫有 `mypy` 或 `bandit` 的 GitHub Actions，請確認您的變更能在本機通過（`make test`、`make lint` 或生態系統中提供的腳本）。
- **Docker 優先：**所有必要的相依項目都必須有文件說明，並可透過 `docker-compose.yml` 取得，讓架構能在 60 秒內啟動，或避免不必要的本機設定阻力。
- **文件為必要項目：**重大變更時請更新 README，並在適用時加入說明圖。
