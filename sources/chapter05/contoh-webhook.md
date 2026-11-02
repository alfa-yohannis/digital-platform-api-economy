<!-- Kegunaan: contoh satu kiriman webhook hasil tersedia dan butir kontrak pemberitahuan, untuk kotak pendalaman dan Latihan 1 Bab 5. Cara pakai: baca contoh, lalu isi lembar kontrak untuk satu pemberitahuan di organisasi tim. -->

# Contoh Kiriman Webhook

Semua alamat dan pengenal fiktif. Nilai `webhook-signature` hanya penanda, bukan tanda tangan sungguhan. Nama *header* mengikuti pedoman Standard Webhooks, sedangkan isi mengikuti atribut wajib CloudEvents 1.0.2.

```http
POST /webhook/hasil-laboratorium HTTP/1.1
Host: klinik-mitra.example
Content-Type: application/json
webhook-id: evt-20261102-0187
webhook-timestamp: 1793582100
webhook-signature: v1,CONTOH-BUKAN-TANDA-TANGAN-SUNGGUHAN

{
  "specversion": "1.0",
  "id": "evt-20261102-0187",
  "source": "/medikara/laboratorium-rujukan",
  "type": "hasil.tersedia",
  "time": "2026-11-02T08:15:00+07:00",
  "data": {"idHasil": "HSL-58213", "idKlinik": "KM-017"}
}
```

*Payload* tidak memuat isi hasil dan tidak memuat identitas pasien. Klinik mengambil hasilnya lewat `GET` dengan otorisasi. Otorisasi dibahas di Bab 6.

## Langkah penerima

1. Periksa tanda tangan dan waktu kirim.
2. Cari pengenal kejadian pada catatan. Bila sudah ada, jawab 2xx tanpa memproses ulang.
3. Catat pengenal, jawab 2xx secepatnya, lalu taruh pekerjaan di antrean.
4. Cocokkan status secara berkala lewat REST untuk menemukan kiriman yang hilang.

## Contoh kontrak pemberitahuan Medikara

Angka berikut adalah asumsi latihan, bukan ketentuan dari pedoman yang dirujuk.

| Butir kontrak | Isi |
| --- | --- |
| Kejadian | `hasil.tersedia` |
| Pemilik | Manajer Laboratorium |
| Pengenal kejadian | `webhook-id`, sama pada setiap pengulangan |
| Pembuktian pengirim | Tanda tangan dan waktu kirim, selisih waktu paling lama 5 menit |
| Arti berhasil | Kode 2xx dalam 15 detik |
| Jadwal *retry* | 1 menit, 5 menit, 30 menit, 2 jam, 12 jam |
| Rekonsiliasi | `GET` hasil sejak waktu tertentu, sekali per jam per klinik |
| Bila tetap gagal | Dicatat, dilaporkan ke pemilik, klinik dihubungi |

## Lembar tim

| Butir kontrak | Isi |
| --- | --- |
| Kejadian | ... |
| Pemilik | ... |
| Pengenal kejadian | ... |
| Pembuktian pengirim | ... |
| Arti berhasil | ... |
| Jadwal *retry* | ... |
| Rekonsiliasi | ... |
| Bila tetap gagal | ... |

Rekam medis, kredensial, dan data pribadi nyata tidak boleh dimasukkan ke *payload* contoh.
