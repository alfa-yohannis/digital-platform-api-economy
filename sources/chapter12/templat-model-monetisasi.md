<!-- Kegunaan: lembar kerja model monetisasi Bab 12. Cara pakai: salin berkas, isi tiap tabel, lalu lampirkan pada tonggak C4. -->

# Templat model monetisasi

Lembar kerja Bab 12, Monetisasi API dan Metrik Platform. Contoh Medikara memakai data sintetis. Harga vendor pada lembar tim wajib mencantumkan tanggal akses.

## 1. Penerima nilai dan pembayar

| Sisi | Nilai yang diterima | Yang dibayar | Jenis nilai | Bukti | Risiko bila harga naik |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Pasien | Janji tanpa antre telepon | Rp0 untuk pemesanan | Tidak langsung | Pemesanan unik | 30 persen kembali ke telepon bila Rp10.000 per pemesanan (Bab 2) |
| Klinik mitra | Pasien lewat aplikasi, telepon berkurang | Rp3 juta per bulan sesudah masa uji | Langsung | Tagihan direkonsiliasi | Klinik berhenti, Rp36 juta per klinik per tahun |
| Asuransi swasta | Verifikasi otomatis | Rp10.000 per verifikasi | Langsung | Verifikasi sah | Kontrak belum ada |
| ... | ... | ... | ... | ... | ... |

## 2. Pilihan model harga

| Model | Unit tagihan | Pendapatan per tahun | Siapa menanggung risiko volume | Aturan kegagalan | Keputusan |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Langganan datar | Klinik per bulan | Rp1,44 miliar | Klinik | Kredit SLA | Pembanding |
| Per janji sah | Janji unik | Rp1,44 miliar pada 60.000 janji per bulan | Medikara | Jawaban 5xx tidak ditagih | Ditolak untuk tahun pertama |
| Berjenjang | Paket kecil, sedang, besar | Rp1,44 miliar pada sebaran contoh | Dibagi | Pengulangan tidak memakai jatah | Dipilih bersyarat |
| ... | ... | ... | ... | ... | ... |

## 3. Biaya dan titik impas

Pakai `kalkulator-biaya-api.csv` dan `hitung-monetisasi.py`. Tulis hasilnya di bawah ini.

| Unsur | Nilai tim | Asal angka | Status (fakta, asumsi, target) |
| :-- | :-- | :-- | :-- |
| Biaya tetap per tahun | ... | ... | ... |
| Biaya variabel per pelanggan per tahun | ... | ... | ... |
| Harga per pelanggan per tahun | ... | ... | ... |
| Titik impas | ... | Rumus: biaya tetap dibagi margin per pelanggan | ... |
| Kepekaan terbesar | ... | ... | ... |

## 4. Keputusan

- Model yang dipilih dan alternatif yang ditolak beserta alasannya:
- Akibat yang diterima:
- Subsidi, tujuannya, dan syarat berhentinya:
- Pemeriksaan hukum dan etik yang diperlukan:
- Bukti yang dapat mengubah keputusan dan tanggal tinjau:

Jangan memasukkan rekam medis, kredensial, atau data pribadi nyata. Rincian *business case* dibahas pada IT40513.
