<!-- Kegunaan: daftar berkas pendukung Bab 6. Cara pakai: baca tabel di bawah, lalu salin berkas yang diperlukan ke folder tim sebelum mengisi. -->

# Sumber Bab 06

Berkas ini mendukung Aktivitas dan Latihan Bab 6 untuk tonggak C2. Salin templat sebelum mengisi. Contoh Medikara memakai data latihan dan bukan bukti organisasi nyata.

| Berkas | Kegunaan |
| :-- | :-- |
| [daftar-periksa-owasp-api-2023.md](daftar-periksa-owasp-api-2023.md) | Lembar periksa sepuluh butir OWASP per integrasi, dengan contoh INT-03 |
| [register-risiko-api.csv](register-risiko-api.csv) | Contoh register risiko Medikara RA-01 sampai RA-07, sekaligus templat tim |
| [hitung-risiko-api.py](hitung-risiko-api.py) | Skrip pengurut register dan pemeriksa skor: `python hitung-risiko-api.py register-risiko-api.csv` |
| [kronologi-insiden-medikara.md](kronologi-insiden-medikara.md) | Kronologi insiden vendor 2025 (data latihan), hipotesis butir OWASP, dan biaya langsung untuk Latihan 3 |
| [hitung-paparan-kredensial.py](hitung-paparan-kredensial.py) | Skrip paparan kredensial, batas laju, kuota, dan beban catatan untuk Latihan 2: `python hitung-paparan-kredensial.py` |
| [hitung-pkce.py](hitung-pkce.py) | Skrip perhitungan `code_challenge` PKCE S256, diuji dengan contoh RFC 7636: `python hitung-pkce.py` |
| [contoh-pesan-oauth.md](contoh-pesan-oauth.md) | Contoh pesan alur *client credentials* dan *authorization code* dengan PKCE, memakai nilai sintetis |

Periksa satuan angka dan bedakan bukti, asumsi, serta target. Hapus baris komentar `#` di awal berkas CSV bila diimpor ke *spreadsheet*.

Ketiga skrip hanya berhitung di komputer sendiri dan tidak memanggil server apa pun. Konfigurasi produksi memerlukan tinjauan keamanan dan operasional. Pemindaian, uji beban, dan uji hak akses hanya untuk sistem sendiri atau yang sudah berizin tertulis. Rekam medis, kredensial, dan data pribadi pasien atau karyawan tidak boleh dimasukkan.
