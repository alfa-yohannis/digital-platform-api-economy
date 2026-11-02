# Kegunaan: mengulang hitungan waktu onboarding dan pilihan portal Bab 11. Cara pakai: python hitung-onboarding-portal.py
"""Menghitung waktu per tahap dan biaya empat pilihan portal dari dua berkas CSV.

Tujuannya memperlihatkan bahwa hambatan terbesar berupa waktu tunggu, dan bahwa pilihan
termurah pada penyiapan belum tentu termurah selama 3 tahun. Akibatnya, tim dapat
mengganti asumsi lalu melihat apakah urutannya berubah. Seluruh angka adalah pemisalan.
"""

import csv
from pathlib import Path

LOKASI_BERKAS = Path(__file__).resolve().parent
BERKAS_PERJALANAN = LOKASI_BERKAS / "perjalanan-onboarding-klinik.csv"
BERKAS_PILIHAN = LOKASI_BERKAS / "pilihan-portal.csv"

JAM_PER_HARI_KERJA = 8
HARI_KERJA_PER_BULAN = 25
JUMLAH_KLINIK = 40
BULAN_PER_TAHUN = 12
HORIZON_TAHUN = 3
TARIF_PER_JAM_JUTA = 0.06
MENIT_PER_TIKET = 30
MENIT_PER_JAM = 60
LANGGANAN_PER_BULAN_JUTA = 3
RUANG_PAGU_3_TAHUN_JUTA = 91.2
CADANGAN_JAM_PER_TAHUN = 120
BIAYA_ALTERNATIF_A_PER_TAHUN_JUTA = 261.6
PENYIAPAN_ALTERNATIF_A_JUTA = 24
PAGU_PER_TAHUN_JUTA = 300
KERJA_SAMPAI_PANGGILAN_PERTAMA_JAM = 2.5
PILIHAN_DIPILIH = "P2 portal bawaan"
PILIHAN_PEMBANDING = "P1 halaman statis"


def baca_csv(lokasi):
  """Membaca CSV dan melewati baris komentar, karena catatan kegunaan ada di berkas."""
  with open(lokasi, encoding="utf-8") as berkas:
    baris_data = [baris for baris in berkas if not baris.startswith("#")]
  return list(csv.DictReader(baris_data))


def hitung_jumlah_waktu(perjalanan, kolom_kerja, kolom_tunggu):
  """Menjumlahkan waktu kerja dan waktu tunggu, karena perbaikannya berbeda."""
  kerja = sum(float(baris[kolom_kerja]) for baris in perjalanan)
  tunggu = sum(float(baris[kolom_tunggu]) for baris in perjalanan)
  return kerja, tunggu


def hitung_panggilan_pertama(perjalanan, kolom_kerja, kolom_tunggu):
  """Menghitung jam sampai panggilan pertama dari tahap yang mendahuluinya."""
  awal = [baris for baris in perjalanan if baris["sebelum_panggilan_pertama"] == "ya"]
  return sum(float(baris[kolom_kerja]) + float(baris[kolom_tunggu]) for baris in awal)


