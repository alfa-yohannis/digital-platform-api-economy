# Digital Platform & API Economy

IT40613 · Magister Teknologi Informasi, peminatan Digital Enterprise Architecture, Universitas Pradita.

Mata kuliah ini membahas cara organisasi membuka layanan dan datanya kepada mitra melalui platform digital dan API (*Application Programming Interface*). Bahasannya bergerak dari sisi bisnis ke sisi teknis. Mula-mula dibahas model bisnis platform, efek jaringan, dan ekosistem mitra. Setelah itu dibahas API sebagai produk, gaya API, keamanan, standar sektor, desain kontrak, manajemen, monetisasi, tata kelola, regulasi, dan API untuk agen AI (*Artificial Intelligence*). Mahasiswanya berlatar campuran. Sebagian berasal dari bisnis, manajemen, akuntansi, hukum, atau kesehatan. Sebagian lagi berasal dari ilmu komputer (CS, *Computer Science*), rekayasa perangkat lunak (SE, *Software Engineering*), atau teknologi informasi (TI). Karena itu setiap pertemuan dibuka dengan masalah organisasi yang nyata, baru kemudian masuk ke konsep dan istilah teknis. Kemampuan memprogram tidak dipersyaratkan. Materi teknis yang lebih dalam disediakan sebagai pendalaman opsional bagi mahasiswa berlatar CS, SE, atau TI.

