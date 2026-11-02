# Simulasi dua sisi pasien dan dokter (Bab 02). Pakai: python simulasi-dua-sisi.py
"""Simulasi pertumbuhan dua sisi untuk pendalaman teknis Bab 02.

Model ini sengaja sederhana agar setiap angkanya dapat ditelusuri dengan
kalkulator. Tujuannya bukan meramal, melainkan memperlihatkan dua gejala
platform: titik kritis (critical mass) dan akibat memilih sisi yang disubsidi
beserta lama subsidinya.

Cara memakai:
  python simulasi-dua-sisi.py                          # empat skenario baku
  python simulasi-dua-sisi.py --sisi dokter --bulan 9  # rincian satu skenario
  python simulasi-dua-sisi.py --csv hasil.csv          # simpan baris ke CSV

Seluruh angka adalah pengandaian untuk kasus fiktif Medikara Health.
"""

import argparse
import csv
import sys

# Kondisi awal pada bulan 0. Angka ini mewakili layanan telekonsultasi
# Medikara+ sebelum dibuka untuk dokter klinik mitra.
PASIEN_AWAL = 6000
DOKTER_AWAL = 60

# Lama simulasi dalam bulan.
JUMLAH_BULAN = 24

# Batas pasar. Tanpa batas ini model tumbuh tanpa ujung, padahal jumlah
# calon pengguna dan dokter yang bersedia praktik daring terbatas.
POTENSI_PASIEN = 150000
POTENSI_DOKTER = 400

# Perilaku sisi pasien. Pasien baru datang karena pilihan dokter bertambah
# (efek lintas sisi). Pasien pergi lebih cepat bila pilihan dokter sedikit.
PASIEN_BARU_PER_DOKTER = 20
DOKTER_MINIMUM_UNTUK_PASIEN = 80
LAJU_PASIEN_PERGI_BILA_SEPI = 0.20
LAJU_PASIEN_PERGI_NORMAL = 0.08
KONSULTASI_PER_PASIEN = 0.3

# Perilaku sisi dokter. Dokter baru datang karena pasien bertambah (efek
# lintas sisi). Dokter pergi lebih cepat bila konsultasinya terlalu sedikit.
DOKTER_BARU_PER_SERIBU_PASIEN = 0.4
KONSULTASI_MINIMUM_PER_DOKTER = 40
LAJU_DOKTER_PERGI_BILA_SEPI = 0.15
LAJU_DOKTER_PERGI_NORMAL = 0.03

# Bentuk subsidi. Subsidi pasien berupa kupon konsultasi pertama gratis.
# Subsidi dokter berupa jaminan honor minimum ditambah rekrutmen aktif.
KUPON_PER_BULAN = 1500
NILAI_KUPON_RUPIAH = 50000
REKRUTMEN_DOKTER_PER_BULAN = 5
HONOR_PER_KONSULTASI_RUPIAH = 60000

# Empat skenario baku yang dibahas di modul: (sisi yang disubsidi, lama bulan).
SKENARIO_BAKU = (("tanpa", 0), ("pasien", 9), ("dokter", 6), ("dokter", 9))

# Titik waktu yang dicetak pada ringkasan.
BULAN_RINGKASAN = (0, 6, 12, 24)

RUPIAH_PER_JUTA = 1_000_000


def hitung_pasien_baru(pasien, dokter, sisi, lama_subsidi, bulan):
  """Menghitung pasien yang bergabung pada satu bulan.

  Pasien tertarik oleh banyaknya dokter, tetapi tarikan itu melemah ketika
  pasar hampir jenuh. Kupon menambah pasien hanya selama masa subsidi.
  Fungsi mengembalikan jumlah pasien baru dan jumlah kupon yang terpakai.
  """
  sisa_pasar = max(0.0, 1 - pasien / POTENSI_PASIEN)
  pasien_baru = PASIEN_BARU_PER_DOKTER * dokter * sisa_pasar
  kupon = 0
  if sisi == "pasien" and bulan <= lama_subsidi:
    kupon = KUPON_PER_BULAN
  return pasien_baru + kupon, kupon


