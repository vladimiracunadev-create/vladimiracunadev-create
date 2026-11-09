# 🛠️ Panduan evaluasi teknis

[← Mulai dari mana](../START_HERE.id.md) · [Español](TECH_LEAD.md) · [English](TECH_LEAD.en.md) · [Português](TECH_LEAD.pt.md) · [Italiano](TECH_LEAD.it.md) · [Français](TECH_LEAD.fr.md) · [简体中文](TECH_LEAD.zh.md) · [繁體中文](TECH_LEAD.zh-TW.md) · [日本語](TECH_LEAD.ja.md) · [한국어](TECH_LEAD.ko.md) · [Türkçe](TECH_LEAD.tr.md) · [Русский](TECH_LEAD.ru.md) · [Tiếng Việt](TECH_LEAD.vi.md) · [ไทย](TECH_LEAD.th.md) · [Deutsch](TECH_LEAD.de.md) · [Українська](TECH_LEAD.uk.md) · [Polski](TECH_LEAD.pl.md) · [العربية](TECH_LEAD.ar.md) · [فارسی](TECH_LEAD.fa.md) · **Bahasa Indonesia** · [Nederlands](TECH_LEAD.nl.md) · [हिन्दी](TECH_LEAD.hi.md) · [Ελληνικά](TECH_LEAD.el.md)

## Dalam satu baris

Anda tidak perlu membaca kode untuk menilai cara saya berpikir: cukup lihat apa yang bisa dijalankan, apa yang diuji, dan apa yang dinyatakan tertunda.

## Empat jalur 10 menit

| Jalur | Untuk melihat… | Cara |
|---|---|---|
| **A. Observabilitas dan orkestrasi** | Workflow, metrik, dasbor, dan guardrail pada 20 kasus dan 18+ mesin basis data | `git clone https://github.com/vladimiracunadev-create/social-bot-scheduler.git` |
| **B. Infrastruktur yang dapat direproduksi** | Laboratorium kontainer menyala dalam hitungan menit | `git clone https://github.com/vladimiracunadev-create/docker-labs.git` |
| **C. Agen berstatus bertipe** | 25 backend LangGraph, DEMO/LIVE, rantai penyimpanan barang bukti | `git clone https://github.com/vladimiracunadev-create/langgraph-realworld.git` |
| **D. Produk forensik dalam Rust** | Installer dan biner dengan checksum, tanpa clone | [Rilis RootCause](https://github.com/vladimiracunadev-create/rootcause-windows-inspector/releases) |

## Sinyal kualitas yang dapat Anda verifikasi

| Sinyal | Di mana melihat |
|---|---|
| Tes | GabySQL dengan 850 tes dan fuzz 503,8 juta kueri tanpa panic; Empresa Operativa Chile dengan 230 tes; Automa dengan 150 pytest |
| Rantai pasok | CodeQL, Semgrep, Bandit, Trivy, Grype, Gitleaks, TruffleHog, SBOM CycloneDX, dan Scorecard, sesuai repositori |
| Telemetri | Nol pada produk forensik dan di Empresa Operativa Chile, diverifikasi di setiap build |
| Distribusi | Rilis dengan checksum dan bukti build; penandatanganan komersial dinyatakan tertunda |
| Kejujuran | Setiap repositori menyatakan statusnya dan apa yang **tidak** dilakukannya |

Semua angka beserta sumbernya ada di [Status Dapat Diverifikasi](../../README.id.md#status-dapat-diverifikasi).

## Cara saya merancang

- **Dari model ke luar:** domain dahulu, antarmuka sebagai proyeksi.
- **Observabilitas sejak hari pertama:** `/health`, `/ready`, `/metrics`, dan ketertelusuran.
- **Ketahanan nyata:** idempotensi, circuit breaker, dan degradasi terkendali.
- **Poliglot secara desain:** bahasa dan mesin dipilih per kasus penggunaan.
- **DX lebih dulu:** `doctor` dan `smoke` per repositori; jika tidak mudah dijalankan, tidak layak jadi dasar tim.

## Untuk mendalami

- [Tumpukan teknologi](../../README.id.md#-tumpukan-teknologi) yang terdeteksi di repositori.
- [Lihat ekosistem lengkap](../ECOSYSTEM.id.md): setiap produk dengan versi, tes, dan rilisnya.
- Fork pihak ketiga dipisahkan dan tidak dihitung sebagai karya sendiri: [Fork proyek pihak ketiga](../ECOSYSTEM.id.md#forks).

## Langkah berikutnya

Untuk tinjauan arsitektur atau percakapan teknis, tulis ke [vladimir.acuna.dev@gmail.com](mailto:vladimir.acuna.dev@gmail.com).
