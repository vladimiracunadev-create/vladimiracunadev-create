# Посібник з участі

**Мови:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

Дякуємо, що розглядаєте можливість зробити внесок у цю екосистему. Оскільки вона побудована навколо **спостережуваності**, **відтворюваності**, **local-first якості** та **ідемпотентності**, ми висуваємо високі вимоги до цілісності коду, щоб це портфоліо залишалося відображенням сучасної інженерії.

## Внески, яким ми раді

- 🐛 **Виправлення помилок:** Усувайте виявлені проблеми, бажано з автоматичним тестом (`pytest` тощо), що підтверджує виправлення.
- 🚀 **Нові можливості:** Архітектурні покращення та нові інтеграції, наприклад з n8n, Ollama або LangGraph.
- 📖 **Документація:** Зрозуміліші пояснення, переклади або явні архітектурні діаграми (Mermaid або draw.io).
- 🏗️ **Інфраструктура:** Покращення DevOps-процесів (Kubernetes, CI/CD, Makefile та конфігурація PWA).

## Робочий процес (Git Flow)

Цей проєкт використовує стандартизований процес із гілками функціональності:

1. **Зробіть форк** репозиторію у свій обліковий запис.
2. **Створіть гілку** для вашої функції чи виправлення від актуальної гілки `main`:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. **Розробіть** зміну.
   - Дотримуйтеся усталеного підходу репозиторію. Якщо він використовує `uv` для високопродуктивних процесів Python, не замінюйте його без обґрунтування.
   - Запустіть наявні в проєкті захисні перевірки.
4. **Зафіксуйте** зміни (commit). Ми використовуємо **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:` тощо):

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. **Надішліть** гілку (push):

   ```bash
   git push origin feature/new-aws-magic
   ```

6. **Відкрийте Pull Request (PR)** до гілки `main` цього репозиторію.

## Стандарти коду

- **Розробка через тестування (необов'язково, але рекомендовано):** Вкажіть команди запуску тестів. Якщо в репозиторії є GitHub Actions для `mypy` або `bandit`, переконайтеся, що зміни проходять локально (`make test`, `make lint` або скрипти екосистеми).
- **Docker-first:** Кожна потрібна залежність має бути описана й доступна через `docker-compose.yml`, щоб архітектура запускалася менш ніж за 60 секунд або іншим чином уникала зайвих труднощів локального налаштування.
- **Документація обов'язкова:** У разі значної зміни оновіть README і, коли доречно, додайте пояснювальну діаграму.
