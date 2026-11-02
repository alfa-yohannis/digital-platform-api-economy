<!-- Kegunaan: templat syarat penggunaan, tingkat layanan, dan dukungan untuk Bab 11. Cara pakai: salin berkas, isi lembar tim, lalu mintakan tinjauan hukum. -->
# Templat syarat penggunaan

Lembar kerja Bab 11: Developer Experience dan Portal Pengembang. Templat ini latihan dan bukan nasihat hukum. Naskah untuk organisasi nyata wajib ditinjau bagian hukum. Seluruh angka Medikara adalah data latihan.

## Langkah kerja

1. Pisahkan isi syarat penggunaan, perjanjian kerja sama, dan kontrak API.
2. Isi butir syarat beserta pemiliknya.
3. Hitung ketersediaan rantai sebelum menulis janji.
4. Tetapkan prioritas dukungan dan waktu tanggap.
5. Samakan seluruh angka dengan kontrak API. Kuota wajib sama di semua dokumen.

## Contoh terisi: butir syarat API-01

| Butir | Isi pada contoh | Tempat | Pemilik |
| :-- | :-- | :-- | :-- |
| Tujuan pemakaian | Mencari jadwal dan membuat janji bagi pasien klinik mitra | Syarat penggunaan | Pemilik kemitraan |
| Kewenangan | Hanya petugas yang diverifikasi. Kredensial tidak boleh dibagi | Syarat penggunaan | Pemilik kemitraan |
| Batas konsumsi | Kuota uji 100, kuota produksi 300 panggilan per hari per klinik | Syarat, perjanjian, kontrak | Tim integrasi |
| Data sandbox | Hanya 20 pasien sintetis. Data pasien nyata dilarang | Syarat penggunaan | Petugas pelindungan data |
| Tanggung jawab mitra | Hanya 201 yang ditulis sebagai janji terkonfirmasi | Kontrak API, syarat | Manajer Layanan Rawat Jalan |
| Biaya | Rp3 juta per klinik per bulan, masih usulan | Perjanjian kerja sama | Manajer Keuangan |
| Perubahan versi | Masa transisi 6 bulan, tanggal sunset | Perjanjian, portal | Pemilik produk |
| Penghentian | Akses dicabut, janji aktif diselesaikan | Perjanjian kerja sama | Pemilik kemitraan |

## Contoh terisi: janji ketersediaan API-01

| Ukuran | Nilai contoh | Sifat |
| :-- | :-- | :-- |
| SLI | Permintaan pemesanan yang dijawab tanpa 5xx, dibagi seluruh permintaan, per bulan | Cara mengukur |
| SLO | 99,4 persen | Target internal |
| SLA | 99,0 persen, di luar pemeliharaan yang diumumkan 14 hari sebelumnya | Janji kepada mitra |
| Akibat | Kredit 10 persen langganan bulan itu, Rp300.000 per klinik | Konsekuensi |

## Contoh terisi: prioritas dukungan

| Prioritas | Contoh | Waktu tanggap | Eskalasi |
| :-- | :-- | :-- | :-- |
| 1 Kritis | Salah pasien, dugaan kebocoran data | 15 menit | Kepala Keamanan Informasi dan petugas pelindungan data |
| 2 Tinggi | Satu klinik tidak dapat memesan | 1 jam | Tim integrasi |
| 3 Sedang | Galat tidak jelas, kuota perlu ditinjau | 4 jam kerja | Tim integrasi |
| 4 Rendah | Permintaan contoh dokumentasi | 5 hari kerja | Pemilik produk |

## Lembar tim

| Butir | Isi usulan tim | Tempat | Pemilik | Bukti dan asumsi |
| :-- | :-- | :-- | :-- | :-- |
| Tujuan pemakaian | ... | ... | ... | ... |
| Kewenangan | ... | ... | ... | ... |
| Batas konsumsi | ... | ... | ... | ... |
| Tingkat layanan dan akibatnya | ... | ... | ... | ... |
| Dukungan | ... | ... | ... | ... |
| Penghentian | ... | ... | ... | ... |

## Tinjauan

- Apakah janji lebih tinggi daripada ketersediaan rantai yang terukur?
- Pemeliharaan apa yang dikecualikan, dan bagaimana diumumkan?
- Apakah kuota pada syarat, perjanjian, dan kontrak sudah sama?

Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata.
