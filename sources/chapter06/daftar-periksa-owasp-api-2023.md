<!-- Kegunaan: daftar periksa OWASP API Security Top 10 edisi 2023 untuk Aktivitas Bab 6. Cara pakai: salin satu lembar per integrasi, isi dari sumber berizin, lalu pindahkan temuan ke register-risiko-api.csv. -->

# Daftar Periksa OWASP API Security Top 10 Edisi 2023

Lembar ini dipakai untuk satu integrasi. Satu integrasi yang belum memakai API tetap dinilai: pertanyaannya tetap berlaku, walaupun butirnya hanya mendekati.

**Peringatan.** Pemeriksaan bukti memakai dokumen, konfigurasi, wawancara, dan catatan yang sudah diizinkan. Uji coba, misalnya mengganti ID pasien, hanya dilakukan pada sistem sendiri atau yang sudah berizin tertulis, pada lingkungan uji, dengan data sintetis. Mengganti ID pada sistem milik orang lain tetap termasuk akses tanpa izin, walaupun tokennya sah.

## Identitas

| Unsur | Isi |
| :-- | :-- |
| ID integrasi | ... |
| Versi peta integrasi | ... |
| Pemilik bisnis | ... |
| Pemilik teknis | ... |
| Tanggal tinjau | ... |

## Daftar periksa

| Butir | Pertanyaan pemeriksaan | Bukti berizin yang dicari | Temuan tim | Dampak (1 sampai 3) | Kemungkinan (1 sampai 3) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| API1 *Broken Object Level Authorization* | Apakah setiap permintaan dengan ID objek diperiksa haknya di server? | Aturan hak per objek, catatan akses yang ditolak | ... | ... | ... |
| API2 *Broken Authentication* | Apakah kredensial dipakai bersama, tidak dirotasi, atau masa berlakunya tidak diperiksa? | Daftar akun dan klien, jadwal rotasi | ... | ... | ... |
| API3 *Broken Object Property Level Authorization* | Apakah jawaban memuat bidang di luar kebutuhan pemanggil? | Contoh jawaban sintetis, daftar bidang | ... | ... | ... |
| API4 *Unrestricted Resource Consumption* | Adakah batas laju, kuota, ukuran, dan batas waktu? | Konfigurasi batas, catatan kode 429 | ... | ... | ... |
| API5 *Broken Function Level Authorization* | Dapatkah akun biasa menjalankan fungsi administrator? | Matriks peran dan fungsi | ... | ... | ... |
| API6 *Unrestricted Access to Sensitive Business Flows* | Dapatkah alur bisnis sah dipakai berlebihan secara otomatis? | Pola pemakaian, batas per pasien atau per mitra | ... | ... | ... |
| API7 *Server Side Request Forgery* | Apakah API mengambil alamat dari pemanggil tanpa validasi? | Daftar tujuan yang diizinkan | ... | ... | ... |
| API8 *Security Misconfiguration* | Adakah konfigurasi bawaan yang longgar atau pesan *error* yang membuka rincian teknis? | Hasil tinjauan konfigurasi | ... | ... | ... |
| API9 *Improper Inventory Management* | Apakah semua versi, sambungan, dan aliran data ke pihak ketiga tercatat dan punya pemilik? | Inventaris Bab 4, alasan bisnis tiap aliran | ... | ... | ... |
| API10 *Unsafe Consumption of APIs* | Apakah data dari API pihak ketiga divalidasi dan dibatasi waktunya? | Aturan validasi, batas waktu | ... | ... | ... |

## Contoh terisi: INT-03 Medikara (data latihan)

| Butir | Temuan | Status bukti | Dampak | Kemungkinan | Skor |
| :-- | :-- | :-- | :-- | :-- | :-- |
| API3 | Akun vendor membaca 140 tabel SIMRS, kebutuhan 2 tabel | Terverifikasi | 3 | 3 | 9 |
| API1 | API bawaan di 2 rumah sakit diduga tidak memeriksa hubungan layanan | Hipotesis | 3 | 3 | 9 |

## Tinjauan

- Apakah temuan membedakan fakta, dugaan, dan bukti yang belum tersedia?
- Apakah dampak terhadap pasien, kepatuhan, dan reputasi dinilai oleh anggota berlatar hukum, kesehatan, atau bisnis?
- Apakah pemilik, tenggat, dan pemicu peninjauan sudah dicatat?

Bila dokumen organisasi tidak boleh dibagikan, catat metadata buktinya saja. Rekam medis, kredensial, dan data pribadi pasien atau karyawan tidak boleh dimasukkan.
