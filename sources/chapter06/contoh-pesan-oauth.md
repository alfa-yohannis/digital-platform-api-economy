<!-- Kegunaan: contoh isi pesan dua alur OAuth 2.0 dengan nilai sintetis, bahan pendalaman Bab 6. Cara pakai: baca berurutan, bandingkan dengan langkah pada gambar alur, jangan mengirimkannya ke server mana pun. -->

# Contoh Pesan OAuth 2.0

Alamat `auth.medikara.example` memakai domain `.example` yang dicadangkan untuk contoh, sehingga tidak merujuk server nyata. Rahasia dan token di bawah ini adalah nilai sintetis.

## Alur client credentials: laboratorium meminta token

Langkah 1 pada gambar alur *client credentials*. Pesan ini berjalan antarserver, dan rahasia klien tidak ikut pada panggilan API berikutnya.

```http
POST /oauth2/token HTTP/1.1
Host: auth.medikara.example
Content-Type: application/x-www-form-urlencoded
Authorization: Basic bGFiLXNpbnRldGlzOnJhaGFzaWEtc2ludGV0aXM=

grant_type=client_credentials&scope=hasil.tulis
```

Jawaban server otorisasi:

```json
{
  "access_token": "token-sintetis-1",
  "token_type": "Bearer",
  "expires_in": 900,
  "scope": "hasil.tulis"
}
```

Nilai `expires_in` 900 detik sama dengan 15 menit, sesuai asumsi Bab 6.

## Alur authorization code dengan PKCE: Medikara+ meminta izin pasien

Nilai `code_challenge` dan `code_verifier` di bawah ini adalah contoh uji RFC 7636 Lampiran B. Skrip `hitung-pkce.py` menghitung ulang nilainya.

Langkah 3, aplikasi mengalihkan pasien ke server otorisasi:

```http
GET /oauth2/authorize?response_type=code&client_id=medikara-plus
  &redirect_uri=https%3A%2F%2Fapp.medikara.example%2Fkembali
  &scope=janji.baca
  &code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM
  &code_challenge_method=S256 HTTP/1.1
Host: auth.medikara.example
```

Langkah 6, aplikasi menebus kode dengan `code_verifier`:

```http
POST /oauth2/token HTTP/1.1
Host: auth.medikara.example
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&client_id=medikara-plus
&code=kode-sintetis-1
&redirect_uri=https%3A%2F%2Fapp.medikara.example%2Fkembali
&code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
```

## Pertanyaan baca

1. Pada alur pertama, pesan mana yang membawa rahasia klien? Mengapa rahasia itu tidak ikut pada panggilan API?
2. Pada alur kedua, mengapa `code_challenge` aman terlihat, sedangkan `code_verifier` baru muncul pada langkah 6?
3. Token pada kedua alur tidak memuat pasien tertentu. Pemeriksaan apa yang harus dilakukan layanan bisnis pada setiap permintaan?

Pengujian ke server nyata hanya dilakukan pada sistem sendiri atau yang sudah berizin tertulis.
