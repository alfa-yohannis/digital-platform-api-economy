<!-- Kegunaan: lembar kerja model tata kelola API Bab 13. Cara pakai: salin berkas, lalu isi lembar tim dengan bukti organisasi. -->

# Model tata kelola API

Lembar kerja Bab 13, Tata Kelola API dan Regulasi Platform. Contoh Medikara memakai data sintetis. Pisahkan fakta, asumsi, dan target.

## Langkah kerja

1. Pilih model: terpusat, terdistribusi, atau federasi. Tulis alasan dan akibat yang diterima.
2. Bagi hak keputusan antara forum bersama, pemilik produk, tim integrasi, serta keamanan dan petugas pelindungan data.
3. Tetapkan kelas perubahan beserta jalur tinjauan, sasaran waktu, dan peninjaunya.
4. Tetapkan titik pemeriksaan sebelum rilis, serta bukti yang masuk katalog.
5. Tetapkan aturan pengecualian: alasan, pemilik, tenggat, dan penerima risiko.
6. Hitung biaya jam dan waktu tunggu dengan `hitung-tata-kelola.py`, memakai asumsi tim.

## Contoh terisi: hak keputusan

| Keputusan | Forum bersama | Pemilik produk | Tim integrasi | Keamanan dan petugas pelindungan data |
| :-- | :-- | :-- | :-- | :-- |
| Panduan gaya dan format galat | Memutuskan | Memberi masukan | Mengusulkan | Meninjau |
| Masa transisi versi, 6 bulan | Memutuskan | Menerima biaya | Menerapkan | Boleh memangkas saat kerentanan serius |
| Bidang data baru | Memutuskan bila kelas C | Mengusulkan tujuan | Menilai dampak kontrak | Menilai dasar dan dampak |
| Isi API-01 dan prioritas perubahan | Tidak terlibat | Memutuskan | Memberi perkiraan | Dimintai pendapat |
| Adaptor SIMRS tiap rumah sakit | Tidak terlibat | Dikabari | Memutuskan bersama tim rumah sakit | Meninjau bila menyentuh hak akses |

## Contoh terisi: kelas perubahan

Angka ini pemisalan pada 48 usulan API-01 per tahun. Rapat forum 12 kali, 2 jam, 5 orang.

| Kelas | Ciri | Usulan | Peninjau | Tunggu (hari kerja) | Jam |
| :-- | :-- | --: | :-- | --: | --: |
| A | Kontrak tidak berubah, atau dokumentasi saja | 30 | Pemilik produk, 1 orang, 0,5 jam | 1 | 15 |
| B | Perubahan kontrak yang kompatibel, tanpa data baru | 14 | Tinjauan sejawat, 2 orang, 1 jam | 3 | 28 |
| C | Perubahan yang merusak, data spesifik baru, atau mitra jenis baru | 4 | Forum bersama, rapat bulanan | 10 | Di dalam 120 jam forum |

## Contoh terisi: register pengecualian

| ID | Butir | Alasan | Pemilik | Tenggat | Penerima risiko |
| :-- | :-- | :-- | :-- | :-- | :-- |
| PGC-01 | GAYA-04 | SIMRS lama belum dapat membentuk `application/problem+json`, adaptor sedang dibuat, 40 jam | Tim integrasi | 6 bulan | Manajer Layanan Rawat Jalan |

## Lembar tim: hak keputusan

| Keputusan | Forum bersama | Pemilik produk | Tim integrasi | Keamanan dan data |
| :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

## Lembar tim: kelas perubahan

| Kelas | Ciri | Usulan per tahun | Peninjau | Sasaran tunggu | Bukti |
| :-- | :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |

## Lembar tim: register pengecualian

| ID | Butir | Alasan | Pemilik | Tenggat | Penerima risiko |
| :-- | :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... | ... |

## Tinjauan

- Apakah setiap keputusan punya satu pemegang keputusan, bukan sekadar daftar peserta rapat?
- Apakah usulan berisiko rendah bebas dari antrean forum?
- Adakah bukti yang dapat mengubah model dalam 6 bulan?
- Apakah tiap pengecualian punya penerima risiko yang menyetujuinya?

Gunakan metadata bukti bila dokumen organisasi tidak boleh dibagikan. Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata.
