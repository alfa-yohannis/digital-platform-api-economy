<!-- Kegunaan: kerangka portal pengembang dan ukuran keberhasilannya untuk Bab 11. Cara pakai: salin berkas, isi lembar tim, lalu lampirkan pada artefak C3. -->
# Kerangka portal pengembang

Lembar kerja Bab 11: Developer Experience dan Portal Pengembang. Seluruh angka Medikara adalah data latihan. Pisahkan fakta, asumsi, dan target.

## Langkah kerja

1. Tulis pertanyaan tiap pengguna sebelum menyusun menu.
2. Tentukan isi portal minimum dan isi yang ditunda.
3. Tentukan sumber tunggal tiap isi, supaya angka tidak berbeda antarhalaman.
4. Bandingkan pilihan lingkup portal dengan batas anggaran dan jam tim.
5. Tetapkan ukuran keberhasilan, sumber data, periode, dan cara ukuran itu dapat menyesatkan.

## Contoh terisi: isi portal minimum API-01

| Kelompok | Halaman | Pertanyaan yang dijawab | Sumber isi | Pemilik | Kapan |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Temukan | Katalog | API apa yang ada, milik siapa, pada tahap apa? | Katalog Bab 10 | Pemilik produk | Sejak klinik uji |
| Temukan | Syarat dan tingkat akses | Apa syarat tiap tingkat? | Tangga keterbukaan Bab 3 | Pemilik kemitraan | Sejak klinik uji |
| Mulai | Panduan mulai cepat | Bagaimana mencapai panggilan pertama? | Ditulis, diuji rekan baru | Tim integrasi | Sejak klinik uji |
| Mulai | Pendaftaran dan kredensial uji | Bagaimana memperoleh akses uji? | Fitur portal | Pemilik kemitraan | Sejak klinik uji |
| Bangun | Referensi | Apa isi tiap operasi? | Dibangkitkan dari kontrak Bab 9 | Tim integrasi | Sejak klinik uji |
| Bangun | Panduan galat dan koleksi contoh | Apa arti gagal dan langkah berikutnya? | Model galat Bab 9 | Tim integrasi | Sejak klinik uji |
| Operasikan | Status layanan | Apakah sedang ada gangguan? | Pemantauan Bab 10 | Tim integrasi | Sebelum klinik ke-6 |
| Operasikan | Jadwal versi dan sunset | Apa yang berubah dan kapan? | Kebijakan siklus hidup Bab 10 | Pemilik produk | Sebelum klinik ke-6 |
| Operasikan | Dukungan | Ke mana melapor, berapa lama dijawab? | Tabel prioritas | Layanan pelanggan | Sejak klinik uji |

Isi yang ditunda pada contoh: SDK per bahasa, video, forum terbuka, dan acara pengembang.

## Contoh terisi: tiga ukuran hasil

| Ukuran | Awal dan akhir pengukuran | Sumber data | Periode | Dapat menyesatkan bila |
| :-- | :-- | :-- | :-- | :-- |
| Waktu sampai panggilan pertama | Dari pendaftaran sampai jawaban 200 pertama di sandbox | Catatan portal dan gateway | Median per gelombang klinik | Akun dibuatkan staf sebelum jam mulai dicatat |
| Tugas selesai tanpa bantuan | 3 tugas normal dan 6 skenario gagal | Hasil uji dan catatan tiket | Per klinik saat uji integrasi | Skenario sulit dihapus dari daftar |
| Aktivasi mitra | Klinik dengan minimal satu 201 produksi dalam 30 hari | Identitas klien pada gateway | Bulanan | Klinik menguji di produksi agar terlihat aktif |

## Lembar tim

| ID | Halaman atau ukuran | Pertanyaan atau definisi | Sumber dan pemilik | Bukti dan asumsi | Tanggal tinjau |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | ... | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... | ... |

## Tinjauan

- Apakah menu mengikuti pertanyaan pengguna, atau mengikuti susunan organisasi?
- Halaman mana yang berisiko berbeda angka dengan kontrak?
- Ukuran mana yang masih benar bila jumlah mitra berubah?

Gunakan metadata bukti bila dokumen organisasi tidak boleh dibagikan. Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata.
