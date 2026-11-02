<!-- Kegunaan: kronologi insiden vendor 2025 sebagai data latihan untuk Latihan 3 dan Aktivitas Bab 6. Cara pakai: baca sebelum mengisi hipotesis, pisahkan fakta dari dugaan, jangan disalin sebagai bukti organisasi nyata. -->

# Kronologi Insiden Vendor Medikara 2025

Fakta dasar kasus hanya menyebut kebocoran data pasien skala kecil lewat vendor pada 2025. Seluruh rincian di bawah ini adalah pengandaian latihan Bab 6.

## Kronologi

| Hari | Peristiwa | Sumber | Status |
| :-- | :-- | :-- | :-- |
| Sebelum hari 1 | Kontrak pekerjaan vendor selesai, akun dukungan tetap aktif | Daftar akun | Fakta latihan |
| 1 sampai 8 | Akun dukungan memanggil *endpoint* kunjungan pada API bawaan SIMRS di dua rumah sakit, 155 panggilan per malam | Rekap jumlah panggilan harian | Fakta latihan |
| 1 sampai 8 | Jumlah seluruhnya 1.240 rekam kunjungan, tanpa hubungan layanan dengan pekerjaan vendor | Rekap harian dan catatan rinci | Fakta latihan |
| 11 | Medikara mengetahui kejadian lewat keluhan pasien, bukan lewat alarm | Tiket layanan pasien | Fakta latihan |
| 11 | Catatan rinci hanya disimpan 7 hari, sehingga tersisa hari 5 sampai 11 | Konfigurasi penyimpanan | Fakta latihan |
| 11 | Rekam malam 5 sampai 8 (620 rekam) dapat ditelusuri, malam 1 sampai 4 (620 rekam) tidak dapat ditelusuri | Catatan rinci | Fakta latihan |

## Yang belum diketahui

| Pertanyaan | Bukti yang dibutuhkan | Status |
| :-- | :-- | :-- |
| Siapa orang yang memakai akun itu? | Catatan vendor, catatan akses per orang | Belum ada: catatan hanya memuat ID aplikasi |
| Apakah kredensial bocor, atau dipakai oleh staf vendor? | Keterangan vendor, jejak alamat jaringan | Belum ada |
| Apakah data disalin keluar dari sistem vendor? | Hasil pemeriksaan di sisi vendor, sesuai kontrak | Belum ada |
| Apakah layanan memeriksa hubungan layanan? | Uji berizin dengan data sintetis pada lingkungan uji | Belum selesai |

## Hipotesis butir OWASP

| Butir | Fakta pendukung | Yang dapat menggugurkan |
| :-- | :-- | :-- |
| API1 *Broken Object Level Authorization* | Token sah, 1.240 rekam tanpa hubungan layanan | Uji berizin membuktikan layanan menolak, dan kebocoran lewat jalur lain |
| API9 *Improper Inventory Management* | Akun dukungan aktif setelah kontrak selesai, sepuluh baris inventaris Bab 4 tidak memuat akses itu | Inventaris lain ditemukan, tetapi tidak dibaca |
| API2 *Broken Authentication* | Catatan hanya memuat ID aplikasi, sehingga kredensial diduga dipakai bersama | Kredensial per orang ditemukan, dengan masa berlaku yang diperiksa |
| API10 *Unsafe Consumption of APIs* | Tidak ada: butir ini tentang API Medikara yang terlalu percaya pada data masuk dari API pihak ketiga | Ditemukan data vendor yang masuk tanpa validasi |

Butir API4 tidak menjadi penyebab utama. Pola 155 panggilan per malam berada di bawah kuota 300 panggilan per hari, sehingga pembatasan konsumsi tidak akan menghentikannya.

## Hitungan biaya langsung

| Unsur | Hitungan | Hasil |
| :-- | :-- | :-- |
| Penanganan | 6 orang, 5 hari, 8 jam per hari, Rp60.000 per jam | Rp14,4 juta |
| Pemberitahuan | 620 pasien, 15 menit per pasien, Rp60.000 per jam | Rp9,3 juta |
| Jumlah | | Rp23,7 juta |

Sanksi, kehilangan kepercayaan, dan akibat bagi pasien belum dihitung.

## Lembar tim

| Hari | Peristiwa | Sumber | Status: fakta, dugaan, atau belum diketahui |
| :-- | :-- | :-- | :-- |
| ... | ... | ... | ... |
| ... | ... | ... | ... |
| ... | ... | ... | ... |

Rekam medis, kredensial, dan data pribadi pasien atau karyawan tidak boleh dimasukkan.
