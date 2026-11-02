<!-- Kegunaan: lembar aturan bisnis Bab 09, ditulis dalam bahasa biasa sebelum kontrak OpenAPI. Cara pakai: salin, isi bersama pemilik proses, lalu serahkan kepada anggota teknis. -->
# Lembar aturan bisnis untuk kontrak API

Lembar kerja Bab 9: Desain Kontrak API dengan OpenAPI. Lembar ini diisi anggota berlatar non-teknis, tanpa YAML. Anggota teknis menuangkannya ke [templat-kontrak-openapi.yaml](templat-kontrak-openapi.yaml). Contoh Medikara adalah data latihan. Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata.

## Bagian 1. Identitas

| Butir | Contoh API-01 | Isian tim |
| :-- | :-- | :-- |
| API prioritas dari Bab 8 | API-01 Jadwal dan Janji Temu | ... |
| Kapabilitas dan baris inventaris | CAP-L03, INT-03 | ... |
| Pemilik proses | Manajer Layanan Rawat Jalan | ... |
| Konsumen | Aplikasi Medikara+ dan 40 klinik mitra | ... |
| Kuota | 300 panggilan per hari per klinik | ... |
| Data yang tidak boleh keluar | Isi rekam medis | ... |

## Bagian 2. Kosakata

Tulis arti satu kata yang sering tertukar. Satu kata punya satu arti di seluruh kontrak.

| Kata | Arti dalam kontrak | Bukan berarti |
| :-- | :-- | :-- |
| Slot | Satu rentang waktu yang dapat dipesan | Janji temu |
| Janji temu | Pemesanan seorang pasien atas satu slot | Kunjungan |
| Terkonfirmasi | Slot sudah terkunci di SIMRS | Permintaan sudah diterima |
| Menunggu | Permintaan diterima, hasilnya belum pasti | Janji pasti ada |
| ... | ... | ... |

## Bagian 3. Aturan bisnis

| ID | Aturan dalam bahasa biasa | Alasan | Bila dilanggar |
| :-- | :-- | :-- | :-- |
| AB-01 | Hanya janji terkonfirmasi yang boleh ditampilkan sebagai janji pasti | Pasien tidak datang tanpa janji | Layar menulis menunggu kepastian |
| AB-02 | Satu slot hanya untuk satu pasien | Mencegah slot ganda | Pemesan kedua diminta memilih slot lain |
| AB-03 | Kiriman ulang pemesanan yang sama tidak membuat janji kedua | Jawaban dapat hilang di jaringan | Janji yang sudah ada dikembalikan |
| AB-04 | Pembatalan paling lambat dua jam sebelum slot mulai | Dokter sudah bersiap | Pasien diminta menghubungi rumah sakit |
| AB-05 | Klinik hanya melihat janji pasien yang dipesannya | Kerahasiaan pasien | Dijawab seperti janji tidak ada |
| ... | ... | ... | ... |

## Bagian 4. Contoh data sintetis

| Bidang | Contoh | Boleh keluar? | Catatan |
| :-- | :-- | :-- | :-- |
| Pengenal slot | BKS-20261102-0915 | Ya | Bukan nomor tabel SIMRS |
| Nomor pasien | PSN-58213 | Ya, kepada klinik yang memesan | Nomor sintetis |
| Status janji | terkonfirmasi | Ya | Empat nilai pada Bagian 2 kontrak |
| Diagnosis | Tidak dipakai | Tidak | Di luar API-01 |
| ... | ... | ... | ... |

## Bagian 5. Kasus gagal

Tulis apa yang dilihat petugas, apa yang dilakukan selanjutnya, dan siapa yang dihubungi.

| Kasus gagal | Pesan bagi petugas | Tindakan berikutnya | Yang dihubungi |
| :-- | :-- | :-- | :-- |
| Slot penuh | Slot sudah terisi. Pilih slot lain | Aplikasi menawarkan slot lain | Tidak ada |
| Format salah | Periksa tanggal dan nomor pasien | Petugas memperbaiki isian | Tidak ada |
| Kode akses kedaluwarsa | Akses kedaluwarsa | Aplikasi meminta token baru | Admin klinik bila berulang |
| Kuota habis | Kuota hari ini habis, coba lagi setelah waktu tunggu | Pemesanan ditunda | Pemilik kemitraan bila berulang |
| SIMRS diperbarui | Jadwal sementara tidak dapat dibaca, bukan berarti tidak ada dokter | Coba lagi setelah waktu tunggu | Rumah sakit bila mendesak |
| ... | ... | ... | ... |

## Tinjauan

- Apakah pemilik proses membaca dan menyetujui lembar ini?
- Aturan mana yang masih berupa asumsi, dan siapa yang dapat memastikannya?
- Apakah ada istilah yang artinya berbeda di dua rumah sakit?
