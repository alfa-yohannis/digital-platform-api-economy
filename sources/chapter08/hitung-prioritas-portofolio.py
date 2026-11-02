# Kegunaan: skor dan sisa kapasitas portofolio Bab 8. Cara pakai: jalankan via python.
"""Menghitung skor kandidat API dan sisa kapasitas portofolio.

Skrip dipisah dari lembar kerja supaya bobot dapat diubah tanpa menyentuh data.
Akibatnya, tim dapat menguji kepekaan urutan terhadap bobot, bukan hanya satu
hasil. Skrip hanya membaca berkas CSV lokal dan tidak memanggil server.
"""

import csv
from pathlib import Path

BERKAS_MATRIKS = Path(__file__).with_name("matriks-prioritas-api.csv")
GERBANG_DINILAI = "dinilai"
SKALA_TERATAS = 5

# Usaha dan risiko dibalik, karena angka besar pada keduanya berarti kurang menarik.
PENGGESER_SKALA = SKALA_TERATAS + 1
BOBOT_DASAR = {"nilai": 0.5, "usaha": 0.3, "risiko": 0.2}
BOBOT_RISIKO_NAIK = {"nilai": 0.4, "usaha": 0.2, "risiko": 0.4}

ANGGOTA_TIM = 4
JAM_PER_BULAN = 160
BULAN_PER_TAHUN = 12
TARIF_PER_JAM_JUTA = 0.06
JAM_KEWAJIBAN = 600
PORTOFOLIO_TERPILIH = ["API-06", "API-01", "API-02"]


def baca_kandidat(berkas):
  """Membaca CSV dan melewati komentar, karena baris itu bukan data."""
  with berkas.open(encoding="utf-8", newline="") as sumber:
    baris_data = [baris for baris in sumber if not baris.startswith("#")]
  return list(csv.DictReader(baris_data))


def hitung_skor(kandidat, bobot):
  """Menghitung skor tertimbang; skor tidak menggantikan prasyarat."""
  skor_nilai = bobot["nilai"] * int(kandidat["nilai"])
  skor_usaha = bobot["usaha"] * (PENGGESER_SKALA - int(kandidat["usaha"]))
  skor_risiko = bobot["risiko"] * (PENGGESER_SKALA - int(kandidat["risiko"]))
  return round(skor_nilai + skor_usaha + skor_risiko, 1)


def hitung_sisa_kapasitas(daftar_kandidat, urutan_terpilih):
  """Mengurangi kapasitas per pekerjaan; kewajiban memakai jam dahulu."""
  kapasitas = ANGGOTA_TIM * JAM_PER_BULAN * BULAN_PER_TAHUN
  jam_per_id = {
    baris["id"]: int(baris["jam_usaha"]) for baris in daftar_kandidat
  }
  sisa = kapasitas - JAM_KEWAJIBAN
  catatan = [("Kapasitas", kapasitas), ("Sesudah kewajiban", sisa)]
  for id_kandidat in urutan_terpilih:
    sisa -= jam_per_id[id_kandidat]
    catatan.append((f"Sesudah {id_kandidat}", sisa))
  return catatan


def cetak_skor(daftar_kandidat):
  """Mencetak dua perangkat bobot berdampingan, supaya perubahan urutan terlihat."""
  print("ID      Skor dasar  Skor risiko naik  Kandidat")
  for kandidat in daftar_kandidat:
    skor_dasar = hitung_skor(kandidat, BOBOT_DASAR)
    skor_risiko = hitung_skor(kandidat, BOBOT_RISIKO_NAIK)
    nama = kandidat["kandidat"]
    print(f"{kandidat['id']}  {skor_dasar:>10}  {skor_risiko:>16}  {nama}")


def cetak_kapasitas(catatan_kapasitas):
  """Mencetak sisa jam dan padanan rupiah pada tarif yang sama dengan bab lain."""
  for keterangan, jam in catatan_kapasitas:
    biaya_juta = round(jam * TARIF_PER_JAM_JUTA, 1)
    print(f"{keterangan:<20} {jam:>6} jam  Rp{biaya_juta} juta")


def main():
  """Menjalankan perhitungan pada kandidat yang lolos tiga gerbang."""
  semua_kandidat = baca_kandidat(BERKAS_MATRIKS)
  kandidat_dinilai = [
    baris for baris in semua_kandidat if baris["gerbang"] == GERBANG_DINILAI
  ]
  cetak_skor(kandidat_dinilai)
  print()
  cetak_kapasitas(hitung_sisa_kapasitas(kandidat_dinilai, PORTOFOLIO_TERPILIH))


if __name__ == "__main__":
  main()
