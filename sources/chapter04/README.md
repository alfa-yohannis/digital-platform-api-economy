<!-- Kegunaan: daftar berkas pendukung Bab 4. Cara pakai: baca tabel di bawah, lalu salin berkas yang diperlukan ke folder tim sebelum mengisi. -->

# Sumber Bab 04

Berkas ini mendukung Aktivitas dan Latihan Bab 4 untuk tonggak C2. Salin templat sebelum mengisi. Contoh Medikara memakai data latihan dan bukan bukti organisasi nyata.

| Berkas | Kegunaan |
| --- | --- |
| [inventaris-integrasi.csv](inventaris-integrasi.csv) | Templat kosong inventaris integrasi dan API, satu baris per hubungan |
| [contoh-inventaris-medikara.csv](contoh-inventaris-medikara.csv) | Contoh terisi: 10 baris yang mewakili 100 sambungan Medikara |
| [panduan-wawancara-pemilik-proses.md](panduan-wawancara-pemilik-proses.md) | Pertanyaan bagi anggota non-teknis, beserta kolom inventaris yang terisi dari tiap jawaban |
| [catatan-integrasi-rawan.md](catatan-integrasi-rawan.md) | Templat catatan integrasi paling mahal atau paling rawan beserta contoh terisi |
| [periksa-inventaris.py](periksa-inventaris.py) | Skrip pemeriksa inventaris: `python periksa-inventaris.py contoh-inventaris-medikara.csv` |
| [hitung-beban-integrasi.py](hitung-beban-integrasi.py) | Skrip sambungan, biaya, dan titik impas untuk Latihan 1: `python hitung-beban-integrasi.py` |

CSV memakai UTF-8 dan koma. Hapus komentar `#` di baris pertama saat impor ke *spreadsheet*. Periksa satuan angka dan bedakan bukti, asumsi, serta target.

Skrip hanya dipakai pada data sintetis atau sumber berizin. Penelusuran konfigurasi hanya untuk sistem sendiri atau yang sudah berizin tertulis. Rekam medis, kredensial, dan data pribadi pasien atau karyawan tidak boleh dimasukkan.
