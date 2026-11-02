# Kegunaan: mengurutkan register risiko. Cara pakai: python hitung-risiko-api.py [csv]
"""Mengurutkan temuan menurut skor dampak kali kemungkinan.

Tim mengisi register sendiri. Skrip menghitung ulang skor, supaya salah ketik
tidak mengubah urutan prioritas, dan menandai temuan tinggi tanpa pemilik,
karena temuan tanpa pemilik tidak akan pernah ditindak.
"""

import csv
import pathlib
import sys

BERKAS_BAWAAN = pathlib.Path(__file__).with_name("register-risiko-api.csv")
AWALAN_KOMENTAR = "#"
# Ambang mengikuti Gambar matriks risiko Bab 6: skala dampak dan kemungkinan 1 sampai 3.
AMBANG_TINGGI = 6
AMBANG_SEDANG = 3
NILAI_TANPA_PEMILIK = "Belum ada"


def baca_register(jalur_berkas):
  """Membaca register dan melewati baris komentar agar berkas tetap bisa dibagikan."""
  with open(jalur_berkas, encoding="utf-8", newline="") as berkas:
    baris_data = [baris for baris in berkas if not baris.startswith(AWALAN_KOMENTAR)]
  return list(csv.DictReader(baris_data))


def tentukan_tingkat(skor):
  """Mengubah skor menjadi tingkat, supaya tiap tim memakai batas yang sama."""
  if skor >= AMBANG_TINGGI:
    return "Tinggi"
  if skor >= AMBANG_SEDANG:
    return "Sedang"
  return "Rendah"


def nilai_temuan(temuan):
  """Menghitung skor satu temuan dari nilai dampak dan kemungkinan."""
  skor = int(temuan["dampak"]) * int(temuan["kemungkinan"])
  return {**temuan, "skor_hitung": skor, "tingkat_hitung": tentukan_tingkat(skor)}


def cari_masalah(temuan):
  """Mencari isi yang tidak konsisten, agar diperbaiki sebelum tinjauan C2."""
  masalah = []
  if int(temuan["skor"]) != temuan["skor_hitung"]:
    masalah.append("skor tertulis berbeda dari hasil hitung")
  if temuan["tingkat"] != temuan["tingkat_hitung"]:
    masalah.append("tingkat tertulis berbeda dari hasil hitung")
  if temuan["tingkat_hitung"] == "Tinggi" and temuan["pemilik"] == NILAI_TANPA_PEMILIK:
    masalah.append("temuan tinggi belum punya pemilik")
  return masalah


def main():
  """Mencetak register terurut beserta catatan masalah."""
  jalur_berkas = sys.argv[1] if len(sys.argv) > 1 else BERKAS_BAWAAN
  daftar_temuan = [nilai_temuan(temuan) for temuan in baca_register(jalur_berkas)]
  daftar_temuan.sort(key=lambda temuan: temuan["skor_hitung"], reverse=True)
  for temuan in daftar_temuan:
    print(temuan["id"], temuan["id_integrasi"], temuan["butir_owasp"],
          "skor", temuan["skor_hitung"], temuan["tingkat_hitung"],
          "bukti:", temuan["status_bukti"])
    for masalah in cari_masalah(temuan):
      print("  periksa:", masalah)


if __name__ == "__main__":
  main()
