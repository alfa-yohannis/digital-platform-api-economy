<!-- Kegunaan: lembar kerja peta jalan platform dan API Bab 14. Cara pakai: salin, lalu isi tabel bertanda "...". -->
# Peta Jalan Platform dan API

Peta jalan menghubungkan C1 (nilai dan ekosistem), C2 (kondisi serta risiko), C3 (kontrak dan platform target), dan C4 (pelaksanaan). Seluruh angka tambahan Medikara adalah pemisalan latihan. Periksa angkanya terhadap kapasitas, rencana enterprise IT40513, dan rencana platform IT40713. Hitungan contoh dapat diulang dengan `python hitung-peta-jalan.py`.

## 1. Neraca serentak

Jumlahkan seluruh keputusan pada periode yang sama sebelum menyusun urutan.

| Pekerjaan dan bab asal | Jam | Sisa |
| :-- | :-- | :-- |
| Kapasitas: 4 orang, 160 jam per bulan, 12 bulan (Bab 8) | | 7.680 |
| Kewajiban KI-01 dan KI-02 (Bab 8) | 600 | 7.080 |
| API-06 Identitas dan Akses (Bab 8) | 1.200 | 5.880 |
| API-01 Jadwal dan Janji Temu (Bab 8) | 2.400 | 3.480 |
| API-02 Hasil Pemeriksaan (Bab 8) | 2.400 | 1.080 |
| Operasi gateway alternatif A (Bab 10) | 960 | 120 |
| Pemeliharaan isi portal P2 (Bab 11) | 60 | 60 |
| Federasi, bagian tim integrasi (Bab 13) | 227 | -167 |
| Misalkan penyiapan A dan P2 dikerjakan tim sendiri (Bab 10 dan 11) | 800 | -967 |
| Uji coba gateway dua minggu (Bab 10) | 160 | -1.127 |
| Misalkan pendampingan 5 klinik uji, 40 jam per klinik | 200 | -1.327 |

Kekurangan 1.327 jam, atau 17,3 persen kapasitas, setara Rp79,62 juta. Angka itu nilai jam, bukan tagihan, kecuali jam dibeli dari kontraktor.

| Pekerjaan tim dan artefak asal | Jam | Sisa |
| :-- | :-- | :-- |
| Kapasitas | | ... |
| ... | ... | ... |
| ... | ... | ... |

## 2. Tiga gelombang: contoh Medikara

| Gelombang | Periode | Hasil layanan | Prasyarat | Jam | Gerbang keluar |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 2027 | Lima klinik uji mencoba jadwal nyata dan pemesanan di sandbox. KI-01 dan KI-02 tertutup | Kontrol akses P1, kontrak Bab 9, pemilik API | 7.007 dari 7.680, sisa 673 | Uji lintas objek 0 lolos. Panggilan pertama paling lama 6,5 jam. Tiket paling banyak 1,08 per klinik per bulan. Bukti lokasi data tertulis |
| 2 | 2028 | Medikara+ dan 18 klinik sendiri memakai API-01 bertahap sejak April. API-02 rilis Oktober. API-04 menggantikan rekap di surel | MPI selesai Maret 2028, penilaian dampak API-02 | 5.327 dari 7.680, sisa 2.353 | Salah gabung MPI di bawah 0,1 persen. SLO 99,4 persen selama 3 bulan. Penilaian risiko vendor selesai |
| 3 | 2029 sampai 2030 | Lima klinik mitra Januari 2029, 35 klinik Juli 2029, paket berjenjang dibayar. Agen pada 2030 | Portal P2, masa transisi 6 bulan, API-01 versi 1.1.0 | 5.214 dari 15.360, sisa 10.146 | SLA 99,0 persen ke mitra. 13 klinik membayar. Aksi tulis agen: delapan aspek bernilai 2, permintaan menuju 1.250 janji per bulan |

Uji lima klinik pada 2027 memakai jadwal nyata tanpa data pasien, dan pemesanannya di sandbox. Identitas mitra pada gelombang pertama berbeda dari penyelesaian MPI enterprise. Portal dan API mitra (P8) tidak dirilis sebelum paket P2 dan P3 selesai, sesuai IT40513 Bab 12. Waktu kalender tidak menggantikan bukti penerimaan.

## 3. Tiga gelombang: isian tim

| Gelombang tim | Nilai dan pengguna | API dan versi | Dependensi | Pemilik | Jam dan biaya | Gerbang keluar |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | ... | ... | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... | ... |

## 4. Sumbu waktu pendapatan

Contoh: 5 klinik membayar sejak Juli 2029 dan 35 klinik sejak Januari 2030. Pendapatan 2029 Rp90 juta, pendapatan 2030 Rp1,44 miliar. Bila P8 memakai kelonggaran 9 bulan, pendapatan dua tahun itu turun Rp1,08 miliar.

| Tahun | Pengguna membayar | Pendapatan | Biaya | Selisih kumulatif |
| :-- | :-- | :-- | :-- | :-- |
| ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

## 5. Inisiatif yang sengaja ditunda

| Inisiatif | Alasan penundaan | Risiko bila dipercepat | Pemicu peninjauan | Pemilik |
| :-- | :-- | :-- | :-- | :-- |
| Pemesanan agen tanpa konfirmasi | Otorisasi dan pengulangan belum teruji | Janji salah atau ganda | 6 bulan aksi tulis dengan konfirmasi berjalan tanpa insiden | Manajer Layanan Rawat Jalan |
| A2A | Rp45 juta per tahun untuk segelintir pemakai | Biaya tanpa pemakai | 12 dari 36 perusahaan memintanya | Pemilik kemitraan |
| ... | ... | ... | ... | ... |

## 6. Titik sambung

| Mata kuliah | Yang harus cocok | Sudah cocok? | Tindak lanjut |
| :-- | :-- | :-- | :-- |
| IT40513 | Jadwal API mitra sama dengan paket kerja enterprise | ... | ... |
| IT40713 | Lokasi gateway dan log terhadap landing zone | ... | ... |
| IT40813 | Penilaian risiko vendor dan kebijakan AI | ... | ... |

Pertanyaan: apa akibat jika gelombang dibalik? Dependensi mana yang paling mungkin terlambat? Nilai apa tetap diterima bila gelombang berikutnya ditunda?
