<!-- Kegunaan: lembar kerja kesiapan agen AI Bab 14. Cara pakai: salin lembar ini untuk satu API prioritas C3. -->
# Penilaian Kesiapan API untuk Agen AI

Salin lembar ini untuk satu API prioritas C3. Nilai tiap operasi, bukan API secara keseluruhan. Gunakan bukti pengujian dan data sintetis.

Skala latihan: **0 belum ada**, **1 sebagian**, **2 sudah dibuktikan**. Skala ini alat bab, bukan standar industri. Skor membantu diskusi, dan syarat keselamatan tidak boleh dikompensasi oleh skor tinggi pada aspek lain.

- Aksi baca mensyaratkan identitas, konsumsi, konteks asing, dan audit bernilai 2.
- Aksi tulis mensyaratkan seluruh delapan aspek bernilai 2.

## Contoh terisi: dua operasi API-01

Skor mencerminkan keadaan sesudah Bab 13, saat kontrak baru ada di atas kertas. Seluruh skor adalah pemisalan latihan.

| Aspek | Pertanyaan pemeriksaan | Bukti minimum | `cariJadwalDokter` | `buatJanjiTemu` |
| :-- | :-- | :-- | :-- | :-- |
| Deskripsi | Apakah arti aksi dan akibatnya jelas? | Kontrak serta contoh normal dan gagal, diuji pada agen | 1 | 1 |
| Identitas | Siapa diwakili agen? | Identitas agen dan pihak yang diwakili | 1 | 1 |
| Otorisasi | Objek dan tindakan apa yang diizinkan? | Uji akses sah dan ditolak pada server | 1 | 1 |
| Pratinjau | Dapatkah pengguna meninjau akibat sebelum transaksi? | Dokter, fasilitas, waktu, dan akibat relevan | 2 | 0 |
| Pengulangan | Apakah panggilan ulang menggandakan transaksi? | Kontrak idempotensi dan uji pengulangan | 2 | 1 |
| Konsumsi | Bagaimana langkah, waktu, dan biaya dibatasi? | Kuota per agen serta kondisi penghentian | 1 | 1 |
| Konteks asing | Dapatkah hasil tool mengubah kewenangan? | Uji instruksi berbahaya sebagai data tak tepercaya | 0 | 0 |
| Audit | Dapatkah tindakan ditelusuri tanpa mencatat data klinis? | ID permintaan, agen, pihak diwakili, aksi, dan keputusan | 1 | 1 |
| **Jumlah** | | Dari 16 | **9** | **6** |

Keputusan: keduanya belum boleh dibuka bagi agen pada data nyata. Skor 2 pada pratinjau dan pengulangan untuk `cariJadwalDokter` terpenuhi karena operasi itu tidak mengubah keadaan.

## Contoh pemilahan aksi

`cari_slot` dan `tinjau_slot` pada demo lokal hanya membaca data sintetis. Contoh layak untuk latihan pemilihan tool dan pratinjau. Demo belum menjadi integrasi produksi karena tidak menerapkan autentikasi, akses pasien, penyimpanan transaksi, atau persetujuan pemesanan.

| Aksi | Jenis | Kewenangan yang diperlukan | Tinjauan manusia | Keputusan contoh |
| :-- | :-- | :-- | :-- | :-- |
| `cariJadwalDokter` | Baca | Identitas agen dan batas konsumsi | Tidak per panggilan | Diuji dengan data sintetis |
| `pratinjauJanjiTemu` (usulan) | Pratinjau | Hak atas karyawan yang diwakili | Hasil ditampilkan untuk dinilai | Masuk kontrak 1.1.0, kelas B |
| `bacaJanjiTemu` | Baca terbatas | Hanya janji milik pihak yang diwakili | Tidak per panggilan | Sesudah uji lintas objek |
| `buatJanjiTemu`, `batalkanJanjiTemu` | Tulis | Hak atas pasien dan operasi | Konfirmasi sebelum tindakan | Tidak disediakan demo |
| API-02 Hasil Pemeriksaan | Ditutup | Identitas, hubungan layanan, tujuan yang sah | Sesuai kebijakan data | Ditunda sampai kontrol teruji |

## Ambang kelayakan

Siap secara teknis berbeda dari layak secara bisnis. Contoh: satu antarmuka Rp45 juta per tahun, penghematan Rp3.000 per janji, sehingga ambangnya 15.000 janji per tahun atau 1.250 per bulan. Satu perusahaan dengan 400 janji per bulan menghemat Rp14,4 juta per tahun.

## Lembar isian tim

| Aspek | Operasi 1: ... | Operasi 2: ... | Bukti dan tautan | Pemilik perbaikan |
| :-- | :-- | :-- | :-- | :-- |
| Deskripsi | ... | ... | ... | ... |
| Identitas | ... | ... | ... | ... |
| Otorisasi | ... | ... | ... | ... |
| Pratinjau | ... | ... | ... | ... |
| Pengulangan | ... | ... | ... | ... |
| Konsumsi | ... | ... | ... | ... |
| Konteks asing | ... | ... | ... | ... |
| Audit | ... | ... | ... | ... |
| **Jumlah** | ... | ... | ... | ... |

## Catatan keputusan tim

- API dan versi: ...
- Tujuan dan pihak yang diwakili: ...
- Aksi diizinkan dan dilarang: ...
- Aksi yang wajib mendapat persetujuan manusia: ...
- Kuota agen dan batas langkah per tugas: ...
- Ambang pemakaian yang membuat antarmuka baru sepadan: ...
- Bukti yang belum ada dan pemilik perbaikan: ...
- Gerbang persetujuan serta tanggal peninjauan: ...

Analisis: risiko apa yang tidak dapat dinilai hanya dari kontrak? Bukti apa yang membolehkan satu aksi berpindah dari uji ke produksi?
