# 🛠️ 技術評価ガイド

[← はじめに](../START_HERE.ja.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · **日本語** · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## 一言で

私の考え方を判断するのにコードを読む必要はありません。何が実行でき、何がテストされ、何が未完として明示されているかを見れば十分です。

## 10 分で見られる 4 つのルート

| ルート | 見られるもの | 方法 |
|---|---|---|
| **A. 可観測性とオーケストレーション** | 20 のケースと 18 以上の DB エンジンにわたるワークフロー、メトリクス、ダッシュボード、ガードレール | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. 再現可能なインフラ** | 数分で立ち上がるコンテナラボ | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. 型付き状態のエージェント** | 25 の LangGraph バックエンド、DEMO/LIVE、証拠保全の連鎖 | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Rust 製フォレンジックプロダクト** | チェックサム付きのインストーラーとバイナリ（クローン不要） | [RootCause のリリース](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## 検証できる品質のシグナル

| シグナル | 確認する場所 |
|---|---|
| テスト | GabySQL は 850 テストと、パニックなしの 5 億 380 万クエリのファジング。Empresa Operativa Chile は 230 テスト。Automa は 150 の pytest |
| サプライチェーン | リポジトリに応じて CodeQL、Semgrep、Bandit、Trivy、Grype、Gitleaks、TruffleHog、CycloneDX SBOM、Scorecard |
| テレメトリ | フォレンジック系プロダクトと Empresa Operativa Chile ではゼロ。ビルドごとに検証 |
| 配布 | チェックサムとビルド証拠付きのリリース。商用署名は未対応として明示 |
| 誠実さ | 各リポジトリが状態と「しないこと」を明記 |

出典付きの数値はすべて[検証可能なステータス](../../README.ja.md#検証可能なステータス)にあります。

## 設計の考え方

- **モデルから外へ：**まずドメイン、インターフェースはその投影。
- **初日からの可観測性：**`/health`、`/ready`、`/metrics`、トレーサビリティ。
- **実効性のあるレジリエンス：**冪等性、サーキットブレーカー、制御された縮退。
- **設計としてのポリグロット：**ユースケースごとに言語とエンジンを選ぶ。
- **DX 最優先：**リポジトリごとに `doctor` と `smoke`。簡単に動かせないものはチームの土台になりません。

## さらに深く知るには

- リポジトリから検出された[技術スタック](../../README.ja.md#-技術スタック)。
- [エコシステム全体を見る](../ECOSYSTEM.ja.md)：各プロダクトのバージョン、テスト、リリース。
- サードパーティのフォークは別扱いで、自作には数えません：[サードパーティプロジェクトのフォーク](../ECOSYSTEM.ja.md#forks)。

## 次のステップ

アーキテクチャレビューや技術的な会話をご希望の場合は [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com) へご連絡ください。
