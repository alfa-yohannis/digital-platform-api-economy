# Sumber Bab 09

Salin templat sebelum mengisi. Contoh Medikara memakai data sintetis dan bukan bukti organisasi nyata.

| Berkas | Kegunaan |
| :-- | :-- |
| [lembar-aturan-bisnis.md](lembar-aturan-bisnis.md) | Lembar bagi anggota non-teknis: kosakata, aturan bisnis, contoh data, dan kasus gagal dalam bahasa biasa, dengan contoh API-01 |
| [templat-kontrak-openapi.yaml](templat-kontrak-openapi.yaml) | Templat OpenAPI 3.2.0 bagi anggota teknis. Setiap teks ISI diganti dari lembar aturan bisnis |
| [kontrak-api-01-janji-temu.yaml](kontrak-api-01-janji-temu.yaml) | Contoh kontrak terisi untuk API-01 Jadwal dan Janji Temu. Sumber listing Bab 9 dan slide sesi 09 |
| [daftar-periksa-desain-api.md](daftar-periksa-desain-api.md) | Daftar periksa tinjauan bersama, dengan bukti contoh API-01 dan lembar tim |
| [periksa-kontrak.py](periksa-kontrak.py) | Memeriksa kelengkapan tiap operasi dan mencetak ringkasan operasi, scope, serta kode jawaban |
| [latihan2-usulan-perubahan.yaml](latihan2-usulan-perubahan.yaml) | Potongan usulan vendor untuk Latihan 2. Sengaja berisi perubahan yang merusak |
| [event-hasil-tersedia-asyncapi.yaml](event-hasil-tersedia-asyncapi.yaml) | Contoh kontrak AsyncAPI 3.1.0 untuk pemberitahuan hasil pemeriksaan, sebagai pembanding OpenAPI |
| [aturan-spectral.yaml](aturan-spectral.yaml) | Aturan Spectral opsional untuk Pendalaman Teknis pada Aktivitas |

## Cara memeriksa

Jalankan perintah berikut dari folder ini.

```
pip install pyyaml
python periksa-kontrak.py kontrak-api-01-janji-temu.yaml
spectral lint kontrak-api-01-janji-temu.yaml --ruleset aturan-spectral.yaml
prism mock kontrak-api-01-janji-temu.yaml
```

Dua baris pertama adalah pemeriksaan struktur. Skrip hanya membaca berkas lokal dan tidak memanggil server. Lulus pemeriksaan tidak berarti arti kontrak sudah benar. Berkas latihan 2 memang menghasilkan temuan.

Dua baris terakhir bersifat opsional dan membutuhkan Spectral dan Prism yang dipasang lewat Node.js. Saat diuji, Spectral 6.17.0 menerima kontrak 3.2.0 tanpa galat, dan Prism 5.14.2 menjawab 200 dengan token serta 401 tanpa token. Kontrak API-01 tidak memakai bidang khusus versi 3.2, sehingga salinannya tetap valid sebagai 3.1.1 bila versi alat lain belum mendukung 3.2.

Mock server hanya dijalankan di komputer sendiri. Pemindaian atau uji beban pada sistem pihak lain tidak boleh dilakukan tanpa izin tertulis.

## Catatan data

Domain `.example` dicadangkan untuk contoh. Nama dokter, nomor pasien, dan pengenal lain bersifat sintetis. Data organisasi nyata dipakai dengan izin dan dianonimkan. Data pribadi pasien atau karyawan tidak boleh dipakai.
