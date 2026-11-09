# 🗂️ Экосистема: продукты, лаборатории, прикладной ИИ и научные вычисления

[← Назад к профилю](../README.ru.md)

**🌐** [Español](ECOSYSTEM.md) · [English](ECOSYSTEM.en.md) · [Português](ECOSYSTEM.pt.md) · [Italiano](ECOSYSTEM.it.md) · [Français](ECOSYSTEM.fr.md) · [简体中文](ECOSYSTEM.zh.md) · [繁體中文](ECOSYSTEM.zh-TW.md) · [日本語](ECOSYSTEM.ja.md) · [한국어](ECOSYSTEM.ko.md) · [Türkçe](ECOSYSTEM.tr.md) · **Русский** · [Tiếng Việt](ECOSYSTEM.vi.md) · [ไทย](ECOSYSTEM.th.md) · [Deutsch](ECOSYSTEM.de.md) · [Українська](ECOSYSTEM.uk.md) · [Polski](ECOSYSTEM.pl.md) · [العربية](ECOSYSTEM.ar.md) · [فارسی](ECOSYSTEM.fa.md) · [Bahasa Indonesia](ECOSYSTEM.id.md) · [Nederlands](ECOSYSTEM.nl.md) · [हिन्दी](ECOSYSTEM.hi.md) · [Ελληνικά](ECOSYSTEM.el.md)

Практическая работа профиля вынесена в отдельный документ: программы, которые скачивают и устанавливают, инженерные лаборатории, прикладной ИИ и научные вычисления, а также описание каждого форка сторонних проектов в аккаунте.

## 📦Продукты с реальным распределением

Программное обеспечение, которое загружается, устанавливается и используется, не только клонируется.

