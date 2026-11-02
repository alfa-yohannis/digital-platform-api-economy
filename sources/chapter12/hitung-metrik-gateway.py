# Kegunaan: metrik API dari log Bab 12. Cara pakai: python hitung-metrik-gateway.py
"""Menyusun bahan dashboard metrik API dari log gateway, tanpa data pasien.

Skrip ini sengaja memisahkan panggilan dari transaksi unik. Tanpa pemisahan itu,
pengulangan dan polling terbaca sebagai pertumbuhan pemakaian.
"""
import csv
import math
from collections import defaultdict
from pathlib import Path

LOKASI_LOG = Path(__file__).with_name("contoh-log-gateway.csv")
OPERASI_PEMESANAN = "POST /janji-temu"
STATUS_TERBENTUK = 201
AWAL_GALAT_PENYEDIA = 500
AWAL_GALAT_KLIEN = 400
PERSENTIL_EKOR = 95
HARGA_PER_PANGGILAN = 667
HARGA_PER_JANJI = 2_000


def baca_log(lokasi):
  """Membaca log dan melewati komentar, agar catatan asal data tetap menempel."""
  with lokasi.open(encoding="utf-8", newline="") as berkas:
    baris_data = (baris for baris in berkas if not baris.startswith("#"))
    return list(csv.DictReader(baris_data))


def persentil(nilai, persen):
  """Peringkat terdekat, karena sampel kecil tidak perlu interpolasi."""
  urutan = sorted(nilai)
  peringkat = math.ceil(persen / 100 * len(urutan))
  return urutan[peringkat - 1]


def transaksi_unik(baris_log):
  """Menghitung janji sah per id, agar pengulangan tidak terhitung dua."""
  return {
    baris["id_transaksi"]
    for baris in baris_log
    if baris["operasi"] == OPERASI_PEMESANAN
    and int(baris["status"]) == STATUS_TERBENTUK
  }


def latensi_menurut_hasil(baris_log):
  """Memisahkan latensi berhasil dan gagal, karena keduanya punya arti berbeda."""
  kelompok = defaultdict(list)
  for baris in baris_log:
    if baris["operasi"] == OPERASI_PEMESANAN:
      hasil = "berhasil" if int(baris["status"]) < AWAL_GALAT_KLIEN else "gagal"
      kelompok[hasil].append(int(baris["latensi_ms"]))
  return kelompok


def cetak_ringkasan(baris_log):
  """Mencetak metrik gabungan dan selisih tagihan pada dua unit."""
  panggilan = len(baris_log)
  unik = transaksi_unik(baris_log)
  status = [int(baris["status"]) for baris in baris_log]
  galat_penyedia = sum(kode >= AWAL_GALAT_PENYEDIA for kode in status)
  galat_klien = sum(AWAL_GALAT_KLIEN <= kode < AWAL_GALAT_PENYEDIA for kode in status)
  print(f"Panggilan {panggilan}, transaksi unik {len(unik)}")
  print(f"Panggilan per transaksi {panggilan / len(unik):.2f}")
  print(f"Galat penyedia {galat_penyedia} ({galat_penyedia / panggilan:.1%})")
  print(f"Galat klien {galat_klien} ({galat_klien / panggilan:.1%})")
  print(f"Tagihan per panggilan Rp{panggilan * HARGA_PER_PANGGILAN:,}")
  print(f"Tagihan per janji Rp{len(unik) * HARGA_PER_JANJI:,}")
  semua_pemesanan = []
  for hasil, nilai in latensi_menurut_hasil(baris_log).items():
    semua_pemesanan.extend(nilai)
    median = persentil(nilai, 50)
    ekor = persentil(nilai, PERSENTIL_EKOR)
    print(f"Latensi pemesanan {hasil}: n={len(nilai)}, median {median}, p95 {ekor} ms")
  print(f"Rata-rata pemesanan {sum(semua_pemesanan) / len(semua_pemesanan):.0f} ms")


def cetak_per_klinik(baris_log):
  """Mencetak per klinik, karena rata-rata gabungan menyembunyikan klinik yang gagal."""
  per_klinik = defaultdict(list)
  for baris in baris_log:
    per_klinik[baris["klinik"]].append(baris)
  aktif = 0
  for klinik, baris_klinik in sorted(per_klinik.items()):
    unik = transaksi_unik(baris_klinik)
    aktif += bool(unik)
    print(f"{klinik}: {len(baris_klinik)} panggilan, {len(unik)} transaksi unik")
  print(f"Klinik dengan minimal satu 201: {aktif} dari {len(per_klinik)}")


def main():
  """Menjalankan ringkasan lalu rincian per klinik dari satu berkas log."""
  baris_log = baca_log(LOKASI_LOG)
  cetak_ringkasan(baris_log)
  cetak_per_klinik(baris_log)


if __name__ == "__main__":
  main()
