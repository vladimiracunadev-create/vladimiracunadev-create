# 贡献指南

**语言：** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md)

感谢你考虑为本生态系统作出贡献。本生态以**可观测性**、**可复现性**、**本地优先质量**和**幂等性**为设计原则，因此我们对代码完整性保持较高要求，使该作品集持续体现现代工程实践。

## 我们欢迎的贡献类型

- 🐛 **修复 Bug：** 解决已发现的问题，并尽可能添加自动化测试（`pytest` 等）来证明修复有效。
- 🚀 **新增功能：** 架构改进以及与 n8n、Ollama 或 LangGraph 等工具的新集成。
- 📖 **文档：** 提升说明的清晰度、增加翻译，或补充明确的架构图（Mermaid 或 draw.io）。
- 🏗️ **基础设施：** 改进 DevOps 流程（Kubernetes、CI/CD、Makefile 和 PWA 配置）。

## 工作流程（Git Flow）

本项目采用基于功能分支的标准化流程：

1. 将仓库 **Fork** 到你的账户。
2. 从最新的 `main` 分支**创建分支**，用于功能开发或问题修复：

   ```bash
   git checkout -b feature/new-aws-magic
   # 修复可使用
   git checkout -b fix/auth-bypass
   ```

3. **开发**你的更改。
   - 遵循仓库既有方案。如果仓库在高性能 Python 工作流中使用 `uv`，请勿在没有充分理由的情况下替换它。
   - 运行项目已有的 guardrails。
4. **提交**更改。我们使用 **Conventional Commits**（`feat:`、`fix:`、`docs:`、`chore:` 等）：

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. **推送**分支：

   ```bash
   git push origin feature/new-aws-magic
   ```

6. 向本仓库的 `main` 分支发起 **Pull Request（PR）**。

## 代码标准

- **测试驱动开发（可选但推荐）：** 请提供运行测试的命令。如果仓库配置了使用 `mypy` 或 `bandit` 的 GitHub Actions，请确保更改能在本地通过（`make test`、`make lint` 或生态系统中提供的脚本）。
- **Docker-first：** 所有必需依赖都应记录在文档中，并可通过 `docker-compose.yml` 使用，使架构能在 60 秒内启动，或以其他方式减少不必要的本地配置摩擦。
- **必须更新文档：** 对于重大更改，请更新 README，并在适用时添加说明图。
