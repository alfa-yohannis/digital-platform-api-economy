<!-- Kegunaan: lembar kebijakan siklus hidup API pada Bab 10, dengan contoh API-01. Cara pakai: salin, isi bersama pemilik API, lalu lampirkan pada luaran C3. -->
# Kebijakan siklus hidup API

Lembar kerja Bab 10: Manajemen Siklus Hidup API dan API Gateway. Salin berkas sebelum mengisi. Contoh Medikara adalah data sintetis. Pisahkan fakta, asumsi, dan target. Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata.

## Langkah kerja

1. Tetapkan tahap API prioritas pada tabel gerbang.
2. Tuliskan gerbang persetujuan dari desain sampai pensiun beserta pemiliknya.
3. Hitung masa transisi dari konsumen paling lambat.
4. Tulis aturan pengecualian, termasuk pengecualian keamanan.
5. Catat pemicu tinjauan dan bukti yang belum tersedia.

## Contoh terisi: gerbang pada API-01

| Tahap | Keputusan penting | Bukti gerbang | Pemilik |
| :-- | :-- | :-- | :-- |
| Pembuatan | Layak dibangun atau tidak, dan apa isi kontraknya | Kanvas Bab 8, kontrak Bab 9, uji otorisasi objek | Manajer Layanan Rawat Jalan |
| Penerbitan | Siapa yang boleh memakai, dan kapan | 5 klinik uji berhasil, jalur dukungan siap, rencana cadangan saat SIMRS diperbarui | Manajer Layanan Rawat Jalan, Kepala Keamanan Informasi |
| Realisasi nilai | Apakah janji nilai terbukti | Telepon konfirmasi turun dari 10 ke 2 persen, atau dari 240 ke 48 per hari | Manajer Layanan Rawat Jalan |
| Pemeliharaan | Perubahan mana yang dikerjakan | Penilaian tiga gerbang Bab 9, 12 usulan per triwulan dengan kapasitas 6 | Pemilik produk, tim integrasi |
| Pensiun | Kapan dihentikan, dan apa penggantinya | Pemakai aktif nol atau pengecualian tercatat. Pemicu Bab 8: klinik mitra aktif di bawah 30 | Manajer Layanan Rawat Jalan |

## Contoh terisi: masa transisi API-01

| Unsur | Keputusan | Dasar |
| :-- | :-- | :-- |
| Lama transisi | 6 bulan | Vendor Medikara+ 4 bulan, uji bersama 1 bulan, cadangan 1 bulan |
| Biaya tumpang tindih | Rp22,5 juta | Rp45 juta per tahun dibagi 12, dikali 6 bulan |
| Biaya migrasi | Rp14,4 juta | 80 jam vendor dan 160 jam klinik pada Rp60.000 per jam |
| Pilihan yang ditolak | 3 bulan dan 12 bulan | Jumlah Rp109,65 juta dan Rp59,4 juta, dibanding Rp36,9 juta |
| Klinik baru | Langsung memakai versi 2 | Jumlah pemakai versi 1 hanya boleh turun |
| Perpanjangan | Satu kali, paling lama 1 bulan, alasan tertulis | Pendampingan 8 jam per klinik lebih murah daripada perpanjangan seluruh versi |
| Pengecualian keamanan | Masa transisi dapat dipangkas menjadi 14 hari | Keputusan Kepala Keamanan Informasi, klinik terdampak dibantu lebih dulu |
| Penutupan | Versi 1 menjawab 410 | Pemakai aktif nol atau pengecualian tercatat, keputusan diarsipkan |

## Lembar tim: gerbang

| Tahap | Keputusan penting | Bukti gerbang | Pemilik | Tanggal tinjau |
| :-- | :-- | :-- | :-- | :-- |
| Pembuatan | ... | ... | ... | ... |
| Penerbitan | ... | ... | ... | ... |
| Realisasi nilai | ... | ... | ... | ... |
| Pemeliharaan | ... | ... | ... | ... |
| Pensiun | ... | ... | ... | ... |

## Lembar tim: masa transisi

| Pilihan lama transisi | Biaya tumpang tindih | Biaya bila konsumen belum siap | Biaya migrasi | Jumlah |
| :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

## Tinjauan

- Apakah pilihan menjawab masalah layanan pada bab ini?
- Adakah alternatif yang ditolak beserta alasannya?
- Apakah pemilik, sumber bukti, dan pemicu peninjauan sudah dicatat?
- Apakah identitas klien cukup untuk mengetahui siapa yang masih memakai versi lama?

Gunakan metadata bukti bila dokumen organisasi tidak boleh dibagikan.
