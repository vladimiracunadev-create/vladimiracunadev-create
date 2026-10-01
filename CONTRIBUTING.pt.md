# Guia de Contribuição

**Idiomas:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md)

Obrigado por considerar contribuir para este ecossistema. Como ele foi projetado com base em **observabilidade**, **reprodutibilidade**, **qualidade local-first** e **idempotência**, mantemos expectativas elevadas sobre a integridade do código para que este portfólio continue refletindo a engenharia moderna.

## Tipos de Contribuição que Buscamos

- 🐛 **Correção de bugs:** Resolva problemas identificados, de preferência adicionando um teste automatizado (`pytest` etc.) que comprove a solução.
- 🚀 **Novas funcionalidades:** Melhorias arquiteturais e novas integrações, por exemplo com n8n, Ollama ou LangGraph.
- 📖 **Documentação:** Mais clareza, traduções ou diagramas explícitos de arquitetura (Mermaid ou draw.io).
- 🏗️ **Infraestrutura:** Melhorias nos fluxos DevOps (Kubernetes, CI/CD, Makefiles e configuração de PWA).

## Fluxo de Trabalho (Git Flow)

Este projeto usa um fluxo padronizado baseado em branches de funcionalidade:

1. **Faça um fork** do repositório para sua conta.
2. **Crie uma branch** para sua funcionalidade ou correção a partir do estado mais recente de `main`:

   ```bash
   git checkout -b feature/nova-magia-na-aws
   # ou para correções
   git checkout -b fix/auth-bypass
   ```

3. **Desenvolva** sua alteração.
   - Siga a abordagem estabelecida no repositório. Se ele usa `uv` em fluxos Python de alto desempenho, não o substitua sem justificar a mudança.
   - Execute os guardrails existentes no projeto.
4. **Faça commit** das alterações. Usamos **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:` etc.):

   ```bash
   git commit -m "feat: implementar circuit breaker global para chamadas com falha"
   ```

5. **Envie** sua branch:

   ```bash
   git push origin feature/nova-magia-na-aws
   ```

6. **Abra um Pull Request (PR)** para a branch `main` deste repositório.

## Padrões de Código

- **Desenvolvimento orientado a testes (opcional, mas recomendado):** Inclua os comandos para executar os testes. Se o repositório tiver GitHub Actions com `mypy` ou `bandit`, garanta que suas alterações passem localmente (`make test`, `make lint` ou os scripts disponíveis no ecossistema).
- **Docker-first:** Toda dependência obrigatória deve estar documentada e disponível por meio de `docker-compose.yml`, para iniciar a arquitetura em menos de 60 segundos ou evitar atrito desnecessário na configuração local.
- **Documentação obrigatória:** Em uma alteração importante, atualize o README e, quando aplicável, adicione um diagrama explicativo.
