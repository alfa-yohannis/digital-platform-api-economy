<!-- Kegunaan: panduan wawancara pemilik proses untuk mengisi inventaris Bab 4. Cara pakai: salin berkas, pakai satu lembar per integrasi, lalu pindahkan jawaban ke inventaris-integrasi.csv. -->

# Panduan Wawancara Pemilik Proses

Lembar kerja Bab 4: API sebagai Produk dan Ekonomi API. Panduan ini dipakai anggota tim berlatar non-teknis. Pewawancara tidak perlu memahami cara kerja sistem. Tujuannya mengetahui kegunaan dan masalah tiap integrasi dari orang yang merasakannya.

## Sebelum wawancara

1. Minta izin organisasi secara tertulis. Jelaskan bahwa nama orang dan data pribadi tidak dicatat.
2. Baca daftar pertukaran data dari Bab 1 dan tiga sambungan terlemah dari Bab 3.
3. Siapkan satu lembar untuk tiap integrasi yang akan ditanyakan.

## Pertanyaan

| No | Pertanyaan | Kolom inventaris yang terisi |
| --- | --- | --- |
| 1 | Data apa yang diterima atau dikirim, dari mana, ke mana? | `sistem_asal`, `sistem_tujuan`, `data` |
| 2 | Bagaimana data itu berpindah sehari-hari: surel, portal, berkas, atau otomatis? | `cara_pertukaran` |
| 3 | Seberapa sering, dan berapa jumlahnya per bulan? | `frekuensi_volume` |
| 4 | Berapa sambungan atau pihak yang memakai cara ini? | `jumlah_sambungan` |
| 5 | Siapa yang memutuskan perubahan dan siapa yang menanggung biayanya? | `pemilik_bisnis` |
| 6 | Siapa yang dihubungi ketika sambungan ini rusak? | `pemilik_teknis` |
| 7 | Berapa jam kerja manual per bulan yang dihabiskan? Bagaimana cara mengetahuinya? | `jam_manual_per_bulan` |
| 8 | Apa yang terjadi pada pasien, keuangan, atau mitra ketika sambungan ini gagal? | `masalah` |
| 9 | Dokumen atau catatan apa yang dapat memperlihatkan hal tadi? | `sumber_bukti`, `status_bukti` |
| 10 | Bila boleh mengubah satu hal, apa yang diubah lebih dahulu? | catatan integrasi rawan |

## Contoh terisi: hasil pemeriksaan dari laboratorium mitra

Contoh ini memakai data latihan Medikara, bukan organisasi nyata.

| Pertanyaan | Jawaban | Status |
| --- | --- | --- |
| Data dan arah | Hasil pemeriksaan khusus, dari 3 laboratorium mitra ke SIMRS | Wawancara |
| Cara | Surel berisi hasil pindaian, lalu diketik ulang | Wawancara |
| Volume | Sekitar 1.100 pemeriksaan per bulan | Wawancara |
| Kerja manual | Misalkan 6 menit per hasil, jadi 110 jam per bulan | Asumsi, perlu catatan waktu |
| Pemilik | Manajer Laboratorium, pemilik teknis belum ada | Wawancara |
| Akibat kegagalan | Salah ketik hasil, dokter menunggu | Wawancara |
| Bukti lanjutan | Contoh surel yang dianonimkan, catatan koreksi hasil | Belum diperoleh |

## Lembar tim

| ID | Jawaban singkat | Bukti dan asumsi | Pemilik | Tanggal tinjau |
| --- | --- | --- | --- | --- |
| INT-01 | ... | ... | ... | ... |
| INT-02 | ... | ... | ... | ... |
| INT-03 | ... | ... | ... | ... |

## Sesudah wawancara

- Tandai status bukti: terverifikasi, wawancara, atau belum terverifikasi.
- Baris yang belum diketahui tetap ditulis sebagai ketidakpastian.
- Angka dari ingatan ditulis sebagai asumsi sampai ada catatan atau dokumen.

Bila dokumen organisasi tidak boleh dibagikan, tim mencatat metadata buktinya saja. Rekam medis, kredensial, dan data pribadi pasien atau karyawan tidak boleh dimasukkan.
