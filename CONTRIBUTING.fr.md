# Guide de Contribution

**Langues :** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md)

Merci d'envisager de contribuer à cet écosystème. Comme il est conçu autour de l'**observabilité**, de la **reproductibilité**, de la **qualité local-first** et de l'**idempotence**, nous maintenons des exigences élevées en matière d'intégrité du code afin que ce portfolio reste le reflet d'une ingénierie moderne.

## Contributions Recherchées

- 🐛 **Correction de bugs :** Résolvez les problèmes identifiés, de préférence en ajoutant un test automatisé (`pytest`, etc.) qui prouve la correction.
- 🚀 **Nouvelles fonctionnalités :** Améliorations architecturales et nouvelles intégrations, par exemple avec n8n, Ollama ou LangGraph.
- 📖 **Documentation :** Explications plus claires, traductions ou diagrammes d'architecture explicites (Mermaid ou draw.io).
- 🏗️ **Infrastructure :** Améliorations des flux DevOps (Kubernetes, CI/CD, Makefiles et configuration PWA).

## Flux de Travail (Git Flow)

Ce projet utilise un flux standardisé fondé sur des branches de fonctionnalité :

1. **Forkez** le dépôt vers votre compte.
2. **Créez une branche** pour votre fonctionnalité ou correction à partir du dernier état de `main` :

   ```bash
   git checkout -b feature/nouvelle-magie-aws
   # ou pour les corrections
   git checkout -b fix/auth-bypass
   ```

3. **Développez** votre modification.
   - Suivez l'approche établie dans le dépôt. S'il utilise `uv` pour des flux Python haute performance, ne le remplacez pas sans justifier ce changement.
   - Exécutez les guardrails existants du projet.
4. **Commitez** vos modifications. Nous utilisons les **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:`, etc.) :

   ```bash
   git commit -m "feat: implémenter un circuit breaker global pour les appels en échec"
   ```

5. **Poussez** votre branche :

   ```bash
   git push origin feature/nouvelle-magie-aws
   ```

6. **Ouvrez une Pull Request (PR)** vers la branche `main` de ce dépôt.

## Standards de Code

- **Développement piloté par les tests (facultatif mais recommandé) :** Indiquez les commandes permettant d'exécuter les tests. Si le dépôt possède des GitHub Actions avec `mypy` ou `bandit`, assurez-vous que vos modifications passent localement (`make test`, `make lint` ou les scripts disponibles dans l'écosystème).
- **Docker-first :** Toute dépendance requise doit être documentée et disponible via `docker-compose.yml`, afin de démarrer l'architecture en moins de 60 secondes ou d'éviter toute friction inutile de configuration locale.
- **Documentation obligatoire :** Pour une modification majeure, mettez à jour le README et, lorsque cela s'applique, ajoutez un diagramme explicatif.
