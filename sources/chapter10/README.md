# Sumber Bab 10

Salin templat sebelum mengisi. Contoh Medikara memakai data sintetis dan bukan bukti organisasi nyata.

| Berkas | Kegunaan |
| :-- | :-- |
| [kebijakan-siklus-hidup-api.md](kebijakan-siklus-hidup-api.md) | Lembar kebijakan: gerbang tiap tahap dan masa transisi, dengan contoh API-01 dan lembar tim |
| [templat-pemberitahuan-deprecation.md](templat-pemberitahuan-deprecation.md) | Templat surat dan jadwal komunikasi kepada mitra bagi anggota bisnis dan hukum |
| [biaya-platform-3-tahun.csv](biaya-platform-3-tahun.csv) | Pemisalan biaya tiga alternatif selama 3 tahun, sumber Tabel biaya pada Bab 10 |
| [matriks-pemilihan-platform-api.csv](matriks-pemilihan-platform-api.csv) | Matriks berbobot tiga alternatif, sumber Tabel matriks pada Bab 10 |
| [hitung-matriks-platform.py](hitung-matriks-platform.py) | Menghitung biaya, nilai, dan pengaruh perubahan asumsi dari kedua CSV |
| [simulasi-batas-laju.py](simulasi-batas-laju.py) | Mengulang hitungan batas laju dan kuota Bab 6 dengan token bucket, tanpa memanggil sistem apa pun |
| [contoh-header-deprecation.http](contoh-header-deprecation.http) | Contoh jawaban versi lama dengan header Deprecation dan Sunset, sumber listing Bab 10 |
| [gateway-lokal/docker-compose.yaml](gateway-lokal/docker-compose.yaml) | Menjalankan Apache APISIX dan layanan contoh di komputer sendiri, untuk pendalaman opsional |
| [gateway-lokal/config.yaml](gateway-lokal/config.yaml) | Menetapkan APISIX sebagai mode standalone tanpa etcd |
| [gateway-lokal/apisix.yaml](gateway-lokal/apisix.yaml) | Rute API-01 dengan token, batas laju, dan kuota, sumber listing Bab 10 |
| [gateway-lokal/layanan-contoh.py](gateway-lokal/layanan-contoh.py) | Layanan tiruan yang menjawab data sintetis di belakang gateway |
| [gateway-lokal/buat-token-latihan.py](gateway-lokal/buat-token-latihan.py) | Membuat token latihan dengan rahasia yang hanya berlaku untuk contoh ini |

CSV memakai UTF-8 dan koma. Hapus komentar `#` di awal saat impor ke spreadsheet. Periksa satuan angka dan bedakan bukti, asumsi, serta target. Harga pada CSV contoh bukan harga produk. Harga yang dipakai tim wajib menyebut sumber dan tanggal.

## Menghitung pilihan platform

```bash
python hitung-matriks-platform.py
python simulasi-batas-laju.py
```

## Pendalaman opsional: gateway lokal

Peringatan: jalankan hanya pada komputer sendiri. Rahasia pada berkas contoh tidak boleh dipakai di produksi. Uji beban dan pemindaian pada sistem milik orang lain memerlukan izin tertulis.

Berkas gateway lokal sudah dijalankan dengan image `apache/apisix:3.19.0-debian`. Image ini membutuhkan `config.yaml`, karena variabel `APISIX_STAND_ALONE` saja membuat gateway berhenti saat dinyalakan. Bila versi image berubah, periksa kembali dokumentasinya.

```bash
cd gateway-lokal
docker compose up -d
TOKEN=$(python buat-token-latihan.py)
URL=http://localhost:9080/jadwal-dokter
curl -i $URL
curl -i -H "Authorization: $TOKEN" $URL
for i in $(seq 10); do curl -s -o /dev/null -w "%{http_code}\n" \
  -H "Authorization: $TOKEN" $URL; done
docker compose down
```

Hasil yang diharapkan: permintaan tanpa token dijawab 401, permintaan dengan token dijawab 200, dan sebagian permintaan cepat pada perulangan dijawab 429. Saat diuji, dari 10 permintaan cepat, 3 dijawab 200 dan 7 dijawab 429.

Skrip hanya dipakai pada data sintetis atau sumber berizin. Contoh teknis adalah latihan lokal. Konfigurasi produksi memerlukan tinjauan keamanan dan operasional.
