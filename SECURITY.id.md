# Kebijakan Keamanan dan Pengungkapan yang Bertanggung Jawab

**Bahasa:** [ES](SECURITY.md) · [EN](SECURITY.en.md) · [PT](SECURITY.pt.md) · [IT](SECURITY.it.md) · [FR](SECURITY.fr.md) · [ZH](SECURITY.zh.md) · [ZH-TW](SECURITY.zh-TW.md) · [JA](SECURITY.ja.md) · [KO](SECURITY.ko.md) · [TR](SECURITY.tr.md) · [RU](SECURITY.ru.md) · [VI](SECURITY.vi.md) · [TH](SECURITY.th.md) · [DE](SECURITY.de.md) · [UK](SECURITY.uk.md) · [PL](SECURITY.pl.md) · [AR](SECURITY.ar.md) · [FA](SECURITY.fa.md) · [ID](SECURITY.id.md) · [NL](SECURITY.nl.md) · [HI](SECURITY.hi.md) · [EL](SECURITY.el.md)

Keamanan, ketertelusuran, dan observabilitas adalah pilar ekosistem proyek ini. Kami menanggapi setiap laporan tentang integritas aplikasi kami dengan serius.

## Versi yang Didukung

Saat ini, hanya `main` — iterasi atau tag rilis terbaru — di seluruh repositori yang menerima pembaruan langsung dan patch keamanan. Versi lama di bawah tag yang tidak didukung tidak tercakup kecuali catatan repositori menyatakan sebaliknya secara eksplisit.

## Melaporkan Kerentanan

**Mohon jangan melaporkan masalah keamanan melalui GitHub Issues publik.** Hal itu mengekspos kerentanan kepada pihak jahat sebelum patch dapat dirilis.

Untuk laporan keamanan, kegagalan integritas kritis, atau pengaturan bawaan tidak aman yang dapat dimitigasi — seperti kredensial yang terekspos, eksekusi kode jarak jauh, injeksi kode serius, atau pintasan autentikasi — ikuti langkah berikut:

1. **Kirim email** langsung ke `vladimir.acuna.dev@gmail.com`.
2. Sertakan:
   - Ekosistem atau repositori yang terdampak, misalnya `mcp-ollama-local` atau `social-bot-scheduler`.
   - Langkah rinci untuk mereproduksi kerentanan.
   - Opsional, bukti konsep (PoC) berupa skrip atau video, bila berlaku.
   - Kemungkinan dampak keamanan yang dinilai berdasarkan standar teknis yang relevan.

Saya akan menghubungi Anda secepat mungkin, umumnya dalam 48 jam kerja. Setelah masalah dianalisis dan dimitigasi, jika Anda ingin dicantumkan dan temuan dapat diverifikasi, Anda akan mendapat pengakuan publik yang layak dalam laporan keamanan atau CHANGELOG kami.

Terima kasih telah membantu menjaga infrastruktur ini tetap aman dan profesional.
