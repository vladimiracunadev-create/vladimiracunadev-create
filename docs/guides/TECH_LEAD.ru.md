# 🛠️ Руководство по технической оценке

[← С чего начать](../START_HERE.ru.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · **Русский** · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## Одной строкой

Чтобы оценить, как я думаю, читать код не нужно: достаточно увидеть, что можно запустить, что тестируется и что заявлено как незавершённое.

## Четыре маршрута по 10 минут

| Маршрут | Чтобы увидеть… | Как |
|---|---|---|
| **A. Наблюдаемость и оркестрация** | Рабочие процессы, метрики, дашборды и ограничители на 20 кейсах и 18+ СУБД | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Воспроизводимая инфраструктура** | Контейнерные лаборатории за считанные минуты | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Агенты с типизированным состоянием** | 25 бэкендов LangGraph, DEMO/LIVE, цепочка хранения | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Форензик-продукт на Rust** | Установщики и бинарные файлы с контрольными суммами, без клонирования | [Релизы RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Проверяемые признаки качества

| Признак | Где смотреть |
|---|---|
| Тесты | GabySQL — 850 тестов и фаззинг на 503,8 млн запросов без паник; Empresa Operativa Chile — 230 тестов; Automa — 150 pytest |
| Цепочка поставок | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, SBOM CycloneDX и Scorecard — в зависимости от репозитория |
| Телеметрия | Ноль в форензик-продуктах и в Empresa Operativa Chile, проверяется при каждой сборке |
| Распространение | Релизы с контрольными суммами и подтверждением сборки; коммерческие подписи заявлены как ожидающие |
| Честность | Каждый репозиторий указывает свой статус и чего он **не** делает |

Все цифры с источниками приведены в [Проверяемый статус](../../README.ru.md#проверяемый-статус).

## Как я проектирую

- **От модели наружу:** сначала предметная область, интерфейс — её проекция.
- **Наблюдаемость с первого дня:** `/health`, `/ready`, `/metrics` и прослеживаемость.
- **Настоящая устойчивость:** идемпотентность, circuit breaker и управляемая деградация.
- **Полиглот по замыслу:** язык и движок выбираются под сценарий.
- **DX прежде всего:** `doctor` и `smoke` в каждом репозитории; если не запускается легко, как основа для команды не годится.

## Где углубиться

- [Технологический стек](../../README.ru.md#-технологический-стек), обнаруженный в репозиториях.
- [Смотреть всю экосистему](../ECOSYSTEM.ru.md): каждый продукт с версией, тестами и релизом.
- Форки сторонних проектов хранятся отдельно и не считаются собственной работой: [Форки сторонних проектов](../ECOSYSTEM.ru.md#forks).

## Следующий шаг

Для архитектурного ревью или технической беседы напишите на [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
