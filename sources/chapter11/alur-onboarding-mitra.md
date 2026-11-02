<!-- Kegunaan: lembar alur onboarding mitra Bab 11, dengan contoh klinik mitra pada API-01. Cara pakai: salin berkas, isi lembar tim, lalu lampirkan pada artefak C3. -->
# Alur onboarding mitra

Lembar kerja Bab 11: Developer Experience dan Portal Pengembang. Seluruh angka Medikara adalah data latihan. Pisahkan fakta, asumsi, dan target.

## Langkah kerja

1. Tentukan mitra yang dipakai, misalnya klinik mitra atau asuransi, dan API yang dibukanya.
2. Tentukan pemilik, bukti kelulusan, dan sasaran waktu setiap tahap.
3. Tandai tingkat keterbukaan Bab 3 yang dicapai pada tiap tahap.
4. Catat waktu kerja dan waktu tunggu tiap tahap secara terpisah.
5. Tulis rencana penghentian mitra sebelum memberi akses produksi.

## Contoh terisi: klinik mitra pada API-01

| Tahap | Bukti kelulusan | Pemilik | Sasaran tunggu | Tingkat Bab 3 |
| :-- | :-- | :-- | :-- | :-- |
| Pendaftaran mitra | Identitas organisasi dan kontak teknis | Klinik | Tanpa tunggu | Tingkat 0 ke 1 |
| Verifikasi | Petugas berwenang mewakili klinik, syarat penggunaan disetujui | Pemilik kemitraan | 4 jam | Tingkat 1 |
| Sandbox | Kredensial uji terbit, 200 pada `GET /jadwal-dokter` | Sistem portal | Tanpa tunggu | Tingkat 1, kuota 100 |
| Uji integrasi | 3 tugas normal, 6 skenario gagal, uji otorisasi objek | Tim integrasi | 16 jam | Tingkat 1 |
| Persetujuan pemilik | Izin usaha, perjanjian, cakupan akses terbatas | Manajer Layanan Rawat Jalan | 16 jam | Syarat tingkat 2 |
| Akses produksi | Kredensial terpisah, kuota 300, kontak insiden | Tim integrasi | 4 jam | Tingkat 2 |
| Dukungan berlanjut | Kanal, prioritas, status, jadwal tinjau | Layanan pelanggan | Menurut prioritas | Tingkat 2 |

## Enam skenario gagal API-01

Skenario penjamin menolak dari Bab 3 berada di luar API-01, sehingga diganti SIMRS diperbarui, sesuai Bab 9.

| Skenario | Kode dan tipe masalah | Pemicu pada sandbox | Perilaku yang diharapkan |
| :-- | :-- | :-- | :-- |
| Pasien tidak ditemukan | 400 `pasien-tidak-dapat-dipakai` | Nomor di luar `PSN-00001` sampai `PSN-00020` | Periksa nomor, jangan menebak |
| Slot penuh | 409 `slot-terisi` | Slot `BKS-20261102-0930` | Tawarkan slot lain |
| Kode akses kedaluwarsa | 401 `token-tidak-sah` | Token `token-uji-kedaluwarsa` | Minta token baru |
| Kuota habis | 429 `kuota-habis` | Panggilan ke-101 pada hari yang sama | Tunda sesuai `Retry-After` |
| Format salah | 400 `masukan-tidak-sah` | Kode rumah sakit tidak dikenal | Perbaiki isian |
| SIMRS diperbarui | 503 `simrs-tidak-tersedia` | Tanggal `2026-11-03` | Coba lagi, jangan menulis tidak ada dokter |

## Rencana penghentian mitra

| Butir | Contoh | Pemilik |
| :-- | :-- | :-- |
| Pencabutan akses | Identitas klien dicabut, token terakhir mati paling lama 15 menit kemudian | Tim integrasi |
| Layanan aktif | 300 janji aktif dialihkan, 3 menit per janji, 15 jam | Layanan pelanggan |
| Sisa data | Dicatat apa yang wajib disimpan dan apa yang dihapus klinik | Petugas pelindungan data |
| Pemberitahuan | Status klinik pada katalog dan daftar kontak diperbarui | Pemilik kemitraan |

## Lembar tim

| Tahap | Bukti kelulusan | Pemilik | Sasaran waktu | Kerja saat ini (jam) | Tunggu saat ini (jam) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Pendaftaran mitra | ... | ... | ... | ... | ... |
| Verifikasi | ... | ... | ... | ... | ... |
| Sandbox | ... | ... | ... | ... | ... |
| Uji integrasi | ... | ... | ... | ... | ... |
| Persetujuan pemilik | ... | ... | ... | ... | ... |
| Akses produksi | ... | ... | ... | ... | ... |
| Dukungan berlanjut | ... | ... | ... | ... | ... |

## Tinjauan

- Tahap mana yang paling lama menunggu, dan siapa yang ditunggu?
- Apakah akses uji dan akses produksi sudah terpisah?
- Apa yang terjadi pada janji aktif bila mitra keluar?

Catatan waktu boleh berupa metadata bila dokumen organisasi tidak boleh dibagikan. Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata.
