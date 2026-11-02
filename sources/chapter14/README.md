# Sumber Bab 14

Salin templat sebelum mengisi. Contoh Medikara memakai data sintetis dan bukan bukti organisasi nyata.

| Berkas | Kegunaan |
| :-- | :-- |
| [penilaian-kesiapan-agen-ai.md](penilaian-kesiapan-agen-ai.md) | Lembar kerja kesiapan per operasi, dengan contoh API-01 terisi dan ruang isian tim |
| [templat-peta-jalan-platform.md](templat-peta-jalan-platform.md) | Lembar kerja neraca, tiga gelombang, dan penundaan, dengan contoh Medikara terisi dan ruang isian tim |
| [hitung-peta-jalan.py](hitung-peta-jalan.py) | Mengulang seluruh hitungan bab: kuota agen, biaya kesalahan, konfirmasi, ambang antarmuka, skor kesiapan, neraca, gelombang, dan sumbu waktu pendapatan |
| [alur-janji-temu.arazzo.yaml](alur-janji-temu.arazzo.yaml) | Alur Arazzo tiga langkah di atas kontrak API-01 Bab 9 |
| [periksa-alur-arazzo.py](periksa-alur-arazzo.py) | Memeriksa kecocokan operasi dan parameter alur Arazzo dengan kontrak, tanpa memanggil server |
| [contoh-server-mcp](contoh-server-mcp) | Server MCP latihan dengan dua tool baca dan pratinjau pada data sintetis; baca petunjuk dan batas penggunaannya |
| [illustration-prompt.md](illustration-prompt.md) | Asal ilustrasi `figures/ch14-agen-terkendali.jpg`, yang saat ini belum dipasang pada bab atau slide |

## Cara menjalankan

```powershell
python hitung-peta-jalan.py
python periksa-alur-arazzo.py
```

Skrip pertama hanya memakai pustaka standar Python. Skrip kedua memerlukan PyYAML. Keduanya tidak memanggil sistem mana pun.

## Status pemeriksaan terakhir

| Yang diperiksa | Hasil |
| :-- | :-- |
| `python hitung-peta-jalan.py` pada Python 3.12 | Berjalan, angkanya sama dengan naskah Bab 14 |
| `python periksa-alur-arazzo.py` dengan PyYAML | Berjalan, 3 langkah lulus dan 0 temuan |
| `python contoh-server-mcp/simulasi.py` | Berjalan |
| `python contoh-server-mcp/periksa-demo.py` dengan `mcp==2.3.0` | Berjalan, empat pemeriksaan lulus |
| MCP Inspector | Belum dijalankan, karena `npx` tidak tersedia pada mesin pemeriksaan |

Lulus pada pemeriksaan di atas hanya berarti skrip dan contoh berjalan. Hasil itu bukan bukti bahwa agen aman dipakai. Konfigurasi produksi memerlukan tinjauan keamanan dan operasional.

## Batas pemakaian

Skrip hanya dipakai pada data sintetis atau sumber berizin. Data pribadi pasien atau karyawan tidak boleh dimasukkan ke model, skrip, atau alat apa pun. Uji penyalahgunaan dan pengulangan hanya dijalankan pada sistem sendiri atau yang sudah berizin tertulis.

Periksa satuan angka, dan bedakan bukti, asumsi, serta target. Seluruh angka tambahan Medikara adalah pemisalan latihan.
