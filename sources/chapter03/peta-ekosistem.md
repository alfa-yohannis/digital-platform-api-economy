<!-- Kegunaan: lembar kerja peta ekosistem untuk Aktivitas Bab 3 dan tonggak C1. Cara pakai: salin ke folder tim, isi tawaran nilai, pelaku, aliran, dan status sarana. -->

# Peta Ekosistem

Contoh Medikara adalah data latihan. Pisahkan fakta, asumsi, dan target. Data organisasi nyata wajib seizin organisasi dan dianonimkan. Rekam medis, kredensial, dan data pribadi tidak boleh dimasukkan.

## 1. Tawaran nilai

Tulis satu kalimat. Peta dimulai dari sini, bukan dari daftar mitra.

- Contoh: pasien dan karyawan memperoleh pemeriksaan lintas fasilitas, dengan hasil yang sampai ke dokter tanpa dibawa sendiri.
- Tim: ...

## 2. Pelaku dan peran

Contoh lengkapnya ada di [contoh-peta-ekosistem-medikara.csv](contoh-peta-ekosistem-medikara.csv).

| Pelaku | Jumlah | Peran | Kepentingan utama | Status angka |
| --- | --- | --- | --- | --- |
| Klinik mitra | 40 | Pelengkap | Pasien bertambah, biaya langganan sepadan | Bab 2 |
| Laboratorium mitra | 3 | Pelengkap | Volume pemeriksaan, tagihan tepat waktu | Bab 1 |
| Asuransi swasta | 9 | Pelengkap dan pelanggan | Klaim rapi, kecurangan rendah | Bab 1 |
| Perusahaan klien | 36 | Pelanggan, dapat menjadi saluran | Rekap tanpa kerja manual | Bab 1 |
| ... | ... | ... | ... | ... |

Lembar tim:

| Pelaku | Jumlah | Peran | Kepentingan utama | Status angka |
| --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

## 3. Aliran nilai

Contoh memakai paket pemeriksaan 200 karyawan dengan harga Rp500.000 per karyawan.

| Dari | Kepada | Jenis | Isi | Angka | Fakta, asumsi, atau target |
| --- | --- | --- | --- | --- | --- |
| Perusahaan klien | Medikara+ | Uang | Pembayaran paket | Rp100 juta | Asumsi |
| Medikara+ | Klinik mitra | Uang | Rp350.000 per karyawan | Rp70 juta | Asumsi |
| Medikara+ | Laboratorium mitra | Uang | Rp100.000 per karyawan | Rp20 juta | Asumsi |
| Laboratorium mitra | Klinik mitra | Data | Hasil pemeriksaan | 200 hasil | Asumsi |
| Klinik mitra | Karyawan | Layanan | Pemeriksaan | 200 pemeriksaan | Asumsi |
| Karyawan | Medikara+ | Reputasi | Ulasan | ... | Target |
| Medikara+ | Perusahaan klien | Data | Rekap agregat, tanpa hasil perorangan | 1 rekap | Target |

Lembar tim:

| Dari | Kepada | Jenis | Isi | Angka | Fakta, asumsi, atau target |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... |

## 4. Tiga sambungan terlemah

Urutkan menurut akibatnya bagi pengguna, bukan menurut kemudahan teknisnya.

| Urutan | Sambungan | Volume | Masalah | Pihak yang dirugikan |
| --- | --- | --- | --- | --- |
| 1 | Hasil laboratorium mitra | 1.100 per bulan | Surel berisi pindaian, diketik ulang | Pasien |
| 2 | Klaim asuransi swasta | 7.800 per bulan | 9 format, 468 klaim ditolak | Keuangan |
| 3 | Rekap perusahaan klien | 36 per bulan | Disusun manual empat hari kerja | Karyawan dan staf |

## 5. Status boundary resources

Diisi anggota berlatar teknis.

| Sarana | Kelompok | Status | Uji keberhasilan | Pemilik |
| --- | --- | --- | --- | --- |
| API jadwal dan pemesanan | Akses teknis | Belum | Klinik menguji mandiri | Tim platform |
| *Sandbox* 20 pasien sintetis | Akses teknis | Belum | Lulus 6 dari 6 skenario gagal | Tim platform |
| Panduan dan contoh | Pengetahuan | Belum | Pendampingan setengah hari per klinik | Tim platform |
| Syarat penggunaan | Aturan | Belum | Disetujui pemilik layanan | Bagian hukum |
| ... | ... | ... | ... | ... |

## Tinjauan

- Apakah peta dimulai dari satu tawaran nilai?
- Apakah setiap panah menyebut jenis aliran dan, bila ada, angkanya?
- Apakah pihak yang membayar dibedakan dari pihak yang memakai?
- Apakah pemasok dan pihak wajib dipisahkan dari pelengkap?
