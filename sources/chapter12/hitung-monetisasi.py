# Kegunaan: biaya, impas, dan harga Bab 12. Cara pakai: python hitung-monetisasi.py
"""Mengulang seluruh hitungan biaya, titik impas, dan model harga pada Bab 12.

Angka ditaruh sebagai konstanta dan CSV supaya tim capstone cukup mengganti masukan.
Akibatnya setiap tabel Bab 12 dapat diperiksa ulang tanpa spreadsheet tersembunyi.
"""
import csv
import math
from pathlib import Path

LOKASI_BIAYA = Path(__file__).with_name("kalkulator-biaya-api.csv")
JUTA = 1_000_000
BULAN_PER_TAHUN = 12
JUMLAH_KLINIK = 40
HARGA_LANGGANAN_BULANAN = 3_000_000
HARGA_PER_JANJI = 2_000
HARGA_PER_PANGGILAN = 667
PANGGILAN_PER_JANJI = 3
JANJI_BULANAN_SEMUA_KLINIK = 60_000
JANJI_BULANAN_MENURUT_BAB = (("Bab 8", 60_000), ("Bab 5", 28_000), ("Bab 2", 20_000))

# Uji kepekaan: trafik per klinik, tim produk, dan pagu lapisan, dalam juta per tahun.
TRAFIK_PER_KLINIK_JUTA = 1.5
TIM_PRODUK_JUTA = 180
PAGU_LAPISAN_JUTA = 300
TRAFIK_DAN_TIKET_JUTA = 74.4

# Nama kelompok, jumlah klinik, dan janji temu per bulan per klinik.
KELOMPOK_KLINIK = (("kecil", 10, 500), ("sedang", 20, 1_500), ("besar", 10, 2_500))
# Batas atas janji temu per bulan dan harga bulanan tiap paket klinik.
PAKET_KLINIK = ((750, 1_500_000), (1_800, 3_000_000), (2_500, 4_500_000))
PERSEN_PENGULANGAN_API01 = 10

# Nama, jumlah asuransi, volume dasar, jatah paket, dan harga paket per bulan.
KELOMPOK_ASURANSI = (
  ("kecil", 3, 300, 350, 3_000_000),
  ("sedang", 4, 800, 900, 7_500_000),
  ("besar", 2, 1_950, 2_200, 17_000_000),
)
HARGA_PER_VERIFIKASI = 10_000
VERIFIKASI_PER_TAHUN = 96_000
PENGALI_VOLUME = (0.7, 1.0, 1.3)
PERSEN_PENGULANGAN_VERIFIKASI = 2

# Klinik aktif, pemesanan per klinik, tingkat kecocokan, tingkat selesai tepat waktu.
POHON_DASAR = (28, 1_000, 0.90, 0.80)
POHON_SASARAN = (36, 1_200, 0.95, 0.85)
POHON_UBAHAN = (
  (29, 1_000, 0.90, 0.80),
  (28, 1_100, 0.90, 0.80),
  (28, 1_000, 0.95, 0.80),
  (28, 1_000, 0.90, 0.85),
)


def baca_komponen_biaya(lokasi):
  """Membaca CSV biaya, melewati komentar agar berkas tetap dapat diberi catatan."""
  with lokasi.open(encoding="utf-8", newline="") as berkas:
    baris_data = (baris for baris in berkas if not baris.startswith("#"))
    return list(csv.DictReader(baris_data))


def jumlah_biaya(komponen, jenis):
  """Menjumlahkan satu jenis biaya, karena hanya variabel yang mengurangi margin."""
  terpilih = (baris for baris in komponen if baris["jenis"] == jenis)
  return sum(float(baris["juta_per_tahun"]) for baris in terpilih)


def klinik_impas(biaya_tetap, harga_tahunan, variabel_per_klinik):
  """Mengembalikan klinik minimum, atau None bila margin nol sehingga impas mustahil."""
  margin = harga_tahunan - variabel_per_klinik
  if margin <= 0:
    return None
  return math.ceil(biaya_tetap / margin)


def tagihan_berjenjang(janji_per_bulan):
  """Memilih paket terkecil yang memuat volume, agar beban klinik kecil berkurang."""
  for batas_atas, harga_bulanan in PAKET_KLINIK:
    if janji_per_bulan <= batas_atas:
      return harga_bulanan
  raise ValueError("Volume melampaui kuota 300 panggilan per hari")


def tagihan_asuransi(jatah, harga_paket, volume):
  """Menagih paket ditambah kelebihan, sehingga lonjakan tidak gratis bagi pemakai."""
  return harga_paket + max(0, volume - jatah) * HARGA_PER_VERIFIKASI


