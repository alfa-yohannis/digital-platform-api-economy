# Diagram Bab

Gambar aktif pada modul dan slide adalah diagram konsep TikZ berlabel. Setiap panah menyatakan alur atau relasi yang tertulis pada labelnya. Diagram disusun dari konsep, batasan, dan kasus pada naskah masing-masing bab, bukan hanya dari judul bab.

Setiap berkas `chNN-diagram-konsep.tex` berisi satu `tikzpicture` tanpa preamble. Modul memanggilnya dengan `\input{../figures/chNN-diagram-konsep.tex}`, slide dengan `\input{../../figures/chNN-diagram-konsep.tex}`. Spesifikasi komponen, hubungan, catatan batas, dan dasar pemilihan terdapat pada [chapter-diagrams.json](chapter-diagrams.json). Kotak memakai notasi generik, bukan klaim konformansi ArchiMate atau reproduksi gambar standar.

| Bab | Isi diagram | TikZ |
| --- | --- | --- |
| 01 | Dari rantai layanan ke interaksi platform | [ch01-diagram-konsep.tex](ch01-diagram-konsep.tex) |
| 02 | Efek jaringan dan mutu interaksi | [ch02-diagram-konsep.tex](ch02-diagram-konsep.tex) |
| 03 | Ekosistem dan batas kerja sama mitra | [ch03-diagram-konsep.tex](ch03-diagram-konsep.tex) |
| 04 | API sebagai produk yang terus dipelihara | [ch04-diagram-konsep.tex](ch04-diagram-konsep.tex) |
| 05 | Komunikasi sinkron dan pemberitahuan asinkron | [ch05-diagram-konsep.tex](ch05-diagram-konsep.tex) |
| 06 | Token valid tetap memerlukan izin atas objek | [ch06-diagram-konsep.tex](ch06-diagram-konsep.tex) |
| 07 | Jalur integrasi sektoral mempunyai tujuan berbeda | [ch07-diagram-konsep.tex](ch07-diagram-konsep.tex) |
| 08 | Menurunkan strategi menjadi portofolio API | [ch08-diagram-konsep.tex](ch08-diagram-konsep.tex) |
| 09 | Kontrak sebagai acuan bersama penyedia dan konsumen | [ch09-diagram-konsep.tex](ch09-diagram-konsep.tex) |
| 10 | Gateway dan pengelolaan siklus hidup API | [ch10-diagram-konsep.tex](ch10-diagram-konsep.tex) |
| 11 | Gerbang onboarding dari pendaftaran sampai produksi | [ch11-diagram-konsep.tex](ch11-diagram-konsep.tex) |
| 12 | Keberlanjutan ekonomi dan nilai yang dirasakan pengguna | [ch12-diagram-konsep.tex](ch12-diagram-konsep.tex) |
| 13 | Tata kelola federasi: standar bersama dan keputusan lokal | [ch13-diagram-konsep.tex](ch13-diagram-konsep.tex) |
| 14 | Demo MCP: pencarian dan pratinjau slot tanpa transaksi | [ch14-diagram-konsep.tex](ch14-diagram-konsep.tex) |

## Membuat ulang

Jalankan dari akar repositori dengan Python 3. Skrip hanya memakai pustaka standar:

```powershell
python tools/render-diagrams.py
python tools/render-diagrams.py --chapter 1 5
```

Metrik font Titillium Web dibaca dari `module/fonts/` untuk membungkus teks dan menempatkan label. Jalur panah dicari pada grid agar tidak menembus kotak, dan label tidak menutup ujung panah. Skrip berhenti dengan pesan galat bila teks tidak muat di kotak atau label menimpa kotak. Ubah `chapter-diagrams.json` untuk mengubah komponen atau relasi, lalu jalankan ulang skrip. Berkas `.tex` hasilnya tidak disunting langsung.

JPG ilustrasi terdahulu disimpan sebagai arsip dan tidak lagi dirujuk pada gambar bab aktif. Diagram TikZ pendukung yang sudah ada tetap menjadi bagian materi.
