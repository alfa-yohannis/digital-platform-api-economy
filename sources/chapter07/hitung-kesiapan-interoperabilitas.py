# Kegunaan: skor kesiapan dan cakupan pemetaan Bab 7. Cara pakai: jalankan via python.
"""Menghitung skor kesiapan interoperabilitas dan cakupan pemetaan kolom SIMRS.

Angka bawaan berasal dari data latihan Medikara pada Bab 7. Skrip ini hanya
membaca dua berkas CSV lokal dan tidak memanggil SATUSEHAT atau BPJS Kesehatan,
sehingga aman dipakai tanpa kredensial. Organisasi nyata mengganti isi CSV dengan
data yang sudah dianonimkan dan berizin. Skor ini alat percakapan, bukan penilaian
kepatuhan resmi.
"""

from collections import Counter
import csv
from pathlib import Path

# Skala dinamai supaya aturan penilaian terlihat dan dapat didebat tim.
SKOR_TINGKAT = {"Terpenuhi": 2, "Sebagian": 1, "Belum": 0}
SKOR_MAKSIMUM_PER_BARIS = 2
TINGKAT_DIKECUALIKAN = "Tidak berlaku"
BUKTI_KUAT = "Terverifikasi"
BUKTI_LEMAH = {"Hipotesis", "Belum terverifikasi"}
STATUS_SIAP = "Siap"
FOLDER_SKRIP = Path(__file__).resolve().parent
BERKAS_KESENJANGAN = FOLDER_SKRIP / "contoh-kesenjangan-medikara.csv"
BERKAS_PEMETAAN = FOLDER_SKRIP / "pemetaan-simrs-fhir.csv"


def baca_baris(jalur_berkas):
  """Membaca CSV dan melewati komentar agar petunjuk tetap menempel di berkas."""
  with open(jalur_berkas, encoding="utf-8", newline="") as berkas:
    isi = [baris for baris in berkas if not baris.startswith("#")]
  return list(csv.DictReader(isi))


def hitung_skor(baris_penilaian):
  """Menjumlahkan skor; baris tidak berlaku tidak menambah penyebut."""
  baris_berlaku = [
    baris for baris in baris_penilaian
    if baris["tingkat"] != TINGKAT_DIKECUALIKAN
  ]
  skor = sum(SKOR_TINGKAT[baris["tingkat"]] for baris in baris_berlaku)
  maksimum = len(baris_berlaku) * SKOR_MAKSIMUM_PER_BARIS
  return skor, maksimum, round(100 * skor / maksimum, 1)


def cari_klaim_lemah(baris_penilaian):
  """Menandai Terpenuhi berbukti lemah, karena klaim itu masih diragukan."""
  return [
    baris["id"] for baris in baris_penilaian
    if baris["tingkat"] == "Terpenuhi"
    and baris["status_bukti"] in BUKTI_LEMAH
  ]


def saring_bukti_kuat(baris_penilaian):
  """Memisahkan baris terverifikasi agar pengaruh hipotesis pada skor terlihat."""
  return [
    baris for baris in baris_penilaian if baris["status_bukti"] == BUKTI_KUAT
  ]


def hitung_cakupan_pemetaan(baris_pemetaan):
  """Menghitung status per kolom, karena kolom siap belum berarti data benar."""
  jumlah_status = Counter(baris["status"] for baris in baris_pemetaan)
  persen_siap = round(100 * jumlah_status[STATUS_SIAP] / len(baris_pemetaan), 1)
  return jumlah_status, persen_siap


def cetak_hasil(baris_penilaian, baris_pemetaan):
  """Mencetak ringkasan yang dapat dicocokkan dengan tabel pada Bab 7."""
  skor, maksimum, persen = hitung_skor(baris_penilaian)
  print(f"Skor seluruh baris berlaku: {skor} dari {maksimum} ({persen} persen)")
  skor, maksimum, persen = hitung_skor(saring_bukti_kuat(baris_penilaian))
  print(f"Skor baris terverifikasi: {skor} dari {maksimum} ({persen} persen)")
  print(f"Klaim Terpenuhi berbukti lemah: {cari_klaim_lemah(baris_penilaian)}")
  jumlah_status, persen_siap = hitung_cakupan_pemetaan(baris_pemetaan)
  print(f"Status pemetaan: {dict(jumlah_status)}, siap {persen_siap} persen")


if __name__ == "__main__":
  cetak_hasil(baca_baris(BERKAS_KESENJANGAN), baca_baris(BERKAS_PEMETAAN))
