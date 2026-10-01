# Security and Responsible Disclosure Policy

**Languages:** [ES](SECURITY.md) · [EN](SECURITY.en.md) · [PT](SECURITY.pt.md) · [IT](SECURITY.it.md) · [FR](SECURITY.fr.md) · [ZH](SECURITY.zh.md)

Security, traceability, and observability are pillars of this project ecosystem. We take every report concerning the integrity of our applications seriously.

## Supported Versions

At present, only `main`—the latest iteration or release tag—across the repositories receives direct updates and security patches. Older versions under unsupported tags are not covered unless the repository notes explicitly state otherwise.

## Reporting a Vulnerability

**Please do not report security issues through public GitHub Issues.** Doing so exposes the vulnerability to malicious actors before a patch can be released.

For security reports, critical integrity failures, or mitigable insecure defaults—such as exposed credentials, remote code execution, severe code injection, or authentication bypass—follow these steps:

1. **Send an email** directly to `vladimir.acuna.dev@gmail.com`.
2. Include:
   - The affected ecosystem or repository, for example `mcp-ollama-local` or `social-bot-scheduler`.
   - Detailed steps to reproduce the vulnerability.
   - Optionally, a proof of concept (PoC) as a script or video, when applicable.
   - The possible security impact evaluated against relevant technical standards.

I will contact you as soon as possible, generally within 48 business hours. Once the issue has been analyzed and mitigated, if you wish to be credited and the finding is verifiable, you will receive appropriate public recognition in our security reports or CHANGELOG.

Thank you for helping keep this infrastructure secure and professional.
