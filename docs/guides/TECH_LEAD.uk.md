# 🛠️ Посібник із технічної оцінки

[← З чого почати](../START_HERE.uk.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · **Українська** · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## Одним рядком

Щоб оцінити, як я мислю, читати код не потрібно: досить побачити, що можна запустити, що тестується і що заявлено як незавершене.

## Чотири маршрути по 10 хвилин

| Маршрут | Щоб побачити… | Як |
|---|---|---|
| **A. Спостережуваність і оркестрація** | Робочі процеси, метрики, дашборди та обмежувачі на 20 кейсах і 18+ СУБД | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Відтворювана інфраструктура** | Контейнерні лабораторії за лічені хвилини | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Агенти з типізованим станом** | 25 бекендів LangGraph, DEMO/LIVE, ланцюг зберігання | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Форензік-продукт на Rust** | Інсталятори й бінарні файли з контрольними сумами, без клонування | [Релізи RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Ознаки якості, які можна перевірити

| Ознака | Де дивитися |
|---|---|
| Тести | GabySQL — 850 тестів і фазинг на 503,8 млн запитів без паніки; Empresa Operativa Chile — 230 тестів; Automa — 150 pytest |
| Ланцюг постачання | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, SBOM CycloneDX і Scorecard — залежно від репозиторію |
| Телеметрія | Нуль у форензік-продуктах і в Empresa Operativa Chile, перевіряється під час кожної збірки |
| Поширення | Релізи з контрольними сумами й підтвердженням збірки; комерційні підписи заявлено як очікувані |
| Чесність | Кожен репозиторій зазначає свій статус і чого він **не** робить |

Усі цифри з джерелами наведені в [Вигідний статус](../../README.uk.md#вигідний-статус).

## Як я проєктую

- **Від моделі назовні:** спершу предметна область, інтерфейс — її проєкція.
- **Спостережуваність із першого дня:** `/health`, `/ready`, `/metrics` і простежуваність.
- **Справжня стійкість:** ідемпотентність, circuit breaker і керована деградація.
- **Поліглот за задумом:** мова й рушій обираються під сценарій.
- **DX передусім:** `doctor` і `smoke` у кожному репозиторії; якщо не запускається легко, як основа для команди не годиться.

## Де заглибитися

- [Технологічний стек](../../README.uk.md#-технологічний-стек), виявлений у репозиторіях.
- [Переглянути всю екосистему](../ECOSYSTEM.uk.md): кожен продукт із версією, тестами та релізом.
- Форки сторонніх проєктів зберігаються окремо й не вважаються власною роботою: [Форки сторонніх проєктів](../ECOSYSTEM.uk.md#forks).

## Наступний крок

Для архітектурного рев'ю чи технічної розмови напишіть на [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