def cetak_perjalanan(perjalanan):
  """Mencetak perbandingan saat ini dan sasaran, sumber angka pada naskah bab."""
  kerja_kini, tunggu_kini = hitung_jumlah_waktu(
    perjalanan, "kerja_saat_ini_jam", "tunggu_saat_ini_jam")
  kerja_sasaran, tunggu_sasaran = hitung_jumlah_waktu(
    perjalanan, "kerja_sasaran_jam", "tunggu_sasaran_jam")
  total_kini = kerja_kini + tunggu_kini
  total_sasaran = kerja_sasaran + tunggu_sasaran
  panggilan_kini = hitung_panggilan_pertama(
    perjalanan, "kerja_saat_ini_jam", "tunggu_saat_ini_jam")
  panggilan_sasaran = hitung_panggilan_pertama(
    perjalanan, "kerja_sasaran_jam", "tunggu_sasaran_jam")
  hari_hemat = (total_kini - total_sasaran) / JAM_PER_HARI_KERJA
  langganan_per_hari = LANGGANAN_PER_BULAN_JUTA / HARI_KERJA_PER_BULAN
  print("== Perjalanan satu klinik ==")
  print(f"Saat ini: kerja {kerja_kini} jam, tunggu {tunggu_kini} jam, "
        f"total {total_kini} jam, {total_kini / JAM_PER_HARI_KERJA:.2f} hari kerja")
  print(f"Porsi tunggu saat ini: {tunggu_kini / total_kini * 100:.1f} persen")
  print(f"Sasaran: kerja {kerja_sasaran} jam, tunggu {tunggu_sasaran} jam, "
        f"total {total_sasaran} jam, "
        f"{total_sasaran / JAM_PER_HARI_KERJA:.2f} hari kerja")
  print(f"Panggilan pertama: {panggilan_kini} jam menjadi {panggilan_sasaran} jam")
  print(f"Hemat {hari_hemat} hari kerja, langganan "
        f"Rp{hari_hemat * langganan_per_hari:.2f} juta per klinik, "
        f"Rp{hari_hemat * langganan_per_hari * JUMLAH_KLINIK:.1f} juta untuk 40 klinik")


def hitung_biaya_tahunan(pilihan):
  """Menghitung tiket dan pemeliharaan per tahun, karena keduanya berulang."""
  tiket_per_tahun = (
    float(pilihan["tiket_per_klinik_per_bulan"]) * JUMLAH_KLINIK * BULAN_PER_TAHUN)
  jam_tiket = tiket_per_tahun * MENIT_PER_TIKET / MENIT_PER_JAM
  jam_pemeliharaan = float(pilihan["pemeliharaan_jam_per_tahun"])
  return jam_tiket, jam_pemeliharaan


def hitung_biaya_sekali(pilihan):
  """Menghitung penyiapan dan pendampingan, yang hanya dibayar sekali."""
  jam_pendampingan = float(pilihan["pendampingan_jam_per_klinik"]) * JUMLAH_KLINIK
  biaya_pendampingan = jam_pendampingan * TARIF_PER_JAM_JUTA
  return float(pilihan["penyiapan_juta"]), biaya_pendampingan


def hitung_total_3_tahun(pilihan):
  """Menjumlahkan biaya selama horizon yang sama dengan Bab 10."""
  jam_tiket, jam_pemeliharaan = hitung_biaya_tahunan(pilihan)
  penyiapan, pendampingan = hitung_biaya_sekali(pilihan)
  biaya_berulang = (jam_tiket + jam_pemeliharaan) * TARIF_PER_JAM_JUTA
  return penyiapan + pendampingan + HORIZON_TAHUN * biaya_berulang


def cetak_pilihan(daftar_pilihan):
  """Mencetak biaya, posisi terhadap ruang pagu, dan jam terhadap cadangan."""
  print("== Pilihan portal, juta rupiah ==")
  for pilihan in daftar_pilihan:
    jam_tiket, jam_pemeliharaan = hitung_biaya_tahunan(pilihan)
    penyiapan, pendampingan = hitung_biaya_sekali(pilihan)
    total = hitung_total_3_tahun(pilihan)
    panggilan_pertama = (
      KERJA_SAMPAI_PANGGILAN_PERTAMA_JAM + float(pilihan["tunggu_verifikasi_jam"])
      + float(pilihan["tunggu_akun_uji_jam"]))
    print(f"{pilihan['pilihan']}: penyiapan {penyiapan:.1f}, "
          f"pendampingan {pendampingan:.1f}, "
          f"tiket {jam_tiket * TARIF_PER_JAM_JUTA:.1f}/tahun ({jam_tiket:.0f} jam), "
          f"isi {jam_pemeliharaan * TARIF_PER_JAM_JUTA:.1f}/tahun, total {total:.1f}, "
          f"terhadap ruang {RUANG_PAGU_3_TAHUN_JUTA - total:+.1f}, "
          f"sisa cadangan {CADANGAN_JAM_PER_TAHUN - jam_pemeliharaan:.0f} jam, "
          f"panggilan pertama {panggilan_pertama} jam")


