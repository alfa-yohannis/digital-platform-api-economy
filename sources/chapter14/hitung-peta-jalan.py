# Kegunaan: mengulang hitungan Bab 14. Cara pakai: python hitung-peta-jalan.py
"""Mengulang hitungan agen AI, kesiapan API, neraca, dan peta jalan Bab 14.

Seluruh angka tambahan Medikara di sini adalah pemisalan latihan. Skrip dipisahkan
dari naskah supaya tim dapat mengganti asumsi tanpa menghitung ulang dengan tangan.
Skrip hanya memakai pustaka standar Python dan tidak memanggil sistem mana pun.
"""

from math import ceil

TARIF_PER_JAM = 60_000
MENIT_PER_JAM = 60
DETIK_PER_MENIT = 60
BULAN_PER_TAHUN = 12
HARI_KERJA_PER_BULAN = 22
JUTA = 1_000_000

# Angka bersama dari bab sebelumnya. Mengubahnya berarti mengubah keputusan bab itu.
KUOTA_KLINIK_PER_HARI = 300
PANGGILAN_APLIKASI_PER_JANJI = 3
JANJI_KLINIK_PER_HARI = 60
BIAYA_PER_ANTARMUKA = 45 * JUTA
PERUSAHAAN_KLIEN = 36
KAPASITAS_PER_BULAN = 640
TARIF_KONSULTASI_SPESIALIS = 250_000
MENIT_TELEPON_KONFIRMASI = 3
KUOTA_UJI_PER_HARI = 100
KLINIK_MITRA = 40
HARGA_PER_BULAN = 3 * JUTA
MASA_UJI_BULAN = 6
KELONGGARAN_P8_BULAN = 9
MARGIN_LAPISAN_2030_JUTA = 919.2
BIAYA_TIGA_TAHUN_JUTA = (337.2, 279.6, 279.6)
PAGU_TIGA_TAHUN_JUTA = 900.0
UJI_COBA_GATEWAY_JUTA = 9.6

# Pemisalan bab ini: perilaku agen pada satu perusahaan klien berukuran sedang.
TANGGAL_DICOBA_AGEN = 3
RUMAH_SAKIT_DICOBA_AGEN = 2
PANGGILAN_LAIN_AGEN = 2
PANGGILAN_SESUDAH_PERBAIKAN = 4
JANJI_AGEN_PER_BULAN = 400
PERSEN_SALAH_PILIH = 2
PERSEN_JANJI_GANDA = 1
MENIT_TELEPON_PERBAIKAN = 15
MENIT_TINJAUAN_PER_JANJI = 1
DETIK_KONFIRMASI = 15
PERUSAHAAN_PEMAKAI_A2A = 3
HARI_PEMANTAUAN = 30

# Skala penilaian: 0 belum ada, 1 sebagian, 2 sudah dibuktikan.
ASPEK_KESIAPAN = (
  "Deskripsi", "Identitas", "Otorisasi", "Pratinjau",
  "Pengulangan", "Konsumsi", "Konteks asing", "Audit",
)
SKOR_MAKSIMUM_PER_ASPEK = 2
SKOR_OPERASI = {
  "cariJadwalDokter": (1, 1, 1, 2, 2, 1, 0, 1),
  "buatJanjiTemu": (1, 1, 1, 0, 1, 1, 0, 1),
}
# Syarat keselamatan: skor tinggi pada aspek lain tidak boleh menutupi aspek ini.
SYARAT_AKSI_BACA = ("Identitas", "Konsumsi", "Konteks asing", "Audit")
SYARAT_AKSI_TULIS = ASPEK_KESIAPAN

