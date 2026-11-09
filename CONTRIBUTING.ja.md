# コントリビューションガイド

**言語：** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

このエコシステムへの貢献をご検討いただきありがとうございます。**可観測性**、**再現性**、**ローカルファーストの品質**、**冪等性**を軸に設計されているため、このポートフォリオが現代的なエンジニアリングの姿を映し続けられるよう、コードの完全性には高い水準を求めています。

## 歓迎する貢献

- 🐛 **バグ修正：**確認された問題を解決してください。修正を裏付ける自動テスト（`pytest` など）があると望ましいです。
- 🚀 **新機能：**アーキテクチャの改善や、n8n、Ollama、LangGraph などとの新しい連携。
- 📖 **ドキュメント：**より分かりやすい説明、翻訳、明示的なアーキテクチャ図（Mermaid または draw.io）。
- 🏗️ **インフラ：**DevOps ワークフロー（Kubernetes、CI/CD、Makefile、PWA 設定）の改善。

## ワークフロー（Git Flow）

このプロジェクトは標準化されたフィーチャーブランチのワークフローを採用しています。

1. リポジトリを自分のアカウントに**フォーク**します。
2. 最新の `main` ブランチから、機能または修正用の**ブランチを作成**します。

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. 変更を**開発**します。
   - リポジトリの確立された方針に従ってください。高性能な Python ワークフローに `uv` を使っている場合は、変更の理由を示さない限り置き換えないでください。
   - プロジェクトの既存のガードレールを実行します。
4. 変更を**コミット**します。**Conventional Commits**（`feat:`、`fix:`、`docs:`、`chore:` など）を使用します。

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. ブランチを**プッシュ**します。

   ```bash
   git push origin feature/new-aws-magic
   ```

6. このリポジトリの `main` ブランチに対して**プルリクエスト（PR）を作成**します。

## コード基準

- **テスト駆動開発（任意ですが推奨）：**テストの実行コマンドを記載してください。リポジトリに `mypy` や `bandit` の GitHub Actions がある場合は、変更がローカルで通ることを確認してください（`make test`、`make lint`、またはエコシステム内のスクリプト）。
- **Docker ファースト：**必要な依存関係はすべて文書化し、`docker-compose.yml` で利用できるようにして、アーキテクチャが 60 秒以内に起動する、または不要なローカル設定の手間を避けられるようにしてください。
- **ドキュメントは必須：**大きな変更では README を更新し、必要に応じて説明用の図を追加してください。
