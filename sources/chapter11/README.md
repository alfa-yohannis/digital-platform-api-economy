# Sumber Bab 11

Salin templat sebelum mengisi. Contoh Medikara memakai data sintetis dan bukan bukti organisasi nyata.

| Berkas | Kegunaan |
| :-- | :-- |
| [alur-onboarding-mitra.md](alur-onboarding-mitra.md) | Tujuh tahap onboarding, enam skenario gagal API-01, rencana penghentian mitra, dan lembar tim |
| [kerangka-portal-pengembang.md](kerangka-portal-pengembang.md) | Isi portal minimum, tiga ukuran hasil, dan lembar tim |
| [templat-syarat-penggunaan.md](templat-syarat-penggunaan.md) | Butir syarat penggunaan, janji ketersediaan, prioritas dukungan, dan lembar tim bagi anggota bisnis dan hukum |
| [protokol-uji-panggilan-pertama.md](protokol-uji-panggilan-pertama.md) | Tata cara mengukur waktu sampai panggilan pertama bersama rekan baru, sumber tabel lima klinik uji |
| [perjalanan-onboarding-klinik.csv](perjalanan-onboarding-klinik.csv) | Pemisalan waktu kerja dan waktu tunggu per tahap, sumber gambar perjalanan dan tabel sasaran Bab 11 |
| [pilihan-portal.csv](pilihan-portal.csv) | Pemisalan empat pilihan lingkup portal selama 3 tahun, sumber tabel pilihan portal Bab 11 |
| [hitung-onboarding-portal.py](hitung-onboarding-portal.py) | Menghitung waktu, biaya, dan pengaruh perubahan jumlah tiket dari kedua CSV |
| [sandbox-api-01.py](sandbox-api-01.py) | Sandbox lokal API-01 dengan 20 pasien sintetis dan 6 skenario gagal, untuk pendalaman opsional |

CSV memakai UTF-8 dan koma. Hapus komentar `#` di awal saat impor ke spreadsheet. Periksa satuan angka dan bedakan bukti, asumsi, serta target. Angka pada CSV contoh bukan harga produk.

## Menghitung waktu dan pilihan portal

```bash
python hitung-onboarding-portal.py
```

## Pendalaman opsional: dokumentasi dan sandbox lokal

Peringatan: jalankan hanya pada komputer sendiri. Sandbox ini memakai data sintetis dan tidak boleh diisi data pasien nyata. Uji pada sistem milik orang lain memerlukan izin tertulis.

Skrip sandbox sudah dijalankan pada Python 3.12, dan keempat operasi serta enam skenario gagal sudah dicoba pada waktu bab ditulis. Perintah Redocly CLI sudah dicoba dengan versi 2.72.1 pada kontrak OpenAPI 3.2.0 dan menghasilkan satu berkas HTML. Bila kontrak ditolak pada versi lain, periksa versi alat. Redocly CLI versi 2 memerlukan Node.js 22.12.0 atau lebih baru.

```bash
# Terminal 1: dokumentasi dari kontrak Bab 9
npx @redocly/cli build-docs ../chapter09/kontrak-api-01-janji-temu.yaml \
  --output=dokumentasi-api-01.html

# Terminal 2: sandbox lokal
python sandbox-api-01.py

# Terminal 3: panggilan pertama
curl -i -H "Authorization: Bearer token-uji-klinik-01" \
  "http://127.0.0.1:8011/jadwal-dokter?rumahSakit=bekasi&tanggal=2026-11-02"
```

Hasil yang diharapkan pada perintah terakhir: jawaban 200 dengan satu slot sintetis. Skenario gagal dan pemicunya tercantum pada [alur-onboarding-mitra.md](alur-onboarding-mitra.md).

Skrip hanya dipakai pada data sintetis atau sumber berizin. Contoh teknis adalah latihan lokal. Konfigurasi produksi memerlukan tinjauan keamanan dan operasional.