# Urutan pengurangan mengikuti bab asal, supaya penjumlahan dapat dilacak.
NERACA_SERENTAK = (
  ("Kewajiban KI-01 dan KI-02 (Bab 8)", 600),
  ("API-06 Identitas dan Akses (Bab 8)", 1_200),
  ("API-01 Jadwal dan Janji Temu (Bab 8)", 2_400),
  ("API-02 Hasil Pemeriksaan (Bab 8)", 2_400),
  ("Operasi gateway alternatif A (Bab 10)", 960),
  ("Pemeliharaan isi portal P2 (Bab 11)", 60),
  ("Federasi, bagian tim integrasi (Bab 13)", 227),
  ("Misalkan penyiapan A dan P2 oleh tim sendiri", 800),
  ("Uji coba gateway (Bab 10)", 160),
  ("Misalkan pendampingan 5 klinik uji, 40 jam per klinik", 200),
)

API02_DIGESER_KE_GELOMBANG_2 = 2_000
PERSEN_KERJA_ULANG_SEBELUM_MPI = 25
PERSEN_KERJA_ULANG_RENDAH = 20
MANFAAT_API02_PER_TAHUN = 208_800_000
BULAN_API02_TERTUNDA = 6

GELOMBANG = {
  "Gelombang 1, 2027": {
    "bulan": 12,
    "pekerjaan": (
      ("KI-01 dan KI-02", 600),
      ("API-06", 1_200),
      ("API-01", 2_400),
      ("API-02: penilaian dampak dan kontrak", 400),
      ("Operasi gateway A", 960),
      ("Isi portal P2", 60),
      ("Federasi tahun pertama", 227),
      ("Penyiapan A dan P2", 800),
      ("Uji coba gateway", 160),
      ("Pendampingan 5 klinik uji", 200),
    ),
  },
  "Gelombang 2, 2028": {
    "bulan": 12,
    "pekerjaan": (
      ("API-02: sisa pembangunan", 2_000),
      ("API-04", 800),
      ("Operasi gateway A", 960),
      ("Isi portal P2", 60),
      ("Federasi berjalan", 67),
      ("Sambungan API-01 ke MPI", 480),
      ("Rilis ke 18 klinik sendiri, 20 jam per klinik", 360),
      ("Adaptor SIMRS Depok", 600),
    ),
  },
  "Gelombang 3, 2029 sampai 2030": {
    "bulan": 24,
    "pekerjaan": (
      ("Operasi gateway A", 1_920),
      ("Isi portal P2", 120),
      ("Federasi berjalan", 134),
      ("Pendampingan 40 klinik, 4 jam per klinik", 160),
      ("Adaptor SIMRS 4 rumah sakit", 2_400),
      ("Lapisan agen AI", 480),
    ),
  },
}

# Pekerjaan lapisan agen pada Gelombang 3, seluruhnya pemisalan latihan.
JAM_LAPISAN_AGEN = (
  ("Tiga tool dan deskripsinya", 120),
  ("Operasi pratinjau dan kontrak 1.1.0", 80),
  ("Uji penyalahgunaan dan pengulangan", 160),
  ("Kuota dan audit per agen", 120),
)
JAM_API03 = 4_167

# Klinik mitra dibagi dua kelompok. Bulan dihitung dari Januari 2029 sebagai bulan 0.
KLINIK_KELOMPOK_1 = 5
KLINIK_KELOMPOK_2 = 35
MULAI_KELOMPOK_1 = 0
MULAI_KELOMPOK_2 = 6
BULAN_AWAL_2030 = 12
BULAN_AKHIR_2030 = 24


def format_angka(nilai):
  """Memakai titik sebagai pemisah ribuan, supaya keluaran sama dengan naskah."""
  return f"{nilai:,.0f}".replace(",", ".")


def format_juta(nilai_rupiah):
  """Menulis rupiah dalam juta dengan koma desimal, seperti pada tabel naskah."""
  teks = f"{nilai_rupiah / JUTA:,.2f}".replace(",", " ").replace(".", ",")
  return "Rp" + teks.replace(" ", ".") + " juta"


def format_desimal(nilai, jumlah_digit=1):
  """Menulis angka desimal dengan koma, supaya sama dengan penulisan di naskah."""
  return f"{nilai:.{jumlah_digit}f}".replace(".", ",")