def cetak_kepekaan(daftar_pilihan):
  """Mencari jumlah tiket yang membalik kesimpulan, asumsi yang paling menentukan."""
  menurut_nama = {pilihan["pilihan"]: pilihan for pilihan in daftar_pilihan}
  dipilih = menurut_nama[PILIHAN_DIPILIH]
  pembanding_total = hitung_total_3_tahun(menurut_nama[PILIHAN_PEMBANDING])
  penyiapan, pendampingan = hitung_biaya_sekali(dipilih)
  _, jam_pemeliharaan = hitung_biaya_tahunan(dipilih)
  biaya_tetap = (
    penyiapan + pendampingan
    + HORIZON_TAHUN * jam_pemeliharaan * TARIF_PER_JAM_JUTA)
  jam_tiket_per_satuan = (
    JUMLAH_KLINIK * BULAN_PER_TAHUN * MENIT_PER_TIKET / MENIT_PER_JAM)
  biaya_per_satuan_tiket = HORIZON_TAHUN * jam_tiket_per_satuan * TARIF_PER_JAM_JUTA
  batas_ruang = (RUANG_PAGU_3_TAHUN_JUTA - biaya_tetap) / biaya_per_satuan_tiket
  batas_pembanding = (pembanding_total - biaya_tetap) / biaya_per_satuan_tiket
  total_bila_dua_tiket = biaya_tetap + 2 * biaya_per_satuan_tiket
  print("== Kepekaan P2 terhadap jumlah tiket ==")
  print(f"Muat dalam ruang bila tiket paling banyak {batas_ruang:.2f} per klinik")
  print(f"Lebih murah dari P1 bila tiket di bawah {batas_pembanding:.2f}")
  print(f"Bila tiket 2 per klinik per bulan, totalnya {total_bila_dua_tiket:.1f}")


def cetak_arus_tahunan(daftar_pilihan):
  """Membandingkan beban per tahun dengan pagu, karena biaya sekali jatuh di tahun 1."""
  dipilih = {pilihan["pilihan"]: pilihan for pilihan in daftar_pilihan}[PILIHAN_DIPILIH]
  jam_tiket, jam_pemeliharaan = hitung_biaya_tahunan(dipilih)
  penyiapan, pendampingan = hitung_biaya_sekali(dipilih)
  berulang = (jam_tiket + jam_pemeliharaan) * TARIF_PER_JAM_JUTA
  tahun_pertama = (
    BIAYA_ALTERNATIF_A_PER_TAHUN_JUTA + PENYIAPAN_ALTERNATIF_A_JUTA
    + penyiapan + pendampingan + berulang)
  tahun_berikutnya = BIAYA_ALTERNATIF_A_PER_TAHUN_JUTA + berulang
  print("== Beban per tahun: alternatif A ditambah P2 ==")
  print(f"Tahun 1: {tahun_pertama:.1f}, "
        f"terhadap pagu {PAGU_PER_TAHUN_JUTA - tahun_pertama:+.1f}")
  print(f"Tahun 2 dan 3: {tahun_berikutnya:.1f}, "
        f"terhadap pagu {PAGU_PER_TAHUN_JUTA - tahun_berikutnya:+.1f}")


def utama():
  """Menjalankan seluruh hitungan agar hasilnya dapat dibandingkan dengan naskah."""
  perjalanan = baca_csv(BERKAS_PERJALANAN)
  daftar_pilihan = baca_csv(BERKAS_PILIHAN)
  cetak_perjalanan(perjalanan)
  cetak_pilihan(daftar_pilihan)
  cetak_kepekaan(daftar_pilihan)
  cetak_arus_tahunan(daftar_pilihan)


if __name__ == "__main__":
  utama()
