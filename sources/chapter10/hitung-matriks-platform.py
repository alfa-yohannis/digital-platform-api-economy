# Kegunaan: menghitung biaya, nilai, dan sensitivitas pilihan platform Bab 10. Cara pakai: python hitung-matriks-platform.py
"""Membaca dua berkas CSV, lalu mencetak hasil yang dapat dibandingkan dengan Bab 10.

Skrip memakai pustaka bawaan dan hanya membaca berkas lokal. Skrip tidak memutuskan apa
pun. Tujuannya memperlihatkan seberapa mudah urutan berbalik bila satu asumsi berubah,
sehingga tim tidak memutuskan dari selisih nilai yang kecil. Angka contoh adalah
pemisalan latihan, bukan harga produk.
"""

import csv
from pathlib import Path

FOLDER_SKRIP = Path(__file__).parent
BERKAS_BIAYA = FOLDER_SKRIP / "biaya-platform-3-tahun.csv"
BERKAS_MATRIKS = FOLDER_SKRIP / "matriks-pemilihan-platform-api.csv"
KOLOM_ALTERNATIF = {
  "A": "a_cloud_terkelola",
  "B": "b_open_source_sendiri",
  "C": "c_komersial_sendiri",
}
TAHUN_HORIZON = 3
PAGU_TAHUNAN_JUTA = 300
TARIF_RUPIAH_PER_JAM = 60_000
RUPIAH_PER_JUTA = 1_000_000
CADANGAN_JAM = 1_080
JAM_PER_STAF_PER_TAHUN = 1_920
BOBOT_TOTAL = 100
KENAIKAN_TRAFIK_JUTA_PER_TAHUN = 60
KRITERIA_LOKASI = "Lokasi data"
KRITERIA_KETERAMPILAN = "Keterampilan tim"
KRITERIA_PORTABILITAS = "Portabilitas"
GESERAN_BOBOT = 10
SKOR_LOKASI_A_SESUDAH_BUKTI = 4


def baca_csv(lokasi_berkas):
  """Membaca CSV dan melewati baris komentar, karena baris pertama berisi petunjuk."""
  with lokasi_berkas.open(encoding="utf-8", newline="") as berkas:
    baris_data = (baris for baris in berkas if not baris.startswith("#"))
    return list(csv.DictReader(baris_data))


def jam_ke_juta(jumlah_jam):
  """Mengubah jam ke juta rupiah, supaya tenaga masuk ke perbandingan biaya."""
  return jumlah_jam * TARIF_RUPIAH_PER_JAM / RUPIAH_PER_JUTA


def hitung_biaya(baris_biaya, kolom, jam_operasi=None, tambahan_per_tahun=0):
  """Menghitung biaya per tahun, total horizon, dan jam operasi satu alternatif."""
  per_tahun = tambahan_per_tahun
  jam_tahunan = 0.0
  jam_sekali = 0.0
  for baris in baris_biaya:
    nilai = float(baris[kolom])
    if baris["jenis"] == "juta_per_tahun":
      per_tahun += nilai
    elif baris["jenis"] == "jam_per_tahun":
      jam_tahunan = nilai if jam_operasi is None else jam_operasi
    elif baris["jenis"] == "jam_sekali":
      jam_sekali = nilai
  per_tahun += jam_ke_juta(jam_tahunan)
  total = per_tahun * TAHUN_HORIZON + jam_ke_juta(jam_sekali)
  return per_tahun, total, jam_tahunan


def hitung_nilai(baris_matriks, kolom, ubah_bobot=None, ubah_skor=None):
  """Menghitung nilai berbobot. Perubahan memakai kamus berkunci nama kriteria."""
  ubah_bobot = ubah_bobot or {}
  ubah_skor = ubah_skor or {}
  jumlah = 0.0
  for baris in baris_matriks:
    bobot = float(baris["bobot"]) + ubah_bobot.get(baris["kriteria"], 0)
    skor = ubah_skor.get(baris["kriteria"], float(baris[kolom]))
    jumlah += bobot * skor
  return jumlah / BOBOT_TOTAL


def angka(nilai, desimal=1):
  """Mencetak angka dengan koma desimal, sesuai penulisan pada bab."""
  return f"{nilai:.{desimal}f}".replace(".", ",")


def cetak_biaya(baris_biaya):
  """Mencetak biaya tiap alternatif beserta posisinya terhadap pagu dan cadangan."""
  pagu = PAGU_TAHUNAN_JUTA * TAHUN_HORIZON
  print(f"Biaya {TAHUN_HORIZON} tahun, pagu Rp{pagu} juta, cadangan {CADANGAN_JAM} jam")
  for nama, kolom in KOLOM_ALTERNATIF.items():
    per_tahun, total, jam = hitung_biaya(baris_biaya, kolom)
    print(
      f"  {nama}: Rp{angka(per_tahun)} juta per tahun, total Rp{angka(total)} juta, "
      f"selisih pagu Rp{angka(pagu - total)} juta, sisa jam {CADANGAN_JAM - jam:.0f}"
    )


def cetak_nilai(baris_matriks):
  """Mencetak nilai berbobot sebelum perubahan apa pun."""
  print("Nilai berbobot")
  for nama, kolom in KOLOM_ALTERNATIF.items():
    print(f"  {nama}: {angka(hitung_nilai(baris_matriks, kolom), 2)}")


def cetak_sensitivitas(baris_biaya, baris_matriks):
  """Mencetak empat perubahan asumsi yang dibahas pada bab."""
  print("Sensitivitas")
  _, total_b, _ = hitung_biaya(
    baris_biaya, KOLOM_ALTERNATIF["B"], jam_operasi=JAM_PER_STAF_PER_TAHUN
  )
  print(f"  B bila 1 staf cukup: total Rp{angka(total_b)} juta")
  _, total_a, _ = hitung_biaya(
    baris_biaya,
    KOLOM_ALTERNATIF["A"],
    tambahan_per_tahun=KENAIKAN_TRAFIK_JUTA_PER_TAHUN,
  )
  print(f"  A bila trafik dua kali lipat: total Rp{angka(total_a)} juta")
  nilai_a = hitung_nilai(
    baris_matriks,
    KOLOM_ALTERNATIF["A"],
    ubah_skor={KRITERIA_LOKASI: SKOR_LOKASI_A_SESUDAH_BUKTI},
  )
  print(f"  A bila bukti lokasi tersedia: nilai {angka(nilai_a, 2)}")
  geser = {KRITERIA_KETERAMPILAN: -GESERAN_BOBOT, KRITERIA_PORTABILITAS: GESERAN_BOBOT}
  for nama, kolom in KOLOM_ALTERNATIF.items():
    nilai = hitung_nilai(baris_matriks, kolom, ubah_bobot=geser)
    print(f"  {nama} bila bobot keterampilan 10, portabilitas 20: {angka(nilai, 2)}")


if __name__ == "__main__":
  biaya = baca_csv(BERKAS_BIAYA)
  matriks = baca_csv(BERKAS_MATRIKS)
  cetak_biaya(biaya)
  cetak_nilai(matriks)
  cetak_sensitivitas(biaya, matriks)
