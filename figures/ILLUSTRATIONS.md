# Diagram Bab

Gambar aktif pada modul dan slide adalah diagram PNG berlabel. Setiap panah menyatakan alur atau relasi yang tertulis pada labelnya. Diagram disusun dari konsep, batasan, dan kasus pada naskah masing-masing bab, bukan hanya dari judul bab. Seluruh diagram ini dibuat tanpa TikZ.

PNG dipakai oleh LaTeX; SVG menyimpan versi vektor. Spesifikasi komponen, hubungan, catatan batas, dan dasar pemilihan terdapat pada [chapter-diagrams.json](chapter-diagrams.json). Kotak memakai notasi generik, bukan klaim konformansi ArchiMate atau reproduksi gambar standar.

| Bab | Isi diagram | PNG | SVG |
| --- | --- | --- | --- |
| 01 | Dari rantai layanan ke interaksi platform | [gambar](ch01-diagram-konsep.png) | [vektor](ch01-diagram-konsep.svg) |
| 02 | Efek jaringan dan mutu interaksi | [gambar](ch02-diagram-konsep.png) | [vektor](ch02-diagram-konsep.svg) |
| 03 | Ekosistem dan batas kerja sama mitra | [gambar](ch03-diagram-konsep.png) | [vektor](ch03-diagram-konsep.svg) |
| 04 | API sebagai produk yang terus dipelihara | [gambar](ch04-diagram-konsep.png) | [vektor](ch04-diagram-konsep.svg) |
| 05 | Komunikasi sinkron dan pemberitahuan asinkron | [gambar](ch05-diagram-konsep.png) | [vektor](ch05-diagram-konsep.svg) |
| 06 | Token valid tetap memerlukan izin atas objek | [gambar](ch06-diagram-konsep.png) | [vektor](ch06-diagram-konsep.svg) |
| 07 | Jalur integrasi sektoral mempunyai tujuan berbeda | [gambar](ch07-diagram-konsep.png) | [vektor](ch07-diagram-konsep.svg) |
| 08 | Menurunkan strategi menjadi portofolio API | [gambar](ch08-diagram-konsep.png) | [vektor](ch08-diagram-konsep.svg) |
| 09 | Kontrak sebagai acuan bersama penyedia dan konsumen | [gambar](ch09-diagram-konsep.png) | [vektor](ch09-diagram-konsep.svg) |
| 10 | Gateway dan pengelolaan siklus hidup API | [gambar](ch10-diagram-konsep.png) | [vektor](ch10-diagram-konsep.svg) |
| 11 | Gerbang onboarding dari pendaftaran sampai produksi | [gambar](ch11-diagram-konsep.png) | [vektor](ch11-diagram-konsep.svg) |
| 12 | Keberlanjutan ekonomi dan nilai yang dirasakan pengguna | [gambar](ch12-diagram-konsep.png) | [vektor](ch12-diagram-konsep.svg) |
| 13 | Tata kelola federasi: standar bersama dan keputusan lokal | [gambar](ch13-diagram-konsep.png) | [vektor](ch13-diagram-konsep.svg) |
| 14 | Demo MCP: pencarian dan pratinjau slot tanpa transaksi | [gambar](ch14-diagram-konsep.png) | [vektor](ch14-diagram-konsep.svg) |

## Membuat ulang

Jalankan dari akar repositori dengan Python, Matplotlib, dan Pillow:

```powershell
python tools/render-diagrams.py
python tools/render-diagrams.py --chapter 1 5
```

Font Titillium Web dibaca dari `module/fonts/`. PNG RGB maksimum 500 KiB; SVG menyimpan huruf sebagai path agar tampilannya tetap sama. Ubah `chapter-diagrams.json` untuk mengubah komponen atau relasi.

JPG ilustrasi terdahulu disimpan sebagai arsip dan tidak lagi dirujuk pada gambar bab aktif. Diagram TikZ pendukung yang sudah ada tetap menjadi bagian materi.
