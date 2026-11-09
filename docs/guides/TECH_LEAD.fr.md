# 🛠️ Guide d'évaluation technique

[← Par où commencer](../START_HERE.fr.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · **Français** · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## En une ligne

Nul besoin de lire du code pour juger ma façon de penser : il suffit de voir ce qui s'exécute, ce qui est testé et ce qui est déclaré en suspens.

## Quatre parcours de 10 minutes

| Parcours | Pour voir… | Comment |
|---|---|---|
| **A. Observabilité et orchestration** | Workflows, métriques, tableaux de bord et garde-fous sur 20 cas et plus de 18 moteurs de BD | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Infrastructure reproductible** | Laboratoires de conteneurs lancés en quelques minutes | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Agents à état typé** | 25 backends LangGraph, DEMO/LIVE, chaîne de custodie | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Produit forensique en Rust** | Installeurs et binaires avec checksums, sans cloner | [Releases de RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Signaux de qualité vérifiables

| Signal | Où regarder |
|---|---|
| Tests | GabySQL avec 850 tests et un fuzz de 503,8 M de requêtes sans panic ; Empresa Operativa Chile avec 230 tests ; Automa avec 150 pytest |
| Chaîne d'approvisionnement | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, SBOM CycloneDX et Scorecard, selon le dépôt |
| Télémétrie | Zéro dans les produits forensiques et dans Empresa Operativa Chile, vérifiée à chaque build |
| Distribution | Releases avec checksums et preuves de build ; signatures commerciales déclarées en attente |
| Honnêteté | Chaque dépôt déclare son état et ce qu'il **ne** fait **pas** |

Tous les chiffres avec leur source se trouvent dans [État Vérifiable](../../README.fr.md#-état-vérifiable).

## Ma façon de concevoir

- **Du modèle vers l'extérieur :** le domaine d'abord, l'interface comme projection.
- **Observabilité dès le premier jour :** `/health`, `/ready`, `/metrics` et traçabilité.
- **Résilience réelle :** idempotence, circuit breaker et dégradation contrôlée.
- **Polyglotte par conception :** langage et moteur choisis selon le cas d'usage.
- **DX d'abord :** `doctor` et `smoke` par dépôt ; si cela ne s'exécute pas facilement, ce n'est pas une bonne base d'équipe.

## Pour aller plus loin

- [Stack technologique](../../README.fr.md#-stack-technologique) détecté dans les dépôts.
- [Voir l'écosystème complet](../ECOSYSTEM.fr.md) : chaque produit avec sa version, ses tests et sa release.
- Les forks de tiers sont séparés et ne comptent pas comme œuvre propre : [Forks de projets tiers](../ECOSYSTEM.fr.md#forks).

## Prochaine étape

Pour une revue d'architecture ou un échange technique, écrivez à [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