def hitung_pasien_pergi(pasien, dokter):
  """Menghitung pasien yang berhenti memakai platform pada satu bulan.

  Pilihan dokter yang sedikit membuat pasien kecewa, sehingga laju
  kepergiannya naik. Inilah efek lintas sisi yang bekerja ke arah turun.
  """
  if dokter < DOKTER_MINIMUM_UNTUK_PASIEN:
    return pasien * LAJU_PASIEN_PERGI_BILA_SEPI
  return pasien * LAJU_PASIEN_PERGI_NORMAL


def hitung_dokter_baru(pasien, dokter, sisi, lama_subsidi, bulan):
  """Menghitung dokter yang bergabung pada satu bulan.

  Dokter tertarik oleh banyaknya pasien. Rekrutmen aktif menambah dokter
  hanya selama masa subsidi dokter.
  """
  sisa_pasar = max(0.0, 1 - dokter / POTENSI_DOKTER)
  dokter_baru = DOKTER_BARU_PER_SERIBU_PASIEN * pasien / 1000 * sisa_pasar
  if sisi == "dokter" and bulan <= lama_subsidi:
    dokter_baru += REKRUTMEN_DOKTER_PER_BULAN
  return dokter_baru


def hitung_dokter_pergi(dokter, konsultasi_per_dokter, dijamin):
  """Menghitung dokter yang berhenti membuka jadwal pada satu bulan.

  Dokter yang sepi konsultasi cepat pergi. Jaminan honor minimum menahan
  mereka, karena pendapatannya tidak lagi bergantung pada jumlah pasien.
  """
  if dijamin or konsultasi_per_dokter >= KONSULTASI_MINIMUM_PER_DOKTER:
    return dokter * LAJU_DOKTER_PERGI_NORMAL
  return dokter * LAJU_DOKTER_PERGI_BILA_SEPI


def hitung_biaya_jaminan(dokter, konsultasi_per_dokter):
  """Menghitung selisih honor yang dibayar platform kepada dokter.

  Platform hanya membayar kekurangan dari konsultasi minimum, sehingga
  biayanya turun sendiri ketika pasien bertambah.
  """
  kekurangan = max(0.0, KONSULTASI_MINIMUM_PER_DOKTER - konsultasi_per_dokter)
  return kekurangan * HONOR_PER_KONSULTASI_RUPIAH * dokter


def jalankan_skenario(sisi, lama_subsidi):
  """Menjalankan satu skenario dan mengembalikan baris per bulan.

  Setiap baris memuat jumlah pasien, dokter, konsultasi per dokter, dan
  biaya subsidi bulan itu, agar hasilnya dapat diperiksa satu per satu.
  """
  nama = f"{sisi}-{lama_subsidi}" if sisi != "tanpa" else "tanpa"
  pasien = float(PASIEN_AWAL)
  dokter = float(DOKTER_AWAL)
  daftar_baris = [{"skenario": nama, "bulan": 0, "pasien": pasien,
                   "dokter": dokter,
                   "konsultasi_per_dokter":
                     pasien * KONSULTASI_PER_PASIEN / dokter,
                   "biaya_subsidi": 0.0}]
  for bulan in range(1, JUMLAH_BULAN + 1):
    konsultasi_per_dokter = pasien * KONSULTASI_PER_PASIEN / max(dokter, 1.0)
    dijamin = sisi == "dokter" and bulan <= lama_subsidi
    pasien_baru, kupon = hitung_pasien_baru(
      pasien, dokter, sisi, lama_subsidi, bulan)
    pasien_pergi = hitung_pasien_pergi(pasien, dokter)
    dokter_baru = hitung_dokter_baru(pasien, dokter, sisi, lama_subsidi, bulan)
    dokter_pergi = hitung_dokter_pergi(dokter, konsultasi_per_dokter, dijamin)
    biaya = kupon * NILAI_KUPON_RUPIAH
    if dijamin:
      biaya += hitung_biaya_jaminan(dokter, konsultasi_per_dokter)
    pasien = max(0.0, pasien + pasien_baru - pasien_pergi)
    dokter = max(0.0, dokter + dokter_baru - dokter_pergi)
    # Kolom konsultasi per dokter dihitung dari posisi akhir bulan, sehingga
    # dapat diperiksa langsung dari kolom pasien dan dokter pada baris yang sama.
    daftar_baris.append({"skenario": nama, "bulan": bulan, "pasien": pasien,
                         "dokter": dokter,
                         "konsultasi_per_dokter":
                           pasien * KONSULTASI_PER_PASIEN / max(dokter, 1.0),
                         "biaya_subsidi": biaya})
  return daftar_baris


