# Sumber Bab 13

Salin templat sebelum mengisi. Contoh Medikara memakai data sintetis dan bukan bukti organisasi nyata.

| Berkas | Kegunaan |
| :-- | :-- |
| [model-tata-kelola-api.md](model-tata-kelola-api.md) | Lembar kerja hak keputusan, kelas perubahan, dan register pengecualian, dengan contoh terisi |
| [panduan-gaya-api.md](panduan-gaya-api.md) | Panduan gaya contoh GAYA-01 sampai GAYA-08 dan ruang isian tim |
| [daftar-batasan-regulasi.md](daftar-batasan-regulasi.md) | Daftar batasan persaingan usaha, data, dan sektor, lengkap dengan status verifikasi, untuk tonggak C4 |
| [katalog-api.csv](katalog-api.csv) | Katalog contoh API-01 sampai API-08, turunan matriks Bab 8 |
| [hitung-tata-kelola.py](hitung-tata-kelola.py) | Mengulang hitungan tiga model, biaya tahun pertama, pengecualian, pemeringkatan apotek, ambang DMA, dan kelengkapan katalog |
| [periksa-panduan-gaya.py](periksa-panduan-gaya.py) | Memeriksa enam butir panduan gaya pada kontrak OpenAPI, tanpa memanggil server |
| [aturan-spectral-gaya.yaml](aturan-spectral-gaya.yaml) | Aturan Spectral opsional untuk GAYA-01 dan GAYA-04 |
| [contoh-kontrak-melanggar.yaml](contoh-kontrak-melanggar.yaml) | Kontrak sintetis yang sengaja melanggar panduan, bahan uji pemeriksa |

## Cara menjalankan

```
python hitung-tata-kelola.py
pip install pyyaml
python periksa-panduan-gaya.py ../chapter09/kontrak-api-01-janji-temu.yaml
python periksa-panduan-gaya.py contoh-kontrak-melanggar.yaml
```

Hasil pemeriksa saat diuji: kontrak API-01 punya 4 operasi dan 0 temuan, sedangkan kontrak contoh punya 2 operasi dan 10 temuan. Kode keluar 1 berarti ada temuan.

Aturan Spectral memerlukan Node.js dan belum dijalankan saat berkas ini disusun. Logika dua aturannya diuji lewat `periksa-panduan-gaya.py`. Periksa keluaran Spectral saat pertama kali dipakai.

```
npm install -g @stoplight/spectral-cli
spectral lint ../chapter09/kontrak-api-01-janji-temu.yaml --ruleset aturan-spectral-gaya.yaml
```

CSV memakai UTF-8 dan koma. Hapus baris komentar `#` di awal saat impor ke spreadsheet. Periksa satuan angka, lalu bedakan bukti, asumsi, dan target.

Skrip hanya dipakai pada data sintetis atau data berizin yang sudah dianonimkan. Pemeriksa kontrak tidak memanggil server mana pun.

Daftar batasan regulasi adalah bahan diskusi kuliah, bukan nasihat hukum. Aturan dapat berubah, sehingga status verifikasi dan tanggal akses wajib diperbarui saat dipakai.
