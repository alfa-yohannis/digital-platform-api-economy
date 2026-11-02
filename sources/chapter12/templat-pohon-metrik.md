<!-- Kegunaan: lembar kerja pohon metrik Bab 12. Cara pakai: salin berkas, lalu isi lembar tim dengan bukti organisasi. -->

# Templat pohon metrik

Lembar kerja Bab 12, Monetisasi API dan Metrik Platform. Contoh Medikara memakai data sintetis. Pisahkan fakta, asumsi, dan target.

## Langkah kerja

1. Tulis satu hasil pengguna yang berulang. Hasil itu harus dapat dihitung sebagai interaksi unik yang selesai.
2. Turunkan tiga sampai lima pendorong yang dapat dipengaruhi tim.
3. Di bawah tiap pendorong, tulis metrik operasional beserta sumber datanya di *gateway*, portal, SIMRS, tiket, atau keuangan.
4. Pasang satu penyeimbang untuk tiap risiko pengejaran angka.
5. Tetapkan pemilik, periode, dan tindakan bila angka memburuk.

## Contoh terisi: API-01 Jadwal dan Janji Temu

Ukuran utama: janji temu dan rujukan selesai tepat waktu per bulan.
Rumus contoh: klinik aktif x pemesanan per klinik x tingkat kecocokan x tingkat selesai tepat waktu.

| Lapisan | Metrik | Definisi | Sumber data | Pemilik | Dasar | Sasaran | Tindakan bila memburuk |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Ukuran utama | Interaksi unik selesai | Satu ID janji, pasien dilayani dalam sasaran waktu | SIMRS, *gateway* | Manajer Layanan Rawat Jalan | 20.160 | 34.884 | Telusuri pendorong yang turun |
| Pendorong | Klinik aktif | Klinik dengan minimal satu 201 produksi dalam 30 hari | *Gateway* | Pemilik kemitraan | 28 | 36 | Hubungi klinik yang berhenti |
| Pendorong | Pemesanan per klinik | Permintaan janji unik per klinik aktif per bulan | *Gateway* | Manajer Layanan Rawat Jalan | 1.000 | 1.200 | Periksa hambatan di klinik |
| Pendorong | Tingkat kecocokan | Pemesanan yang memperoleh slot dalam sasaran waktu | *Gateway*, SIMRS | Manajer Layanan Rawat Jalan | 90 persen | 95 persen | Tambah slot, periksa jadwal SIMRS |
| Pendorong | Selesai tepat waktu | Janji yang dilayani dalam sasaran waktu | SIMRS | Manajer Layanan Rawat Jalan | 80 persen | 85 persen | Periksa antrean dan pengingat |
| Operasional | Galat 5xx | Permintaan pemesanan berkode 5xx dibagi seluruh permintaan | *Gateway* | Tim integrasi | Maks 0,6 persen | SLO 99,4 persen | Rapat insiden |
| Operasional | Latensi persentil ke-95 | Latensi pemesanan berhasil, dipisah dari yang gagal | *Gateway* | Tim integrasi | Diukur | Ditetapkan tim | Periksa SIMRS dan cache |
| Operasional | Panggilan per janji | Panggilan dibagi janji unik | *Gateway* | Tim integrasi | 3 | 3 | Periksa polling dan pengulangan |
| Operasional | Tiket per klinik | Tiket dibagi klinik aktif per bulan | Sistem tiket | Layanan pelanggan | 1 | 1 | Perbaiki panduan |
| Penyeimbang | Telepon konfirmasi | Pemesanan yang diikuti telepon | Catatan klinik | Manajer Layanan Rawat Jalan | 10 persen | 2 persen | Tulis ulang tawaran nilai |
| Penyeimbang | Pasien ganda | Janji ganda untuk satu pasien pada slot berdekatan | SIMRS | Tim integrasi | Diukur | Mendekati nol | Perbaiki aturan idempotensi |

## Lembar tim

| Lapisan | Metrik | Definisi | Sumber data | Pemilik | Dasar | Sasaran | Tindakan bila memburuk |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Ukuran utama | ... | ... | ... | ... | ... | ... | ... |
| Pendorong | ... | ... | ... | ... | ... | ... | ... |
| Pendorong | ... | ... | ... | ... | ... | ... | ... |
| Operasional | ... | ... | ... | ... | ... | ... | ... |
| Operasional | ... | ... | ... | ... | ... | ... | ... |
| Penyeimbang | ... | ... | ... | ... | ... | ... | ... |

## Tinjauan

- Apakah ukuran utama tetap benar bila jumlah panggilan API turun separuh?
- Dapatkah ukuran utama dipindahkan langsung oleh satu tim? Bila ya, ukuran itu terlalu dekat dengan aktivitas.
- Apakah setiap metrik punya tindakan bila angkanya memburuk?
- Apakah pemilik, sumber bukti, dan pemicu peninjauan sudah dicatat?

Gunakan metadata bila dokumen organisasi tidak boleh dibagikan. Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata.