| Продукт | Что это такое | стек | Доставка |
|---|---|---|---|
| [🔍 **RootCause Windows**](https://github.com/vladimiracunadev-create/rootcause-windows-inspector) | Кибер-криминалистика: каждое аномальное искажение ресурсов может быть первым признаком угрозы. Сначала диагностировать, потом вмешаться. | Ржавчина🦀 ·ETW/WPR | **v0.19.0** · **16 выпусков** · **5 изданий**: ГУИ·портативный·КЛИ·PowerShell·VS код· [landing](https://vladimiracunadev-create.github.io/rootcause-windows-inspector/) |
| [📱 **RootCause Mobile**](https://github.com/vladimiracunadev-create/rootcause-mobile-inspector) | Мобильный брат: судебный датчик, который сравнивает каждое приложение с самим собой, флаги stalkerware и отделяет предоставленные разрешения от просто запрошенных. | флаттер·Котлин·Свифт | **v0.8.0** ·Проверяемый Android APK·5 языков· **нулевая телеметрия** · [landing](https://vladimiracunadev-create.github.io/rootcause-mobile-inspector/) |
| [🍎 **RootCause macOS**](https://github.com/vladimiracunadev-create/rootcause-macos-inspector) | Издание macOS:`launchd`настойчивость, Gatekeeper, SIP, FileVault, XProtect, разрешения TCC, подписанные процессы и соседи по сети — каждая поверхность проверена на соответствие известному хорошему состоянию | Ржавчина🦀 ·macOS 13+ | **v0.1.0** ·Первый опубликованный выпуск·Apache-2.0· [landing](https://vladimiracunadev-create.github.io/rootcause-macos-inspector/) |
| [🖥️ **RootCause Server**](https://github.com/vladimiracunadev-create/rootcause-server) | Серверный брат: соотносит то, что не видит ни один журнал, — открытую поверхность, всплески попытки доступа, сеанс, предоставленный тому же адресу, критическую целостность файла и тишину датчика — и превращает его в одно действующее предложение | Ржавчина🦀 ·Windows·Linux·Мако | **v0.2.0** · **18 Правила**С доказательствами и руничной книгой·Никогда не совершайте действий самостоятельно·локальная консоль без веб-зависимостей· **Пока не опубликовано ни одного** · [landing](https://vladimiracunadev-create.github.io/rootcause-server/) |
| [🌐 **RootCause Web**](https://github.com/vladimiracunadev-create/rootcause-web-inspector) | Браузерный криминалистический датчик: файлы cookie, сеансы электронной почты, расширения, загрузки, разрешения и страницы, имитирующие реальное окно | JavaScript·Расширение MV3 | **v0.2.0** ·Пока не опубликовано ни одного·панель`127.0.0.1` ·нулевая зависимость·нулевая телеметрия, проверенная в CI· [landing](https://vladimiracunadev-create.github.io/rootcause-web-inspector/) |
| [₿ **RootCause Bitcoin Defense**](https://github.com/vladimiracunadev-create/rootcause-bitcoin-defense) | Защита только от наблюдения за хранением биткойнов: инвентаризация происхождения каждого ключа, перекрестная проверка с опубликованными предупреждениями и объяснение первопричины с доказательствами | JavaScript·Приложение Windows·Местная панель | **v0.3.0** · **2 релиза** ·нулевая зависимость·Никогда не просите семена·Проверено в CI· [landing](https://vladimiracunadev-create.github.io/rootcause-bitcoin-defense/) |
| [⛓️ **RootCause Blockchain Security**](https://github.com/vladimiracunadev-create/rootcause-blockchain-security) | Многоцепочечная консоль только для часов: контракты на запасы, прокси, оракулы, мосты, управление и зависимости и генерирует рутинные книги | JavaScript·Приложение Windows·Местная панель | **v0.3.0**в репозитории·опубликованный релиз:`v0.1.0` ·нулевая зависимость·Никогда не просите приватные ключи·Проверено в CI· [landing](https://vladimiracunadev-create.github.io/rootcause-blockchain-security/) |
| [📷 **RootCause QR Inspector**](https://github.com/vladimiracunadev-create/rootcause-qr-inspector) | Местное приложение для Android для проверки QR-кодов перед действием: объясняет 26 сигналов, отделяет факты от гипотез и экспортирует отредактированные доказательства | флаттер·Дарт | **v0.1.4** · **5 выпусков** · **107 тестов** ·Издательство: Android APK·Проверяемый SHA-256·техническая подпись пакета APK; коммерческие / магазинные подписи в процессе·нулевая телеметрия· [landing](https://vladimiracunadev-create.github.io/rootcause-qr-inspector/) |
| [🏢 **Empresa Operativa Chile**](https://github.com/vladimiracunadev-create/empresa-operativa-chile) | Руководство СПА от до регистрации до каждого ежемесячного закрытия: включение с доказательствами, перенос НДС вперед, проект F29, неизменное закрытие и журнал аудита. Каждое правило указывает на свой официальный источник. | JavaScript·Ржавчина·ПВА | **v1.5.0** ·Android·Windows·браузер· **158 тестов** · **0 производственных зависимостей** ·нулевая телеметрия· [landing](https://vladimiracunadev-create.github.io/empresa-operativa-chile/) |
| [🔍 **Universal Code Scanner**](https://github.com/vladimiracunadev-create/universal-code-scanner) | QR и считыватель штрих-кода, который**толковать перед тем, как действовать**16 локальных сигналов риска URL и явное подтверждение | флаттер·Дарт | **v1.1.0** ·Android·iOS·Мако·ПВА·Зашифрованная история**AES-256-GCM** · [landing](https://vladimiracunadev-create.github.io/universal-code-scanner/) |
| [🗄️ **GabySQL**](https://github.com/vladimiracunadev-create/gabysql) | Встроенная база данных: одиночная`.db`Файл, WAL, оптимизатор на основе затрат, HTTP/JSON API | Ржавчина🦀 | Windows·Мако·Linux· [landing](https://vladimiracunadev-create.github.io/gabysql/) |
| [🤖 **Automa PC**](https://github.com/vladimiracunadev-create/automa-pc) | Местный оркестратор: потоки JSON, которые открывают реальные окна, взаимодействуют с DOM и оставляют доказательства | Python·драматург·pywebview | **v0.3.0** · **27 Поток** ·опубликованный и проверяемый установщик· [landing](https://vladimiracunadev-create.github.io/automa-pc/) |
| [🏭 **AI Dataset Foundry**](https://github.com/vladimiracunadev-create/ai-dataset-foundry) | Завод, который превращает PDF, Word, Web, Git, JSON и CSV в проверяемые наборы данных для предварительной подготовки, тонкой настройки, RAG и оценки | Python | **v0.2.0** ·Windows + оффлайн Android·Первый опубликованный выпуск· [landing](https://vladimiracunadev-create.github.io/ai-dataset-foundry/) |
| [☁️ **AWS Desktop Studio**](https://github.com/vladimiracunadev-create/aws-desktop-studio) | Приложение Local-first с 15 интеграцией инвентаря AWS, 20 учебными пособиями, CLI/SSO и по умолчанию только для чтения; реализация продолжается, а не универсальный доступ | JavaScript·Windows | **v0.1.1** ·Первый опубликованный выпуск· [landing](https://vladimiracunadev-create.github.io/aws-desktop-studio/) |
| [🧭 **Commerce OS**](https://github.com/vladimiracunadev-create/commerce-operating-system) | Руководящая концептуальная демонстрация коммерческих операций: каталог, акции, CRM, заказы, макеты платежей и прослеживаемость | JavaScript·Веб-сайт·Windows·Android | **v0.3.0** · **2 релиза** ·Отсутствие реальных денег или интеграция с налоговыми органами Чили· [landing](https://vladimiracunadev-create.github.io/commerce-operating-system/) |
| [📄 **PDF Reader**](https://github.com/vladimiracunadev-create/pdf-reader-windows-android) | Android-первый локальный читатель только для чтения, с безрезультатным зумом, повторно открываемой историей, обменом WhatsApp и выбором чтения по умолчанию | HTML·Веб-сайт·Android·Windows | **v0.3.3** ·подписанный APK·отсутствие аккаунтов, конфиденциальных разрешений или телеметрии;· [landing](https://vladimiracunadev-create.github.io/pdf-reader-windows-android/) |
| [🎙️ **Video Transcript Studio**](https://github.com/vladimiracunadev-create/video-transcript-studio) | Одно видео, плейлист или**Весь YouTube канал**Текст с метками времени. Не стоит полагаться на существующие субтитры: Whisper распознает звук**На твоей машине**без API, учетной записи или ключа для настройки | Python·PySide6·Быстрый·быстрый шепот | **v0.2.0** ·Windows desktop + локальная панель`127.0.0.1`+ CLI,**разделять одну и ту же очередь** ·MD·PDF·TXT·СТО·ВТТ·Джон·MP3·ОГГ· **89 испытаний** ·FFmpeg в комплекте·нулевая телеметрия· [landing](https://vladimiracunadev-create.github.io/video-transcript-studio/) |
| [🎨 **ChofyAI Studio**](https://github.com/vladimiracunadev-create/chofyai-studio) | Локальная творческая пусковая установка ИИ: оркеструет Qwen3-TTS, whisper.cpp, FaceFusion, AceForge и ComfyUI | Таури 2·Ржавчина·реагировать | v0.5.1· **5/5 инструменты с реальным выводом** ·MacOS Apple Silicon·Экспериментальная Windows· **Пока не опубликовано ни одного** · [site](https://vladimiracunadev-create.github.io/chofyai-studio/) |
| [🦏 **Rhino Suite**](https://github.com/vladimiracunadev-create/rhino-suite) | Office Suite с нуля: правила документов не зависят от DOM — HTML — это только проекция | Ржавчина/WASM·Иди.·Реакция 19 | Эволюционная монорепо по фазам· [landing](https://vladimiracunadev-create.github.io/rhino-suite/) |
| [🎻 **My Violin Adventure**](https://github.com/vladimiracunadev-create/violin-adventure) | Образовательное приложение для детей: хроматический тюнер, аудио-часы-точный метроном, песни с настоящей скрипкой | Таури 2·реагировать·ТС | **v1.3.0** ·Windows·Android·Linux·Мако·ПВА· [landing](https://vladimiracunadev-create.github.io/violin-adventure/) |
| [🎸 **My Guitar Adventure**](https://github.com/vladimiracunadev-create/guitarra-adventure) | Собрат с выщипанной струной: 24 урока в 6 мирах, 6-струнный тюнер, бездрифтовый метроном и 11 настоящих гитарных нот | Таури 2·реагировать·ТС | **v1.0.0** ·Windows·Android·Linux·Мако·iOS·ПВА·Нет аккаунтов, рекламы или онлайн-зависимости· [landing](https://vladimiracunadev-create.github.io/guitarra-adventure/) |
| [🧣 **Pañuelo al Viento**](https://github.com/vladimiracunadev-create/panuelo-al-viento-cueca-app) | Квека с 10 лет: 24 класса на 8 уровнях, 72 занятия, шестиимпульсная лаборатория (3+3 и 2+2+2) и доступные напольные диаграммы. Он утверждает, что**дополняет, а не заменяет**Учителя и носители культуры | флаттер·Дарт | **v0.2.0** ·Android 7+·Windows 10/11·АПХ·EXE·МГИ·портативный· **29 тестов + 2 валидатора** ·Нет камеры, микрофона, аккаунта, рекламы или Интернета· [landing](https://vladimiracunadev-create.github.io/panuelo-al-viento-cueca-app/) |

## 🧪Инженерные лаборатории

| Репо | Что это демонстрирует |
|---|---|
| [🐳 **Problem-Driven Systems Lab**](https://github.com/vladimiracunadev-create/problem-driven-systems-lab) | **20 реальных проблем**(задержка под нагрузкой, N+1, повторные штормы, утечки, монолиты, давка кэша, обратное давление, миграция с нулевым временем простоя, забытый DLQ) с высокоточными инъекционными сбоями, решенными в**7 стеков**PHP 8·Python·Node.js·Java 21·.NET 8· **Иди 1,23** · **Ржавчина 1.83** · [landing](https://vladimiracunadev-create.github.io/problem-driven-systems-lab/) |
| [📆 **Social Bot Scheduler**](https://github.com/vladimiracunadev-create/social-bot-scheduler) | **v4.10.0** · **20 случаев**Источник: ^n8n > приемник**18+ ДБ мотор** —**19 Операционная**Проверка с помощью Docker —**8-слойный**аудит, защитные ограждения от импотенции, выключатель и DLQ· [landing](https://vladimiracunadev-create.github.io/social-bot-scheduler/) |
| [🧰 **Microsistemas**](https://github.com/vladimiracunadev-create/microsistemas) | **12 диагностических и модернизационных микроприложений**для PHP·Локальный MCP-сервер только для чтения·Уплотнение в 3 фазы· [landing](https://vladimiracunadev-create.github.io/microsistemas/) |
| [🧪 **Docker Labs**](https://github.com/vladimiracunadev-create/docker-labs) | **13 Лаборатории**на 4-сервисной платформе + автоматизированный`.exe`установщик с пусковой установкой· [landing](https://vladimiracunadev-create.github.io/docker-labs/) |
| [🐳 **WSL Labs**](https://github.com/vladimiracunadev-create/wsl-labs) | **12 случаев**на`wslc`, родной контейнерный двигатель WSL -**Без Docker Desktop** · [landing](https://vladimiracunadev-create.github.io/wsl-labs/) |
| [⚡ **Unikernel Labs**](https://github.com/vladimiracunadev-create/unikernel-labs) | «Docker Desktop для юникернелей»: Контроль Windows над Unikraft с помощью WSL2 backend`kraft`+ QEMU/KVM· [landing](https://vladimiracunadev-create.github.io/unikernel-labs/) |
| [🧰 **QEMU/KVM Labs**](https://github.com/vladimiracunadev-create/qemu-kvm-labs) | **12 Лаборатории**Реальная виртуализация с QEMU, KVM, libvirt, cloud-init и`vm-manager`Linux и WSL2· [landing](https://vladimiracunadev-create.github.io/qemu-kvm-labs/) |
| [🛡️ **Sandbox Labs**](https://github.com/vladimiracunadev-create/sandbox-labs) | Изоляция Linux: запускает сторонний код, файлы и бизнес-модели в соответствии с объявленными политиками и правилами.**- эмитирует подписанные доказательства того, какие средства контроля фактически применяются** · **36 случаев**в двух семьях — 15 технических и 21 рынок капитала —·объявленный экспериментальным и образовательным, *не продукт безопасности*· [landing](https://vladimiracunadev-create.github.io/sandbox-labs/) |
| [💳 **Universal Payments Engineering Lab**](https://github.com/vladimiracunadev-create/universal-payments-engineering-lab) | **28 платных семей**в демо-версии с местным самоопределением: государства, реестр, примирение, безопасность и руководства по реализации· [landing](https://vladimiracunadev-create.github.io/universal-payments-engineering-lab/) |
| [🕹️ **Decentraland Social Arcade**](https://github.com/vladimiracunadev-create/decentraland-social-arcade) | Native Decentraland Social 3D: один MVP и многопользовательская архитектура с SDK7, ECS и TypeScript·Испанская документация·Никаких платежей или телеметрии |
| [☁️ **AWS Projects**](https://github.com/vladimiracunadev-create/proyectos-aws) | Прогрессивные случаи, когда каждый добавляет один сервис AWS**и**Новая функция GitHub Actions·САА-С03·DVA-C02·Покрытие SOA-C02 |

## 🤖Прикладной ИИ

| Репо | Что это демонстрирует |
|---|---|
| [🤖 **LangGraph RealWorld**](https://github.com/vladimiracunadev-create/langgraph-realworld) | **25/25 операционные бэкэнды**— типизированное состояние, условные маршруты, потоковая передача NDJSON, режим DEMO/LIVE, 8 уровней безопасности, цепочка хранения SHA-256 |
| [🧭 **Operational AI Agents**](https://github.com/vladimiracunadev-create/operational-ai-agents) | **13 оперативных агентов**для Claude Code и совместимых с ним сред выполнения: каждый получает полную миссию — эволюцию хранилища, модернизацию наследия, разработку учебных программ, публикацию портфолио, восстановление безопасности, анализ инцидентов — по задекларированным контрактам, человеческие ворота и поддающиеся проверке доказательства· **39 детерминированных эвалов** ·34 испытания·ноль-депс (только Stdlib)·Linux·Мако·Windows· [site](https://vladimiracunadev-create.github.io/operational-ai-agents/) |
| [🧠 **MCP + Ollama Local**](https://github.com/vladimiracunadev-create/mcp-ollama-local) | Локальный ИИ с инструментами MCP в песочнице· `127.0.0.1`связывание·Многослойный профиль доверия·Честность о своих границах |
| [🧩 **Agentic Plugins Toolkit**](https://github.com/vladimiracunadev-create/agentic-plugins-toolkit) | **6 агентурных плагинов**Установка в Claude Code, OpenAI/Codex, Copilot, Gemini и MCP из одного источника:`repository-engineering`, `legacy-modernization`, `learning-program-studio`, `product-evolution`, `portfolio-governance`и`rootcause-response` · **69 генерируемых просмотров без дрейфа**- каждая среда выполнения получает свой формат из одного и того же контракта -·нулевые глубины·Linux·Мако·Windows· [site](https://vladimiracunadev-create.github.io/agentic-plugins-toolkit/) |
| [🧰 **Claude Skills Toolkit**](https://github.com/vladimiracunadev-create/claude-skills-toolkit) | **15 агентских навыков**Клод Код (Claude Code)· **безопасность**12-слойный`security-audit`ОСВ·КЭВ·EPSS·САНТ·контейнер·Секреты) и 14-ступенчатый`bitcoin-custody-audit` · **ворот репо**: `pre-commit-guard`, `pre-push-guard`, `yaml-control`, `md-lint-fix`, `python-lint-guard` · **согласованность**: `repo-coherence-audit`, `version-bump`, `python-version-control`, `python-deps-pinning` · **Докер**: `docker-cleanup`, `docker-compose-doctor` · **документы**: `md-to-doc` ·нулевые глубины·кроссплатформенный |
| [🧰 **Codex Skills Toolkit**](https://github.com/vladimiracunadev-create/codex-skills-toolkit) | **19 агентурных навыков**для Codex: безопасность и цепочка поставок, префайт, функциональные потоки, устойчивость и состояние, доказательства выпуска, ворота Python / YAML / Markdown, версии, зависимости, Docker и документы·Python-первый· `pnpm` ·Linux·Мако·Windows· [site](https://vladimiracunadev-create.github.io/codex-skills-toolkit/) |

## 🔬Научные вычисления

| Репо | Что это демонстрирует |
|---|---|
| [🧬 **Human Genome Labs**](https://github.com/vladimiracunadev-create/human-genome-labs) | Воспроизводимая платформа геномики: типизированная`ScientificResult<T>`контракты, FASTA/GFF3/VCF, модули с**явная зрелость и доказательства**Радикальная честность: *не выполняет клинического диагноза*· [site](https://vladimiracunadev-create.github.io/human-genome-labs/) |

<a id="forks"></a>

## 🍴 Форки сторонних проектов (52)

Это форки чужих проектов, хранящиеся в этом аккаунте. **Это не моя собственная работа**: заслуга принадлежит их первоначальным авторам, они не входят ни в одну цифру этого профиля, а каждое описание пересказывает то, что заявляет исходный проект, и не подразумевает поддержки, аудита или собственного производственного опыта. Описания по исходному проекту · 2026-11-09.

### 🤖 Кодирующие агенты и фреймворки агентов (18)

| Форк | Исходный проект | Язык | Что это |
|---|---|---|---|
| [**OpenHands**](https://github.com/vladimiracunadev-create/OpenHands) | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | TypeScript | Платформа агентов для разработки ПО под управлением ИИ |
| [**cline**](https://github.com/vladimiracunadev-create/cline) | [cline/cline](https://github.com/cline/cline) | TypeScript | Автономный кодирующий агент в виде SDK, расширения IDE или CLI |
| [**opencode**](https://github.com/vladimiracunadev-create/opencode) | [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | Кодирующий агент с открытым исходным кодом |
| [**qwen-code**](https://github.com/vladimiracunadev-create/qwen-code) | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | TypeScript | Открытый ИИ-агент для написания кода в терминале |
| [**goose**](https://github.com/vladimiracunadev-create/goose) | [aaif-goose/goose](https://github.com/aaif-goose/goose) | Rust | Расширяемый агент, который устанавливает, запускает, правит и тестирует код с любой LLM |
| [**pi**](https://github.com/vladimiracunadev-create/pi) | [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | Набор инструментов агента: единый API LLM, цикл агента, TUI и CLI для кода |
| [**hermes-agent**](https://github.com/vladimiracunadev-create/hermes-agent) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python | Агент, который растёт вместе с вами (NousResearch) |
| [**deepagents**](https://github.com/vladimiracunadev-create/deepagents) | [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | Python | Обвязка для агентов «всё включено» (LangChain) |
| [**crewAI**](https://github.com/vladimiracunadev-create/crewAI) | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | Фреймворк для оркестрации автономных агентов с ролями |
| [**agent-framework**](https://github.com/vladimiracunadev-create/agent-framework) | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Python | Фреймворк Microsoft для создания и развёртывания агентов и мультиагентных процессов на Python и .NET |
| [**deepseek-harness**](https://github.com/vladimiracunadev-create/deepseek-harness) | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | TypeScript | Обвязка агентов DeepSeek, где всё является плагином |
| [**agent-orchestrator**](https://github.com/vladimiracunadev-create/agent-orchestrator) | [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Go | Планирует, запускает и контролирует флоты агентов — от задачи до слитого PR |
| [**orca**](https://github.com/vladimiracunadev-create/orca) | [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | Рабочее пространство для флота кодирующих агентов (десктоп, мобильные и удалённо) |
| [**kander**](https://github.com/vladimiracunadev-create/kander) | [dualface/kander](https://github.com/dualface/kander) | Go | Канбан-доска, координирующая кодирующих агентов с изолированными git worktree и агентами-ревьюерами |
| [**OpenBot**](https://github.com/vladimiracunadev-create/OpenBot) | [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | TypeScript | ИИ-коллеги, у каждого свой компьютер; каждое действие решается заранее и записывается после |
| [**browser-use**](https://github.com/vladimiracunadev-create/browser-use) | [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | Библиотека Python для ИИ-агентов, управляющих браузером |
| [**agent-desktop**](https://github.com/vladimiracunadev-create/agent-desktop) | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | Rust | CLI для computer use ИИ-агентов |
| [**treg**](https://github.com/vladimiracunadev-create/treg) | [superdesigndev/treg](https://github.com/superdesigndev/treg) | Python | «OpenRouter для инструментов агентов» |

### 🧩 Навыки (skills), плагины и сценарии для агентов (11)

| Форк | Исходный проект | Язык | Что это |
|---|---|---|---|
| [**claude-plugins-official**](https://github.com/vladimiracunadev-create/claude-plugins-official) | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Python | Официальный каталог качественных плагинов Claude Code под управлением Anthropic |
| [**agentic-awesome-skills**](https://github.com/vladimiracunadev-create/agentic-awesome-skills) | [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | Python | Локальная панель управления для поиска, выбора и проверки большого каталога agentic-навыков (CLI, локальный MCP, плагины) |
| [**claude-review-all**](https://github.com/vladimiracunadev-create/claude-review-all) | [ncoevoet/claude-review-all](https://github.com/ncoevoet/claude-review-all) | Python | Мультиагентное ревью кода для Claude Code |
| [**blender-skills**](https://github.com/vladimiracunadev-create/blender-skills) | [arjun988/blender-skills](https://github.com/arjun988/blender-skills) | TypeScript | Специализированные навыки Blender для кодирующих агентов с конвейером на MCP |
| [**diagram-design**](https://github.com/vladimiracunadev-create/diagram-design) | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | Редакционный дизайн диаграмм (HTML + SVG) для кодирующих агентов |
| [**elephant-goldfish-model**](https://github.com/vladimiracunadev-create/elephant-goldfish-model) | [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model) | Python | Открытые навыки Google для проектирования и ревью ПО с ИИ-агентами |
| [**Claude-Code-Game-Studios**](https://github.com/vladimiracunadev-create/Claude-Code-Game-Studios) | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | Shell | Превращает Claude Code в игровую студию из согласованных агентов |
| [**headcount**](https://github.com/vladimiracunadev-create/headcount) | [cbrock84/headcount](https://github.com/cbrock84/headcount) | Markdown | Организация агентов, устроенная как компания: отделы и устанавливаемые навыки |
| [**agentic-qe**](https://github.com/vladimiracunadev-create/agentic-qe) | [proffesor-for-testing/agentic-qe](https://github.com/proffesor-for-testing/agentic-qe) | TypeScript | Открытая платформа QA/QE с агентами и навыками на всём жизненном цикле ПО |
| [**OpenExecutive**](https://github.com/vladimiracunadev-create/OpenExecutive) | [SenteLabsAI/OpenExecutive](https://github.com/SenteLabsAI/OpenExecutive) | Python | Виртуальная команда руководителей: одна управленческая персона на базе 8 специализированных агентов Claude |
| [**n8n-mcp**](https://github.com/vladimiracunadev-create/n8n-mcp) | [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp) | TypeScript | MCP-сервер, чтобы Claude, Cursor или Windsurf строили процессы n8n |

### 🛡️ Безопасность и анализ ПО (8)

| Форк | Исходный проект | Язык | Что это |
|---|---|---|---|
| [**raptor**](https://github.com/vladimiracunadev-create/raptor) | [gadievron/raptor](https://github.com/gadievron/raptor) | Python | Превращает Claude Code в агента наступательной и оборонительной безопасности |
| [**Cybersecurity-Projects**](https://github.com/vladimiracunadev-create/Cybersecurity-Projects) | [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects) | Go | 70 проектов по кибербезопасности от начального до продвинутого уровня |
| [**SkillSpector**](https://github.com/vladimiracunadev-create/SkillSpector) | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | Python | Сканер безопасности NVIDIA для навыков агентов (инъекции промптов, эксфильтрация, цепочка поставок) |
| [**Anthropic-Cybersecurity-Skills**](https://github.com/vladimiracunadev-create/Anthropic-Cybersecurity-Skills) | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Python | Сотни навыков по кибербезопасности для агентов, сопоставленных с MITRE ATT&CK, NIST CSF и другими фреймворками |
| [**security-audit-skill**](https://github.com/vladimiracunadev-create/security-audit-skill) | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | Навык Cloudflare для многоэтапного аудита безопасности с независимо проверенными находками |
| [**siteone-crawler**](https://github.com/vladimiracunadev-create/siteone-crawler) | [janreges/siteone-crawler](https://github.com/janreges/siteone-crawler) | Rust | Краулер и анализатор сайтов для SEO, безопасности, доступности и производительности |
| [**rea**](https://github.com/vladimiracunadev-create/rea) | [morluto/rea](https://github.com/morluto/rea) | TypeScript | Обратная разработка с агентами — от поведения приложения до нативных бинарников |
| [**craft-anything**](https://github.com/vladimiracunadev-create/craft-anything) | [storytold/craft-anything](https://github.com/storytold/craft-anything) | Rust | Понять, как устроено любое ПО, и создать собственное |

### 🧠 Модели ИИ и инфраструктура (5)

| Форк | Исходный проект | Язык | Что это |
|---|---|---|---|
| [**marin**](https://github.com/vladimiracunadev-create/marin) | [marin-community/marin](https://github.com/marin-community/marin) | Python | Открытый фреймворк для исследований и разработки базовых моделей |
| [**prime-rl**](https://github.com/vladimiracunadev-create/prime-rl) | [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) | Python | Агентное обучение с подкреплением в больших масштабах |
| [**Olmo-core**](https://github.com/vladimiracunadev-create/Olmo-core) | [allenai/Olmo-core](https://github.com/allenai/Olmo-core) | Python | Строительные блоки PyTorch для экосистемы OLMo |
| [**DeepInfer**](https://github.com/vladimiracunadev-create/DeepInfer) | [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | Python | Высокопроизводительный фреймворк масштабного инференса для моделей DeepSeek |
| [**heretic**](https://github.com/vladimiracunadev-create/heretic) | [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | Модификация языковых моделей без дообучения (цензура, угодливость и др.) |

### 🏢 Управление бизнесом и платформы (6)

| Форк | Исходный проект | Язык | Что это |
|---|---|---|---|
| [**erpnext**](https://github.com/vladimiracunadev-create/erpnext) | [frappe/erpnext](https://github.com/frappe/erpnext) | Python | Свободная ERP с открытым исходным кодом |
| [**odoo**](https://github.com/vladimiracunadev-create/odoo) | [odoo/odoo](https://github.com/odoo/odoo) | Python | Бизнес-приложения с открытым исходным кодом |
| [**mautic**](https://github.com/vladimiracunadev-create/mautic) | [mautic/mautic](https://github.com/mautic/mautic) | PHP | Автоматизация маркетинга с открытым исходным кодом |
| [**crm**](https://github.com/vladimiracunadev-create/crm) | [trycompai/crm](https://github.com/trycompai/crm) | TypeScript | CRM с открытым исходным кодом, созданная для ИИ-агентов (Comp AI) |
| [**harness**](https://github.com/vladimiracunadev-create/harness) | [harness/harness](https://github.com/harness/harness) | Go | Сквозная платформа разработки: контроль кода, CI/CD, среды и реестры артефактов |
| [**traccar**](https://github.com/vladimiracunadev-create/traccar) | [traccar/traccar](https://github.com/traccar/traccar) | Java | Платформа GPS-слежения с открытым кодом, более 200 протоколов устройств |

### 🎓 Образование и справочные материалы (4)

| Форк | Исходный проект | Язык | Что это |
|---|---|---|---|
| [**computer-science**](https://github.com/vladimiracunadev-create/computer-science) | [ossu/computer-science](https://github.com/ossu/computer-science) | HTML | Бесплатный путь самообучения по информатике (OSSU) |
| [**math**](https://github.com/vladimiracunadev-create/math) | [ossu/math](https://github.com/ossu/math) | — | Бесплатный путь самообучения по математике (OSSU) |
| [**manim**](https://github.com/vladimiracunadev-create/manim) | [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | Python | Сообщественный фреймворк Python для математических анимаций |
| [**asm-atari-2600**](https://github.com/vladimiracunadev-create/asm-atari-2600) | [johnidm/asm-atari-2600](https://github.com/johnidm/asm-atari-2600) | Assembly | Примеры исходного кода игр для Atari 2600 на ассемблере |
