# 🗂️ エコシステム：プロダクト、ラボ、応用AI、科学計算

[← プロフィールに戻る](../README.ja.md)

**🌐** [Español](ECOSYSTEM.md) · [English](ECOSYSTEM.en.md) · [Português](ECOSYSTEM.pt.md) · [Italiano](ECOSYSTEM.it.md) · [Français](ECOSYSTEM.fr.md) · [简体中文](ECOSYSTEM.zh.md) · [繁體中文](ECOSYSTEM.zh-TW.md) · **日本語** · [한국어](ECOSYSTEM.ko.md) · [Türkçe](ECOSYSTEM.tr.md) · [Русский](ECOSYSTEM.ru.md) · [Tiếng Việt](ECOSYSTEM.vi.md) · [ไทย](ECOSYSTEM.th.md) · [Deutsch](ECOSYSTEM.de.md) · [Українська](ECOSYSTEM.uk.md) · [Polski](ECOSYSTEM.pl.md) · [العربية](ECOSYSTEM.ar.md) · [فارسی](ECOSYSTEM.fa.md) · [Bahasa Indonesia](ECOSYSTEM.id.md) · [Nederlands](ECOSYSTEM.nl.md) · [हिन्दी](ECOSYSTEM.hi.md) · [Ελληνικά](ECOSYSTEM.el.md)

このプロフィールの実践的な成果は独立したドキュメントにまとめています。ダウンロードしてインストールできるソフトウェア、エンジニアリングラボ、応用AI、科学計算に加え、アカウント内にあるサードパーティプロジェクトの各フォークの説明も含みます。

## 📦実質の配分を用いるプロダクト

ダウンロード、インストール、および使用中のソフトウェアは、クローン化されるだけでなく、

