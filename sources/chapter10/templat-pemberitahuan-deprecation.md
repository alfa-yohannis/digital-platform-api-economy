<!-- Kegunaan: templat surat pemberitahuan deprecation kepada mitra pada Bab 10. Cara pakai: salin, isi bersama anggota hukum dan pemilik API, lalu mintakan pendapat satu calon mitra. -->
# Templat pemberitahuan deprecation kepada mitra

Lembar kerja Bab 10, Aktivitas: Rancangan Manajemen API. Lembar ini diisi anggota berlatar bisnis dan hukum. Contoh Medikara adalah data latihan. Surat tidak boleh memuat rekam medis, kredensial, atau data pribadi pasien.

## Unsur wajib

| Unsur | Pertanyaan yang dijawab | Contoh API-01 |
| :-- | :-- | :-- |
| Alasan | Mengapa versi lama dihentikan? | Pengenal pasien baru untuk strategi "Satu Pasien, Satu Rekam Medis" adalah perubahan merusak |
| Pengganti | Apa penggantinya, dan apa bedanya? | API-01 versi 2 pada alamat `/v2`, tipe `pasien` berubah |
| Tanggal | Kapan deprecation dan sunset berlaku? | Misalkan deprecation 1 Juli 2028, sunset 31 Desember 2028 |
| Cara menguji | Di mana dan dengan data apa? | Sandbox dengan data sintetis, 6 skenario |
| Bantuan | Siapa yang membantu, dan berapa lama? | Pendampingan 8 jam per klinik pada bulan ke-5 bila belum siap |
| Akibat | Apa yang terjadi sesudah tanggal sunset? | Versi 1 menjawab 410 dengan tautan panduan |
| Pengecualian | Bagaimana mengajukan perpanjangan? | Satu kali, paling lama 1 bulan, dengan alasan tertulis |
| Kontak | Siapa yang dihubungi? | Pemilik API dan kanal dukungan, bukan nama pribadi pasien atau petugas klinik |

## Contoh isi surat

Perihal: Penghentian API-01 Jadwal dan Janji Temu versi 1 pada 31 Desember 2028

Kepada pemilik integrasi [nama klinik mitra],

Medikara menerbitkan API-01 versi 2 pada 1 Juli 2028. Versi 1 tetap bekerja seperti semula sampai 31 Desember 2028. Sesudah tanggal itu, versi 1 menjawab kode 410.

Penggantian ini diperlukan karena [alasan]. Perubahan yang berdampak pada klinik adalah [daftar perubahan]. Panduan migrasi tersedia di [tautan], dan versi 2 dapat dicoba di sandbox dengan data sintetis.

Klinik diminta mengonfirmasi penerima surat ini sampai [tanggal], serta menyampaikan perkiraan waktu perubahan dari vendor perangkat lunak klinik sampai [tanggal]. Klinik yang memperkirakan belum siap pada bulan kelima dapat mengajukan pendampingan atau perpanjangan lewat [kanal]. Pengecualian keamanan akan diumumkan terpisah.

Hormat [nama jabatan pemilik API]

## Jadwal komunikasi

| Waktu | Saluran | Isi | Bukti terkirim | Pemilik |
| :-- | :-- | :-- | :-- | :-- |
| Bulan 0 | Surel, portal, header `Deprecation` dan `Sunset` | Surat lengkap | Konfirmasi 41 penerima | Manajer Layanan Rawat Jalan |
| Bulan 3 | Surel kepada pemakai tersisa | Sisa waktu, hasil uji, tawaran bantuan | Daftar 16 pemakai tersisa | Tim integrasi |
| Bulan 5 | Telepon dan surel | Status tiap klinik, keputusan pengecualian | Daftar 3 pemakai tersisa | Manajer Layanan Rawat Jalan |
| Bulan 6 | Surel, portal | Penutupan versi 1 | Arsip keputusan | Manajer Layanan Rawat Jalan |

## Lembar tim

| Waktu | Saluran | Isi | Bukti terkirim | Pemilik |
| :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

## Tinjauan

- Apakah penerima surat adalah pemilik integrasi yang sudah dikonfirmasi?
- Apakah tanggal yang sama tertulis di perjanjian kerja sama, portal, dan header?
- Apakah calon mitra dapat menyebut langkah berikutnya sesudah membaca surat?
