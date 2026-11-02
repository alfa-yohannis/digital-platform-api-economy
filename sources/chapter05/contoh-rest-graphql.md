<!-- Kegunaan: contoh satu kebutuhan data sebagai permintaan REST dan query GraphQL, untuk kotak pendalaman dan Latihan 3 Bab 5. Cara pakai: salin berkas, ganti contoh dengan kebutuhan data tim, lalu isi tabel perbandingan. Uji hanya pada sistem sendiri atau mock lokal. -->

# Contoh REST dan GraphQL

Semua alamat dan pengenal di bawah ini fiktif. Angka ukuran data adalah asumsi latihan Medikara Health, bukan hasil pengukuran sistem nyata.

## Membaca jadwal dan membuat janji temu dengan REST

Panggilan kedua membawa kunci idempotensi. `Idempotency-Key` masih berupa draf IETF, sehingga kontrak harus menuliskan sendiri cara memakainya dan masa simpannya. Bila kiriman diulang dengan kunci yang sama, server mengembalikan janji yang sudah ada.

```http
GET /jadwal-dokter?rumahSakit=bekasi&tanggal=2026-11-02 HTTP/1.1
Host: api.medikara.example
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: max-age=300

{"rumahSakit": "bekasi", "tanggal": "2026-11-02", "slot": []}

POST /janji-temu HTTP/1.1
Host: api.medikara.example
Content-Type: application/json
Idempotency-Key: "8e03978e-40d5-43e8-bc93-6894a57f9324"

{"slot": "BKS-20261102-0915", "pasien": "PSN-58213"}

HTTP/1.1 201 Created
Location: /janji-temu/JT-40771
```

## Layar Ringkasan Kunjungan dengan empat panggilan REST

```http
GET /kunjungan/KJG-1042 HTTP/1.1
GET /dokter/DR-221 HTTP/1.1
GET /lokasi/RS-BKS HTTP/1.1
GET /kunjungan/KJG-1042/hasil HTTP/1.1
```

## Layar yang sama dengan satu query GraphQL

```graphql
query RingkasanKunjungan {
  kunjungan(id: "KJG-1042") {
    tanggal
    status
    jenisLayanan
    dokter { nama spesialisasi ruangan }
    lokasi { namaFasilitas kota alamat }
    hasil { jenis status waktuSelesai }
  }
}
```

## Contoh terisi

Misalkan layar dibuka 3.000 kali per hari.

| Ukuran | REST | GraphQL |
| --- | --- | --- |
| Panggilan per layar | 4 | 1 |
| Bidang yang dijawab | 60 | 12 |
| Data per layar | 30 KB | 6 KB |
| Panggilan per hari | 12.000 | 3.000 |
| Data per hari | 90 MB | 18 MB |
| Waktu per layar, berurutan | 1,2 detik | 0,5 detik |
| Objek terburuk dari satu panggilan | Mengikuti batas halaman `/kunjungan` | 180.000 tanpa batas kedalaman dan biaya |

## Lembar tim

Kolom bukti diisi dari pengukuran pada sistem sendiri atau *mock* lokal.

| Ukuran | REST | GraphQL | Bukti atau asumsi |
| --- | --- | --- | --- |
| Panggilan per layar | ... | ... | ... |
| Bidang yang dijawab | ... | ... | ... |
| Data per layar | ... | ... | ... |
| Objek terburuk dari satu panggilan | ... | ... | ... |
| Pengendalian yang wajib dipasang | ... | ... | ... |

## Tinjauan

- Apakah layar ini benar-benar punya kebutuhan data yang beragam, atau hanya satu bentuk tetap?
- Apakah tim mampu menjaga batas kedalaman, biaya, dan otorisasi per objek?
- Apakah pemantauan membaca isi jawaban, bukan hanya kode status?

Kegiatan yang membebani sistem milik orang lain, termasuk uji beban, hanya untuk sistem sendiri atau yang sudah berizin tertulis. Rekam medis, kredensial, dan data pribadi nyata tidak boleh dipakai.
