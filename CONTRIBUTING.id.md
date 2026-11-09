# Panduan Kontribusi

**Bahasa:** [ES](CONTRIBUTING.md) · [EN](CONTRIBUTING.en.md) · [PT](CONTRIBUTING.pt.md) · [IT](CONTRIBUTING.it.md) · [FR](CONTRIBUTING.fr.md) · [ZH](CONTRIBUTING.zh.md) · [ZH-TW](CONTRIBUTING.zh-TW.md) · [JA](CONTRIBUTING.ja.md) · [KO](CONTRIBUTING.ko.md) · [TR](CONTRIBUTING.tr.md) · [RU](CONTRIBUTING.ru.md) · [VI](CONTRIBUTING.vi.md) · [TH](CONTRIBUTING.th.md) · [DE](CONTRIBUTING.de.md) · [UK](CONTRIBUTING.uk.md) · [PL](CONTRIBUTING.pl.md) · [AR](CONTRIBUTING.ar.md) · [FA](CONTRIBUTING.fa.md) · [ID](CONTRIBUTING.id.md) · [NL](CONTRIBUTING.nl.md) · [HI](CONTRIBUTING.hi.md) · [EL](CONTRIBUTING.el.md)

Terima kasih telah mempertimbangkan untuk berkontribusi pada ekosistem ini. Karena dirancang berdasarkan **observabilitas**, **reproduksibilitas**, **kualitas local-first**, dan **idempotensi**, kami menjaga ekspektasi tinggi terhadap integritas kode agar portofolio ini tetap mencerminkan rekayasa modern.

## Kontribusi yang Kami Terima

- 🐛 **Perbaikan bug:** Selesaikan masalah yang teridentifikasi, sebaiknya dengan tes otomatis (`pytest`, dll.) yang membuktikan perbaikan tersebut.
- 🚀 **Fitur baru:** Peningkatan arsitektur dan integrasi baru, misalnya dengan n8n, Ollama, atau LangGraph.
- 📖 **Dokumentasi:** Penjelasan yang lebih jelas, terjemahan, atau diagram arsitektur eksplisit (Mermaid atau draw.io).
- 🏗️ **Infrastruktur:** Peningkatan alur kerja DevOps (Kubernetes, CI/CD, Makefile, dan konfigurasi PWA).

## Alur Kerja (Git Flow)

Proyek ini menggunakan alur kerja feature-branch yang terstandar:

1. **Fork** repositori ke akun Anda.
2. **Buat branch** untuk fitur atau perbaikan Anda dari branch `main` terbaru:

   ```bash
   git checkout -b feature/new-aws-magic
   # or for fixes
   git checkout -b fix/auth-bypass
   ```

3. **Kembangkan** perubahan Anda.
   - Ikuti pendekatan yang sudah ada di repositori. Jika menggunakan `uv` untuk alur kerja Python berkinerja tinggi, jangan menggantinya kecuali Anda membenarkan perubahan tersebut.
   - Jalankan pagar pengaman (guardrail) yang sudah ada di proyek.
4. **Commit** perubahan Anda. Kami menggunakan **Conventional Commits** (`feat:`, `fix:`, `docs:`, `chore:`, dll.):

   ```bash
   git commit -m "feat: implement global circuit breaker for failed calls"
   ```

5. **Push** branch Anda:

   ```bash
   git push origin feature/new-aws-magic
   ```

6. **Buka Pull Request (PR)** ke branch `main` repositori ini.

## Standar Kode

- **Pengembangan berbasis tes (opsional tetapi disarankan):** Sertakan perintah untuk menjalankan tes Anda. Jika repositori memiliki GitHub Actions untuk `mypy` atau `bandit`, pastikan perubahan Anda lolos secara lokal (`make test`, `make lint`, atau skrip yang tersedia di ekosistem).
- **Docker-first:** Setiap dependensi yang diperlukan harus didokumentasikan dan tersedia melalui `docker-compose.yml` agar arsitektur dapat berjalan dalam waktu kurang dari 60 detik atau menghindari hambatan pengaturan lokal yang tidak perlu.
- **Dokumentasi wajib:** Untuk perubahan besar, perbarui README dan, bila relevan, tambahkan diagram penjelas.
