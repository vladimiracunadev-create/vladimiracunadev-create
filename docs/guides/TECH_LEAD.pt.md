# 🛠️ Guia de avaliação técnica

[← Por onde começar](../START_HERE.pt.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · **Português** · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## Em uma linha

Não é preciso ler código para julgar como penso: basta ver o que pode ser executado, o que é testado e o que é declarado como pendente.

## Quatro rotas de 10 minutos

| Rota | Para ver… | Como |
|---|---|---|
| **A. Observabilidade e orquestração** | Workflows, métricas, dashboards e guardrails em 20 casos e mais de 18 motores de BD | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Infraestrutura reproduzível** | Laboratórios de contêineres no ar em minutos | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Agentes com estado tipado** | 25 backends LangGraph, DEMO/LIVE, cadeia de custódia | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Produto forense em Rust** | Instaladores e binários com checksums, sem clonar | [Releases do RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Sinais de qualidade que você pode verificar

| Sinal | Onde olhar |
|---|---|
| Testes | GabySQL com 850 testes e fuzz de 503,8 M de queries sem panics; Empresa Operativa Chile com 230 testes; Automa com 150 pytest |
| Cadeia de suprimentos | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, SBOM CycloneDX e Scorecard, conforme o repositório |
| Telemetria | Zero nos produtos forenses e em Empresa Operativa Chile, verificada em cada build |
| Distribuição | Releases com checksums e evidência de build; assinaturas comerciais declaradas como pendentes |
| Honestidade | Cada repositório declara seu estado e o que **não** faz |

Todos os números, com sua fonte, estão em [Estado Verificável](../../README.pt.md#-estado-verificável).

## Como projeto

- **Do modelo para fora:** o domínio primeiro, a interface como projeção.
- **Observabilidade desde o dia 1:** `/health`, `/ready`, `/metrics` e rastreabilidade.
- **Resiliência real:** idempotência, circuit breaker e degradação controlada.
- **Poliglota por design:** linguagem e motor escolhidos por caso de uso.
- **DX primeiro:** `doctor` e `smoke` por repositório; se não roda fácil, não serve como base de equipe.

## Para aprofundar

- [Stack tecnológico](../../README.pt.md#-stack-tecnológico) detectado nos repositórios.
- [Ver o ecossistema completo](../ECOSYSTEM.pt.md): cada produto com sua versão, testes e release.
- Os forks de terceiros ficam à parte e não contam como obra própria: [Forks de projetos de terceiros](../ECOSYSTEM.pt.md#forks).

## Próximo passo

Para uma revisão de arquitetura ou uma conversa técnica, escreva para [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
