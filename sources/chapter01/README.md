# Sumber Bab 01: Orientasi: Platform, API, dan Capstone

| Berkas | Kegunaan |
| --- | --- |
| `profil-organisasi.md` | Templat profil organisasi satu halaman untuk Aktivitas, lengkap dengan contoh singkat Medikara Health |
| `panduan-wawancara-singkat.md` | Panduan wawancara sekitar 20 menit dan penelusuran dokumen tentang pihak luar, termasuk aturan izin dan anonimisasi |
| `daftar-pertukaran-data.md` | Lembar kerja daftar pertukaran data dengan pihak luar, beserta petunjuk pengisian dan daftar periksa sebelum dikumpulkan |
| `contoh-pertukaran-data-medikara.csv` | Data kasus: daftar pertukaran data Medikara Health yang sudah terisi, dipakai di Aktivitas dan Latihan 3 |
| `panggil-api-publik.py` | Pendalaman teknis: memanggil API gempa terbaru BMKG tanpa akun, lalu menampilkan kode status HTTP dan isi JSON |

Berkas `.md` diawali komentar yang menjelaskan kegunaan dan cara memakainya.
Berkas `.csv` tidak diberi komentar agar tetap terbaca rapi di aplikasi
*spreadsheet*. Baris pertamanya berisi nama kolom.

## Memakai lembar kerja

Salin `profil-organisasi.md` dan `daftar-pertukaran-data.md` ke folder tim, lalu
isi bersama. Tim yang memakai Medikara Health dapat membuka
`contoh-pertukaran-data-medikara.csv` di aplikasi *spreadsheet* sebagai
pembanding. Data organisasi nyata dipakai dengan izin tertulis dan dianonimkan.
Data pribadi pasien atau karyawan tidak boleh dipakai.

## Menjalankan pendalaman teknis

Skrip hanya memakai pustaka standar Python 3, sehingga tidak perlu memasang paket.
Dari direktori bab ini:

```bash
cd sources/chapter01
python panggil-api-publik.py                   # panggilan yang benar, kode 200
python panggil-api-publik.py autogempaa.json   # sengaja salah ketik, kode 404
```

Padanannya dengan `curl`:

```bash
curl -i https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json
```

Data berasal dari BMKG, dan setiap pemakaiannya wajib mencantumkan BMKG sebagai
sumber. Panggil API beberapa kali secara manual saja, bukan dalam putaran yang
cepat, agar tidak membebani server milik pihak lain.
