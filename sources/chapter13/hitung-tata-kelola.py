# Kegunaan: mengulang hitungan Bab 13. Cara pakai: python hitung-tata-kelola.py
"""Mengulang hitungan model tata kelola, pemeringkatan apotek, dan katalog Bab 13.

Seluruh angka Medikara di sini adalah pemisalan latihan. Skrip dipisahkan dari
naskah supaya tim dapat mengganti asumsi tanpa menghitung ulang dengan tangan.
Skrip hanya memakai pustaka standar Python dan hanya membaca CSV di folder ini.
"""

import csv
from pathlib import Path

TARIF_PER_JAM = 60_000
USULAN_PER_TRIWULAN = 12
TRIWULAN_PER_TAHUN = 4
BULAN_PER_TAHUN = 12

# Satu baris per kelas perubahan: jumlah usulan, tunggu, orang, dan jam per orang.
# Kelas C tidak punya jam sendiri, karena dibahas di rapat forum bulanan.
KELAS_PERUBAHAN = {
  "A": {"usulan": 30, "tunggu_hari": 1, "orang": 1, "jam": 0.5},
  "B": {"usulan": 14, "tunggu_hari": 3, "orang": 2, "jam": 1.0},
  "C": {"usulan": 4, "tunggu_hari": 10, "orang": 0, "jam": 0.0},
}

RAPAT_FORUM_PER_TAHUN = 12
JAM_PER_RAPAT = 2
ANGGOTA_FORUM = 5
TUNGGU_FORUM_HARI = 10
TUNGGU_SEJAWAT_HARI = 1
JAM_SEJAWAT = 0.5

KLINIK_MITRA = 40
FORMAT_GALAT_TAMBAHAN = 4
JAM_PER_FORMAT = 4

PAGU_LAPISAN_JUTA = 300.0
ALTERNATIF_A_JUTA = 269.6
PORTAL_P2_JUTA = 29.2
JAM_PANDUAN_GAYA = 80
JAM_PENDAMPINGAN_PER_TIM = 40
TIM_DIDAMPINGI = 2

APOTEK_MILIK = 12
APOTEK_MITRA = 18
TEBUS_PER_BULAN = 20_000
PILIH_PERTAMA = 0.60
MARGIN_PER_TEBUS = 15_000
APOTEK_DI_WILAYAH = 1_200
BATAS_POSISI_DOMINAN = 0.50

KUNJUNGAN_PER_TAHUN = 1_200_000
AMBANG_PENGGUNA_DMA = 45_000_000
AMBANG_BISNIS_DMA = 10_000

PENGECUALIAN_PER_TRIWULAN = 2
TENGGAT_TRIWULAN = 2
TAHUN_PENGAMATAN = 3

REKAM_INSIDEN = 1_240
BIDANG_MINIMUM = 4
BIDANG_USULAN_VENDOR = 10


def rupiah_juta(jam):
  """Mengubah jam ke juta rupiah, supaya semua tabel memakai satuan yang sama."""
  return jam * TARIF_PER_JAM / 1_000_000


def hitung_model():
  """Membandingkan tiga model dengan 48 usulan yang sama, supaya selisihnya adil."""
  usulan_setahun = USULAN_PER_TRIWULAN * TRIWULAN_PER_TAHUN
  jam_forum = RAPAT_FORUM_PER_TAHUN * JAM_PER_RAPAT * ANGGOTA_FORUM
  tunggu_federasi = sum(
    kelas["usulan"] * kelas["tunggu_hari"] for kelas in KELAS_PERUBAHAN.values()
  )
  jam_tinjauan = sum(
    kelas["usulan"] * kelas["orang"] * kelas["jam"]
    for kelas in KELAS_PERUBAHAN.values()
  )
  return [
    ("Terpusat", usulan_setahun * TUNGGU_FORUM_HARI, jam_forum),
    (
      "Terdistribusi",
      usulan_setahun * TUNGGU_SEJAWAT_HARI,
      usulan_setahun * JAM_SEJAWAT,
    ),
    ("Federasi", tunggu_federasi, jam_forum + jam_tinjauan),
  ]


def cetak_model():
  """Mencetak tabel tiga model, sumber Tabel perbandingan model di naskah."""
  print("== Tiga model tata kelola untuk 48 usulan API-01 per tahun ==")
  for nama, tunggu, jam in hitung_model():
    print(f"{nama:14} tunggu {tunggu:4} hari-usulan, {jam:5.0f} jam, "
          f"Rp{rupiah_juta(jam):.2f} juta")
  jam_klinik = KLINIK_MITRA * FORMAT_GALAT_TAMBAHAN * JAM_PER_FORMAT
  print(f"Biaya format galat berbeda: {jam_klinik} jam, "
        f"Rp{rupiah_juta(jam_klinik):.1f} juta, sekali di sisi klinik")
  terpusat = hitung_model()[0][1]
  federasi = hitung_model()[2][1]
  print(f"Tunggu turun {terpusat - federasi} hari-usulan, "
        f"{(terpusat - federasi) / terpusat:.0%}\n")


