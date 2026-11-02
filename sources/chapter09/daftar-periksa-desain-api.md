<!-- Kegunaan: daftar periksa tinjauan kontrak API Bab 09. Cara pakai: salin, isi bersama pemilik proses dan konsumen, lalu lampirkan pada luaran C3. -->
# Daftar periksa desain API

Lembar kerja Bab 9: Desain Kontrak API dengan OpenAPI. Salin berkas sebelum mengisi. Contoh Medikara adalah data sintetis. Pisahkan fakta, asumsi, dan target.

## Langkah kerja

1. Pilih satu API prioritas dari Bab 8.
2. Tuliskan aturan bisnis serta skenario galat bersama pengguna pada [lembar-aturan-bisnis.md](lembar-aturan-bisnis.md).
3. Lengkapi OpenAPI dan contoh pesan dengan data sintetis, dimulai dari [templat-kontrak-openapi.yaml](templat-kontrak-openapi.yaml).
4. Tinjau perubahan, jalankan pemeriksaan struktur, lalu catat keputusan C3.

## Daftar periksa dan contoh API-01

Status diisi Ya, Belum, atau Tidak berlaku. Daftar ini sama dengan tabel daftar periksa pada Bab 9.

| No | Pertanyaan tinjauan | Penanggung jawab | Bukti pada contoh API-01 | Status |
| :-- | :-- | :-- | :-- | :-- |
| 1 | Apakah nama sumber daya dikenali pengguna dan bukan nama tabel? | Pemilik proses | `/jadwal-dokter`, `/janji-temu` | Ya |
| 2 | Apakah satu kata punya satu arti di seluruh kontrak? | Analis | Tabel kosakata: slot, janji temu, kunjungan | Ya |
| 3 | Apakah arti berhasil ditulis, termasuk bedanya dengan diterima? | Pemilik proses | 201 terkonfirmasi, 202 menunggu | Ya |
| 4 | Apakah setiap kasus gagal punya tindakan berikutnya? | Layanan pelanggan | 409 slot terisi, tawarkan slot lain | Ya |
| 5 | Apakah pesan galat bebas dari data sensitif dan rincian internal? | Keamanan | `detail` tanpa nama pasien, tanpa nama tabel | Ya |
| 6 | Apakah data hanya yang dibutuhkan? | Petugas pelindungan data | Tanpa isi rekam medis | Ya |
| 7 | Apakah scope tiap operasi tertulis dan hak atas objek tetap diperiksa? | Keamanan | `janji.tulis`, 404 untuk janji klinik lain | Ya |
| 8 | Apakah kiriman ulang aman? | Tim teknis | Kunci idempotensi 24 jam | Ya |
| 9 | Apakah batas halaman, urutan, dan penyaringan tertulis? | Tim teknis | 20 slot, paling banyak 50, urut menurut waktu mulai | Ya |
| 10 | Apakah aturan bidang tak dikenal dan kebijakan versi tertulis? | Pemilik proses | Konsumen mengabaikan bidang tak dikenal, versi 1.0.0 | Ya |
| 11 | Apakah contoh sesuai schema dan memakai data sintetis? | Tim teknis | `PSN-58213`, `BKS-20261102-0915` | Ya |
| 12 | Apakah konsumen sudah mencoba skenario gagal pada mock? | Konsumen | Misalkan 5 klinik, 6 skenario | Belum |

## Lembar tim

| ID | Usulan tim | Bukti dan asumsi | Pemilik | Tanggal tinjau |
| :-- | :-- | :-- | :-- | :-- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

## Tinjauan

- Apakah pilihan menjawab masalah layanan pada bab ini?
- Adakah alternatif yang ditolak beserta alasannya?
- Apakah pemilik, sumber bukti, dan pemicu peninjauan sudah dicatat?
- Bukti mana yang hanya berasal dari mock, sehingga masih perlu uji pada sistem nyata?

Gunakan metadata bukti bila dokumen organisasi tidak boleh dibagikan. Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata.
