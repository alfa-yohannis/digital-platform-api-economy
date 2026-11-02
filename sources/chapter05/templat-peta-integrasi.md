<!-- Kegunaan: templat peta integrasi saat ini beserta tiga titik masalah utama untuk tonggak C2. Cara pakai: salin berkas, pindahkan baris dan ID dari inventaris Bab 4, isi semua kolom, lalu gambar petanya. -->

# Templat Peta Integrasi Saat Ini

Satu baris mewakili satu garis pada peta. ID dan versi inventaris Bab 4 dipertahankan. Baris yang belum jelas ditandai, bukan ditebak.

## Identitas

| Unsur | Isi |
| --- | --- |
| Organisasi | ... |
| Versi inventaris Bab 4 | ... |
| Versi peta | ... |
| Penggambar dan penelaah | ... |
| Tanggal tinjau | ... |

## Pilihan label

- Gaya: berkas, basis data bersama, panggilan langsung, pesan. Tuliskan juga REST, GraphQL, gRPC, atau *webhook* bila diketahui.
- Sifat: sinkron atau asinkron.
- Status bukti: terverifikasi, wawancara, atau belum terverifikasi.

## Label per garis

| ID | Asal ke tujuan | Gaya | Sifat | Frekuensi dan volume | Status bukti |
| --- | --- | --- | --- | --- | --- |
| INT-... | ... | ... | ... | ... | ... |
| INT-... | ... | ... | ... | ... | ... |
| INT-... | ... | ... | ... | ... | ... |

## Penilaian layanan, oleh anggota berlatar non-teknis

Tandai integrasi yang menyebabkan antrean, kerja ulang, atau laporan terlambat. Sertakan satu angka untuk setiap tanda.

| ID | Akibat | Angka | Sumber angka |
| --- | --- | --- | --- |
| INT-... | ... | ... | ... |
| INT-... | ... | ... | ... |

## Penilaian teknis, oleh anggota berlatar teknis

Bila sistem ini berubah atau mati hari ini, siapa yang berhenti?

| ID | Keterikatan: yang ikut berubah | Titik kegagalan tunggal | Sumber |
| --- | --- | --- | --- |
| INT-... | ... | ... | ... |
| INT-... | ... | ... | ... |

## Tiga titik masalah utama

| Urutan | ID | Jenis masalah | Alasan dengan angka | Usulan gaya | Cara pemulihan | Pemilik |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ... | ... | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... | ... |

Alternatif yang tidak dipilih beserta alasannya: ...

## Tinjauan

- Apakah label dapat ditelusuri ke inventaris, dokumen, atau wawancara?
- Apakah pilihan menjawab masalah layanan yang tertulis di peta?
- Apakah pemilik, sumber bukti, dan pemicu peninjauan sudah dicatat?

Bila dokumen organisasi tidak boleh dibagikan, catat metadata buktinya saja. Rekam medis, kredensial, dan data pribadi pasien atau karyawan tidak boleh dimasukkan.
