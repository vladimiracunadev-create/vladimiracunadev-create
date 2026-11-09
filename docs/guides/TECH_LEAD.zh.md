# 🛠️ 技术评估指南

[← 从哪里开始](../START_HERE.zh.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · **简体中文** · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## 一句话

无需阅读代码就能判断我如何思考：只需看哪些可以运行、哪些经过测试、哪些被声明为待办。

## 四条 10 分钟路线

| 路线 | 查看… | 方法 |
|---|---|---|
| **A. 可观测性与编排** | 覆盖 20 个案例与 18 种以上数据库引擎的工作流、指标、仪表盘与护栏 | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. 可复现的基础设施** | 几分钟内启动的容器实验室 | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. 类型化状态的代理** | 25 个 LangGraph 后端、DEMO/LIVE、证据保管链 | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Rust 取证产品** | 带校验和的安装包与二进制文件，无需克隆 | [RootCause 发布](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## 你可以核实的质量信号

| 信号 | 在哪里看 |
|---|---|
| 测试 | GabySQL 850 项测试，以及 5.038 亿次查询的模糊测试且无 panic；Empresa Operativa Chile 230 项测试；Automa 150 项 pytest |
| 供应链 | 视仓库而定，使用 CodeQL、Semgrep、Bandit、Trivy、Grype、Gitleaks、TruffleHog、CycloneDX SBOM 与 Scorecard |
| 遥测 | 取证类产品与 Empresa Operativa Chile 为零，每次构建都会核验 |
| 分发 | 附校验和与构建证据的发布；商业签名声明为待办 |
| 诚实 | 每个仓库都会说明自身状态以及它**不做**什么 |

所有带来源的数据见[可验证状态](../../README.zh.md#-可验证状态)。

## 我如何设计

- **由模型向外：**先有领域，界面只是其投影。
- **从第一天起的可观测性：**`/health`、`/ready`、`/metrics` 与可追溯性。
- **真正的韧性：**幂等、断路器与受控降级。
- **多语言是设计使然：**按用例选择语言与引擎。
- **DX 优先：**每个仓库都有 `doctor` 与 `smoke`；如果不能轻松运行，就不适合作为团队基础。

## 深入了解

- 在各仓库中检测到的[技术栈](../../README.zh.md#-技术栈)。
- [查看完整生态系统](../ECOSYSTEM.zh.md)：每个产品都有版本、测试与发布。
- 第三方 fork 单独存放，不计入自有作品：[第三方项目的 fork](../ECOSYSTEM.zh.md#forks)。

## 下一步

如需架构评审或技术交流，请写信至 [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com)。