def cetak_biaya_dan_impas(komponen):
  """Mencetak titik impas dan kepekaannya, karena satu angka impas mudah menyesatkan."""
  tetap = jumlah_biaya(komponen, "tetap")
  variabel = jumlah_biaya(komponen, "variabel")
  per_klinik = variabel / JUMLAH_KLINIK
  harga_tahunan = HARGA_LANGGANAN_BULANAN * BULAN_PER_TAHUN / JUTA
  print(f"Biaya tetap {tetap:.1f} juta, variabel {variabel:.1f} juta")
  print(f"Variabel per klinik {per_klinik:.2f} juta, harga {harga_tahunan:.0f} juta")
  print(f"Biaya total 40 klinik {tetap + variabel:.1f} juta")
  print(f"Impas {tetap / (harga_tahunan - per_klinik):.2f} klinik")
  for jumlah in (12, 13, 28, 30, 40):
    margin = jumlah * (harga_tahunan - per_klinik) - tetap
    print(f"  {jumlah} klinik: margin {margin:.2f} juta")
  for harga_bulanan in (3.0, 2.0, 1.0, 0.24):
    hasil = klinik_impas(tetap, harga_bulanan * BULAN_PER_TAHUN, per_klinik)
    print(f"  harga {harga_bulanan} juta per bulan: impas {hasil} klinik")
  dua_trafik = klinik_impas(tetap, harga_tahunan, per_klinik + TRAFIK_PER_KLINIK_JUTA)
  print(f"  trafik dua kali: impas {dua_trafik} klinik")
  dua_tim = klinik_impas(tetap + TIM_PRODUK_JUTA, harga_tahunan, per_klinik)
  print(f"  tim produk dua kali: impas {dua_tim} klinik")
  tetap_polos = PAGU_LAPISAN_JUTA + TIM_PRODUK_JUTA
  variabel_sisa = (variabel - TRAFIK_DAN_TIKET_JUTA) / JUMLAH_KLINIK
  polos = klinik_impas(tetap_polos, harga_tahunan, variabel_sisa)
  print(f"  seluruh pagu dianggap tetap: impas {polos} klinik")


def cetak_model_harga_klinik(komponen):
  """Membandingkan tiga model pada total sama, agar terlihat siapa menanggung biaya."""
  total = jumlah_biaya(komponen, "tetap") + jumlah_biaya(komponen, "variabel")
  pendapatan = {"datar": 0, "per janji": 0, "berjenjang": 0}
  for nama, jumlah, janji in KELOMPOK_KLINIK:
    per_janji = janji * HARGA_PER_JANJI
    paket = tagihan_berjenjang(janji)
    pendapatan["datar"] += jumlah * HARGA_LANGGANAN_BULANAN
    pendapatan["per janji"] += jumlah * per_janji
    pendapatan["berjenjang"] += jumlah * paket
    print(
      f"  {nama}: {janji} janji, {janji * PANGGILAN_PER_JANJI} panggilan, "
      f"datar efektif {HARGA_LANGGANAN_BULANAN / janji:.0f}, "
      f"per janji {per_janji / JUTA:.1f} juta, "
      f"paket {paket / JUTA:.1f} juta, efektif {paket / janji:.0f}"
    )
  for nama, nilai in pendapatan.items():
    print(f"  pendapatan {nama}: {nilai * BULAN_PER_TAHUN / JUTA:.1f} juta per tahun")
  for bab, janji_bulanan in JANJI_BULANAN_MENURUT_BAB:
    hasil = janji_bulanan * HARGA_PER_JANJI * BULAN_PER_TAHUN / JUTA
    sisa = hasil - total
    print(f"  {bab}: {janji_bulanan} janji, {hasil:.1f} juta, sisa {sisa:.1f} juta")
  impas_janji = total * JUTA / HARGA_PER_JANJI / BULAN_PER_TAHUN
  print(f"  impas per janji pada 40 klinik: {impas_janji:.0f} janji per bulan")
  panggilan = JANJI_BULANAN_SEMUA_KLINIK * PANGGILAN_PER_JANJI
  tambahan = panggilan * PERSEN_PENGULANGAN_API01 // 100
  print(f"  panggilan {panggilan}, diulang {tambahan}")
  print(f"  biaya pengulangan Rp{tambahan * HARGA_PER_PANGGILAN:,} per bulan")


def cetak_latihan_asuransi():
  """Mengulang tabel contoh Latihan 2 pada volume turun, dasar, dan naik."""
  for pengali in PENGALI_VOLUME:
    pemakaian = paket = 0.0
    for nama, jumlah, volume_dasar, jatah, harga in KELOMPOK_ASURANSI:
      volume = volume_dasar * pengali
      pemakaian += jumlah * volume * HARGA_PER_VERIFIKASI
      paket += jumlah * tagihan_asuransi(jatah, harga, volume)
    print(
      f"  volume x{pengali}: per pemakaian {pemakaian * BULAN_PER_TAHUN / JUTA:.1f} "
      f"juta, berjenjang {paket * BULAN_PER_TAHUN / JUTA:.1f} juta per tahun"
    )
  for nama, jumlah, volume_dasar, jatah, harga in KELOMPOK_ASURANSI:
    print(f"  {nama}: efektif Rp{harga / volume_dasar:.0f} per verifikasi")
  ulang = VERIFIKASI_PER_TAHUN * PERSEN_PENGULANGAN_VERIFIKASI / 100
  biaya_ulang = ulang * HARGA_PER_VERIFIKASI / JUTA
  print(f"  pengulangan 2 persen bila ditagih per permintaan: {biaya_ulang:.1f} juta")


def cetak_pohon_metrik():
  """Mengalikan empat pendorong, karena ukuran utama adalah hasil, bukan penjumlahan."""
  dasar = math.prod(POHON_DASAR)
  print(f"  dasar {dasar:.0f}, sasaran {math.prod(POHON_SASARAN):.0f}")
  for nilai in POHON_UBAHAN:
    hasil = math.prod(nilai)
    print(f"  {nilai}: {hasil:.0f}, naik {hasil - dasar:.0f}")


def main():
  """Menjalankan semua hitungan berurutan sesuai urutan seksi Bab 12."""
  komponen = baca_komponen_biaya(LOKASI_BIAYA)
  print("Biaya dan titik impas API-01")
  cetak_biaya_dan_impas(komponen)
  print("Model harga klinik")
  cetak_model_harga_klinik(komponen)
  print("Latihan 2: verifikasi kepesertaan")
  cetak_latihan_asuransi()
  print("Pohon metrik")
  cetak_pohon_metrik()


if __name__ == "__main__":
  main()
