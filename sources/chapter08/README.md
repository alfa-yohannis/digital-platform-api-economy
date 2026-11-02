# Sumber Bab 08

Salin templat sebelum mengisi. Contoh Medikara memakai data latihan dan bukan bukti organisasi nyata. Status "Tahun depan" pada matriks adalah usulan Bab 8, sebelum beban Bab 10, Bab 11, dan Bab 13 dijumlahkan. Bab 14 menggeser 2.000 jam pembangunan API-02 ke 2028.

| Berkas | Kegunaan |
| :-- | :-- |
| [kanvas-produk-api.md](kanvas-produk-api.md) | Templat kanvas delapan unsur untuk Aktivitas, dengan pertanyaan dan kolom status bukti |
| [contoh-kanvas-janji-temu.md](contoh-kanvas-janji-temu.md) | Contoh kanvas terisi untuk API-01 Jadwal dan Janji Temu, beserta hitungan pendukungnya |
| [matriks-prioritas-api.csv](matriks-prioritas-api.csv) | Delapan kandidat Medikara dengan gerbang, skor, jam usaha, manfaat, dan keputusan |
| [hitung-prioritas-portofolio.py](hitung-prioritas-portofolio.py) | Menghitung skor pada dua perangkat bobot dan sisa kapasitas dari matriks CSV |

CSV memakai UTF-8 dan koma. Hapus komentar `#` di awal saat impor ke spreadsheet. Periksa satuan angka dan bedakan bukti, asumsi, serta target. Kolom `manfaat_juta_per_tahun` memakai titik sebagai pemisah desimal, sedangkan naskah memakai koma.

Skrip dijalankan dengan `python hitung-prioritas-portofolio.py`. Skrip hanya membaca CSV lokal dan tidak memanggil server. Tidak ada uji beban atau pemindaian pada sistem pihak lain. Skrip hanya dipakai pada data latihan atau sumber berizin.
