# Sumber Bab 12

Salin templat sebelum mengisi. Contoh Medikara memakai data sintetis dan bukan bukti organisasi nyata.

| Berkas | Kegunaan |
| :-- | :-- |
| [kalkulator-biaya-api.csv](kalkulator-biaya-api.csv) | Pemisalan biaya tetap dan variabel API-01, sumber tabel biaya dan gambar titik impas Bab 12 |
| [hitung-monetisasi.py](hitung-monetisasi.py) | Mengulang hitungan titik impas, model harga klinik, tabel Latihan 2, dan pohon metrik |
| [contoh-log-gateway.csv](contoh-log-gateway.csv) | Log *gateway* sintetis dari klinik uji U1 sampai U5, tanpa data pasien |
| [hitung-metrik-gateway.py](hitung-metrik-gateway.py) | Menghitung panggilan, transaksi unik, galat, dan latensi dari log, bahan *dashboard* pada kotak pendalaman |
| [templat-model-monetisasi.md](templat-model-monetisasi.md) | Lembar kerja pembayar, model harga, titik impas, dan keputusan untuk Aktivitas |
| [templat-pohon-metrik.md](templat-pohon-metrik.md) | Lembar kerja pohon metrik dengan contoh terisi API-01 dan ruang isian tim |

## Cara menjalankan

```
python hitung-monetisasi.py
python hitung-metrik-gateway.py
```

Kedua skrip hanya memakai pustaka standar Python dan membaca CSV dari folder yang sama. Skrip hanya dipakai pada data sintetis atau data berizin yang sudah dianonimkan.

CSV memakai UTF-8 dan koma. Hapus baris komentar `#` di awal saat impor ke spreadsheet. Periksa satuan angka, lalu bedakan bukti, asumsi, dan target.

Log nyata tidak boleh memuat identitas pasien. Kolom `id_transaksi` berisi kunci semu. Harga vendor yang dipakai tim wajib mencantumkan tanggal akses, karena harga dapat berubah.