| 産品展示 | とりあえず | スタック | 配達: |
|---|---|---|---|
| [🔍 **RootCause Windows**](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) | サイバーセキュリティフォレンジック: あらゆる異常リソースの歪みは、脅威の最初の兆候かもしれません。 診断 最初に、後で介入 | コース🦀 ·ETW/WPRの特長 | **...............................................................................................................................................................................................................................................................** · **16 リリース** · **5 エディション**: GUI の·ポータブル·おすすめ·パワーシェル·VSコード· [landing](https://vladimiracunadev-create.github.io/rootcause-windows-inspector/) |
| [📱 **RootCause Mobile**](https://github.com/vladimiracunadev-create/rootcause-mobile-inspector) | モバイル・シブル:各アプリを単独と比較するフォレンジックセンサー、ストークウェアのフラグ、および与えられた権限を単に要求したものから分離する | フラッタ·コルテリン·Swift の | **..0 の .** ·検証可能なAndroid APK·5 の言語· **ゼロテレメトリー** · [landing](https://vladimiracunadev-create.github.io/rootcause-mobile-inspector/) |
| [🍎 **RootCause macOS**](https://github.com/vladimiracunadev-create/rootcause-macos-inspector) | macOS edition: `launchd` persistence, Gatekeeper, SIP, FileVault, XProtect, TCC permissions, signed processes, and network neighbors — every surface checked against a known-good state | Rust 🦀 · macOS 13+ | **v0.1.0** · first published release · Apache-2.0 · [landing](https://vladimiracunadev-create.github.io/rootcause-macos-inspector/) |
| [🖥️ **RootCause Server**](https://github.com/vladimiracunadev-create/rootcause-server) | サーバのシブル:単一のログが一緒に見ていないもの、露出された表面、アクセスアテンプトバースト、同じアドレス、重要なファイル完全性、センサーのサイレンスに付与されたセッションを相関し、それを1つの実用的な文に変える | コース🦀 ·ウィンドウズ·リリース·マックオース | **.2.0 の** · **18 ルール**証拠とランブック·自らの行動を決して実行しない·ウェブ依存関係のないローカルコンソール· **公開されていないリリースはまだありません** · [landing](https://vladimiracunadev-create.github.io/rootcause-server/) |
| [🌐 **RootCause Web**](https://github.com/vladimiracunadev-create/rootcause-web-inspector) | ブラウザのフォレンジックセンサー:クッキー、メールセッション、拡張機能、ダウンロード、パーミッション、および実際のウィンドウを模倣するページ | コンテンツ·MV3 拡張子 | **.2.0 の** ·公開されていないリリースはまだありません·パネル`127.0.0.1` ·ゼロ依存関係·CIで検証されたゼロテレメトリー· [landing](https://vladimiracunadev-create.github.io/rootcause-web-inspector/) |
| [₿ **RootCause Bitcoin Defense**](https://github.com/vladimiracunadev-create/rootcause-bitcoin-defense) | ビットコインの保管のための時計だけ防衛:各キーの起源を発明し、公開された警告でそれをクロスチェックし、証拠と根本的な原因を説明します | コンテンツ·Windowsアプリ·ローカル パネル | **.3.0 の** · **2 リリース** ·ゼロ依存関係·種子を要求しない·CIで検証· [landing](https://vladimiracunadev-create.github.io/rootcause-bitcoin-defense/) |
| [⛓️ **RootCause Blockchain Security**](https://github.com/vladimiracunadev-create/rootcause-blockchain-security) | マルチチェーンの監視のみコンソール: 在庫契約、プロキシ、オラクル、ブリッジ、ガバナンス、および依存関係、ルート・ヒューズのランブックを生成し、 | コンテンツ·Windowsアプリ·ローカル パネル | **.3.0 の**リポジトリに·公開リリース:`v0.1.0` ·ゼロ依存関係·プライベートキーを要求しない·CIで検証· [landing](https://vladimiracunadev-create.github.io/rootcause-blockchain-security/) |
| [📷 **RootCause QR Inspector**](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) | 行動する前にQRコードを検査するためのローカルAndroidアプリ:26信号を説明し、偽物から事実を分離し、赤字の証拠をエクスポートします | フラッタ·ダーツ | **..4 .** · **5 リリース** · **107テスト** ·公開されたAndroid APK·検証可能なSHA-256·技術的なAPKパッケージ署名; 進行中の商業/ストア署名·ゼロテレメトリー· [landing](https://vladimiracunadev-create.github.io/rootcause-qr-inspector/) |
| [🏢 **Empresa Operativa Chile**](https://github.com/vladimiracunadev-create/empresa-operativa-chile) | 毎月のクローズに組み込まれる前に、SPA をガイド: 証拠、VAT の持ち方、F29 ドラフト、不変なクローズ、および監査ログと組み込む。 正規のソースにすべての規則がポイント | コンテンツ·コース·プワワ | **.5.0 の v1.5.0** ·アンドロイド·ウィンドウズ·ブラウザ· **158 件のテスト** · **0 生産の依存性** ·ゼロテレメトリー· [landing](https://vladimiracunadev-create.github.io/empresa-operativa-chile/) |
| [🔍 **Universal Code Scanner**](https://github.com/vladimiracunadev-create/universal-code-scanner) | QR とバーコードリーダー**演技前の解釈**: 16 ローカル URL の危険信号と明示的な確認 | フラッタ·ダーツ | **.1.0 の v1.1.0 の** ·アンドロイド·スマートフォン·マックオース·プワワ·暗号化された履歴**AES-256-GCM(オプション)** · [landing](https://vladimiracunadev-create.github.io/universal-code-scanner/) |
| [🗄️ **GabySQL**](https://github.com/vladimiracunadev-create/gabysql) | 組み込みデータベース: シングル`.db`ファイル名、WAL、コストベース最適化、HTTP/JSON API | コース🦀 | ウィンドウズ·マックオース·リリース· [landing](https://vladimiracunadev-create.github.io/gabysql/) |
| [🤖 **Automa PC**](https://github.com/vladimiracunadev-create/automa-pc) | ローカルオーケストレーター:JSON は、実際のウィンドウを開き、DOM とやり取りし、証拠を残している | フィードバック·プレイライト·pywebview の使い方 | **.3.0 の** · **27 流れ** ·公開および検証可能なインストーラ· [landing](https://vladimiracunadev-create.github.io/automa-pc/) |
| [🏭 **AI Dataset Foundry**](https://github.com/vladimiracunadev-create/ai-dataset-foundry) | PDF、Word、Web、Git、JSON、CSVを事前トレーニング、微調整、RAG、評価のための監査可能なデータセットに変換するローカルファースト工場 | フィードバック | **.2.0 の** ·Windows + オフライン Android·初公開リリース· [landing](https://vladimiracunadev-create.github.io/ai-dataset-foundry/) |
| [☁️ **AWS Desktop Studio**](https://github.com/vladimiracunadev-create/aws-desktop-studio) | ローカルファーストアプリで15 AWSインベントリの統合、20 のチュートリアル、CLI/SSO、および読み取り専用デフォルト; 進捗の実装、ユニバーサルアクセスではなく | コンテンツ·ウィンドウズ | **.1. .** ·初公開リリース· [landing](https://vladimiracunadev-create.github.io/aws-desktop-studio/) |
| [🧭 **Commerce OS**](https://github.com/vladimiracunadev-create/commerce-operating-system) | 商用操作の概念のデモ:カタログ、株式、CRM、注文、モック支払い、およびトレーサビリティ | コンテンツ·コンテンツ·ウィンドウズ·アンドロイド | **.3.0 の** · **2 リリース** ·実際のお金やチリの税務当局の統合はありません· [landing](https://vladimiracunadev-create.github.io/commerce-operating-system/) |
| [📄 **PDF Reader**](https://github.com/vladimiracunadev-create/pdf-reader-windows-android) | アンドロイド初のローカル読み取り専用リーダー、無作物ズーム、再オープン可能な履歴、WhatsApp共有、および既定のリーダー選択 | コンテンツ·コンテンツ·アンドロイド·ウィンドウズ | **..3 .** ·署名されたAPK·口座、機密権限、またはテレメトリーなし· [landing](https://vladimiracunadev-create.github.io/pdf-reader-windows-android/) |
| [🎙️ **Video Transcript Studio**](https://github.com/vladimiracunadev-create/video-transcript-studio) | ワンビデオ、プレイリスト、または**YouTubeチャンネル全体**タイムスタンプでテキストに。 既存の字幕に依存しません。 ウィスパーは、オーディオを認識**お使いのマシンで**、API、アカウント、またはキーを構成しないで | フィードバック·ピシド6·速いAPI·より高速ホイスパー | **.2.0 の** ·Windowsデスクトップ+ローカルパネル`127.0.0.1`+ クライアント**同じキューを共有** ·ダイバーシティ·パンフレット·TXT(TXT)·エスアールティ·ヴィット·ジェイソン·エムピー・スリー·トピックス· **89 件のテスト** ·バンドル FFmpeg·ゼロテレメトリー· [landing](https://vladimiracunadev-create.github.io/video-transcript-studio/) |
| [🎨 **ChofyAI Studio**](https://github.com/vladimiracunadev-create/chofyai-studio) | ローカルクリエイティブAIランチャー:Qwen3-TTS、Whysper.cpp、FaceFusion、AceForge、ComfyUIをオーケスト | 田栗 2·コース·反応する | .1 の v0.5.1· **実際の推論の5/5ツール** ·macOS Apple シリコン·実験的なWindows· **公開されていないリリースはまだありません** · [site](https://vladimiracunadev-create.github.io/chofyai-studio/) |
| [🦏 **Rhino Suite**](https://github.com/vladimiracunadev-create/rhino-suite) | 文書ルールは DOM に依存しない - HTML は単なる投影である | ラースト/WASM·おすすめ·反応 19 | フェーズによる進化単球· [landing](https://vladimiracunadev-create.github.io/rhino-suite/) |
| [🎻 **My Violin Adventure**](https://github.com/vladimiracunadev-create/violin-adventure) | 子供のための教育アプリ: クロマチックチューナー、オーディオクロック-正確メトロノーム、本物のバイオリンと曲 | 田栗 2·反応する·ツイート | **.3.0 の v1.3.0** ·ウィンドウズ·アンドロイド·リリース·マックオース·プワワ· [landing](https://vladimiracunadev-create.github.io/violin-adventure/) |
| [🎸 **My Guitar Adventure**](https://github.com/vladimiracunadev-create/guitarra-adventure) | plucked-string の兄弟: 6 の世界の 24 のレッスン、6 弦のチューナー、漂流なしのメトロノーム、および 11 実質のギターのノート | 田栗 2·反応する·ツイート | **.0.0 の** ·ウィンドウズ·アンドロイド·リリース·マックオース·スマートフォン·プワワ·口座、広告、またはオンラインの依存関係なし· [landing](https://vladimiracunadev-create.github.io/guitarra-adventure/) |
| [🧣 **Pañuelo al Viento**](https://github.com/vladimiracunadev-create/panuelo-al-viento-cueca-app) | 10歳からCueca: 8レベル、24クラス、72アクティビティ、6パルスラボ(3 + 3、2 + 2 + 2)、およびアクセス可能なフロア図。 それを述べる**補完、置換しない**, 教師と文化のベアラー | フラッタ·ダーツ | **.2.0 の** ·アンドロイド 7+·ウィンドウズ 10/11·ツイート·エクスクルーシブ·エムシー·ポータブル· **29 個のテスト + 2 個のバリデータ** ·カメラ、マイク、アカウント、広告、インターネットなし· [landing](https://vladimiracunadev-create.github.io/panuelo-al-viento-cueca-app/) |

## 🧪エンジニアリング研究所

| リポジトリ | 何が実証するか |
|---|---|
| [🐳 **Problem-Driven Systems Lab**](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) | **20 実際の問題**(負荷、N+1、再試行嵐、漏れ、モノリス、キャッシュスタンプ、バックプレッシャー、ゼロダウンタイム移行、DLQを忘れた)、高忠実度注入障害で解決**7 スタック**: PHP 8 の·フィードバック·Node.js の使い方·Java 21 の·.NET 8 の特長· **ゴー 1.23** · **ラースト 1.83** · [landing](https://vladimiracunadev-create.github.io/problem-driven-systems-lab/) |
| [📆 **Social Bot Scheduler**](https://github.com/vladimiracunadev-create/social-bot-scheduler) | **...............................................................................................................................................................................................................................................................** · **20件**source→n8n→receiver オーバーオーバー**18 + DBエンジン** —**19 業務**, 個別にドッカーで監査**8層**監査、出没ガードレール、遮断器、DLQ· [landing](https://vladimiracunadev-create.github.io/social-bot-scheduler/) |
| [🧰 **Microsistemas**](https://github.com/vladimiracunadev-create/microsistemas) | **12 の診断および近代化の microapps**PHP の·ローカル読み取り専用MCPサーバー·3相硬化症· [landing](https://vladimiracunadev-create.github.io/microsistemas/) |
| [🧪 **Docker Labs**](https://github.com/vladimiracunadev-create/docker-labs) | **13 の実験室**4つのサービスプラットフォーム+自動化`.exe`インストーラーとランチャー· [landing](https://vladimiracunadev-create.github.io/docker-labs/) |
| [🐳 **WSL Labs**](https://github.com/vladimiracunadev-create/wsl-labs) | **12 件**にほんご`wslc`、 ネイティブWSLコンテナエンジン —**Dockerデスクトップなし** · [landing](https://vladimiracunadev-create.github.io/wsl-labs/) |
| [⚡ **Unikernel Labs**](https://github.com/vladimiracunadev-create/unikernel-labs) | 「ドッカーデスクトップユニカネル」: WindowsはWSL2のバックエンドが付いているUnikraft上の制御を、`kraft`電子メール: qEMU· [landing](https://vladimiracunadev-create.github.io/unikernel-labs/) |
| [🧰 **QEMU/KVM Labs**](https://github.com/vladimiracunadev-create/qemu-kvm-labs) | **12 の実験室**QEMU、KVM、libvirt、クラウド・インシット、および`vm-manager`Linux と WSL2 の· [landing](https://vladimiracunadev-create.github.io/qemu-kvm-labs/) |
| [🛡️ **Sandbox Labs**](https://github.com/vladimiracunadev-create/sandbox-labs) | Linux の分離: 宣言されたポリシーの下でサードパーティのコード、ファイル、およびビジネス モデルを実行します。**署名された証拠を発し、実際に適用された制御をします** · **36 件**2つの家族で —15 の技術と 21 の資本市場 —·実験的・教育的宣言、*セキュリティ製品ではない*· [landing](https://vladimiracunadev-create.github.io/sandbox-labs/) |
| [💳 **Universal Payments Engineering Lab**](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) | **28 支払家族**ローカルの自己表現のデモ: 状態、レジャー、調整、セキュリティ、および実装ガイド· [landing](https://vladimiracunadev-create.github.io/universal-payments-engineering-lab/) |
| [🕹️ **Decentraland Social Arcade**](https://github.com/vladimiracunadev-create/decentraland-social-arcade) | ネイティブ・デカルトランド・ソーシャル3D体験: 1つのMVPとSDK7、ECS、TypeScriptのマルチゲームアーキテクチャ·スペイン語のドキュメント·支払いやテレメトリーなし |
| [☁️ **AWS Projects**](https://github.com/vladimiracunadev-create/proyectos-aws) | Progressive cases where each one adds one AWS service **and** a new GitHub Actions capability · SAA-C03 · DVA-C02 · SOA-C02 coverage |

## 🤖応用AI

| リポジトリ | 何が実証するか |
|---|---|
| [🤖 **LangGraph RealWorld**](https://github.com/vladimiracunadev-create/langgraph-realworld) | **25/25 操作バックエンド**— 型の状態、条件付きルート、NDJSON ストリーミング、DEMO/LIVE モード、8 セキュリティーレイヤー、SHA-256 チェーンのクラスト |
| [🧭 **Operational AI Agents**](https://github.com/vladimiracunadev-create/operational-ai-agents) | **13 業務委託業者**クロードコードと互換性のあるランタイム:それぞれが完全なミッションを受け取ります。リポジトリの進化、レガシーモダナイゼーション、カリキュラム設計、ポートフォリオの公開、セキュリティの修正、インシデント分析、宣言された契約、人門、および検証可能な証拠· **39 の決定的な楕円** ·34 件のテスト·ゼロ・デプス(stdlibのみ)·リリース·マックオース·ウィンドウズ· [site](https://vladimiracunadev-create.github.io/operational-ai-agents/) |
| [🧠 **MCP + Ollama Local**](https://github.com/vladimiracunadev-create/mcp-ollama-local) | ローカルファーストAIとMCPツールをサンドボックスに· `127.0.0.1`ビーコン·多層信頼のプロフィール·限界について正直に |
| [🧩 **Agentic Plugins Toolkit**](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) | **6 の有剤のプラグイン**ロードコード、OpenAI/Codex、Copilot、Gemini、MCP に 1 つのソースからインストール可能:`repository-engineering`, `legacy-modernization`, `learning-program-studio`, `product-evolution`, `portfolio-governance`と と と と 、`rootcause-response` · **69 ドリフトなしの生成されたビュー**—各ランタイムは、同じ契約からその形式を受け取ります。·ゼロデプス·リリース·マックオース·ウィンドウズ· [site](https://vladimiracunadev-create.github.io/agentic-plugins-toolkit/) |
| [🧰 **Claude Skills Toolkit**](https://github.com/vladimiracunadev-create/claude-skills-toolkit) | **15 代理スキル**クラウデコード· **セキュリティー**: 12層`security-audit`ログアウト·ケベック·EPSS(エプス)·ツイート·コンテナ·秘密)14段`bitcoin-custody-audit` · **リポジトリゲート**: `pre-commit-guard`, `pre-push-guard`, `yaml-control`, `md-lint-fix`, `python-lint-guard` · **カンファレンス**: `repo-coherence-audit`, `version-bump`, `python-version-control`, `python-deps-pinning` · **ドッカー**: `docker-cleanup`, `docker-compose-doctor` · **ドキュメント**: `md-to-doc` ·ゼロデプス·クロスプラットフォーム |
| [🧰 **Codex Skills Toolkit**](https://github.com/vladimiracunadev-create/codex-skills-toolkit) | **19 代理スキル**Codex: セキュリティとサプライチェーン、プレッライト、機能フロー、レジリエンス、状態、リリースの証拠、Python/YAML/Markdownゲート、バージョン管理、依存関係、ドッカー、ドキュメント·Python 優先· `pnpm` ·リリース·マックオース·ウィンドウズ· [site](https://vladimiracunadev-create.github.io/codex-skills-toolkit/) |

## 🔬科学コンピューティング

| リポジトリ | 何が実証するか |
|---|---|
| [🧬 **Human Genome Labs**](https://github.com/vladimiracunadev-create/human-genome-labs) | 再現性ゲノムプラットフォーム:タイプ`ScientificResult<T>`契約、FASTA/GFF3/VCF、モジュールと**明示的な成熟度と証拠**. 放射性正直: *それは臨床診断を実行しません*· [site](https://vladimiracunadev-create.github.io/human-genome-labs/) |

<a id="forks"></a>

## 🍴 サードパーティプロジェクトのフォーク (52)

このアカウントに保管している他者のプロジェクトのフォークです。**自作ではありません**。功績は元の作者にあり、このプロフィールのどの数値にも含めません。各説明は元プロジェクトが自ら宣言している内容の要約であり、サポート、監査、自身の本番運用経験を意味するものではありません。説明は元プロジェクトに基づく · 2026-11-09。

### 🤖 コーディングエージェントとエージェントフレームワーク (18)

| フォーク | 元プロジェクト | 言語 | 概要 |
|---|---|---|---|
| [**OpenHands**](https://github.com/vladimiracunadev-create/OpenHands) | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | TypeScript | AI駆動のソフトウェア開発のためのエージェントプラットフォーム |
| [**cline**](https://github.com/vladimiracunadev-create/cline) | [cline/cline](https://github.com/cline/cline) | TypeScript | SDK・IDE拡張・CLIとして使える自律型コーディングエージェント |
| [**opencode**](https://github.com/vladimiracunadev-create/opencode) | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | オープンソースのコーディングエージェント |
| [**qwen-code**](https://github.com/vladimiracunadev-create/qwen-code) | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | TypeScript | ターミナル向けオープンソースAIコーディングエージェント |
| [**goose**](https://github.com/vladimiracunadev-create/goose) | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Rust | 任意のLLMでコードのインストール・実行・編集・テストを行う拡張可能なエージェント |
| [**pi**](https://github.com/vladimiracunadev-create/pi) | [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | エージェントツールキット：統合LLM API、エージェントループ、TUI、コーディングCLI |
| [**hermes-agent**](https://github.com/vladimiracunadev-create/hermes-agent) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | あなたとともに成長するエージェント（NousResearch） |
| [**deepagents**](https://github.com/vladimiracunadev-create/deepagents) | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Python | 「電池付き」のエージェントハーネス（LangChain） |
| [**crewAI**](https://github.com/vladimiracunadev-create/crewAI) | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | 役割を持つ自律エージェントを統率するフレームワーク |
| [**agent-framework**](https://github.com/vladimiracunadev-create/agent-framework) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Python | Pythonと.NETでエージェントやマルチエージェントのワークフローを構築・展開するMicrosoftのフレームワーク |
| [**deepseek-harness**](https://github.com/vladimiracunadev-create/deepseek-harness) | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | TypeScript | すべてがプラグインのDeepSeekエージェントハーネス |
| [**agent-orchestrator**](https://github.com/vladimiracunadev-create/agent-orchestrator) | [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Go | エージェント群をタスクからマージ済みPRまで計画・実行・監督 |
| [**orca**](https://github.com/vladimiracunadev-create/orca) | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | コーディングエージェント群を扱うワークスペース（デスクトップ・モバイル・リモート） |
| [**kander**](https://github.com/vladimiracunadev-create/kander) | [dualface/kander](https://github.com/dualface/kander) | Go | 分離したgit worktreeとレビュアーエージェントでコーディングエージェントを調整するカンバン |
| [**OpenBot**](https://github.com/vladimiracunadev-create/OpenBot) | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | TypeScript | 各自が専用コンピュータを持つAI同僚。すべての操作は事前に決定され、事後に記録される |
| [**browser-use**](https://github.com/vladimiracunadev-create/browser-use) | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | ブラウザを操作するAIエージェント向けPythonライブラリ |
| [**agent-desktop**](https://github.com/vladimiracunadev-create/agent-desktop) | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Rust | AIエージェント向けのcomputer use CLI |
| [**treg**](https://github.com/vladimiracunadev-create/treg) | [superdesigndev/treg](https://github.com/superdesigndev/treg) | Python | 「エージェントツール版OpenRouter」 |

### 🧩 エージェント向けスキル・プラグイン・ワークフロー (11)

| フォーク | 元プロジェクト | 言語 | 概要 |
|---|---|---|---|
| [**claude-plugins-official**](https://github.com/vladimiracunadev-create/claude-plugins-official) | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | Anthropicが管理する高品質なClaude Codeプラグインの公式ディレクトリ |
| [**agentic-awesome-skills**](https://github.com/vladimiracunadev-create/agentic-awesome-skills) | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | Python | 大規模なagenticスキルのカタログを発見・選択・検証するローカルコントロールプレーン（CLI、ローカルMCP、プラグイン） |
| [**claude-review-all**](https://github.com/vladimiracunadev-create/claude-review-all) | [ncoevoet/claude-review-all](https://github.com/ncoevoet/claude-review-all) | Python | Claude Code向けマルチエージェントコードレビュー |
| [**blender-skills**](https://github.com/vladimiracunadev-create/blender-skills) | [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | TypeScript | コーディングエージェント向けのBlender専門スキル（MCPベースのパイプライン） |
| [**diagram-design**](https://github.com/vladimiracunadev-create/diagram-design) | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | コーディングエージェント向けのエディトリアル図解デザイン（HTML + SVG） |
| [**elephant-goldfish-model**](https://github.com/vladimiracunadev-create/elephant-goldfish-model) | [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) | Python | AIエージェントでソフトウェアを設計・レビューするためのGoogleのオープンスキル |
| [**Claude-Code-Game-Studios**](https://github.com/vladimiracunadev-create/Claude-Code-Game-Studios) | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | Claude Codeを連携するエージェントのゲームスタジオに変える |
| [**headcount**](https://github.com/vladimiracunadev-create/headcount) | [cbrock84/headcount](https://github.com/cbrock84/headcount) | Markdown | 会社のように構成したエージェント組織：部門とインストール可能なスキル |
| [**agentic-qe**](https://github.com/vladimiracunadev-create/agentic-qe) | [proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) | TypeScript | ソフトウェアのライフサイクル全体をエージェントとスキルで支えるオープンなQA/QEプラットフォーム |
| [**OpenExecutive**](https://github.com/vladimiracunadev-create/OpenExecutive) | [SenteLabsAI/OpenExecutive](https://github.com/SenteLabsAI/OpenExecutive) | Python | 仮想の経営チーム：8つの専門Claudeエージェントが支える一人の経営者像 |
| [**n8n-mcp**](https://github.com/vladimiracunadev-create/n8n-mcp) | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | TypeScript | Claude・Cursor・Windsurfにn8nワークフローを構築させるMCPサーバー |

### 🛡️ セキュリティとソフトウェア解析 (8)

| フォーク | 元プロジェクト | 言語 | 概要 |
|---|---|---|---|
| [**raptor**](https://github.com/vladimiracunadev-create/raptor) | [gadievron/raptor](https://github.com/gadievron/raptor) | Python | Claude Codeを攻撃・防御の両面を担うセキュリティエージェントに変える |
| [**Cybersecurity-Projects**](https://github.com/vladimiracunadev-create/Cybersecurity-Projects) | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | Go | 初級から上級までの70のサイバーセキュリティプロジェクト |
| [**SkillSpector**](https://github.com/vladimiracunadev-create/SkillSpector) | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Python | エージェントスキル向けNVIDIAのセキュリティスキャナ（プロンプトインジェクション、情報流出、サプライチェーン） |
| [**Anthropic-Cybersecurity-Skills**](https://github.com/vladimiracunadev-create/Anthropic-Cybersecurity-Skills) | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | MITRE ATT&CK、NIST CSFなどに対応付けたエージェント向けサイバーセキュリティスキル数百件 |
| [**security-audit-skill**](https://github.com/vladimiracunadev-create/security-audit-skill) | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 独立検証された所見を伴う多段階セキュリティ監査のためのCloudflareのスキル |
| [**siteone-crawler**](https://github.com/vladimiracunadev-create/siteone-crawler) | [janreges/siteone-crawler](https://github.com/janreges/siteone-crawler) | Rust | SEO・セキュリティ・アクセシビリティ・性能のためのWebサイトクローラー兼アナライザー |
| [**rea**](https://github.com/vladimiracunadev-create/rea) | [morluto/rea](https://github.com/morluto/rea) | TypeScript | エージェントによるリバースエンジニアリング。アプリの挙動からネイティブバイナリまで |
| [**craft-anything**](https://github.com/vladimiracunadev-create/craft-anything) | [storytold/craft-anything](https://github.com/storytold/craft-anything) | Rust | あらゆるソフトウェアの仕組みを理解し、自分のものを作る |

### 🧠 AIモデルとインフラ (5)

| フォーク | 元プロジェクト | 言語 | 概要 |
|---|---|---|---|
| [**marin**](https://github.com/vladimiracunadev-create/marin) | [marin-community/marin](https://github.com/marin-community/marin) | Python | 基盤モデルの研究開発のためのオープンなフレームワーク |
| [**prime-rl**](https://github.com/vladimiracunadev-create/prime-rl) | [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) | Python | 大規模なエージェント型強化学習トレーニング |
| [**Olmo-core**](https://github.com/vladimiracunadev-create/Olmo-core) | [allenai/Olmo-core](https://github.com/allenai/Olmo-core) | Python | OLMoエコシステム向けのPyTorch構成要素 |
| [**DeepInfer**](https://github.com/vladimiracunadev-create/DeepInfer) | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | Python | DeepSeekモデル向けの高性能・大規模推論フレームワーク |
| [**heretic**](https://github.com/vladimiracunadev-create/heretic) | [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | 再学習なしで言語モデルを改変（検閲、迎合など） |

### 🏢 企業経営とプラットフォーム (6)

| フォーク | 元プロジェクト | 言語 | 概要 |
|---|---|---|---|
| [**erpnext**](https://github.com/vladimiracunadev-create/erpnext) | [frappe/erpnext](https://github.com/frappe/erpnext) | Python | 自由なオープンソースERP |
| [**odoo**](https://github.com/vladimiracunadev-create/odoo) | [odoo/odoo](https://github.com/odoo/odoo) | Python | オープンソースの業務アプリ |
| [**mautic**](https://github.com/vladimiracunadev-create/mautic) | [mautic/mautic](https://github.com/mautic/mautic) | PHP | オープンソースのマーケティングオートメーション |
| [**crm**](https://github.com/vladimiracunadev-create/crm) | [trycompai/crm](https://github.com/trycompai/crm) | TypeScript | AIエージェント向けに設計されたオープンソースCRM（Comp AI） |
| [**harness**](https://github.com/vladimiracunadev-create/harness) | [harness/harness](https://github.com/harness/harness) | Go | ソース管理・CI/CD・環境・アーティファクトレジストリを備えたエンドツーエンドの開発プラットフォーム |
| [**traccar**](https://github.com/vladimiracunadev-create/traccar) | [traccar/traccar](https://github.com/traccar/traccar) | Java | オープンソースのGPS追跡プラットフォーム。200以上のデバイスプロトコルに対応 |

### 🎓 教育とリファレンス (4)

| フォーク | 元プロジェクト | 言語 | 概要 |
|---|---|---|---|
| [**computer-science**](https://github.com/vladimiracunadev-create/computer-science) | [ossu/computer-science](https://github.com/ossu/computer-science) | HTML | コンピュータサイエンスの無料独学パス（OSSU） |
| [**math**](https://github.com/vladimiracunadev-create/math) | [ossu/math](https://github.com/ossu/math) | — | 数学の無料独学パス（OSSU） |
| [**manim**](https://github.com/vladimiracunadev-create/manim) | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Python | 数学アニメーション用のコミュニティ製Pythonフレームワーク |
| [**asm-atari-2600**](https://github.com/vladimiracunadev-create/asm-atari-2600) | [johnidm/asm-atari-2600](https://github.com/johnidm/asm-atari-2600) | Assembly | Atari 2600ゲームのアセンブリ版サンプルソース |
