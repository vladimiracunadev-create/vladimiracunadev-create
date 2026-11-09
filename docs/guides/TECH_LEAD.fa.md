# 🛠️ راهنمای ارزیابی فنی

[← از کجا شروع کنیم](../START_HERE.fa.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · **فارسی** · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## در یک خط

برای قضاوت دربارهٔ شیوهٔ فکر کردن من لازم نیست کد بخوانید: کافی است ببینید چه چیزی اجرا می‌شود، چه چیزی آزمایش می‌شود و چه چیزی معوق اعلام شده است.

## چهار مسیر ۱۰ دقیقه‌ای

| مسیر | برای دیدن… | چگونه |
|---|---|---|
| **A. مشاهده‌پذیری و هماهنگی** | گردش‌کار، سنجه‌ها، داشبوردها و guardrailها روی ۲۰ مورد و بیش از ۱۸ موتور پایگاه‌داده | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. زیرساخت تکرارپذیر** | آزمایشگاه‌های کانتینری که در چند دقیقه بالا می‌آیند | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. عامل‌هایی با وضعیت نوع‌دار** | ۲۵ بک‌اند LangGraph، DEMO/LIVE، زنجیرهٔ نگهداری شواهد | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. محصول جرم‌یابی دیجیتال با Rust** | نصب‌کننده‌ها و باینری‌ها با checksum، بدون کلون | [انتشارهای RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## نشانه‌های کیفیتی که می‌توانید بررسی کنید

| نشانه | کجا ببینید |
|---|---|
| آزمون‌ها | GabySQL با ۸۵۰ آزمون و fuzz ۵۰۳٫۸ میلیون پرس‌وجو بدون panic؛ Empresa Operativa Chile با ۲۳۰ آزمون؛ Automa با ۱۵۰ pytest |
| زنجیرهٔ تأمین | CodeQL، Semgrep، Bandit، Trivy، Grype، Gitleaks، TruffleHog، SBOM با قالب CycloneDX و Scorecard، بسته به مخزن |
| تله‌متری | صفر در محصولات جرم‌یابی و در Empresa Operativa Chile، در هر ساخت راستی‌آزمایی می‌شود |
| توزیع | انتشارهایی با checksum و شواهد ساخت؛ امضای تجاری معوق اعلام شده است |
| صداقت | هر مخزن وضعیت خود و آنچه **انجام نمی‌دهد** را اعلام می‌کند |

همهٔ ارقام همراه با منبع در [وضعیت قابل تایید](../../README.fa.md#وضعیت-قابل-تایید) آمده است.

## شیوهٔ طراحی من

- **از مدل به بیرون:** نخست دامنه، رابط فقط یک تصویر از آن است.
- **مشاهده‌پذیری از روز اول:** `/health`، `/ready`، `/metrics` و ردیابی‌پذیری.
- **تاب‌آوری واقعی:** idempotency، circuit breaker و تنزل کنترل‌شده.
- **چندزبانه بر اساس طراحی:** زبان و موتور بر اساس مورد استفاده انتخاب می‌شود.
- **DX در اولویت:** `doctor` و `smoke` برای هر مخزن؛ اگر آسان اجرا نشود، پایهٔ مناسبی برای تیم نیست.

## برای مطالعهٔ بیشتر

- [پشتهٔ فناوری](../../README.fa.md#-پشتهٔ-فناوری) شناسایی‌شده در مخزن‌ها.
- [مشاهدهٔ کل اکوسیستم](../ECOSYSTEM.fa.md): هر محصول با نسخه، آزمون‌ها و انتشارش.
- forkهای اشخاص ثالث جدا نگه داشته می‌شوند و کار شخصی به حساب نمی‌آیند: [forkهای پروژه‌های اشخاص ثالث](../ECOSYSTEM.fa.md#forks).

## گام بعدی

برای بازبینی معماری یا گفت‌وگوی فنی به [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com) بنویسید.
