# راهنمای مشارکت

**زبان‌ها:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

سپاس از اینکه به مشارکت در این اکوسیستم فکر می‌کنید. چون این مجموعه بر پایهٔ **مشاهده‌پذیری**، **تکرارپذیری**، **کیفیت local-first** و **idempotency** طراحی شده است، انتظارات بالایی از یکپارچگی کد داریم تا این نمونه‌کارها همچنان بازتابی از مهندسی مدرن باشد.

## مشارکت‌هایی که از آن‌ها استقبال می‌کنیم

- 🐛 **رفع اشکال:** مشکلات شناسایی‌شده را حل کنید، ترجیحاً با یک آزمون خودکار (`pytest` و مانند آن) که درستی رفع را ثابت کند.
- 🚀 **قابلیت‌های جدید:** بهبودهای معماری و یکپارچه‌سازی‌های تازه، مثلاً با n8n، Ollama یا LangGraph.
- 📖 **مستندات:** توضیحات روشن‌تر، ترجمه‌ها یا نمودارهای معماری صریح (Mermaid یا draw.io).
- 🏗️ **زیرساخت:** بهبود گردش‌کارهای DevOps (Kubernetes، CI/CD، Makefile و پیکربندی PWA).

## گردش کار (Git Flow)

این پروژه از یک گردش کار استاندارد مبتنی بر شاخهٔ ویژگی (feature-branch) استفاده می‌کند:

1. مخزن را به حساب خود **Fork** کنید.
2. برای ویژگی یا رفع اشکال خود از آخرین شاخهٔ `main` **یک شاخه بسازید**:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. تغییر خود را **توسعه دهید**.
   - از رویکرد جاافتادهٔ مخزن پیروی کنید. اگر برای گردش‌کارهای پرسرعت Python از `uv` استفاده می‌کند، جز با توجیه تغییر، آن را جایگزین نکنید.
   - سازوکارهای محافظ (guardrail) موجود پروژه را اجرا کنید.
4. تغییرات خود را **Commit** کنید. ما از **Conventional Commits** (مانند `feat:`، `fix:`، `docs:`، `chore:`) استفاده می‌کنیم:

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. شاخهٔ خود را **Push** کنید:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. یک **Pull Request (PR)** به شاخهٔ `main` این مخزن باز کنید.

## استانداردهای کد

- **توسعهٔ آزمون‌محور (اختیاری اما توصیه‌شده):** دستورهای اجرای آزمون‌های خود را بیاورید. اگر مخزن GitHub Actions برای `mypy` یا `bandit` دارد، مطمئن شوید تغییرات شما به‌صورت محلی موفق می‌شود (`make test`، `make lint` یا اسکریپت‌های موجود در اکوسیستم).
- **Docker در اولویت:** هر وابستگی لازم باید مستند و از طریق `docker-compose.yml` در دسترس باشد تا معماری در کمتر از ۶۰ ثانیه راه‌اندازی شود یا از اصطکاک غیرضروری راه‌اندازی محلی پرهیز شود.
- **مستندسازی الزامی است:** برای تغییرات بزرگ، README را به‌روز کنید و در صورت لزوم نموداری توضیحی بیفزایید.