Mata kuliah ini satu dari empat mata kuliah yang dijalankan sebagai satu proyek capstone. Tiga lainnya adalah [IT40513 Enterprise Architecture & Digital Blueprint](https://github.com/alfa-yohannis/enterprise-architecture-digital-blueprint), [IT40713 Cloud-Native & Microservices Architecture](https://github.com/alfa-yohannis/cloud-native-microservices-architecture), dan [IT40813 IT Governance, Risk & Compliance](https://github.com/alfa-yohannis/it-governance-risk-compliance). Tiap tim menyusun "Cetak Biru Transformasi Digital" untuk satu organisasi nyata, atau untuk kasus fiktif Medikara Health bila tidak punya akses. Sumbangan mata kuliah ini adalah strategi platform, potret integrasi dan API saat ini, rancangan platform API target, serta tata kelola dan peta jalan platform. Tatap muka hanya hari Sabtu untuk membahas progres proyek. Oleh karena itu modul dan slide disusun agar dapat dipelajari mandiri.

**Berkas siap pakai.** [Modul PDF](module/digital-platform-api-economy.pdf) memuat 14 bab. Slide setiap sesi tersedia melalui kolom Slide pada Peta Pertemuan di bawah. Seluruh PDF dibuat dengan XeLaTeX dan BibTeX dari sumber di repositori ini.

## Peta Pertemuan

Urutan pertemuan mengikuti empat tonggak capstone. Pertemuan 1 sampai 3 menjawab pertanyaan strategi: perlukah organisasi menjadi platform, dan dengan siapa organisasi itu bekerja sama. Pertemuan 4 sampai 7 memotret integrasi dan API yang berjalan saat ini, lalu hasilnya ditinjau menjelang UTS (Ujian Tengah Semester). Pertemuan 8 sampai 11 merancang platform API target. Pertemuan 12 sampai 14 menutup dengan nilai, tata kelola, dan peta jalan, lalu hasilnya dipresentasikan menjelang UAS (Ujian Akhir Semester). Kolom Luaran Capstone menunjukkan artefak yang masuk ke tonggak capstone, dan kolom Slide menautkan PDF slide sesi itu.

| # | Pertemuan | Aktivitas | Luaran Capstone | Slide |
| --- | --- | --- | --- | --- |
| 1 | **Orientasi: Platform, API, dan Capstone** | Membentuk tim campuran, memilih organisasi, dan mendaftar pertukaran data dengan pihak luar | C1: profil organisasi dan daftar pertukaran data | [PDF](slides/session01/session01.pdf) |
| 2 | Model Bisnis Platform dan Efek Jaringan | Mengisi kanvas platform dan memetakan efek jaringan | C1: kanvas platform dan peta efek jaringan | [PDF](slides/session02/session02.pdf) |
| 3 | Ekosistem dan Orkestrasi Mitra | Memetakan ekosistem mitra dan membandingkan opsi strategi platform | C1: peta ekosistem dan catatan keputusan strategi platform | [PDF](slides/session03/session03.pdf) |
| 4 | API sebagai Produk dan Ekonomi API | Menyusun inventaris integrasi dan API yang berjalan | C2: inventaris integrasi dan API | [PDF](slides/session04/session04.pdf) |
| 5 | Gaya API dan Pola Integrasi | Menggambar peta integrasi beserta gaya dan titik masalahnya | C2: peta integrasi saat ini | [PDF](slides/session05/session05.pdf) |
| 6 | Keamanan API: OAuth 2.0 dan OWASP API Security Top 10 | Menilai integrasi yang berjalan dengan daftar periksa OWASP API Security Top 10 | C2: penilaian risiko keamanan API | [PDF](slides/session06/session06.pdf) |
| 7 | Standar API Sektoral: SATUSEHAT, HL7 FHIR, dan SNAP | Menilai kesenjangan integrasi terhadap standar sektor | C2: penilaian kesiapan interoperabilitas, ditinjau menjelang UTS | [PDF](slides/session07/session07.pdf) |
| 8 | Strategi dan Portofolio API | Menurunkan kandidat API dari kebutuhan bisnis, lalu memprioritaskannya | C3: portofolio API target | [PDF](slides/session08/session08.pdf) |
| 9 | Desain Kontrak API dengan OpenAPI | Menyusun dan meninjau kontrak OpenAPI untuk satu API prioritas | C3: kontrak API prioritas | [PDF](slides/session09/session09.pdf) |
| 10 | Manajemen Siklus Hidup API dan API Gateway | Merancang arsitektur manajemen API dan kebijakan versi | C3: rancangan manajemen API | [PDF](slides/session10/session10.pdf) |
| 11 | Developer Experience dan Portal Pengembang | Merancang alur *onboarding* mitra dan kerangka portal pengembang | C3: rancangan portal pengembang dan alur *onboarding* mitra | [PDF](slides/session11/session11.pdf) |
| 12 | Monetisasi API dan Metrik Platform | Memilih model nilai dan harga, lalu menyusun pohon metrik | C4: model monetisasi dan pohon metrik platform | [PDF](slides/session12/session12.pdf) |
| 13 | Tata Kelola API dan Regulasi Platform | Menyusun model tata kelola API dan memeriksa batasan regulasi | C4: model tata kelola API dan daftar batasan regulasi | [PDF](slides/session13/session13.pdf) |
| 14 | API untuk Agen AI dan Peta Jalan Platform | Menilai kesiapan API bagi agen AI, lalu menyusun peta jalan platform | C4: peta jalan platform dan API, dipresentasikan menjelang UAS | [PDF](slides/session14/session14.pdf) |

Keempat Bagian sejajar dengan tonggak capstone. **Bagian I** (1 sampai 3) membangun strategi platform lebih dahulu, karena API yang dibuka tanpa strategi hanya menambah integrasi baru yang mahal. **Bagian II** (4 sampai 7) memotret kondisi saat ini. Keamanan API dibahas sebelum standar sektor karena SNAP dan SATUSEHAT memakai token akses dan otorisasi yang konsepnya dibahas di Pertemuan 6. Dengan begitu Pertemuan 7 menjadi rangkuman sebelum tinjauan C2 menjelang UTS. **Bagian III** (8 sampai 11) merancang kondisi target, berurutan dari portofolio, kontrak, manajemen, sampai pengalaman mitra. **Bagian IV** (12 sampai 14) menghubungkan rancangan dengan nilai bisnis, aturan main, dan peta jalan. Bagian ini berakhir dengan presentasi C4 menjelang UAS.

---

## Rencana Pertemuan

### Bagian I. Strategi Platform dan Ekosistem (1 sampai 3)

#### Pertemuan 01 · Orientasi: Platform, API, dan Capstone

**Tujuan.**
1. Menjelaskan perbedaan bisnis *pipeline* dan bisnis platform dengan contoh dari sektor yang dikenal.
2. Menjelaskan cara kerja API (*Application Programming Interface*) dengan bahasa sehari-hari, termasuk *request*, *response*, dan data JSON (*JavaScript Object Notation*).
3. Mengidentifikasi pertukaran data utama antara organisasi capstone dan pihak luarnya.

**Topik.** Alur mata kuliah dan kaitannya dengan tiga mata kuliah lain. Capstone, tonggak C1 sampai C4, dan cara kerja tim campuran. Bisnis *pipeline* dan bisnis platform. Platform digital sehari-hari: transportasi daring, *marketplace*, dompet digital, dan telekonsultasi. API sebagai loket layanan antarsistem. *Request*, *response*, *endpoint*, dan JSON. Pertukaran data lewat surel, berkas, portal, dan API. Kosakata bersama untuk tim campuran. Pengenalan kasus Medikara Health.

**Aktivitas.** Tim dibentuk dengan komposisi campuran, minimal satu anggota berlatar non-teknis dan satu anggota berlatar teknis. Tim memilih organisasi capstone atau memakai Medikara Health. Anggota berlatar bisnis, hukum, atau kesehatan memimpin wawancara singkat dan penelusuran dokumen tentang pihak luar yang berhubungan dengan organisasi. Anggota berlatar teknis mencatat cara pertukaran data yang terjadi: surel, unggah berkas, portal, atau API. Luarannya adalah profil organisasi satu halaman dan daftar pertukaran data dengan pihak luar. *Pendalaman teknis (opsional):* memanggil satu API publik tanpa akun dengan Postman atau `curl`, lalu membaca kode status HTTP (*HyperText Transfer Protocol*) dan isi JSON yang kembali.

**Latihan.**
1. Pilih satu layanan digital yang sering dipakai. Tentukan apakah layanan itu berpola *pipeline* atau platform, lalu beri dua alasan.
2. Jelaskan kepada rekan non-teknis apa yang terjadi ketika aplikasi pasien menampilkan jadwal dokter, dengan memakai istilah *request*, *response*, dan API.
3. Bandingkan pengiriman data klaim asuransi lewat unggah berkas dan lewat API. Sebutkan satu kelebihan dan satu risiko masing-masing.

#### Pertemuan 02 · Model Bisnis Platform dan Efek Jaringan

**Tujuan.**
1. Mengidentifikasi sisi pasar, interaksi inti, dan nilai bagi tiap sisi pada sebuah platform.
2. Membedakan efek jaringan sisi sama dan lintas sisi, baik yang positif maupun yang negatif.
3. Menganalisis strategi mengatasi masalah ayam dan telur (*chicken-and-egg problem*) saat platform diluncurkan.

**Topik.** Pasar dua sisi dan pasar multi-sisi. Interaksi inti: partisipan, unit nilai, dan filter. Platform transaksi dan platform inovasi. Efek jaringan langsung dan tidak langsung. Efek jaringan negatif dan penurunan mutu interaksi. Masalah ayam dan telur beserta strategi peluncuran. Strategi harga lintas sisi: sisi yang disubsidi dan sisi yang membayar. *Multi-homing* dan biaya berpindah. Kapan model platform tidak cocok.

**Aktivitas.** Tim mengisi kanvas platform untuk organisasi capstone: sisi pasar, interaksi inti, nilai bagi tiap sisi, dan sumber efek jaringan. Anggota berlatar bisnis dan kesehatan memimpin identifikasi sisi pasar dan nilai. Anggota berlatar teknis memeriksa data dan sistem yang dibutuhkan agar interaksi inti terjadi. Tim lalu menggambar peta efek jaringan dan menandai satu efek negatif yang perlu dikendalikan. Luarannya adalah kanvas platform dan peta efek jaringan untuk tonggak C1. *Pendalaman teknis (opsional):* membuat simulasi sederhana dengan *spreadsheet* atau Python tentang pertumbuhan dua sisi, dengan dan tanpa subsidi pada satu sisi.

**Latihan.**
1. Untuk sebuah platform telekonsultasi, tentukan sisi pasarnya, lalu jelaskan sisi mana yang sebaiknya disubsidi pada tahap awal.
2. Beri satu contoh efek jaringan negatif pada platform layanan kesehatan, lalu usulkan satu mekanisme untuk menekannya.
3. Jelaskan mengapa jaringan rumah sakit belum tentu cocok menjadi platform, dengan memakai konsep *multi-homing* dan biaya berpindah.

#### Pertemuan 03 · Ekosistem dan Orkestrasi Mitra

**Tujuan.**
1. Memetakan pelaku ekosistem, peran, dan aliran nilai di sekitar organisasi.
2. Membandingkan opsi strategi platform, yaitu membangun, bergabung, atau bermitra, beserta *tradeoff* masing-masing.
3. Merumuskan aturan dasar keterbukaan platform bagi mitra.

**Topik.** Ekosistem sebagai struktur kerja sama antara pelaku yang saling melengkapi. Komplementaritas dan modularitas. Peran orkestrator, pelengkap (*complementor*), dan pengguna. Aliran nilai berupa uang, data, layanan, dan reputasi. *Boundary resources*: API, SDK (*Software Development Kit*), dokumentasi, dan aturan. Keterbukaan dan kendali. Tata kelola ekosistem: siapa boleh bergabung, apa aturannya, dan bagaimana nilai dibagi. *Platform envelopment*. Opsi strategi: membangun platform sendiri, bergabung ke platform lain, atau bermitra.

**Aktivitas.** Tim menggambar peta ekosistem organisasi capstone yang memuat pelaku, peran, dan aliran nilai. Anggota berlatar bisnis dan hukum memimpin analisis peran dan kepentingan tiap pelaku. Anggota berlatar teknis menandai *boundary resources* yang sudah ada dan yang belum ada. Tim lalu membandingkan tiga opsi strategi dalam matriks keputusan dan menulis catatan keputusan satu halaman beserta justifikasinya. Luarannya adalah peta ekosistem mitra dan catatan keputusan strategi platform untuk tonggak C1. *Pendalaman teknis (opsional):* menelaah portal pengembang satu platform publik, lalu mengelompokkan *boundary resources* yang disediakannya.

**Latihan.**
1. Jelaskan perbedaan mitra dan pelanggan dalam ekosistem layanan kesehatan, dengan satu contoh untuk masing-masing.
2. Misalkan sebuah perusahaan asuransi mengajak Medikara bergabung ke platform milik asuransi tersebut. Analisis untung dan ruginya bagi Medikara dibandingkan membangun platform sendiri.
3. Tentukan tiga *boundary resources* yang perlu disediakan agar klinik mitra dapat terhubung tanpa pendampingan intensif.

### Bagian II. API dan Kondisi Integrasi Saat Ini (4 sampai 7)

#### Pertemuan 04 · API sebagai Produk dan Ekonomi API

**Tujuan.**
1. Menjelaskan konsep API sebagai produk dan perbedaannya dengan API sebagai proyek integrasi.
2. Mengklasifikasikan API menurut audiensnya: privat, mitra, dan publik.
3. Menyusun inventaris integrasi dan API yang berjalan di organisasi.

**Topik.** Ekonomi API dan cara API mengubah batas perusahaan. Temuan laporan industri terbaru tentang adopsi API. API sebagai produk: pengguna, nilai, dan pemilik produk. Pendekatan API-*first*. API privat, API mitra, dan API publik. Integrasi *point-to-point* dan biaya tersembunyinya. Utang integrasi. Model bisnis berbasis API di sektor pembayaran dan kesehatan. Cara menyusun inventaris integrasi.

**Aktivitas.** Tim menyusun inventaris integrasi dan API yang berjalan di organisasi capstone. Setiap baris mencatat sistem asal, sistem tujuan, data yang dipertukarkan, pemilik, cara pertukaran, dan audiens. Anggota berlatar non-teknis mewawancarai pemilik proses untuk mengetahui kegunaan dan masalah tiap integrasi. Anggota berlatar teknis menelusuri dokumentasi, konfigurasi, atau kontrak vendor. Luarannya adalah inventaris integrasi dan API untuk tonggak C2, disertai catatan tentang integrasi yang paling mahal atau paling rawan. *Pendalaman teknis (opsional):* menelusuri katalog API pada SNAP Developer Site milik ASPI (Asosiasi Sistem Pembayaran Indonesia), lalu membandingkan cara katalog itu mendeskripsikan produk API.

**Latihan.**
1. Jelaskan dengan contoh mengapa integrasi *point-to-point* yang jumlahnya terus bertambah menaikkan biaya organisasi.
2. Tentukan apakah API pendaftaran pasien Medikara sebaiknya privat, mitra, atau publik, lalu tuliskan alasannya.
3. Sebutkan tiga ciri yang membedakan API yang dikelola sebagai produk dari API yang dibangun sebagai proyek sekali jadi.

#### Pertemuan 05 · Gaya API dan Pola Integrasi

**Tujuan.**
1. Membedakan REST (*Representational State Transfer*), GraphQL, *event*, dan *webhook* berdasarkan cara kerja dan kegunaannya.
2. Menilai kecocokan gaya API untuk suatu kebutuhan bisnis beserta *tradeoff*-nya.
3. Memetakan integrasi yang berjalan beserta gaya dan titik masalahnya.

**Topik.** Empat cara sistem bertukar data: berkas, basis data bersama, panggilan langsung, dan pesan. Komunikasi sinkron dan asinkron. REST: sumber daya, metode HTTP, dan kode status. GraphQL untuk kebutuhan data yang beragam. *Event* dan *webhook* untuk pemberitahuan perubahan. gRPC sebagai pembanding singkat. Kriteria memilih gaya API. Arsitektur berbasis *event* hanya disinggung, karena dibahas rinci di IT40713 Cloud-Native & Microservices Architecture.

**Aktivitas.** Tim menggambar peta integrasi saat ini berdasarkan inventaris Pertemuan 4. Setiap garis integrasi diberi label gaya, frekuensi, arah, dan sifat sinkron atau asinkron. Anggota berlatar non-teknis menandai integrasi yang menyebabkan antrean, kerja ulang, atau laporan terlambat. Anggota berlatar teknis menilai keterikatan (*coupling*) dan titik kegagalan tunggal. Luarannya adalah peta integrasi saat ini dengan tiga titik masalah utama untuk tonggak C2. *Pendalaman teknis (opsional):* menyusun satu kebutuhan data, misalnya ringkasan kunjungan pasien, sebagai permintaan REST dan sebagai *query* GraphQL, lalu membandingkan jumlah panggilan dan ukuran data yang dibutuhkan.

**Latihan.**
1. Klinik mitra perlu segera tahu ketika hasil laboratorium selesai. Bandingkan *polling* lewat REST dan *webhook*, lalu pilih salah satu beserta alasannya.
2. Jelaskan dalam bahasa non-teknis perbedaan komunikasi sinkron dan asinkron, dengan contoh dari layanan rumah sakit.
3. Tentukan kapan GraphQL lebih tepat daripada REST, dan kapan GraphQL justru menambah risiko.

#### Pertemuan 06 · Keamanan API: OAuth 2.0 dan OWASP API Security Top 10

**Tujuan.**
1. Membedakan autentikasi dan otorisasi pada API, serta peran *API key*, token, dan *scope*.
2. Menjelaskan alur OAuth (*Open Authorization*) 2.0 yang umum dipakai aplikasi dan mitra pada tingkat konsep.
3. Menilai risiko keamanan integrasi yang berjalan dengan OWASP (*Open Worldwide Application Security Project*) API Security Top 10 edisi 2023.

**Topik.** Pola insiden kebocoran data lewat API. Autentikasi dan otorisasi. *API key*, token, dan *scope*. Peran dalam OAuth 2.0. Alur *client credentials* dan *authorization code* dengan PKCE (*Proof Key for Code Exchange*). OpenID Connect secara singkat. Praktik keamanan OAuth terbaru dalam RFC (*Request for Comments*) 9700. Profil FAPI (*Financial-grade API*) 2.0 untuk data berisiko tinggi. Persetujuan (*consent*) pemilik data. OWASP API Security Top 10 edisi 2023. *Rate limiting* dan pencatatan akses. Kerangka keamanan informasi organisasi dibahas rinci di IT40813 IT Governance, Risk & Compliance.

**Aktivitas.** Tim menilai integrasi pada peta integrasi memakai daftar periksa OWASP API Security Top 10. Tiap temuan diberi tingkat dampak dan kemungkinan. Anggota berlatar hukum, kesehatan, atau bisnis menilai dampak temuan terhadap pasien, kepatuhan, dan reputasi. Anggota berlatar teknis memeriksa bukti teknis, misalnya cara autentikasi, pembatasan akses per objek, dan pencatatan akses. Luarannya adalah penilaian risiko keamanan API untuk tonggak C2. *Pendalaman teknis (opsional):* menelusuri alur *authorization code* dengan PKCE pada OAuth *playground* publik, lalu menjelaskan isi tiap pesan.

**Latihan.**
1. Jelaskan dengan contoh rekam medis mengapa *Broken Object Level Authorization* menempati urutan pertama.
2. Bandingkan pemakaian *API key* dan OAuth 2.0 *client credentials* untuk integrasi dengan laboratorium mitra.
3. Kebocoran data Medikara pada 2025 terjadi lewat vendor. Tentukan dua butir OWASP API Security Top 10 yang paling relevan, lalu jelaskan alasannya.

#### Pertemuan 07 · Standar API Sektoral: SATUSEHAT, HL7 FHIR, dan SNAP

**Tujuan.**
1. Menjelaskan alasan regulator menetapkan standar API sektoral dan dampaknya bagi organisasi.
2. Menjelaskan konsep dasar HL7 FHIR (*Health Level Seven Fast Healthcare Interoperability Resources*): *resource*, profil, dan terminologi.
3. Menilai kesenjangan integrasi organisasi terhadap standar sektor yang berlaku.

**Topik.** Standar sektoral sebagai infrastruktur bersama. HL7 FHIR R4: *resource*, profil, dan terminologi. Status FHIR R5 dan R6. SATUSEHAT dan kewajiban rekam medis elektronik dalam Peraturan Menteri Kesehatan (Permenkes) 24/2022. Integrasi dengan layanan BPJS (Badan Penyelenggara Jaminan Sosial) Kesehatan. *Open banking* dan *open finance*. SNAP (Standar Nasional Open API Pembayaran) dari Bank Indonesia yang sejak 2023 dikelola ASPI. Layanan digital bank bersama mitra menurut POJK (Peraturan Otoritas Jasa Keuangan) 21/2023. Pelajaran dari PSD2 (*Payment Services Directive 2*) di Uni Eropa.

**Aktivitas.** Tim menilai kesenjangan integrasi organisasi terhadap standar sektor yang relevan. Untuk Medikara, fokusnya SATUSEHAT dan BPJS Kesehatan. Untuk organisasi keuangan, fokusnya SNAP. Anggota berlatar kesehatan, hukum, atau keuangan membaca kewajiban regulasi beserta tenggatnya. Anggota berlatar teknis membandingkan data yang dikirim saat ini dengan *resource* atau spesifikasi standar. Luarannya adalah penilaian kesiapan interoperabilitas. Bersama luaran Pertemuan 4 sampai 6, luaran ini melengkapi tonggak C2 yang ditinjau menjelang UTS. *Pendalaman teknis (opsional):* membaca contoh *resource* Patient dan Encounter pada spesifikasi FHIR R4, lalu memetakan kolom data SIMRS (Sistem Informasi Manajemen Rumah Sakit) ke elemen *resource* tersebut.

**Latihan.**
1. Jelaskan mengapa SATUSEHAT memakai standar terbuka seperti HL7 FHIR, bukan format buatan sendiri.
2. Bandingkan cara Indonesia melalui SNAP dan Uni Eropa melalui PSD2 mendorong *open banking*. Sebutkan satu persamaan dan satu perbedaan.
3. Misalkan data kunjungan pasien dari dua rumah sakit Medikara belum terkirim ke SATUSEHAT. Uraikan tiga kemungkinan penyebab dari sisi proses, data, dan teknologi.

### Bagian III. Merancang Platform API Target (8 sampai 11)

#### Pertemuan 08 · Strategi dan Portofolio API

**Tujuan.**
1. Menurunkan kandidat API dari tujuan strategis dan kapabilitas bisnis organisasi.
2. Memprioritaskan portofolio API dengan kriteria nilai, usaha, dan risiko.
3. Menyusun kanvas produk API untuk API prioritas.

**Topik.** Dari strategi platform ke strategi API. Menurunkan kandidat API dari *capability map* dan *value stream* hasil IT40513 Enterprise Architecture & Digital Blueprint. Batas API mengikuti batas domain bisnis. Lapisan API: sistem, proses, dan pengalaman. Lanskap API dan delapan aspeknya: *variety*, *vocabulary*, *volume*, *velocity*, *vulnerability*, *visibility*, *versioning*, dan *volatility*. Kanvas produk API. Prioritisasi portofolio. Membangun sendiri, membeli, atau memakai API pihak lain. Pemilik produk API.

**Aktivitas.** Tim menurunkan kandidat API dari tujuan strategis dan kapabilitas organisasi, lalu memprioritaskannya dalam matriks nilai dan usaha. Anggota berlatar bisnis menilai nilai bagi pengguna dan mitra. Anggota berlatar teknis menilai usaha, ketergantungan sistem, dan risiko. Tim mengisi kanvas produk API untuk dua atau tiga API teratas. Luarannya adalah portofolio API target dan kanvas produk API untuk tonggak C3. *Pendalaman teknis (opsional):* memetakan kandidat API ke batas domain hasil analisis *Domain-Driven Design* (dibahas rinci di IT40713), lalu menandai API yang melintasi lebih dari satu domain.

**Latihan.**
1. Jelaskan mengapa daftar API yang diturunkan dari daftar sistem berbeda dengan daftar API yang diturunkan dari kapabilitas bisnis.
2. Misalkan Medikara hanya punya anggaran untuk tiga API tahun depan. Susun kriteria prioritisasi, lalu terapkan pada lima kandidat API.
3. Tentukan siapa pemilik produk yang tepat untuk API janji temu Medikara, lalu jelaskan tanggung jawabnya.

#### Pertemuan 09 · Desain Kontrak API dengan OpenAPI

**Tujuan.**
1. Menjelaskan pendekatan *contract-first* dan manfaatnya bagi kerja sama dengan vendor dan mitra.
2. Membaca dan meninjau kontrak OpenAPI dari sisi bisnis maupun teknis.
3. Menyusun kontrak OpenAPI sederhana untuk satu API prioritas.

**Topik.** Kontrak API sebagai kesepakatan antara penyedia dan pengguna. Pendekatan *contract-first*. Pemodelan sumber daya dan penamaan. Pola desain API. Model galat dengan *Problem Details* (RFC 9457). *Pagination* dan penyaringan. Kompatibilitas mundur dan perubahan yang merusak (*breaking change*). Struktur OpenAPI 3.2. AsyncAPI 3.1 untuk API berbasis *event*. Tinjauan desain bersama pengguna API. *Mock server* untuk menguji kontrak sebelum API dibangun.

**Aktivitas.** Tim menyusun kontrak OpenAPI untuk satu API prioritas dari Pertemuan 8, misalnya API jadwal dokter dan janji temu. Anggota berlatar non-teknis menulis aturan bisnis, contoh data, dan kasus galat dalam bahasa biasa. Anggota berlatar teknis menuangkannya ke berkas OpenAPI berdasarkan templat. Seluruh tim meninjau kontrak itu dengan daftar periksa desain. Luarannya adalah kontrak API prioritas untuk tonggak C3. *Pendalaman teknis (opsional):* menjalankan *mock server* dari kontrak, lalu memeriksa kontrak dengan *linter* seperti Spectral.

**Latihan.**
1. Jelaskan kepada manajer proyek mengapa kontrak API perlu disepakati sebelum vendor mulai membangun.
2. Dari sebuah potongan kontrak OpenAPI, tentukan perubahan yang merusak bagi mitra dan perubahan yang aman.
3. Rancang tiga pesan galat untuk API janji temu yang jelas bagi pengembang mitra maupun petugas layanan pelanggan.

#### Pertemuan 10 · Manajemen Siklus Hidup API dan API Gateway

**Tujuan.**
1. Menjelaskan tahap siklus hidup API dan keputusan penting di tiap tahap.
2. Menjelaskan fungsi *API gateway* dan komponen platform manajemen API.
3. Membandingkan alternatif platform manajemen API dengan kriteria yang dapat dipertanggungjawabkan.

**Topik.** Siklus hidup API dari perancangan sampai pensiun. Tingkat kematangan API. Kebijakan versi dan *deprecation*. *API gateway*: *routing*, autentikasi, *rate limiting*, kuota, transformasi, dan pencatatan. Komponen platform manajemen API: *gateway*, portal, analitik, dan kebijakan. Pilihan *open source* dan layanan *cloud*. Penerapan kebijakan keamanan dari Pertemuan 6 di *gateway*. *API gateway* dan *service mesh*, yang dibahas rinci di IT40713.

**Aktivitas.** Tim merancang arsitektur manajemen API target dan kebijakan siklus hidup API. Anggota berlatar bisnis dan hukum menyusun kebijakan versi dan tata cara pemberitahuan *deprecation* kepada mitra. Anggota berlatar teknis menggambar posisi *gateway* dan aliran permintaan. Tim membandingkan tiga alternatif platform manajemen API dalam matriks keputusan. Luarannya adalah rancangan manajemen API dan kebijakan siklus hidup untuk tonggak C3. *Pendalaman teknis (opsional):* menjalankan *gateway* *open source* di Docker, lalu menerapkan *rate limiting* dan validasi token pada satu API contoh.

**Latihan.**
1. Misalkan seorang mitra masih memakai API versi lama yang akan dipensiunkan. Susun langkah komunikasi dan tenggat yang adil bagi kedua pihak.
2. Jelaskan fungsi *API gateway* dengan analogi pos pemeriksaan, lalu sebutkan batas analogi tersebut.
3. Bandingkan layanan manajemen API dari penyedia *cloud* dengan produk *open source* yang dipasang sendiri, dari sisi biaya, kendali, dan keterampilan tim.

#### Pertemuan 11 · Developer Experience dan Portal Pengembang

**Tujuan.**
1. Menjelaskan unsur *developer experience* yang menentukan cepat atau lambatnya mitra terhubung.
2. Merancang alur *onboarding* mitra dari pendaftaran sampai produksi.
3. Menyusun kerangka portal pengembang beserta ukuran keberhasilannya.

**Topik.** Mitra sebagai pengguna API. *Developer experience* dan waktu sampai panggilan pertama (*time to first call*). Dokumentasi: referensi, panduan, dan contoh. *Sandbox* dan data uji sintetis. SDK dan koleksi contoh permintaan. Portal pengembang dan katalog API. Alur *onboarding* dan verifikasi mitra. Syarat penggunaan, SLA (*Service Level Agreement*), dan dukungan. Komunitas pengembang.

**Aktivitas.** Tim merancang alur *onboarding* mitra, misalnya klinik mitra atau asuransi, mulai dari pendaftaran, verifikasi, akses *sandbox*, pengujian, sampai akses produksi. Anggota berlatar bisnis dan hukum menyusun syarat penggunaan, tingkat layanan, dan alur persetujuan. Anggota berlatar teknis menyusun kerangka portal dan isi dokumentasi minimum. Tim menetapkan target waktu sampai panggilan pertama. Luarannya adalah rancangan portal pengembang dan alur *onboarding* mitra untuk tonggak C3. *Pendalaman teknis (opsional):* membangkitkan halaman dokumentasi dari kontrak OpenAPI Pertemuan 9 dengan alat gratis, lalu mengukur waktu sampai panggilan pertama bersama rekan yang belum pernah melihat API tersebut.

**Latihan.**
1. Jelaskan mengapa dokumentasi yang lengkap belum tentu menghasilkan *developer experience* yang baik.
2. Susun lima langkah *onboarding* untuk laboratorium mitra, lalu tandai langkah yang paling mungkin menjadi hambatan.
3. Tentukan tiga ukuran keberhasilan portal pengembang dan jelaskan cara mengumpulkan datanya.

### Bagian IV. Nilai, Tata Kelola, dan Masa Depan Platform (12 sampai 14)

#### Pertemuan 12 · Monetisasi API dan Metrik Platform

**Tujuan.**
1. Membedakan nilai API langsung dan tidak langsung beserta contoh penerapannya.
2. Memilih model harga API yang sesuai dengan strategi platform dan sisi pasar.
3. Menyusun pohon metrik yang menghubungkan aktivitas API dengan tujuan bisnis.

**Topik.** Nilai API langsung dan tidak langsung. Model harga: gratis, *freemium*, berjenjang, bayar per pemakaian, dan bagi hasil. Pihak yang membayar dalam pasar multi-sisi. Biaya menjalankan API dan titik impas. Metrik platform: likuiditas, tingkat kecocokan, aktivasi mitra, dan retensi. Metrik API: adopsi, volume panggilan, tingkat galat, dan latensi. *North star metric*. Metrik semu (*vanity metric*) dan cara menghindarinya. *Business case* dibahas rinci di IT40513, sedangkan pelaporan KPI (*Key Performance Indicator*) ke direksi dibahas rinci di IT40813.

**Aktivitas.** Tim memilih model nilai dan harga untuk API mitra organisasi capstone. Tim lalu menyusun pohon metrik dari *north star metric* sampai metrik operasional API. Anggota berlatar bisnis dan akuntansi menghitung perkiraan biaya, pendapatan, dan titik impas. Anggota berlatar teknis menentukan sumber data tiap metrik di *gateway* atau portal. Luarannya adalah model monetisasi dan pohon metrik platform untuk tonggak C4. *Pendalaman teknis (opsional):* merancang *dashboard* metrik API dari contoh data log *gateway*.

**Latihan.**
1. Jelaskan mengapa API internal yang tidak menghasilkan uang tetap bisa bernilai tinggi, dengan satu contoh dari Medikara.
2. Bandingkan model bayar per pemakaian dan langganan berjenjang untuk API pengecekan kepesertaan asuransi.
3. Tentukan satu *north star metric* untuk ekosistem mitra Medikara, lalu jelaskan mengapa jumlah panggilan API bukan pilihan yang tepat.

#### Pertemuan 13 · Tata Kelola API dan Regulasi Platform

**Tujuan.**
1. Merancang model tata kelola API yang menjaga konsistensi tanpa memperlambat tim.
2. Menjelaskan risiko persaingan usaha pada platform beserta regulasinya di Indonesia dan Uni Eropa.
3. Menilai batasan regulasi terhadap rancangan platform organisasi.

**Topik.** Tata kelola API sebagai pemungkin, bukan penghambat. Model tata kelola terpusat, terdistribusi, dan federasi. Panduan gaya API (*API style guide*). Tinjauan desain dan pemeriksaan otomatis. Katalog dan kepemilikan API. Tata kelola ekosistem: aturan masuk, kurasi, dan sanksi bagi mitra. Penyalahgunaan posisi dominan dan *self-preferencing*. UU (Undang-Undang) 5/1999 dan peran KPPU (Komisi Pengawas Persaingan Usaha). Putusan KPPU tentang Google Play Billing. DMA (*Digital Markets Act*) Uni Eropa dan kewajiban *gatekeeper*. Batas pemakaian data menurut UU 27/2022 tentang Pelindungan Data Pribadi (UU PDP), yang dibahas rinci di IT40813.

**Aktivitas.** Tim menyusun model tata kelola API yang memuat struktur keputusan, peran, standar minimum, dan titik pemeriksaan. Anggota berlatar hukum dan bisnis memeriksa batasan regulasi persaingan usaha, pelindungan data, dan sektor terhadap rancangan platform. Anggota berlatar teknis menyusun aturan pemeriksaan otomatis untuk panduan gaya API. Luarannya adalah model tata kelola API dan daftar batasan regulasi untuk tonggak C4. *Pendalaman teknis (opsional):* menulis aturan Spectral untuk dua butir panduan gaya, lalu menjalankannya pada kontrak OpenAPI Pertemuan 9.

**Latihan.**
1. Jelaskan perbedaan tata kelola API terpusat dan federasi, lalu tentukan model yang cocok bagi Medikara dengan lima rumah sakit hasil akuisisi.
2. Misalkan Medikara berencana menampilkan apotek miliknya di urutan teratas aplikasi Medikara+, di atas apotek mitra. Analisis risikonya dari sudut persaingan usaha.
3. Ambil satu kewajiban *gatekeeper* dalam DMA, lalu jelaskan apakah prinsipnya relevan bagi platform kesehatan di Indonesia.

#### Pertemuan 14 · API untuk Agen AI dan Peta Jalan Platform

**Tujuan.**
1. Menjelaskan cara agen AI memakai API dan peran MCP (*Model Context Protocol*).
2. Menilai kesiapan API organisasi untuk dipakai agen AI beserta risikonya.
3. Menyusun peta jalan platform dan API yang merangkum tonggak C1 sampai C3.

**Topik.** Agen AI sebagai jenis baru pengguna API. Arsitektur MCP: *host*, *client*, dan *server*. Fitur MCP: *tools*, *resources*, dan *prompts*. Spesifikasi MCP revisi 2026-07-28. Protokol A2A (*Agent2Agent*) sebagai pembanding. API yang siap dipakai agen: deskripsi yang jelas, alur kerja dengan Arazzo, dan batasan aksi. Risiko berupa panggilan berlebihan, *prompt injection*, dan penyalahgunaan *tool*. Persetujuan manusia untuk aksi berisiko. Peta jalan platform dan API dalam gelombang rilis. Tata kelola AI dibahas rinci di IT40813.

**Aktivitas.** Aktivitas terdiri atas dua bagian. Pertama, tim menilai kesiapan satu API prioritas untuk dipakai agen AI, misalnya agen penjadwalan janji temu, lalu menetapkan aksi yang wajib mendapat persetujuan manusia. Kedua, tim menyusun peta jalan platform dan API dalam tiga gelombang rilis. Peta jalan ini merangkum luaran C1 sampai C3 dan menjadi masukan bagi peta jalan transformasi di IT40513. Anggota berlatar bisnis memimpin penentuan urutan nilai dan kesiapan mitra. Anggota berlatar teknis memeriksa ketergantungan teknis antar-API. Luarannya adalah peta jalan platform dan API untuk tonggak C4 yang dipresentasikan menjelang UAS. *Pendalaman teknis (opsional):* membungkus satu API contoh menjadi *server* MCP sederhana dengan SDK resmi, lalu mengujinya dengan MCP Inspector.

**Latihan.**
1. Jelaskan perbedaan API yang dirancang untuk pengembang manusia dengan API yang dipakai agen AI.
2. Misalkan agen AI milik perusahaan klien ingin memesan jadwal dokter untuk karyawannya. Tentukan tiga batasan yang perlu diterapkan Medikara.
3. Jelaskan alasan urutan gelombang dalam peta jalan tim, termasuk satu inisiatif yang sengaja ditunda.

---

## Kaitan dengan Capstone

| Tonggak | Pertemuan | Luaran dari mata kuliah ini |
| --- | --- | --- |
| C1 Konteks dan Strategi | 1 sampai 3 | Profil organisasi dan daftar pertukaran data. Kanvas platform dan peta efek jaringan. Peta ekosistem mitra dan catatan keputusan strategi platform. |
| C2 Kondisi Saat Ini | 4 sampai 7 | Inventaris integrasi dan API. Peta integrasi saat ini beserta titik masalahnya. Penilaian risiko keamanan API. Penilaian kesiapan interoperabilitas sektor. Ditinjau menjelang UTS. |
| C3 Kondisi Target | 8 sampai 11 | Portofolio API target dan kanvas produk API. Kontrak OpenAPI untuk API prioritas. Rancangan manajemen API dan kebijakan siklus hidup. Rancangan portal pengembang dan alur *onboarding* mitra. |
| C4 Peta Jalan dan Tata Kelola | 12 sampai 14 | Model monetisasi dan pohon metrik platform. Model tata kelola API dan daftar batasan regulasi. Penilaian kesiapan agen AI. Peta jalan platform dan API. Dipresentasikan menjelang UAS. |

Luaran di atas melengkapi luaran tiga mata kuliah lain, bukan menggantikannya. IT40513 menyediakan *capability map*, *value stream*, arsitektur aplikasi, dan peta jalan transformasi secara keseluruhan. Mata kuliah ini memakai *capability map* sebagai bahan portofolio API, lalu mengembalikan peta jalan platform dan API sebagai bagian dari peta jalan transformasi. IT40713 merancang layanan, *container*, dan infrastruktur *cloud* yang menjalankan API. IT40813 menetapkan kerangka risiko, keamanan informasi, dan kepatuhan. Penilaian risiko API dan daftar batasan regulasi dari mata kuliah ini menjadi masukan bagi kerangka tersebut.

## Kasus Berjalan: Medikara Health

PT Medikara Nusa Sehat ("Medikara Health") adalah **organisasi fiktif** yang dipakai bersama oleh keempat mata kuliah. Medikara adalah jaringan layanan kesehatan swasta dengan 5 rumah sakit (Jakarta, Bekasi, Depok, Bogor, Bandung), 18 klinik pratama, 1 laboratorium rujukan, dan 12 apotek. Karyawannya sekitar 4.800 orang, dengan sekitar 1,2 juta kunjungan pasien per tahun.

**Kondisi saat ini.** Tiap rumah sakit menjalankan SIMRS monolitik *on-premise* dengan versi berbeda, akibat riwayat akuisisi. Keuangan memakai ERP (*Enterprise Resource Planning*) terpusat. Aplikasi pasien Medikara+ untuk janji temu dan telekonsultasi dibuat oleh vendor. Integrasi ke BPJS Kesehatan dan SATUSEHAT milik Kementerian Kesehatan, yang berbasis HL7 FHIR, dibangun *point-to-point*. Data pasien tersebar, dan banyak laporan manajemen masih disusun dengan *spreadsheet*.

**Strategi 2026 sampai 2030.** Strateginya berjudul "Satu Pasien, Satu Rekam Medis". Isinya layanan terintegrasi lintas fasilitas, ekosistem mitra yang terbuka (klinik mitra, asuransi, laboratorium, apotek daring, dan layanan kesehatan karyawan perusahaan), modernisasi ke *cloud*, serta kepatuhan pada UU PDP dan aturan rekam medis elektronik.

**Pemicu.** Pada 2025 terjadi kebocoran data pasien skala kecil lewat vendor. Audit internal menemukan kontrol akses yang lemah. Antrean layanan panjang, dan biaya integrasi tinggi.

**Pemakaian di mata kuliah ini.** Bagian I memakai strategi "Satu Pasien, Satu Rekam Medis" untuk menguji apakah Medikara layak menjadi orkestrator ekosistem kesehatan, dan siapa saja sisi pasarnya. Bagian II memakai integrasi *point-to-point* ke BPJS Kesehatan dan SATUSEHAT, aplikasi Medikara+, serta kebocoran data lewat vendor sebagai bahan inventaris, peta integrasi, dan penilaian risiko. Bagian III memakai janji temu, hasil laboratorium, dan layanan kesehatan karyawan perusahaan sebagai calon API prioritas. Bagian IV memakai rencana ekosistem mitra untuk membahas model harga, tata kelola mitra, persaingan usaha, dan agen AI dari perusahaan klien. Tim yang memakai organisasi sendiri tetap dapat memakai Medikara sebagai contoh pembanding. Data organisasi nyata dipakai dengan izin dan dianonimkan.

## Struktur Repositori

| Folder | Isi |
| --- | --- |
| `figures/` | Gambar bersama untuk modul dan slide: diagram TikZ `chNN-nama.tex`, diagram konsep PNG dan SVG `chNN-diagram-konsep`, ilustrasi JPG arsip, serta logo universitas dan foto gedung sebagai berkas asli. Daftarnya ada di `figures/README.md`. |
| `module/` | Naskah modul LaTeX. Berkas induk `digital-platform-api-economy.tex`, halaman judul `titlepage.tex`, empat belas bab `chapter01.tex` sampai `chapter14.tex`, rujukan inti dan rujukan lintas bab `references.bib`, rujukan khusus bab di `bib/chapterNN.bib`, font di `fonts/` sebagai berkas asli, dan PDF siap pakai `digital-platform-api-economy.pdf`. |
| `slides/` | Slide Beamer. Pengaturan bersama di `preamble.tex` dan tema di `theme/` sebagai berkas asli. Sumber dan PDF siap pakai tiap pertemuan ada di `slides/sessionNN/`. |
| `sources/` | Berkas pendukung tiap bab di `sources/chapterNN/`: lembar kerja, templat, data kasus, dan berkas teknis opsional yang dirujuk dari naskah modul. |
| `tools/` | Skrip pembantu: `render-diagrams.py` membangkitkan diagram konsep dari `figures/chapter-diagrams.json`, `build.py` membangun buku dan slide, dan `check-materials.py` memeriksa kelengkapan modul. |

Modul dikompilasi dengan XeLaTeX dari folder `module`:

```
cd module
xelatex digital-platform-api-economy.tex
bibtex digital-platform-api-economy
xelatex digital-platform-api-economy.tex
xelatex digital-platform-api-economy.tex
```

Slide dikompilasi dengan XeLaTeX dua kali dari folder pertemuan, misalnya `slides/session01`:

```
cd slides/session01
xelatex session01.tex
xelatex session01.tex
```

**Berkas asli.** `module/fonts`, `slides/theme`, `figures/logo_universitas.png`, dan `figures/building.png` adalah berkas asli di repo ini, sehingga modul dan slide dapat dikompilasi di Windows tanpa symlink.

## Rujukan Utama

Daftar berikut merangkum rujukan inti hasil penelusuran per 30 Oktober 2026. Entri BibTeX-nya ada di `module/references.bib`, bersama rujukan yang dipakai lebih dari satu bab. Rujukan khusus satu bab ada di `module/bib/chapterNN.bib`.

**Buku**
- Parker, G. G., Van Alstyne, M. W., dan Choudary, S. P. (2016). *Platform Revolution*. W. W. Norton. ISBN 978-0-393-24913-2. https://wwnorton.com/books/Platform-Revolution
- Cusumano, M. A., Gawer, A., dan Yoffie, D. B. (2019). *The Business of Platforms*. Harper Business. ISBN 978-0-06-289632-2. https://openlibrary.org/isbn/9780062896322
- Medjaoui, M., Wilde, E., Mitra, R., dan Amundsen, M. (2021). *Continuous API Management*, edisi ke-2. O'Reilly. https://www.oreilly.com/library/view/continuous-api-management/9781098103514/
- Zimmermann, O., Stocker, M., Lübke, D., Zdun, U., dan Pautasso, C. (2022). *Patterns for API Design*. Addison-Wesley. https://api-patterns.org/
- Lauret, A. (2025). *The Design of Web APIs*, edisi ke-2. Manning. https://www.manning.com/books/the-design-of-web-apis-second-edition

**Artikel ilmiah**
- Rochet, J.-C. dan Tirole, J. (2003). Platform competition in two-sided markets. *Journal of the European Economic Association*, 1(4), 990 sampai 1029. https://doi.org/10.1162/154247603322493212
- Parker, G. G. dan Van Alstyne, M. W. (2005). Two-sided network effects: A theory of information product design. *Management Science*, 51(10), 1494 sampai 1504. https://doi.org/10.1287/mnsc.1050.0400
- Eisenmann, T., Parker, G., dan Van Alstyne, M. (2011). Platform envelopment. *Strategic Management Journal*, 32(12), 1270 sampai 1285. https://doi.org/10.1002/smj.935
- Ghazawneh, A. dan Henfridsson, O. (2013). Balancing platform control and external contribution in third-party development: The boundary resources model. *Information Systems Journal*, 23(2), 173 sampai 192. https://doi.org/10.1111/j.1365-2575.2012.00406.x
- Hagiu, A. dan Wright, J. (2015). Multi-sided platforms. *International Journal of Industrial Organization*, 43, 162 sampai 174. https://doi.org/10.1016/j.ijindorg.2015.03.003
- Parker, G., Van Alstyne, M., dan Jiang, X. (2017). Platform ecosystems: How developers invert the firm. *MIS Quarterly*, 41(1), 255 sampai 266. https://doi.org/10.25300/MISQ/2017/41.1.13
- Jacobides, M. G., Cennamo, C., dan Gawer, A. (2018). Towards a theory of ecosystems. *Strategic Management Journal*, 39(8), 2255 sampai 2276. https://doi.org/10.1002/smj.2904
- Hein, A. dkk. (2020). Digital platform ecosystems. *Electronic Markets*, 30(1), 87 sampai 98. https://doi.org/10.1007/s12525-019-00377-4
- Benzell, S. G., Hersh, J., dan Van Alstyne, M. (2024). How APIs create growth by inverting the firm. *Management Science*, 70(10), 7120 sampai 7141. https://doi.org/10.1287/mnsc.2023.4968

**Spesifikasi dan standar**
- OpenAPI Specification 3.2.0, terbit 19 September 2025. https://spec.openapis.org/oas/v3.2.0.html
- AsyncAPI Specification 3.1.0, catatan rilis terbit 31 Januari 2026. https://www.asyncapi.com/docs/reference/specification/v3.1.0
- OWASP API Security Top 10 edisi 2023, masih edisi terbaru per Oktober 2026. https://api-security.owasp.org/editions/2023/en/0x11-t10/
- RFC 6749, The OAuth 2.0 Authorization Framework (2012). https://www.rfc-editor.org/rfc/rfc6749
- RFC 9700, Best Current Practice for OAuth 2.0 Security (Januari 2025). OAuth 2.1 masih berupa *draft* di IETF (*Internet Engineering Task Force*). https://www.rfc-editor.org/rfc/rfc9700
- FAPI 2.0 Security Profile, status *Final* (Februari 2025). https://openid.net/specs/fapi-security-profile-2_0-final.html
- HL7 FHIR R4 (4.0.1), versi yang dipakai SATUSEHAT. R5 adalah rilis terbit terbaru, sedangkan R6 masih dalam proses *ballot*. https://hl7.org/fhir/R4/
- Model Context Protocol, spesifikasi revisi 2026-07-28. https://modelcontextprotocol.io/specification/2026-07-28

**Regulasi dan kebijakan**
- Bank Indonesia. Standar Nasional Open API Pembayaran (SNAP). https://www.bi.go.id/id/layanan/Standar/SNAP/default.aspx. Pengelolaan dialihkan ke ASPI sejak 1 September 2023. Standar teknis dan keamanan serta standar data direvisi menjadi versi 1.0.2 pada September 2024. https://apidevportal.aspi-indonesia.or.id/
- Kementerian Kesehatan. Dokumentasi SATUSEHAT Platform. https://satusehat.kemkes.go.id/platform/docs/id/playbook/
- Permenkes 24/2022 tentang Rekam Medis. https://peraturan.bpk.go.id/Details/245544/permenkes-no-24-tahun-2022
- POJK 21/2023 tentang Layanan Digital oleh Bank Umum. https://ojk.go.id/id/regulasi/Pages/Layanan-Digital-oleh-Bank-Umum.aspx
- UU 27/2022 tentang Pelindungan Data Pribadi. https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022. Peraturan pelaksananya, PP (Peraturan Pemerintah) 33/2026, ditetapkan 16 Juli 2026 dan menurut pemberitaan mulai berlaku 16 Januari 2027. Bab 13 membaca teksnya dari salinan pada situs pihak ketiga, sehingga teks resminya perlu dicek di JDIH (Jaringan Dokumentasi dan Informasi Hukum) sebelum dirujuk.
- UU 5/1999 tentang Larangan Praktek Monopoli dan Persaingan Usaha Tidak Sehat. https://peraturan.bpk.go.id/Details/45280/uu-no-5-tahun-1999
- Regulation (EU) 2022/1925, Digital Markets Act. https://eur-lex.europa.eu/eli/reg/2022/1925/oj. Daftar *gatekeeper*: https://digital-markets-act.ec.europa.eu/gatekeepers_en

**Laporan industri**
- Postman (2025). *2025 State of the API Report*, laporan tahunan ketujuh dengan lebih dari 5.700 responden. Survei 2026 masih berjalan per Oktober 2026. https://www.postman.com/state-of-api/2025/

**Rujukan pendukung**
- GraphQL Specification, edisi September 2025. https://spec.graphql.org/September2025/
- Arazzo Specification 1.1.0 (Mei 2026). https://spec.openapis.org/arazzo/v1.1.0.html
- RFC 9457, Problem Details for HTTP APIs. https://www.rfc-editor.org/rfc/rfc9457
- Agent2Agent (A2A) Protocol, versi 1.0 di bawah Linux Foundation. https://a2a-protocol.org/latest/specification/
- UU 17/2023 tentang Kesehatan. https://peraturan.bpk.go.id/Details/258028/uu-no-17-tahun-2023

**Silabus pembanding**
- University of Gothenburg, TIA320 Platforms, Digital Leadership Master's Programme (berlaku sejak Autumn 2025). https://www.gu.se/en/study-gothenburg/platforms-tia320/syllabus/7605f547-4ac5-11f0-8e50-d6e0442f447c
- University of Oslo, IN4150 Digital Ecosystems (jenjang master). https://www.uio.no/studier/emner/matnat/ifi/IN4150/index-eng.html
- TU Dortmund, Managing Digital Platform Ecosystems (jenjang master, semester musim panas 2026). https://dt.wiwi.tu-dortmund.de/en/teaching/lectures/summer-term-2026/master-digital-platforms/
- Copenhagen Business School, KAN-CSAAO2401U Designing Market-Based Digital Platforms (2025/2026). https://kursuskatalog.cbs.dk/2025-2026/KAN-CSAAO2401U.aspx
- Tampere University, Introduction to API Economy. https://opiskelijanopas.tuni.fi/en/tampere-university/curriculum/course-units/tut-cu-g-49623?year=2023

## Daftar Singkatan

| Singkatan | Kepanjangan |
| --- | --- |
| A2A | Agent2Agent |
| AI | Artificial Intelligence |
| AIP | API Improvement Proposal |
| API | Application Programming Interface |
| API-m-FAMM | API Management Focus Area Maturity Model |
| ASPI | Asosiasi Sistem Pembayaran Indonesia |
| BMKG | Badan Meteorologi, Klimatologi, dan Geofisika |
| BOLA | Broken Object Level Authorization |
| BPJS | Badan Penyelenggara Jaminan Sosial |
| BPK | Badan Pemeriksa Keuangan |
| CFR | Code of Federal Regulations |
| CLI | Command Line Interface |
| COBIT | Control Objectives for Information and Related Technologies |
| CS | Computer Science |
| CSV | Comma-Separated Values |
| DDD | Domain-Driven Design |
| DMA | Digital Markets Act |
| DPoP | Demonstrating Proof of Possession |
| EBA | European Banking Authority |
| ERP | Enterprise Resource Planning |
| FAPI | Financial-grade API |
| FHIR | Fast Healthcare Interoperability Resources |
| GraphQL | Graph Query Language |
| gRPC | gRPC Remote Procedure Call, *framework* RPC dari Google |
| HL7 | Health Level Seven |
| HTTP | HyperText Transfer Protocol |
| ICD | International Classification of Diseases. ICD-9 CM memakai *Clinical Modification* |
| IETF | Internet Engineering Task Force |
| IHS | Nomor identitas di SATUSEHAT. Sumber tidak menjabarkan singkatannya |
| ISBN | International Standard Book Number |
| IT | Information Technology |
| JDIH | Jaringan Dokumentasi dan Informasi Hukum |
| JSON | JavaScript Object Notation |
| JSON-RPC | JavaScript Object Notation Remote Procedure Call |
| JWT | JSON Web Token |
| KPI | Key Performance Indicator |
| KPPU | Komisi Pengawas Persaingan Usaha |
| LLM | Large Language Model |
| LOINC | Logical Observation Identifiers Names and Codes |
| MCP | Model Context Protocol |
| MPI | Master Patient Index |
| mTLS | Mutual Transport Layer Security |
| NIK | Nomor Induk Kependudukan |
| NIST | National Institute of Standards and Technology |
| OAuth | Open Authorization |
| OWASP | Open Worldwide Application Security Project |
| PADG | Peraturan Anggota Dewan Gubernur |
| PDP | Pelindungan Data Pribadi |
| Permenkes | Peraturan Menteri Kesehatan |
| PJP | Penyedia Jasa Pembayaran |
| PKCE | Proof Key for Code Exchange |
| POJK | Peraturan Otoritas Jasa Keuangan |
| PP | Peraturan Pemerintah |
| PSD2 | Payment Services Directive 2 |
| PSD3 | Payment Services Directive 3 |
| PSR | Payment Services Regulation |
| PT | Perseroan Terbatas |
| REST | Representational State Transfer |
| RFC | Request for Comments |
| RPC | Remote Procedure Call |
| RT | Rukun Tetangga |
| SDK | Software Development Kit |
| SE | Software Engineering |
| SEP | Surat Eligibilitas Peserta |
| SIMRS | Sistem Informasi Manajemen Rumah Sakit |
| SLA | Service Level Agreement |
| SLI | Service Level Indicator |
| SLO | Service Level Objective |
| SMART | Substitutable Medical Applications and Reusable Technologies |
| SNAP | Standar Nasional Open API Pembayaran |
| SNOMED CT | Systematized Nomenclature of Medicine Clinical Terms |
| SP | Special Publication, seri terbitan NIST |
| SRE | Site Reliability Engineering |
| SSRF | Server Side Request Forgery |
| TI | Teknologi Informasi |
| TOGAF | The Open Group Architecture Framework |
| UAS | Ujian Akhir Semester |
| UCB | User Choice Billing |
| URL | Uniform Resource Locator |
| UTC | Coordinated Universal Time |
| UTS | Ujian Tengah Semester |
| UU | Undang-Undang |
| WIB | Waktu Indonesia Barat |
| YAML | YAML Ain't Markup Language |