def hitung_kuota_agen():
  """Membandingkan pemakaian kuota aplikasi, agen coba-coba, dan agen sesudah perbaikan.

  Kontrak 1.0.0 hanya mencari satu rumah sakit dan satu tanggal per panggilan, sehingga
  agen yang mencoba beberapa pilihan memakai jauh lebih banyak panggilan.
  """
  panggilan_agen = TANGGAL_DICOBA_AGEN * RUMAH_SAKIT_DICOBA_AGEN + PANGGILAN_LAIN_AGEN
  kebutuhan_aplikasi = JANJI_KLINIK_PER_HARI * PANGGILAN_APLIKASI_PER_JANJI
  kebutuhan_agen = JANJI_KLINIK_PER_HARI * panggilan_agen
  selesai = KUOTA_KLINIK_PER_HARI // panggilan_agen
  sesudah_perbaikan = JANJI_KLINIK_PER_HARI * PANGGILAN_SESUDAH_PERBAIKAN
  print("== Kuota 300 panggilan per hari per klinik ==")
  print(f"Aplikasi: {kebutuhan_aplikasi} panggilan")
  print(f"Agen: {panggilan_agen} per janji, {kebutuhan_agen} panggilan")
  print(f"Selesai {selesai} dari {JANJI_KLINIK_PER_HARI}, "
        f"tertolak {JANJI_KLINIK_PER_HARI - selesai}")
  print(f"Sesudah perbaikan: {sesudah_perbaikan} panggilan, "
        f"cadangan {KUOTA_KLINIK_PER_HARI - sesudah_perbaikan}")
  return panggilan_agen


def hitung_biaya_kesalahan():
  """Menaruh harga pada salah pilih dan janji ganda, supaya kendali dapat ditimbang."""
  salah_pilih = JANJI_AGEN_PER_BULAN * PERSEN_SALAH_PILIH // 100
  biaya_telepon = TARIF_PER_JAM * MENIT_TELEPON_PERBAIKAN // MENIT_PER_JAM
  biaya_per_salah = TARIF_KONSULTASI_SPESIALIS + biaya_telepon
  biaya_salah_bulan = salah_pilih * biaya_per_salah
  janji_ganda = JANJI_AGEN_PER_BULAN * PERSEN_JANJI_GANDA // 100
  biaya_ganda_bulan = janji_ganda * TARIF_KONSULTASI_SPESIALIS
  print("== Biaya kesalahan agen, 400 janji per bulan ==")
  print(f"Salah pilih: {salah_pilih} janji, {format_juta(biaya_salah_bulan)} "
        f"per bulan, {format_juta(biaya_salah_bulan * BULAN_PER_TAHUN)} per tahun")
  print(f"Janji ganda: {janji_ganda} janji, {format_juta(biaya_ganda_bulan)} "
        f"per bulan, {format_juta(biaya_ganda_bulan * BULAN_PER_TAHUN)} per tahun")


