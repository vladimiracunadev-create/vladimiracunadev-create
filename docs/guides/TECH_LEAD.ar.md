# 🛠️ دليل التقييم التقني

[← من أين تبدأ](../START_HERE.ar.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · **العربية** · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## في سطر واحد

لا تحتاج إلى قراءة الشيفرة لتحكم على طريقة تفكيري: يكفي أن ترى ما يمكن تشغيله وما يُختبر وما يُعلن أنه معلّق.

## أربعة مسارات بعشر دقائق

| المسار | لتشاهد… | الطريقة |
|---|---|---|
| **A. قابلية الرصد والتنسيق** | تدفقات عمل ومقاييس ولوحات متابعة وضوابط حماية عبر 20 حالة وأكثر من 18 محرك قواعد بيانات | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. بنية تحتية قابلة لإعادة الإنتاج** | مختبرات حاويات تعمل في دقائق | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. وكلاء بحالة مُنمَّطة** | 25 واجهة خلفية LangGraph وDEMO/LIVE وسلسلة حيازة الأدلة | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. منتج جنائي رقمي بلغة Rust** | مثبّتات وملفات ثنائية مع قيم تحقق، دون استنساخ | [إصدارات RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## إشارات جودة يمكنك التحقق منها

| الإشارة | أين تنظر |
|---|---|
| الاختبارات | GabySQL بـ850 اختبارًا وتشويش (fuzz) على 503.8 مليون استعلام دون أي panic؛ وEmpresa Operativa Chile بـ230 اختبارًا؛ وAutoma بـ150 اختبار pytest |
| سلسلة التوريد | CodeQL وSemgrep وBandit وTrivy وGrype وGitleaks وTruffleHog وSBOM بصيغة CycloneDX وScorecard، بحسب المستودع |
| القياس عن بُعد | صفر في المنتجات الجنائية وفي Empresa Operativa Chile، ويُتحقَّق منه في كل بناء |
| التوزيع | إصدارات مع قيم تحقق وأدلة بناء؛ والتوقيع التجاري معلن أنه معلّق |
| الصدق | كل مستودع يذكر حالته وما **لا** يفعله |

جميع الأرقام مع مصادرها في [الحالة التي يمكن التحقق منها](../../README.ar.md#الحالة-التي-يمكن-التحقق-منها).

## كيف أصمّم

- **من النموذج إلى الخارج:** المجال أولًا والواجهة مجرد إسقاط.
- **قابلية الرصد منذ اليوم الأول:** `/health` و`/ready` و`/metrics` وقابلية التتبع.
- **مرونة حقيقية:** idempotency وcircuit breaker وتدهور مضبوط.
- **متعدد اللغات بالتصميم:** تُختار اللغة والمحرك لكل حالة استخدام.
- **تجربة المطوّر أولًا:** `doctor` و`smoke` في كل مستودع؛ وما لا يعمل بسهولة لا يصلح أساسًا للفريق.

## للتعمق أكثر

- [المكدس التقني](../../README.ar.md#-المكدس-التقني) المرصودة في المستودعات.
- [عرض المنظومة كاملة](../ECOSYSTEM.ar.md): كل منتج مع إصداره واختباراته.
- تُحفظ forks الأطراف الثالثة منفصلة ولا تُحتسب عملًا خاصًا بي: [forks لمشاريع أطراف ثالثة](../ECOSYSTEM.ar.md#forks).

## الخطوة التالية

لمراجعة معمارية أو محادثة تقنية اكتب إلى [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
