# Contribution Guide

**Languages:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md)

Thank you for considering contributing to this ecosystem. Because it is designed around **observability**, **reproducibility**, **local-first quality**, and **idempotency**, we maintain high expectations for code integrity so that this portfolio remains a reflection of modern engineering.

## Contributions We Welcome

- 🐛 **Bug fixes:** Resolve identified issues, preferably with an automated test (`pytest`, etc.) that proves the fix.
- 🚀 **New features:** Architectural improvements and new integrations, for example with n8n, Ollama, or LangGraph.
- 📖 **Documentation:** Clearer explanations, translations, or explicit architecture diagrams (Mermaid or draw.io).
- 🏗️ **Infrastructure:** Improvements to DevOps workflows (Kubernetes, CI/CD, Makefiles, and PWA configuration).

## Workflow (Git Flow)

This project uses a standardized feature-branch workflow:

1. **Fork** the repository to your account.
2. **Create a branch** for your feature or fix from the latest `main` branch:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. **Develop** your change.
   - Follow the repository's established approach. If it uses `uv` for high-performance Python workflows, do not replace it unless you justify the change.
   - Run the project's existing guardrails.
4. **Commit** your changes. We use **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:`, etc.):

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. **Push** your branch:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. **Open a Pull Request (PR)** against this repository's `main` branch.

## Code Standards

- **Test-driven development (optional but recommended):** Include commands for running your tests. If the repository has GitHub Actions for `mypy` or `bandit`, make sure your changes pass locally (`make test`, `make lint`, or the scripts available in the ecosystem).
- **Docker-first:** Any required dependency must be documented and available through `docker-compose.yml` so the architecture can start in under 60 seconds or otherwise avoid unnecessary local setup friction.
- **Documentation is required:** For a major change, update the README and, when applicable, add an explanatory diagram.
