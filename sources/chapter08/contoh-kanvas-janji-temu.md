<!-- Kegunaan: contoh kanvas terisi untuk API-01 Bab 8, data latihan. Cara pakai: baca sebagai pembanding, jangan dipakai sebagai bukti organisasi nyata. -->
# Contoh kanvas produk: API-01 Jadwal dan Janji Temu

Contoh Bab 8: Strategi dan Portofolio API. Seluruh angka adalah data latihan Medikara. Isi sama dengan gambar kanvas pada Bab 8.

## Identitas kandidat

| Butir | Isian |
| :-- | :-- |
| ID kandidat | API-01 |
| Nama kandidat | Jadwal dan Janji Temu |
| Kapabilitas dan tahap nilai | CAP-L03 Penjadwalan Layanan, tahap 1 Memesan layanan dan tahap 6 Ditindaklanjuti (IT40513 Bab 5) |
| Baris inventaris Bab 4 | INT-03 |
| Versi | 0.1, seluruh isi masih hipotesis |

## Delapan unsur

| Unsur | Isian | Status | Cara menguji |
| :-- | :-- | :-- | :-- |
| Pengguna | Aplikasi Medikara+ dan petugas 40 klinik mitra | Fakta dari Bab 2 dan Bab 4 | Wawancara petugas pada 5 klinik mitra |
| Masalah | Vendor membaca 140 tabel padahal butuh 2 tabel. Misalkan 10 persen dari 2.400 pemesanan per hari diikuti telepon 3 menit: 300 jam per bulan, Rp216 juta per tahun | 140 tabel fakta audit, telepon asumsi | Catatan telepon 2 minggu |
| Tawaran nilai | Slot terkonfirmasi saat dipesan, tanpa telepon ulang | Hipotesis | Uji dengan jawaban simulasi pada 5 klinik |
| Operasi | Cari jadwal, pilih slot, kunci slot, batalkan, baca status. Tidak membuka rekam medis | Usulan | Ditinjau pada kontrak Bab 9 |
| Dependensi | API-06, adaptor 5 SIMRS, perubahan aplikasi oleh vendor Medikara+ | Fakta dari Bab 6 | Surat kesediaan vendor dan tenggat INT-03 |
| Risiko | Slot ganda, jadwal kosong 7 sampai 14 hari per tahun saat SIMRS diperbarui, akses 138 tabel bila peralihan tertunda | Fakta dari Bab 5, slot ganda asumsi | Uji kunci slot dan rencana peralihan |
| Ukuran | Janji terkonfirmasi tanpa kerja ulang. Telepon konfirmasi turun dari 10 ke 2 persen. Rata-rata 180 panggilan per klinik per hari, di bawah kuota 300 | Target | Dipantau per triwulan |
| Pemilik | Manajer Layanan Rawat Jalan. Tim integrasi menjaga operasi | Pengandaian Bab 4 | Tanda tangan keputusan |

## Hitungan pendukung

| Butir | Hitungan | Hasil |
| :-- | :-- | :-- |
| Kebutuhan panggilan | 40 klinik x 180 panggilan | 7.200 per hari, atau 60 persen dari 12.000 |
| Beban telepon | 2.400 x 10 persen x 3 menit, 25 hari kerja | 300 jam per bulan, Rp18 juta per bulan |
| Biaya pembangunan | 2.400 jam x Rp60.000 | Rp144 juta |
| Biaya perawatan | Satu antarmuka | Rp45 juta per tahun |
| Pendapatan yang bergantung | 40 klinik x Rp3 juta x 12 bulan | Rp1,44 miliar per tahun, skema Bab 2 |

## Lembar tim

| ID | Usulan tim | Bukti dan asumsi | Pemilik | Tanggal tinjau |
| :-- | :-- | :-- | :-- | :-- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |

## Tinjauan

- Apakah telepon konfirmasi benar-benar turun? Bila tidak, tawaran nilai perlu ditulis ulang.
- Apakah 5 klinik uji mewakili 40 klinik mitra?
- Bukti apa yang dapat mengubah keputusan? Contoh: vendor Medikara+ menolak tenggat INT-03.

Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata.
