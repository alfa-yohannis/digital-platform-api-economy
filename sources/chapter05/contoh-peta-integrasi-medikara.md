<!-- Kegunaan: contoh terisi peta integrasi Medikara dan tiga titik masalah, pembanding Aktivitas Bab 5. Cara pakai: baca setelah tim mengisi templat, bandingkan alasan, jangan disalin sebagai bukti organisasi nyata. -->

# Contoh Peta Integrasi Medikara

Contoh ini memakai data latihan dari inventaris Bab 4 (`sources/chapter04/contoh-inventaris-medikara.csv`). Status bukti dan nama pemilik adalah pengandaian latihan. Gambar petanya ada di `figures/ch05-peta-integrasi.tex`.

## Label per garis

| ID | Asal ke tujuan | Gaya | Sifat | Frekuensi dan volume | Sambungan | Status bukti |
| --- | --- | --- | --- | --- | --- | --- |
| INT-01 | SIMRS ke BPJS Kesehatan | Panggilan langsung | Sinkron | Per kunjungan, 55.000 per bulan | 5 | Terverifikasi |
| INT-02 | SIMRS ke SATUSEHAT | Panggilan langsung | Sinkron | Per kunjungan, 100.000 per bulan | 5 | Terverifikasi |
| INT-03 | SIMRS ke Medikara+ | Basis data bersama | Asinkron | Tiap 5 menit, 28.000 janji temu per bulan | 5 | Terverifikasi |
| INT-04 | SIMRS ke ERP keuangan | Berkas | Asinkron | Harian | 5 | Wawancara |
| INT-05 | SIMRS dan ERP ke 9 asuransi | Berkas lewat portal | Asinkron | Mingguan, 7.800 klaim per bulan | 9 | Terverifikasi |
| INT-06 | 3 laboratorium mitra ke SIMRS | Berkas lewat surel | Asinkron | Per pemeriksaan, 1.100 per bulan | 3 | Wawancara |
| INT-07 | SIMRS ke 36 perusahaan klien | Berkas lewat surel | Asinkron | Bulanan, 36 rekap per bulan | 36 | Terverifikasi |
| INT-08 | Portal 2 bank mitra ke ERP | Berkas diunduh | Asinkron | Harian | 2 | Terverifikasi |
| INT-09 | 18 klinik pratama ke kantor pusat | Berkas lewat surel | Asinkron | Mingguan, 936 berkas per tahun | 18 | Terverifikasi |
| INT-10 | SIMRS ke 12 apotek | Berkas | Belum diketahui | Belum diketahui | 12 | Belum terverifikasi |

Jumlah per cara: berkas 85 sambungan, basis data bersama 5, panggilan langsung 10, pesan 0. Dari lima sambungan INT-03, tiga membaca basis data dan dua memakai API bawaan SIMRS, seperti pada Bab 1 dan inventaris Bab 4. Barisnya dihitung menurut cara yang dominan, yaitu basis data bersama.

## Tiga titik masalah utama

| Urutan | ID | Jenis masalah | Alasan dengan angka | Usulan gaya | Cara pemulihan | Pemilik |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | INT-03 | Keterikatan | 140 tabel terbaca, 2 tabel dibutuhkan. Jadwal kosong 7 sampai 14 hari per tahun karena pembaruan SIMRS | REST privat untuk jadwal dan janji temu | Kunci idempotensi, kode 409 | Manajer Layanan Rawat Jalan |
| 2 | INT-02 | Kegagalan senyap | Sekitar 4 persen kunjungan klinik belum terkirim, tanpa pemberitahuan | API HL7 FHIR, mengikuti SATUSEHAT | Antrean kirim ulang, rekonsiliasi harian | Manajer Rekam Medis |
| 3 | INT-06 | Kerja ulang | 1.100 pemeriksaan per bulan diketik ulang, 110 jam per bulan, Rp79,2 juta per tahun | REST dari laboratorium, *event* dan *webhook* ke penerima | *Retry*, rekonsiliasi per jam | Manajer Laboratorium |

Alternatif yang tidak dipilih: INT-05 dengan 468 klaim ditolak per bulan. Akar masalahnya perbedaan format, sehingga ditangani lewat kontrak pada Bab 9.

## Baris usulan tanpa ID baru

Aliran hasil laboratorium ke 40 klinik mitra belum tercatat di inventaris Bab 4, karena saat ini berjalan lewat telepon. Tim mencatatnya sebagai usulan, tanpa mengubah sepuluh ID yang ada. Hitungan pemberitahuannya ada di `hitung-pemberitahuan.py`.

## Tinjauan

- Apakah pilihan menjawab masalah layanan pada bab ini?
- Adakah alternatif yang ditolak beserta alasannya?
- Apakah pemilik, sumber bukti, dan pemicu peninjauan sudah dicatat?

Rekam medis, kredensial, dan data pribadi pasien atau karyawan tidak boleh dimasukkan.
