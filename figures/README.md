# Gambar Bersama

Folder ini memuat gambar yang dipakai bersama oleh modul dan slide. Diagram TikZ `chNN-nama.tex` berisi satu `tikzpicture` tanpa preamble. Modul memanggilnya dengan `\input{../figures/chNN-nama.tex}`, dan slide dengan `\input{../../figures/chNN-nama.tex}`. Diagram konsep PNG dan SVG dibangkitkan dari [chapter-diagrams.json](chapter-diagrams.json) oleh `tools/render-diagrams.py`. Ilustrasi JPG tidak dirujuk bab aktif dan disimpan sebagai arsip. Logo dan foto gedung adalah berkas asli, supaya modul dan slide dapat dikompilasi di Windows tanpa symlink.

| Berkas | Dipakai di | Isi |
| --- | --- | --- |
| [building.png](building.png) | Halaman judul modul | Foto gedung universitas untuk halaman judul. Berkas asli |
| [ch01-diagram-konsep.png](ch01-diagram-konsep.png) | Bab 1, Slide 01 | Diagram konsep: Dari rantai layanan ke interaksi platform |
| [ch01-diagram-konsep.svg](ch01-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch01-medikara-pihak-luar.tex](ch01-medikara-pihak-luar.tex) | Bab 1, Slide 01 | Pihak luar utama Medikara Health dan cara pertukaran datanya saat ini |
| [ch01-peta-capstone.tex](ch01-peta-capstone.tex) | Bab 1, Slide 01 | Empat Bagian mata kuliah sejajar dengan empat tonggak capstone, dan tiap Bagian menyumbang luaran ke satu tonggak |
| [ch01-pipeline-platform.tex](ch01-pipeline-platform.tex) | Bab 1, Slide 01 | *Pipeline* mengalirkan nilai satu arah di dalam satu organisasi, sedangkan platform mempertemukan pihak luar dan mengatur interaksi di antara mereka |
| [ch01-platform-dan-pertukaran.jpg](ch01-platform-dan-pertukaran.jpg) | Belum dirujuk | Ilustrasi tanpa teks: platform dan pertukaran. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch01-point-to-point.tex](ch01-point-to-point.tex) | Bab 1, Slide 01 | Lima SIMRS dan empat tujuan membutuhkan 20 sambungan *point-to-point*, tetapi hanya 9 sambungan lewat satu lapisan API bersama |
| [ch01-request-response.tex](ch01-request-response.tex) | Bab 1, Slide 01 | Medikara+ meminta jadwal dokter lewat API, lalu menerima jawaban berupa kode status dan data JSON |
| [ch02-diagram-konsep.png](ch02-diagram-konsep.png) | Bab 2, Slide 02 | Diagram konsep: Efek jaringan dan mutu interaksi |
| [ch02-diagram-konsep.svg](ch02-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch02-efek-jaringan.jpg](ch02-efek-jaringan.jpg) | Belum dirujuk | Ilustrasi tanpa teks: efek jaringan. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch02-efek-jaringan.tex](ch02-efek-jaringan.tex) | Bab 2, Slide 02 | Peta efek jaringan Medikara+. Hijau menandai efek positif dan merah menandai efek negatif |
| [ch02-interaksi-inti.tex](ch02-interaksi-inti.tex) | Bab 2, Slide 02 | Interaksi inti pemesanan janji temu di Medikara+. Filter ditekankan karena di sanalah platform menambah nilai paling besar |
| [ch02-simulasi-subsidi.tex](ch02-simulasi-subsidi.tex) | Bab 2, Slide 02 | figure |
| [ch02-sisi-pasar.tex](ch02-sisi-pasar.tex) | Bab 2, Slide 02 | Calon sisi pasar Medikara+. Garis putus-putus menandai interaksi langsung antara pasien dan dokter klinik mitra |
| [ch02-tahap-peluncuran.tex](ch02-tahap-peluncuran.tex) | Bab 2, Slide 02 | Rencana peluncuran Medikara+ dalam tiga tahap. Setiap gerbang berisi ukuran yang harus tercapai sebelum sisi baru dibuka |
| [ch03-aliran-nilai.tex](ch03-aliran-nilai.tex) | Bab 3, Slide 03 | Empat aliran nilai pada paket pemeriksaan 200 karyawan. Perusahaan hanya menerima rekap agregat, bukan hasil perorangan |
| [ch03-boundary-resources.tex](ch03-boundary-resources.tex) | Bab 3, Slide 03 | *Boundary resources* berada di antara mitra dan inti platform, dengan dua pendorong yang berlawanan |
| [ch03-diagram-konsep.png](ch03-diagram-konsep.png) | Bab 3, Slide 03 | Diagram konsep: Ekosistem dan batas kerja sama mitra |
| [ch03-diagram-konsep.svg](ch03-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch03-ekosistem-mitra.jpg](ch03-ekosistem-mitra.jpg) | Belum dirujuk | Ilustrasi tanpa teks: ekosistem mitra. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch03-peta-ekosistem.tex](ch03-peta-ekosistem.tex) | Bab 3, Slide 03 | Peta ekosistem Medikara+. Hijau: orkestrator. Oranye: pengguna. Biru: pelengkap dan pembayar. Abu-abu: pihak wajib dan pemasok |
| [ch03-peta-keputusan.tex](ch03-peta-keputusan.tex) | Bab 3, Slide 03 | Peta keputusan membangun, bergabung, atau bermitra untuk satu lapisan layanan |
| [ch03-tangga-keterbukaan.tex](ch03-tangga-keterbukaan.tex) | Bab 3, Slide 03 | Tangga keterbukaan Medikara+. Kenaikan tingkat mengikuti bukti, bukan mengikuti lamanya kerja sama |
| [ch04-api-sebagai-produk.jpg](ch04-api-sebagai-produk.jpg) | Belum dirujuk | Ilustrasi tanpa teks: api sebagai produk. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch04-audiens-sensitivitas.tex](ch04-audiens-sensitivitas.tex) | Bab 4, Slide 04 | Audiens dan kepekaan data adalah dua sumbu yang berbeda. Merah menandai kombinasi yang tidak dibuka, oranye menandai data yang menuntut kontrol tambahan |
| [ch04-batas-perusahaan.tex](ch04-batas-perusahaan.tex) | Bab 4, Slide 04 | API tidak menghapus batas perusahaan, tetapi menurunkan biaya melintasinya |
| [ch04-diagram-konsep.png](ch04-diagram-konsep.png) | Bab 4, Slide 04 | Diagram konsep: API sebagai produk yang terus dipelihara |
| [ch04-diagram-konsep.svg](ch04-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch04-peta-keputusan.tex](ch04-peta-keputusan.tex) | Bab 4, Slide 04 | Peta keputusan untuk setiap baris inventaris, dengan ID contoh dari inventaris Medikara |
| [ch04-proyek-produk.tex](ch04-proyek-produk.tex) | Bab 4, Slide 04 | Proyek berhenti pada serah terima, sedangkan produk melanjutkan pengukuran dan perbaikan |
| [ch04-utang-integrasi.tex](ch04-utang-integrasi.tex) | Bab 4, Slide 04 | Biaya integrasi Medikara yang tercatat dan yang tersembunyi per tahun. Merah sudah dihitung dengan asumsi latihan, abu-abu belum dinilai |
| [ch05-diagram-konsep.png](ch05-diagram-konsep.png) | Bab 5, Slide 05 | Diagram konsep: Komunikasi sinkron dan pemberitahuan asinkron |
| [ch05-diagram-konsep.svg](ch05-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch05-peta-integrasi.tex](ch05-peta-integrasi.tex) | Bab 5, Slide 05 | Peta integrasi Medikara saat ini dengan tiga titik masalah utama |
| [ch05-peta-keputusan.tex](ch05-peta-keputusan.tex) | Bab 5, Slide 05 | Peta keputusan gaya API dimulai dari kebutuhan jawaban, bukan dari teknologi yang sedang populer |
| [ch05-pilihan-jalur-integrasi.jpg](ch05-pilihan-jalur-integrasi.jpg) | Belum dirujuk | Ilustrasi tanpa teks: pilihan jalur integrasi. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch05-polling-webhook.tex](ch05-polling-webhook.tex) | Bab 5, Slide 05 | *Polling* menghabiskan permintaan walaupun tidak ada hasil baru, sedangkan *webhook* mengikuti jumlah kejadian dan tetap butuh rekonsiliasi |
| [ch05-rest-graphql.tex](ch05-rest-graphql.tex) | Bab 5, Slide 05 | GraphQL dapat mengurangi panggilan dan data pada satu layar, tetapi memindahkan biaya dan risiko ke server |
| [ch05-sinkron-asinkron.tex](ch05-sinkron-asinkron.tex) | Bab 5, Slide 05 | Pada pola sinkron pemanggil tertahan sampai hasil tiba, sedangkan pada pola asinkron jawaban pertama hanya berarti permintaan diterima |
| [ch06-akses-sesuai-kewenangan.jpg](ch06-akses-sesuai-kewenangan.jpg) | Belum dirujuk | Ilustrasi tanpa teks: akses sesuai kewenangan. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch06-alur-client-credentials.tex](ch06-alur-client-credentials.tex) | Bab 6, Slide 06 | Alur *client credentials*: rahasia klien hanya dikirim ke server otorisasi, sedangkan API menerima token |
| [ch06-alur-pkce.tex](ch06-alur-pkce.tex) | Bab 6, Slide 06 | Alur *authorization code* dengan PKCE: langkah berwarna adalah tambahan PKCE |
| [ch06-diagram-konsep.png](ch06-diagram-konsep.png) | Bab 6, Slide 06 | Diagram konsep: Token valid tetap memerlukan izin atas objek |
| [ch06-diagram-konsep.svg](ch06-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch06-lapis-pemeriksaan.tex](ch06-lapis-pemeriksaan.tex) | Bab 6, Slide 06 | Empat pemeriksaan pada satu permintaan: dua pemeriksaan umum di *API gateway*, dua pemeriksaan hak di layanan bisnis |
| [ch06-matriks-risiko.tex](ch06-matriks-risiko.tex) | Bab 6, Slide 06 | Matriks dampak dan kemungkinan: angka dalam sel adalah skor, RA adalah ID temuan pada register risiko |
| [ch06-peta-keputusan.tex](ch06-peta-keputusan.tex) | Bab 6, Slide 06 | Peta keputusan alur dan profil keamanan: apa pun jalurnya, layanan bisnis tetap memeriksa hak atas objek |
| [ch07-alur-satusehat.tex](ch07-alur-satusehat.tex) | Bab 7, Slide 07 | Alur kiriman ke SATUSEHAT yang disederhanakan dari panduan rawat jalan, dengan titik gagal di tiap tahap |
| [ch07-anatomi-fhir.tex](ch07-anatomi-fhir.tex) | Bab 7, Slide 07 | Hubungan *resource* pada satu kunjungan, dengan profil dan terminologi sebagai aturan tambahan |
| [ch07-diagram-konsep.png](ch07-diagram-konsep.png) | Bab 7, Slide 07 | Diagram konsep: Jalur integrasi sektoral mempunyai tujuan berbeda |
| [ch07-diagram-konsep.svg](ch07-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch07-lapis-interoperabilitas.tex](ch07-lapis-interoperabilitas.tex) | Bab 7, Slide 07 | Empat lapis interoperabilitas: status terkirim baru membuktikan lapis paling bawah |
| [ch07-peta-keputusan.tex](ch07-peta-keputusan.tex) | Bab 7, Slide 07 | Peta keputusan untuk menilai satu pertukaran data terhadap standar sektor |
| [ch07-rantai-snap.tex](ch07-rantai-snap.tex) | Bab 7, Slide 07 | Dua rel aturan sektor keuangan yang bertemu pada Medikara sebagai mitra |
| [ch07-standar-pertukaran-kesehatan.jpg](ch07-standar-pertukaran-kesehatan.jpg) | Belum dirujuk | Ilustrasi tanpa teks: standar pertukaran kesehatan. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch08-diagram-konsep.png](ch08-diagram-konsep.png) | Bab 8, Slide 08 | Diagram konsep: Menurunkan strategi menjadi portofolio API |
| [ch08-diagram-konsep.svg](ch08-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch08-kanvas-produk.tex](ch08-kanvas-produk.tex) | Bab 8, Slide 08 | Kanvas produk API-01, tersedia di `sources/chapter08/contoh-kanvas-janji-temu.md` |
| [ch08-lapisan-api.tex](ch08-lapisan-api.tex) | Bab 8, Slide 08 | Lapisan pengalaman, proses, dan sistem pada tiga kandidat API Medikara |
| [ch08-matriks-nilai-usaha.tex](ch08-matriks-nilai-usaha.tex) | Bab 8, Slide 08 | Matriks nilai dan usaha lima kandidat. Kotak hijau terpilih, kotak jingga prasyarat, kotak biru antrean |
| [ch08-penurunan-kandidat.tex](ch08-penurunan-kandidat.tex) | Bab 8, Slide 08 | Penurunan kandidat API dari tujuan strategis, tahap *value stream*, dan kapabilitas |
| [ch08-peta-keputusan.tex](ch08-peta-keputusan.tex) | Bab 8, Slide 08 | Peta keputusan portofolio: tiga gerbang, skor, lalu prasyarat dan kapasitas |
| [ch08-prioritas-portofolio-api.jpg](ch08-prioritas-portofolio-api.jpg) | Belum dirujuk | Ilustrasi tanpa teks: prioritas portofolio api. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch09-alur-contract-first.tex](ch09-alur-contract-first.tex) | Bab 9, Slide 09 | Pendekatan *contract-first* memindahkan temuan salah arti ke awal pekerjaan |
| [ch09-anatomi-openapi.tex](ch09-anatomi-openapi.tex) | Bab 9, Slide 09 | Anatomi kontrak OpenAPI dan pertanyaan yang dijawab tiap bagian |
| [ch09-diagram-konsep.png](ch09-diagram-konsep.png) | Bab 9, Slide 09 | Diagram konsep: Kontrak sebagai acuan bersama penyedia dan konsumen |
| [ch09-diagram-konsep.svg](ch09-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch09-kontrak-sebelum-membangun.jpg](ch09-kontrak-sebelum-membangun.jpg) | Belum dirujuk | Ilustrasi tanpa teks: kontrak sebelum membangun. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch09-peta-keputusan.tex](ch09-peta-keputusan.tex) | Bab 9, Slide 09 | Peta keputusan untuk menilai satu perubahan kontrak |
| [ch09-status-janji-temu.tex](ch09-status-janji-temu.tex) | Bab 9, Slide 09 | Status janji temu pada API-01. Hanya status terkonfirmasi yang berarti janji pasti |
| [ch09-tangga-bukti.tex](ch09-tangga-bukti.tex) | Bab 9, Slide 09 | Tangga bukti kontrak: yang dibuktikan dan yang belum dibuktikan tiap pemeriksaan |
| [ch10-diagram-konsep.png](ch10-diagram-konsep.png) | Bab 10, Slide 10 | Diagram konsep: Gateway dan pengelolaan siklus hidup API |
| [ch10-diagram-konsep.svg](ch10-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch10-gateway-mesh.tex](ch10-gateway-mesh.tex) | Bab 10, Slide 10 | *API gateway* mengatur lalu lintas masuk, sedangkan kendali antarlayanan berada di dalam lingkungan layanan |
| [ch10-gerbang-dan-siklus-layanan.jpg](ch10-gerbang-dan-siklus-layanan.jpg) | Belum dirujuk | Ilustrasi tanpa teks: gerbang dan siklus layanan. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch10-linimasa-deprecation.tex](ch10-linimasa-deprecation.tex) | Bab 10, Slide 10 | Linimasa masa transisi 6 bulan pada API-01 dan pemisalan sisa pemakai versi 1 |
| [ch10-peta-keputusan.tex](ch10-peta-keputusan.tex) | Bab 10, Slide 10 | Peta keputusan pemilihan platform: tiga gerbang penyaring, lalu matriks berbobot |
| [ch10-posisi-gateway.tex](ch10-posisi-gateway.tex) | Bab 10, Slide 10 | Posisi *API gateway* pada satu permintaan API-01, dengan kode jawaban bila pemeriksaan gagal |
| [ch10-siklus-hidup.tex](ch10-siklus-hidup.tex) | Bab 10, Slide 10 | Lima tahap siklus hidup API dan empat gerbang bukti |
| [ch11-diagram-konsep.png](ch11-diagram-konsep.png) | Bab 11, Slide 11 | Diagram konsep: Gerbang onboarding dari pendaftaran sampai produksi |
| [ch11-diagram-konsep.svg](ch11-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch11-gerbang-kredensial.tex](ch11-gerbang-kredensial.tex) | Bab 11, Slide 11 | Pemisahan lingkungan uji dan lingkungan produksi, dengan persetujuan pemilik sebagai gerbangnya |
| [ch11-lapisan-ukuran.tex](ch11-lapisan-ukuran.tex) | Bab 11, Slide 11 | Lima garis akhir pada perjalanan mitra, beserta hal yang sudah dan belum terbukti pada tiap garis |
| [ch11-perjalanan-mitra.tex](ch11-perjalanan-mitra.tex) | Bab 11, Slide 11 | Waktu kerja dan waktu tunggu per tahap untuk satu klinik pada API-01, keadaan saat ini dan sasaran |
| [ch11-perjalanan-pengembang-mitra.jpg](ch11-perjalanan-pengembang-mitra.jpg) | Belum dirujuk | Ilustrasi tanpa teks: perjalanan pengembang mitra. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch11-peta-keputusan.tex](ch11-peta-keputusan.tex) | Bab 11, Slide 11 | Enam keputusan pada rancangan portal dan *onboarding*, dengan jawaban pada Medikara |
| [ch11-peta-portal.tex](ch11-peta-portal.tex) | Bab 11, Slide 11 | Kerangka portal pengembang: pertanyaan pengguna, kelompok halaman, isi, dan sumber tunggalnya |
| [ch12-arus-nilai.tex](ch12-arus-nilai.tex) | Bab 12, Slide 12 | Arus nilai dan arus uang pada empat sisi Medikara+, dengan pemisalan Bab 2 dan Bab 4 |
| [ch12-diagram-konsep.png](ch12-diagram-konsep.png) | Bab 12, Slide 12 | Diagram konsep: Keberlanjutan ekonomi dan nilai yang dirasakan pengguna |
| [ch12-diagram-konsep.svg](ch12-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch12-nilai-dan-metrik-platform.jpg](ch12-nilai-dan-metrik-platform.jpg) | Belum dirujuk | Ilustrasi tanpa teks: nilai dan metrik platform. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch12-peta-keputusan.tex](ch12-peta-keputusan.tex) | Bab 12, Slide 12 | Lima pertanyaan keputusan monetisasi dan metrik, serta luarannya untuk tonggak C4 |
| [ch12-pohon-metrik.tex](ch12-pohon-metrik.tex) | Bab 12, Slide 12 | Pohon metrik API-01, dari hasil bisnis sampai metrik operasional. Seluruh angka adalah pemisalan latihan |
| [ch12-tagihan-model.tex](ch12-tagihan-model.tex) | Bab 12, Slide 12 | Tagihan klinik pada tiga model. Paket kecil memuat 750 janji, paket sedang 1.800 janji, dan paket besar 2.500 janji |
| [ch12-titik-impas.tex](ch12-titik-impas.tex) | Bab 12, Slide 12 | Titik impas lapisan API-01 menurut jumlah klinik yang membayar. Seluruh angka adalah pemisalan latihan |
| [ch13-diagram-konsep.png](ch13-diagram-konsep.png) | Bab 13, Slide 13 | Diagram konsep: Tata kelola federasi: standar bersama dan keputusan lokal |
| [ch13-diagram-konsep.svg](ch13-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch13-lapis-batasan.tex](ch13-lapis-batasan.tex) | Bab 13, Slide 13 | Lapis batasan: aturan yang berlaku dan pembanding masuk lewat daftar batasan regulasi ke forum bersama |
| [ch13-model-federasi.tex](ch13-model-federasi.tex) | Bab 13, Slide 13 | Tiga model pada lima rumah sakit. K berarti keputusan lokal, dan panah putus-putus berarti masukan ke forum |
| [ch13-peta-keputusan.tex](ch13-peta-keputusan.tex) | Bab 13, Slide 13 | Peta keputusan: jalur usulan kontrak menurut risiko. Jumlah usulan dan waktu tunggu adalah pemisalan latihan |
| [ch13-tangga-sanksi.tex](ch13-tangga-sanksi.tex) | Bab 13, Slide 13 | Tangga sanksi bagi mitra. Masa perbaikan 30 hari mengikuti pemisalan Bab 3 |
| [ch13-tata-kelola-federasi.jpg](ch13-tata-kelola-federasi.jpg) | Belum dirujuk | Ilustrasi tanpa teks: tata kelola federasi. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch13-uji-persaingan.tex](ch13-uji-persaingan.tex) | Bab 13, Slide 13 | Empat langkah menilai risiko persaingan pada keputusan platform |
| [ch14-agen-terkendali.jpg](ch14-agen-terkendali.jpg) | Belum dirujuk | Ilustrasi tanpa teks: agen terkendali. Disimpan sebagai arsip, belum dirujuk bab aktif |
| [ch14-arsitektur-mcp.tex](ch14-arsitektur-mcp.tex) | Bab 14, Slide 14 | Arsitektur MCP pada perusahaan klien dan Medikara. Pembagian kepemilikan adalah pemisalan latihan |
| [ch14-diagram-konsep.png](ch14-diagram-konsep.png) | Bab 14, Slide 14 | Diagram konsep: Demo MCP: pencarian dan pratinjau slot tanpa transaksi |
| [ch14-diagram-konsep.svg](ch14-diagram-konsep.svg) | Sumber vektor | Versi vektor diagram konsep, dibangkitkan bersama PNG |
| [ch14-mcp-a2a.tex](ch14-mcp-a2a.tex) | Bab 14, Slide 14 | MCP menghubungkan agen dengan alat, A2A menghubungkan agen dengan agen, dan otorisasi tetap berada pada API. Pemicu A2A adalah pemisalan latihan |
| [ch14-peta-jalan.tex](ch14-peta-jalan.tex) | Bab 14, Slide 14 | Peta jalan platform dan API Medikara dalam tiga gelombang. Baris terbawah mengikuti jadwal IT40513 Bab 12. Rincian bulan adalah pemisalan latihan |
| [ch14-peta-keputusan.tex](ch14-peta-keputusan.tex) | Bab 14, Slide 14 | Peta keputusan: jalur satu aksi agen menurut akibatnya, dengan operasi API-01 sebagai contoh |
| [chapter-diagrams.json](chapter-diagrams.json) | Pembuatan gambar | Data kotak dan panah diagram konsep, dibaca `tools/render-diagrams.py` |
| [illustration-prompts.json](illustration-prompts.json) | Pembuatan gambar | Catatan alat, tanggal, dan perintah pembuatan ilustrasi JPG |
| [ILLUSTRATIONS.md](ILLUSTRATIONS.md) | Pembuatan gambar | Daftar diagram konsep dan cara membuatnya ulang |
| [logo_universitas.png](logo_universitas.png) | Halaman judul modul, Semua slide | Logo universitas untuk halaman judul dan slide. Berkas asli |