def cetak_ringkasan(hasil_per_skenario):
  """Mencetak posisi beberapa bulan terpilih dan total biaya tiap skenario.

  Bulan 6, 12, dan 24 cukup untuk melihat apakah platform tumbuh sendiri
  sesudah subsidi berhenti, atau justru menyusut kembali.
  """
  print("Skenario   Bulan  Pasien  Dokter  Konsultasi/dokter  Biaya (juta Rp)")
  for daftar_baris in hasil_per_skenario:
    total_biaya = sum(baris["biaya_subsidi"] for baris in daftar_baris)
    for bulan in BULAN_RINGKASAN:
      baris = daftar_baris[bulan]
      print(f"{baris['skenario']:<9} {bulan:>6} {baris['pasien']:>7.0f}"
            f" {baris['dokter']:>7.0f} {baris['konsultasi_per_dokter']:>18.1f}"
            f" {total_biaya / RUPIAH_PER_JUTA:>16.0f}")


def cetak_rincian(daftar_baris):
  """Mencetak seluruh baris bulanan untuk satu skenario."""
  print("Bulan  Pasien  Dokter  Konsultasi/dokter  Biaya bulan ini (juta Rp)")
  for baris in daftar_baris:
    print(f"{baris['bulan']:>5} {baris['pasien']:>7.0f} {baris['dokter']:>7.0f}"
          f" {baris['konsultasi_per_dokter']:>18.1f}"
          f" {baris['biaya_subsidi'] / RUPIAH_PER_JUTA:>26.1f}")


def bulatkan_baris(baris):
  """Membulatkan angka pecahan satu baris agar CSV mudah dibaca."""
  hasil = {}
  for nama_kolom, nilai in baris.items():
    hasil[nama_kolom] = round(nilai, 1) if isinstance(nilai, float) else nilai
  return hasil


def simpan_csv(hasil_per_skenario, nama_berkas):
  """Menyimpan seluruh baris ke CSV agar dapat dibuka di spreadsheet."""
  kolom = ["skenario", "bulan", "pasien", "dokter",
           "konsultasi_per_dokter", "biaya_subsidi"]
  with open(nama_berkas, "w", newline="", encoding="utf-8") as berkas:
    penulis = csv.DictWriter(berkas, fieldnames=kolom)
    penulis.writeheader()
    for daftar_baris in hasil_per_skenario:
      for baris in daftar_baris:
        penulis.writerow(bulatkan_baris(baris))


def main():
  """Membaca argumen, menjalankan skenario, lalu mencetak hasilnya."""
  parser = argparse.ArgumentParser(description="Simulasi pertumbuhan dua sisi")
  parser.add_argument("--sisi", choices=("tanpa", "pasien", "dokter"),
                      help="sisi yang disubsidi untuk rincian satu skenario")
  parser.add_argument("--bulan", type=int, default=9,
                      help="lama subsidi dalam bulan (bawaan 9)")
  parser.add_argument("--csv", help="simpan seluruh baris ke berkas CSV")
  argumen = parser.parse_args()

  if argumen.sisi:
    hasil_per_skenario = [jalankan_skenario(argumen.sisi, argumen.bulan)]
    cetak_rincian(hasil_per_skenario[0])
  else:
    hasil_per_skenario = [jalankan_skenario(sisi, lama)
                          for sisi, lama in SKENARIO_BAKU]
    cetak_ringkasan(hasil_per_skenario)
  if argumen.csv:
    simpan_csv(hasil_per_skenario, argumen.csv)
  return 0


if __name__ == "__main__":
  sys.exit(main())
