# Periksa kelengkapan inventaris CSV: python periksa-inventaris.py nama-berkas.csv
"""Memeriksa inventaris integrasi dan menjumlahkan beban yang tercatat.

Skrip ini tidak menilai mutu keputusan. Skrip hanya menunjukkan baris yang belum
punya pemilik atau belum punya bukti, karena baris itu paling sering terlewat saat
inventaris disusun dari ingatan. Berkas yang diperiksa tidak boleh memuat data
pribadi pasien atau karyawan.
"""

import csv
import sys

KODE_KOMENTAR = "#"
JAM_KERJA_PER_BULAN_KOLOM = "jam_manual_per_bulan"
BIAYA_KOLOM = "biaya_per_tahun_juta"
SAMBUNGAN_KOLOM = "jumlah_sambungan"
TANDA_BELUM_ADA = {"", "belum ada", "tidak diketahui"}
STATUS_BUKTI_TERVERIFIKASI = "terverifikasi"
TARIF_KERJA_RUPIAH_PER_JAM = 60000
BULAN_PER_TAHUN = 12
RUPIAH_PER_JUTA = 1000000


def baca_baris_inventaris(jalur_berkas):
  """Membaca CSV dan membuang komentar, sehingga templat tidak perlu disunting."""
  with open(jalur_berkas, encoding="utf-8", newline="") as berkas:
    baris_data = [baris for baris in berkas if not baris.startswith(KODE_KOMENTAR)]
  return list(csv.DictReader(baris_data))


def ubah_ke_angka(nilai):
  """Sel kosong dianggap nol agar baris tanpa angka tetap ikut dicetak."""
  return float(nilai) if nilai.strip() else 0.0


def cari_baris_tanpa_pemilik(daftar_baris):
  """Baris tanpa pemilik menjadi risiko operasional walaupun belum pernah gagal."""
  temuan = []
  for baris in daftar_baris:
    if baris["pemilik_bisnis"].strip().lower() in TANDA_BELUM_ADA:
      temuan.append(baris["id"])
  return temuan


def hitung_status_bukti(daftar_baris):
  """Menghitung status bukti agar ketidakpastian terbaca, bukan tersembunyi."""
  jumlah_per_status = {}
  for baris in daftar_baris:
    status = baris["status_bukti"].strip().lower()
    jumlah_per_status[status] = jumlah_per_status.get(status, 0) + 1
  return jumlah_per_status


def cetak_ringkasan(daftar_baris):
  """Mencetak jumlah sambungan, biaya tercatat, kerja manual, dan temuan."""
  sambungan = sum(ubah_ke_angka(baris[SAMBUNGAN_KOLOM]) for baris in daftar_baris)
  biaya = sum(ubah_ke_angka(baris[BIAYA_KOLOM]) for baris in daftar_baris)
  jam = sum(ubah_ke_angka(baris[JAM_KERJA_PER_BULAN_KOLOM]) for baris in daftar_baris)
  biaya_manual = jam * BULAN_PER_TAHUN * TARIF_KERJA_RUPIAH_PER_JAM / RUPIAH_PER_JUTA
  print(f"Baris: {len(daftar_baris)}, sambungan: {sambungan:.0f}")
  print(f"Biaya tercatat per tahun: Rp{biaya:.0f} juta")
  print(f"Kerja manual: {jam:.0f} jam per bulan, Rp{biaya_manual:.2f} juta per tahun")
  print(f"Status bukti: {hitung_status_bukti(daftar_baris)}")
  print(f"Tanpa pemilik: {cari_baris_tanpa_pemilik(daftar_baris)}")


if __name__ == "__main__":
  if len(sys.argv) != 2:
    sys.exit("Pakai: python periksa-inventaris.py nama-berkas.csv")
  cetak_ringkasan(baca_baris_inventaris(sys.argv[1]))
