# 🛠️ Teknik değerlendirme rehberi

[← Nereden başlamalı](../START_HERE.tr.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · **Türkçe** · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · [Bahasa Indonesia](TECH_LEAD.id.md) · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## Tek satırda

Nasıl düşündüğümü anlamak için kod okumanız gerekmez: nelerin çalıştırılabildiğini, nelerin test edildiğini ve nelerin bekleyen olarak beyan edildiğini görmeniz yeter.

## 10 dakikalık dört yol

| Yol | Görmek için… | Nasıl |
|---|---|---|
| **A. Gözlemlenebilirlik ve orkestrasyon** | 20 vaka ve 18+ veritabanı motoru üzerinde iş akışları, metrikler, panolar ve korkuluklar | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Tekrarlanabilir altyapı** | Dakikalar içinde ayağa kalkan konteyner laboratuvarları | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Tipli durumlu ajanlar** | 25 LangGraph arka ucu, DEMO/LIVE, gözetim zinciri | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Rust ile adli ürün** | Sağlama toplamlı kurucular ve ikili dosyalar, klonlamadan | [RootCause sürümleri](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Doğrulayabileceğiniz kalite sinyalleri

| Sinyal | Nereye bakmalı |
|---|---|
| Testler | GabySQL 850 test ve panik olmayan 503,8 milyon sorgulu fuzz; Empresa Operativa Chile 230 test; Automa 150 pytest |
| Tedarik zinciri | Depoya göre CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, CycloneDX SBOM ve Scorecard |
| Telemetri | Adli ürünlerde ve Empresa Operativa Chile'de sıfır, her derlemede doğrulanır |
| Dağıtım | Sağlama toplamları ve derleme kanıtlı sürümler; ticari imzalama bekleyen olarak beyan edilmiştir |
| Dürüstlük | Her depo durumunu ve neyi **yapmadığını** belirtir |

Kaynaklı tüm rakamlar [Doğrulanabilir durum](../../README.tr.md#doğrulanabilir-durum) içindedir.

## Nasıl tasarlarım

- **Modelden dışarıya:** önce alan, arayüz bir izdüşüm olarak.
- **İlk günden gözlemlenebilirlik:** `/health`, `/ready`, `/metrics` ve izlenebilirlik.
- **Gerçek dayanıklılık:** idempotentlik, circuit breaker ve kontrollü bozulma.
- **Tasarımdan çok dilli:** dil ve motor kullanım senaryosuna göre seçilir.
- **Önce DX:** her depoda `doctor` ve `smoke`; kolay çalışmıyorsa ekip tabanı olarak işe yaramaz.

## Daha derine inmek için

- Depolarda tespit edilen [Teknoloji yığını](../../README.tr.md#-teknoloji-yığını).
- [Ekosistemin tamamını gör](../ECOSYSTEM.tr.md): her ürün sürümü, testleri ve sürümüyle.
- Üçüncü taraf fork'lar ayrı tutulur ve kendi eseri sayılmaz: [Üçüncü taraf projelerin fork'ları](../ECOSYSTEM.tr.md#forks).

## Sonraki adım

Mimari incelemesi veya teknik bir görüşme için [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com) adresine yazın.