def cetak_biaya_awal():
  """Memisahkan biaya tahun pertama dari sisa pagu, karena bab memakai pagu Bab 12."""
  jam_berjalan = hitung_model()[2][2]
  jam_pendampingan = TIM_DIDAMPINGI * JAM_PENDAMPINGAN_PER_TIM
  total_jam = jam_berjalan + JAM_PANDUAN_GAYA + jam_pendampingan
  sisa_pagu = PAGU_LAPISAN_JUTA - ALTERNATIF_A_JUTA - PORTAL_P2_JUTA
  print("== Biaya federasi tahun pertama ==")
  print(f"Berjalan {jam_berjalan:.0f} jam, panduan {JAM_PANDUAN_GAYA} jam, "
        f"pendampingan {jam_pendampingan} jam")
  print(f"Total {total_jam:.0f} jam, Rp{rupiah_juta(total_jam):.2f} juta")
  print(f"Sisa pagu lapisan bersama Rp{sisa_pagu:.1f} juta\n")


def cetak_pengecualian():
  """Memperlihatkan akibat tenggat, supaya pengecualian tidak menjadi kebiasaan."""
  tanpa_tenggat = PENGECUALIAN_PER_TRIWULAN * TRIWULAN_PER_TAHUN * TAHUN_PENGAMATAN
  dengan_tenggat = PENGECUALIAN_PER_TRIWULAN * TENGGAT_TRIWULAN
  print("== Pengecualian aktif sesudah 3 tahun ==")
  print(f"Tanpa tenggat {tanpa_tenggat}, dengan tenggat 6 bulan {dengan_tenggat}\n")


def cetak_pemeringkatan():
  """Menghitung pergeseran tebus resep pada Latihan 2, seluruhnya pemisalan."""
  total_apotek = APOTEK_MILIK + APOTEK_MITRA
  bagian_jumlah = APOTEK_MILIK / total_apotek
  sisa = 1 - PILIH_PERTAMA
  bagian_teratas = PILIH_PERTAMA + sisa * bagian_jumlah
  tebus_netral = TEBUS_PER_BULAN * bagian_jumlah
  tebus_teratas = TEBUS_PER_BULAN * bagian_teratas
  geser = tebus_teratas - tebus_netral
  print("== Pemeringkatan apotek pada Medikara+ ==")
  print(f"Bagian jumlah apotek milik: {bagian_jumlah:.0%}")
  print(f"Netral {tebus_netral:.0f} tebus, selalu teratas {tebus_teratas:.0f} tebus "
        f"({bagian_teratas:.0%})")
  margin_setahun = geser * MARGIN_PER_TEBUS * BULAN_PER_TAHUN / 1e9
  print(f"Bergeser {geser:.0f} tebus per bulan, "
        f"Rp{margin_setahun:.3f} miliar per tahun")
  sisa_mitra = TEBUS_PER_BULAN - tebus_teratas
  print(f"Per apotek mitra: {(TEBUS_PER_BULAN - tebus_netral) / APOTEK_MITRA:.0f} "
        f"menjadi {sisa_mitra / APOTEK_MITRA:.0f} tebus per bulan")
  bagian_wilayah = APOTEK_MILIK / APOTEK_DI_WILAYAH
  print(f"Definisi luas {bagian_wilayah:.1%}, definisi sempit {bagian_teratas:.0%}, "
        f"ambang {BATAS_POSISI_DOMINAN:.0%}\n")


def cetak_ambang_dma():
  """Menghitung jarak Medikara dari ambang DMA, walau DMA tidak berlaku baginya."""
  print("== Jarak dari ambang DMA ==")
  print(f"Pengguna: {AMBANG_PENGGUNA_DMA / KUNJUNGAN_PER_TAHUN:.1f} kali kunjungan")
  print(f"Bisnis: {AMBANG_BISNIS_DMA / KLINIK_MITRA:.0f} kali klinik mitra\n")


def cetak_paparan_data():
  """Menghitung butir data terpapar, supaya pembatasan bidang punya angka."""
  print("== Butir data bila 1.240 rekam terpapar ==")
  print(f"{BIDANG_MINIMUM} bidang: {REKAM_INSIDEN * BIDANG_MINIMUM}")
  print(f"{BIDANG_USULAN_VENDOR} bidang: {REKAM_INSIDEN * BIDANG_USULAN_VENDOR}\n")


def cetak_katalog():
  """Membaca katalog contoh, supaya kelengkapan dihitung dari berkas, bukan ingatan."""
  jalur = Path(__file__).with_name("katalog-api.csv")
  with jalur.open(encoding="utf-8") as berkas:
    baris_data = [baris for baris in berkas if not baris.startswith("#")]
  daftar_api = list(csv.DictReader(baris_data))
  punya_pemilik = [api for api in daftar_api if api["pemilik"] != "Belum ada"]
  punya_kontrak = [api for api in daftar_api if api["kontrak"] != "Belum ada"]
  print("== Kelengkapan katalog ==")
  print(f"Baris {len(daftar_api)}, punya pemilik {len(punya_pemilik)}, "
        f"punya kontrak {len(punya_kontrak)}")
  tanpa_pemilik = [api["id"] for api in daftar_api if api["pemilik"] == "Belum ada"]
  print(f"Tanpa pemilik: {', '.join(tanpa_pemilik)}")


if __name__ == "__main__":
  cetak_model()
  cetak_biaya_awal()
  cetak_pengecualian()
  cetak_pemeringkatan()
  cetak_ambang_dma()
  cetak_paparan_data()
  cetak_katalog()
