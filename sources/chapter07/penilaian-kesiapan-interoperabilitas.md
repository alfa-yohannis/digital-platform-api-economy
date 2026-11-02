<!-- Kegunaan: lembar kerja Aktivitas Bab 7, luaran tonggak C2. Cara pakai: salin berkas, lalu isi dengan bukti tim yang berizin. -->
# Penilaian kesiapan interoperabilitas

Lembar kerja Bab 7: Standar API Sektoral: SATUSEHAT, HL7 FHIR, dan SNAP. Salin berkas sebelum mengisi. Contoh Medikara adalah data latihan. Pisahkan fakta, asumsi, dan target.

## Langkah kerja

1. Pilih satu sampai tiga baris dari inventaris Bab 4 dan tandai jalurnya: klinis, administrasi, atau pembayaran.
2. Tentukan apakah standarnya wajib bagi organisasi. Tulis pasal atau dokumen dasarnya, beserta tenggatnya.
3. Petakan satu alur data dari kolom sumber ke elemen standar. Pakai `pemetaan-simrs-fhir.csv` bila berada di sektor kesehatan.
4. Nilai setiap kewajiban dengan skala di bawah, dan cantumkan status buktinya.
5. Tulis kesenjangan pada empat lapis: sintaks, semantik, proses, dan tanggung jawab.
6. Tetapkan pemilik, tindakan, dan tanggal tinjau. Gabungkan hasilnya dengan bukti Bab 4 sampai Bab 6 menjadi C2.

## Skala

| Tingkat | Skor | Syarat |
| :-- | :-- | :-- |
| Terpenuhi | 2 | Ada bukti terverifikasi bahwa kewajiban berjalan |
| Sebagian | 1 | Berjalan pada sebagian lingkup, atau penyebab kegagalannya masih hipotesis |
| Belum | 0 | Tidak berjalan, atau belum diperiksa |
| Tidak berlaku | Tidak dihitung | Ada alasan tertulis mengapa kewajiban ini tidak mengenai organisasi |

Baris berstatus "Belum terverifikasi" tidak boleh diberi tingkat Terpenuhi atau Sebagian.

## Contoh terisi (data latihan Medikara)

| ID | Baris | Kewajiban atau standar | Kondisi | Tingkat | Bukti | Pemilik |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| KI-01 | INT-02 | Kiriman ke platform Kementerian Kesehatan lengkap | Sekitar 4 persen kunjungan klinik belum terkirim | Sebagian | Terverifikasi | Manajer Rekam Medis |
| KI-02 | INT-02 | Status tiap kiriman dapat ditelusuri | Kiriman gagal tanpa pemberitahuan | Belum | Terverifikasi | Manajer Rekam Medis |
| KI-06 | INT-01 | Kepesertaan, surat eligibilitas, dan klaim berjalan | 5 sambungan berjalan | Terpenuhi | Terverifikasi | Manajer Klaim |
| KI-08 | INT-08 | Open API Pembayaran berbasis SNAP | Medikara bukan penyedia jasa pembayaran | Tidak berlaku | Terverifikasi | Manajer Keuangan |

Baris lengkap tersedia di `contoh-kesenjangan-medikara.csv`.

## Lembar tim

| ID | Baris | Kewajiban atau standar | Dasar dan tenggat | Kondisi | Tingkat | Bukti | Pemilik | Tanggal tinjau |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | ... | ... | ... | ... | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... | ... | ... | ... |

## Tinjauan

- Apakah setiap kewajiban punya pasal atau dokumen dasar yang dibaca langsung?
- Apakah baris tidak berlaku punya alasan tertulis?
- Apakah pilihan menjawab masalah layanan, bukan sekadar mengikuti format?
- Adakah alternatif yang ditolak beserta alasannya?
- Apakah pemilik, sumber bukti, dan pemicu peninjauan sudah dicatat?

Gunakan metadata bukti bila dokumen organisasi tidak boleh dibagikan. Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata.
