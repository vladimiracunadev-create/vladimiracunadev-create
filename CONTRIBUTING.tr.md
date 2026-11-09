# Katkı Rehberi

**Diller:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

Bu ekosisteme katkıda bulunmayı düşündüğünüz için teşekkürler. **Gözlemlenebilirlik**, **tekrarlanabilirlik**, **local-first kalite** ve **idempotency** etrafında tasarlandığından, bu portföyün modern mühendisliğin bir yansıması olarak kalması için kod bütünlüğüne yönelik beklentilerimiz yüksektir.

## Memnuniyetle karşıladığımız katkılar

- 🐛 **Hata düzeltmeleri:** Tespit edilen sorunları, tercihen düzeltmeyi kanıtlayan otomatik bir testle (`pytest` vb.) çözün.
- 🚀 **Yeni özellikler:** Mimari iyileştirmeler ve yeni entegrasyonlar; örneğin n8n, Ollama veya LangGraph ile.
- 📖 **Dokümantasyon:** Daha açık anlatımlar, çeviriler veya açık mimari diyagramları (Mermaid veya draw.io).
- 🏗️ **Altyapı:** DevOps iş akışlarında iyileştirmeler (Kubernetes, CI/CD, Makefile'lar ve PWA yapılandırması).

## İş akışı (Git Flow)

Bu proje standartlaştırılmış bir özellik dalı (feature-branch) iş akışı kullanır:

1. Depoyu hesabınıza **fork'layın**.
2. Özelliğiniz veya düzeltmeniz için en güncel `main` dalından **bir dal oluşturun**:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. Değişikliğinizi **geliştirin**.
   - Deponun yerleşik yaklaşımını izleyin. Yüksek performanslı Python iş akışları için `uv` kullanıyorsa, değişikliği gerekçelendirmeden onu değiştirmeyin.
   - Projenin mevcut güvenlik önlemlerini çalıştırın.
4. Değişikliklerinizi **commit'leyin**. **Conventional Commits** kullanıyoruz (`feat:`, `fix:`, `docs:`, `chore:` vb.):

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. Dalınızı **push'layın**:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. Bu deponun `main` dalına karşı bir **Pull Request (PR)** açın.

## Kod standartları

- **Test güdümlü geliştirme (isteğe bağlı ama önerilir):** Testlerinizi çalıştırma komutlarını ekleyin. Depoda `mypy` veya `bandit` için GitHub Actions varsa, değişikliklerinizin yerelde geçtiğinden emin olun (`make test`, `make lint` veya ekosistemdeki betikler).
- **Docker-first:** Gerekli her bağımlılık belgelenmeli ve `docker-compose.yml` üzerinden erişilebilir olmalıdır; böylece mimari 60 saniyeden kısa sürede ayağa kalkar veya gereksiz yerel kurulum sürtünmesi önlenir.
- **Dokümantasyon zorunludur:** Büyük bir değişiklikte README'yi güncelleyin ve uygunsa açıklayıcı bir diyagram ekleyin.