def hitung_tinjauan_manusia(panggilan_agen):
  """Membandingkan konfirmasi pada aksi tulis dengan konfirmasi pada setiap panggilan.

  Biaya uang keduanya kecil. Jumlah konfirmasi lebih penting, karena konfirmasi yang
  terlalu sering cenderung disetujui tanpa dibaca.
  """
  biaya_tinjauan = (JANJI_AGEN_PER_BULAN * MENIT_TINJAUAN_PER_JANJI
                    * TARIF_PER_JAM // MENIT_PER_JAM)
  konfirmasi_semua = JANJI_AGEN_PER_BULAN * panggilan_agen
  detik_semua = konfirmasi_semua * DETIK_KONFIRMASI
  jam_semua = detik_semua / DETIK_PER_MENIT / MENIT_PER_JAM
  penurunan = (konfirmasi_semua - JANJI_AGEN_PER_BULAN) / konfirmasi_semua * 100
  print("== Tinjauan manusia ==")
  print(f"Tinjau tiap janji, 1 menit: {format_juta(biaya_tinjauan)} per bulan, "
        f"{format_juta(biaya_tinjauan * BULAN_PER_TAHUN)} per tahun")
  print(f"Konfirmasi tiap panggilan: {format_angka(konfirmasi_semua)} per bulan, "
        f"{format_desimal(jam_semua, 2)} jam, "
        f"{format_juta(jam_semua * TARIF_PER_JAM)}")
  print(f"Hanya aksi tulis: {JANJI_AGEN_PER_BULAN}, "
        f"turun {format_desimal(penurunan)} persen")


def hitung_ambang_antarmuka():
  """Menghitung volume agar antarmuka baru tertutup oleh telepon yang berkurang."""
  hemat_per_janji = TARIF_PER_JAM * MENIT_TELEPON_KONFIRMASI // MENIT_PER_JAM
  janji_per_tahun = BIAYA_PER_ANTARMUKA // hemat_per_janji
  janji_per_bulan = janji_per_tahun // BULAN_PER_TAHUN
  hemat_satu_perusahaan = JANJI_AGEN_PER_BULAN * BULAN_PER_TAHUN * hemat_per_janji
  perusahaan = ceil(janji_per_bulan / JANJI_AGEN_PER_BULAN)
  print("== Ambang server MCP sebagai antarmuka baru ==")
  print(f"Hemat per janji: Rp{format_angka(hemat_per_janji)}")
  print(f"Ambang: {format_angka(janji_per_tahun)} janji per tahun, "
        f"{format_angka(janji_per_bulan)} per bulan")
  print(f"Satu perusahaan: {format_juta(hemat_satu_perusahaan)} per tahun")
  print(f"Perusahaan yang diperlukan: {perusahaan} dari {PERUSAHAAN_KLIEN}")


def hitung_kuota_perusahaan():
  """Memeriksa kuota uji sebagai kuota awal agen, dan batas kerugian token dicuri."""
  janji_per_hari = KUOTA_UJI_PER_HARI // PANGGILAN_SESUDAH_PERBAIKAN
  janji_per_bulan = janji_per_hari * HARI_KERJA_PER_BULAN
  kebutuhan = (JANJI_AGEN_PER_BULAN / HARI_KERJA_PER_BULAN
               * PANGGILAN_SESUDAH_PERBAIKAN)
  batas_kuota_klinik = KUOTA_KLINIK_PER_HARI * HARI_PEMANTAUAN
  batas_kuota_agen = KUOTA_UJI_PER_HARI * HARI_PEMANTAUAN
  print("== Kuota agen perusahaan ==")
  print(f"Kuota {KUOTA_UJI_PER_HARI}: {janji_per_hari} janji per hari, "
        f"{janji_per_bulan} per bulan")
  print(f"Kebutuhan 400 janji per bulan: {format_desimal(kebutuhan)} panggilan "
        "per hari")
  print(f"Batas 30 hari: {format_angka(batas_kuota_agen)} panggilan, "
        f"banding {format_angka(batas_kuota_klinik)}")


def hitung_a2a():
  """Menunjukkan bahwa standar baru hanya berguna bila banyak mitra memakainya."""
  sambungan_terpisah = PERUSAHAAN_KLIEN * BIAYA_PER_ANTARMUKA
  per_pemakai = BIAYA_PER_ANTARMUKA / PERUSAHAAN_PEMAKAI_A2A
  print("== A2A sebagai antarmuka tambahan ==")
  print(f"36 sambungan terpisah: {format_juta(sambungan_terpisah)} per tahun")
  print(f"Satu antarmuka A2A, 3 pemakai: {format_juta(per_pemakai)} per pemakai")


def hitung_kesiapan():
  """Menjumlahkan skor, lalu menerapkan syarat keselamatan yang tidak dapat ditutupi."""
  print("== Kesiapan dua operasi API-01 ==")
  skor_maksimum = len(ASPEK_KESIAPAN) * SKOR_MAKSIMUM_PER_ASPEK
  for operasi, nilai in SKOR_OPERASI.items():
    skor = dict(zip(ASPEK_KESIAPAN, nilai))
    syarat = SYARAT_AKSI_TULIS if operasi == "buatJanjiTemu" else SYARAT_AKSI_BACA
    kurang = [aspek for aspek in syarat if skor[aspek] < SKOR_MAKSIMUM_PER_ASPEK]
    print(f"{operasi}: {sum(nilai)} dari {skor_maksimum}, "
          f"syarat belum terpenuhi: {', '.join(kurang)}")


def hitung_neraca():
  """Mengurangkan seluruh keputusan dari kapasitas satu tahun yang sama.

  Tiap bab menguji keputusannya terhadap sisa cadangan. Penjumlahan di sini
  memperlihatkan akibat bila semuanya dijalankan pada 12 bulan yang sama.
  """
  sisa = KAPASITAS_PER_BULAN * BULAN_PER_TAHUN
  kapasitas = sisa
  print(f"== Neraca serentak, kapasitas {format_angka(kapasitas)} jam ==")
  for nama, jam in NERACA_SERENTAK:
    sisa -= jam
    print(f"{nama}: {format_angka(jam)}, sisa {format_angka(sisa)}")
  kekurangan = -sisa
  biaya_kontraktor = kekurangan * TARIF_PER_JAM
  print(f"Kekurangan {format_angka(kekurangan)} jam, "
        f"{format_desimal(kekurangan / kapasitas * 100)} persen, "
        f"{format_juta(biaya_kontraktor)}")
  print(f"Sesudah API-02 digeser {format_angka(API02_DIGESER_KE_GELOMBANG_2)} jam: "
        f"sisa {format_angka(sisa + API02_DIGESER_KE_GELOMBANG_2)}")
  hitung_pilihan_api02(biaya_kontraktor)


def hitung_pilihan_api02(biaya_kontraktor):
  """Menimbang manfaat API-02 yang tertunda terhadap kontraktor dan kerja ulang."""
  print("== Dua pilihan bagi API-02 ==")
  manfaat_tertunda = (MANFAAT_API02_PER_TAHUN * BULAN_API02_TERTUNDA
                      // BULAN_PER_TAHUN)
  print(f"Manfaat tertunda paling besar: {format_juta(manfaat_tertunda)}")
  for persen in (PERSEN_KERJA_ULANG_SEBELUM_MPI, PERSEN_KERJA_ULANG_RENDAH):
    jam_ulang = API02_DIGESER_KE_GELOMBANG_2 * persen // 100
    biaya_ulang = jam_ulang * TARIF_PER_JAM
    jumlah = biaya_kontraktor + biaya_ulang
    print(f"Kerja ulang {persen} persen: {format_angka(jam_ulang)} jam, "
          f"{format_juta(biaya_ulang)}. Kontraktor ditambah kerja ulang: "
          f"{format_juta(jumlah)}, "
          f"selisih {format_juta(jumlah - manfaat_tertunda)}")


def jumlahkan_jam(daftar_pekerjaan):
  """Menjumlahkan kolom jam, karena tiap baris pekerjaan berisi nama dan jam."""
  return sum(jam for _nama, jam in daftar_pekerjaan)


def hitung_sisa_gelombang(data_gelombang):
  """Mengembalikan kapasitas, jam yang dijanjikan, dan sisa satu gelombang."""
  kapasitas = data_gelombang["bulan"] * KAPASITAS_PER_BULAN
  dijanjikan = jumlahkan_jam(data_gelombang["pekerjaan"])
  return kapasitas, dijanjikan, kapasitas - dijanjikan


def hitung_gelombang():
  """Mencetak jam tiap gelombang, lalu menguji bila agen dimajukan ke gelombang awal."""
  print("== Tiga gelombang ==")
  for nama, data in GELOMBANG.items():
    kapasitas, dijanjikan, sisa = hitung_sisa_gelombang(data)
    print(f"{nama}: kapasitas {format_angka(kapasitas)}, "
          f"dijanjikan {format_angka(dijanjikan)}, sisa {format_angka(sisa)}, "
          f"{format_desimal(sisa / kapasitas * 100)} persen")
  jam_agen = jumlahkan_jam(JAM_LAPISAN_AGEN)
  print(f"Lapisan agen: {jam_agen} jam, {format_juta(jam_agen * TARIF_PER_JAM)}")
  gelombang_awal = next(iter(GELOMBANG.values()))
  kapasitas_awal, _dijanjikan, sisa_awal = hitung_sisa_gelombang(gelombang_awal)
  sisa_bila_dimajukan = sisa_awal - jam_agen
  persen_sisa = sisa_bila_dimajukan / kapasitas_awal * 100
  print(f"Bila agen dimajukan ke Gelombang 1: sisa {sisa_bila_dimajukan} jam, "
        f"{format_desimal(persen_sisa)} persen")
  print(f"API-03 bila pemicu terpenuhi: {format_angka(JAM_API03)} jam")


def hitung_pendapatan_per_tahun(geser_bulan):
  """Mengembalikan pendapatan 2029 dan 2030 bila rilis mitra digeser sekian bulan."""
  pendapatan_2029 = 0
  pendapatan_2030 = 0
  kelompok = (
    (KLINIK_KELOMPOK_1, MULAI_KELOMPOK_1 + geser_bulan),
    (KLINIK_KELOMPOK_2, MULAI_KELOMPOK_2 + geser_bulan),
  )
  for jumlah_klinik, bulan_mulai in kelompok:
    bulan_bayar = bulan_mulai + MASA_UJI_BULAN
    for bulan in range(bulan_bayar, BULAN_AKHIR_2030):
      if bulan < BULAN_AWAL_2030:
        pendapatan_2029 += jumlah_klinik * HARGA_PER_BULAN
      else:
        pendapatan_2030 += jumlah_klinik * HARGA_PER_BULAN
  return pendapatan_2029, pendapatan_2030


def hitung_sumbu_waktu():
  """Menambahkan sumbu waktu pada titik impas Bab 12, yang dihitung per tahun penuh."""
  biaya_juta = sum(BIAYA_TIGA_TAHUN_JUTA)
  dasar_2029, dasar_2030 = hitung_pendapatan_per_tahun(0)
  geser_2029, geser_2030 = hitung_pendapatan_per_tahun(KELONGGARAN_P8_BULAN)
  selisih_juta = biaya_juta - dasar_2029 / JUTA
  bulan_tutup = selisih_juta / MARGIN_LAPISAN_2030_JUTA * BULAN_PER_TAHUN
  total_dasar = dasar_2029 + dasar_2030
  total_geser = geser_2029 + geser_2030
  print("== Sumbu waktu pendapatan ==")
  print(f"Biaya A dan P2 tiga tahun: Rp{format_desimal(biaya_juta)} juta, dengan "
        f"uji coba Rp{format_desimal(biaya_juta + UJI_COBA_GATEWAY_JUTA)} juta, "
        f"pagu Rp{format_desimal(PAGU_TIGA_TAHUN_JUTA)} juta")
  print(f"Dasar: 2029 {format_juta(dasar_2029)}, 2030 {format_juta(dasar_2030)}")
  print(f"Selisih sampai akhir 2029: Rp{format_desimal(selisih_juta)} juta")
  print(f"Tertutup dalam {format_desimal(bulan_tutup)} bulan pada margin "
        f"Rp{format_desimal(MARGIN_LAPISAN_2030_JUTA)} juta")
  print(f"Geser 9 bulan: 2029 {format_juta(geser_2029)}, "
        f"2030 {format_juta(geser_2030)}, "
        f"turun {format_juta(total_dasar - total_geser)}")


def main():
  """Mencetak seluruh hitungan menurut urutan pembahasan bab."""
  panggilan_agen = hitung_kuota_agen()
  hitung_biaya_kesalahan()
  hitung_tinjauan_manusia(panggilan_agen)
  hitung_ambang_antarmuka()
  hitung_kuota_perusahaan()
  hitung_a2a()
  hitung_kesiapan()
  hitung_neraca()
  hitung_gelombang()
  hitung_sumbu_waktu()


if __name__ == "__main__":
  main()
