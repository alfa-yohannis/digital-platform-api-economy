<!-- Kegunaan: panduan gaya API contoh Bab 13. Cara pakai: salin berkas, sesuaikan butir, lalu turunkan butir mesin ke aturan pemeriksaan. -->

# Panduan gaya API

Lembar kerja Bab 13, Tata Kelola API dan Regulasi Platform. Contoh Medikara memakai data sintetis. Butir yang dapat dinilai mesin diperiksa `periksa-panduan-gaya.py`, dan dua di antaranya juga tersedia sebagai aturan Spectral pada `aturan-spectral-gaya.yaml`.

Kata WAJIB dan SEBAIKNYA mengikuti cara Zalando memakai tingkat kewajiban RFC 2119. Pemilik panduan adalah forum bersama.

## Langkah kerja

1. Ambil kebiasaan yang sudah terbukti pada kontrak Bab 9. Jangan menulis aturan yang belum pernah dipakai.
2. Beri setiap butir nomor, tingkat, alasan, contoh lulus, dan contoh gagal.
3. Tandai butir yang dapat dinilai mesin dan butir yang memerlukan manusia.
4. Jalankan pemeriksa pada satu kontrak nyata milik tim, lalu baca temuan bersama pemilik produk.
5. Catat pengecualian di `model-tata-kelola-api.md`, jangan mematikan aturan.

## Contoh terisi

| Butir | Tingkat | Isi | Alasan | Contoh lulus | Contoh gagal | Pemeriksa |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| GAYA-01 | WAJIB | Jalur memakai huruf kecil dan tanda hubung | Klien membaca seluruh API dengan satu kebiasaan | `/jadwal-dokter` | `/getJadwalDokter`, `/janji_temu` | Mesin |
| GAYA-02 | WAJIB | Setiap operasi punya `operationId` dan `summary` | Uji dan pelacakan butuh pengenal, pemilik produk butuh ringkasan | `buatJanjiTemu` | Operasi tanpa ringkasan | Mesin |
| GAYA-03 | WAJIB | Setiap operasi menyebut `security` dan *scope* | Akses yang tidak tertulis tidak dapat ditinjau | `janji.tulis` | Operasi tanpa `security` | Mesin |
| GAYA-04 | WAJIB | Jawaban 4xx dan 5xx memakai `application/problem+json` | Klien tidak perlu pengurai per rumah sakit | Jawaban 409 slot terisi | `text/plain` | Mesin |
| GAYA-05 | WAJIB | POST pembuat data menerima `Idempotency-Key` | Kirim ulang tidak membuat janji ganda | `POST /janji-temu` | POST tanpa kunci | Mesin |
| GAYA-06 | SEBAIKNYA | Daftar punya parameter `batas` | Jawaban besar membebani SIMRS | `GET /jadwal-dokter` | Daftar tanpa batas | Mesin |
| GAYA-07 | WAJIB | Setiap bidang data punya tujuan tertulis | Mesin tidak mengetahui alasan bidang ada | Bidang `spesialis` untuk mencari slot | Bidang diagnosis pada janji temu | Manusia |
| GAYA-08 | WAJIB | Hak atas objek diuji, bukan hanya token | Token sah dapat membaca objek milik pihak lain | Uji token klinik A pada janji klinik B | Hanya uji 401 | Manusia dan uji perilaku |

## Hasil pada dua kontrak

```
python periksa-panduan-gaya.py ../chapter09/kontrak-api-01-janji-temu.yaml
kontrak-api-01-janji-temu.yaml: 4 operasi, 0 temuan

python periksa-panduan-gaya.py contoh-kontrak-melanggar.yaml
contoh-kontrak-melanggar.yaml: 2 operasi, 10 temuan
```

Nol temuan hanya berarti kebiasaan tertulis dipenuhi. GAYA-07 dan GAYA-08 tetap ditinjau.

## Lembar tim

| Butir | Tingkat | Isi | Alasan | Contoh lulus | Contoh gagal | Pemeriksa | Pemilik |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... | ... |

## Tinjauan

- Apakah setiap butir punya alasan yang dapat dijelaskan kepada anggota non-teknis?
- Apakah butir mesin diuji pada contoh lulus dan contoh gagal?
- Apakah ada butir yang menilai makna, tetapi dipaksakan pada mesin?
- Siapa yang mengubah panduan, dan bagaimana API lama diperlakukan saat panduan berubah?

Gunakan data sintetis pada contoh kontrak. Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata.
