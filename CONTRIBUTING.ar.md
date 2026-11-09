# دليل المساهمة

**اللغات:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

شكرًا لتفكيرك في المساهمة في هذه المنظومة. ولأنها مصمَّمة حول **قابلية الرصد** و**قابلية إعادة الإنتاج** و**جودة local-first** و**خاصية idempotency**، فإننا نحافظ على توقعات عالية لسلامة الشيفرة كي يبقى هذا الملف التعريفي انعكاسًا للهندسة الحديثة.

## المساهمات التي نرحّب بها

- 🐛 **إصلاح الأخطاء:** عالج المشكلات المحدَّدة، ويفضَّل أن يكون ذلك باختبار آلي (`pytest` وغيره) يثبت الإصلاح.
- 🚀 **ميزات جديدة:** تحسينات معمارية وتكاملات جديدة، مثل التكامل مع n8n أو Ollama أو LangGraph.
- 📖 **التوثيق:** شروحات أوضح، أو ترجمات، أو مخططات معمارية صريحة (Mermaid أو draw.io).
- 🏗️ **البنية التحتية:** تحسينات على مسارات DevOps (Kubernetes وCI/CD وMakefile وإعداد PWA).

## مسار العمل (Git Flow)

يعتمد هذا المشروع مسار عمل موحّدًا قائمًا على فروع الميزات:

1. **انسخ (Fork)** المستودع إلى حسابك.
2. **أنشئ فرعًا** لميزتك أو إصلاحك من أحدث فرع `main`:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. **طوِّر** تغييرك.
   - اتبع النهج المعتمد في المستودع. إن كان يستخدم `uv` لمسارات Python عالية الأداء فلا تستبدله إلا إذا برّرت التغيير.
   - شغّل ضوابط الحماية الموجودة في المشروع.
4. **أودِع (Commit)** تغييراتك. نستخدم **Conventional Commits** (`feat:` و`fix:` و`docs:` و`chore:` وغيرها):

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. **ادفع (Push)** فرعك:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. **افتح طلب سحب (PR)** إلى فرع `main` في هذا المستودع.

## معايير الشيفرة

- **التطوير الموجَّه بالاختبارات (اختياري لكنه موصى به):** أرفق أوامر تشغيل اختباراتك. إذا كان في المستودع GitHub Actions لـ `mypy` أو `bandit` فتأكد من نجاح تغييراتك محليًا (`make test` أو `make lint` أو السكربتات المتاحة في المنظومة).
- **Docker أولًا:** يجب توثيق كل اعتماد مطلوب وإتاحته عبر `docker-compose.yml` بحيث تبدأ المعمارية في أقل من 60 ثانية أو تتجنب عوائق الإعداد المحلي غير الضرورية.
- **التوثيق إلزامي:** عند إجراء تغيير كبير حدِّث README، وأضف مخططًا توضيحيًا عند الاقتضاء.
