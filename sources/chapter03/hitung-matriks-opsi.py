# Menghitung matriks opsi strategi Bab 03. Pakai: python hitung-matriks-opsi.py
"""Menguji seberapa peka pilihan opsi strategi terhadap bobot kriteria.

Skor terlihat objektif, padahal bobot adalah pendapat yang diberi angka. Skrip
ini menghitung beberapa set bobot agar tim melihat kapan pemenangnya berganti,
sebelum keputusan ditulis. Seluruh angka adalah asumsi latihan Medikara. Tim
mengganti konstanta di bawah dengan penilaian organisasinya sendiri.
"""

# Urutan kriteria sama dengan urutan angka pada SKOR_OPSI dan SKENARIO_BOBOT.
KRITERIA = (
  "Kendali hubungan pasien",
  "Kendali dan kepatuhan data",
  "Kecepatan masuk pasar",
  "Biaya tiga tahun",
  "Kesesuaian kemampuan tim",
)

# Skor 1 sampai 5. Skor 5 berarti opsi paling menguntungkan pada kriteria itu.
SKOR_OPSI = {
  "Membangun": (5, 5, 1, 1, 2),
  "Bergabung": (1, 2, 5, 4, 4),
  "Bermitra": (3, 4, 3, 3, 3),
}

# Bobot dalam persen. Tiap skenario mewakili satu pandangan yang wajar di rapat.
SKENARIO_BOBOT = {
  "Dasar": (25, 25, 20, 15, 15),
  "Pasar lebih dahulu": (15, 15, 40, 15, 15),
  "Kendali lebih dahulu": (35, 35, 10, 10, 10),
}

TOTAL_BOBOT_PERSEN = 100

# Asumsi tawaran platform asuransi pada Latihan 2.
CALON_PENGGUNA_PER_BULAN = 2000
TARIF_KONSULTASI_RUPIAH = 250000
KOMISI_PLATFORM = 0.12
MARGIN_PASIEN_BARU = 0.40


def hitung_skor_tertimbang(skor_per_kriteria, bobot_per_kriteria):
  """Mengubah skor mentah menjadi satu angka pembanding.

  Bobot wajib berjumlah 100 persen. Bila tidak, skor
  antarskenario tidak sebanding dan pemenangnya salah dibaca.
  """
  if sum(bobot_per_kriteria) != TOTAL_BOBOT_PERSEN:
    raise ValueError("Jumlah bobot harus 100 persen.")
  total = 0
  for skor, bobot in zip(skor_per_kriteria, bobot_per_kriteria):
    total += skor * bobot
  return total / TOTAL_BOBOT_PERSEN


def cari_pemenang(skor_per_opsi):
  """Mengembalikan opsi berskor tertinggi sebagai bahan diskusi, bukan putusan."""
  return max(skor_per_opsi, key=skor_per_opsi.get)


def hitung_titik_impas_pasien_baru():
  """Menghitung pasien baru minimum agar margin menutup komisi seluruh pasien.

  Komisi dibayar untuk semua pasien yang datang lewat platform, sedangkan margin
  tambahan hanya datang dari pasien yang sebelumnya bukan pasien Medikara.
  """
  komisi_per_bulan = (
    CALON_PENGGUNA_PER_BULAN * TARIF_KONSULTASI_RUPIAH * KOMISI_PLATFORM
  )
  margin_per_pasien = TARIF_KONSULTASI_RUPIAH * MARGIN_PASIEN_BARU
  return komisi_per_bulan / margin_per_pasien, komisi_per_bulan


def cetak_hasil():
  """Mencetak skor tiap skenario dan titik impas ke layar."""
  for nama_skenario, bobot in SKENARIO_BOBOT.items():
    skor_per_opsi = {
      opsi: hitung_skor_tertimbang(skor, bobot)
      for opsi, skor in SKOR_OPSI.items()
    }
    rincian = "  ".join(
      f"{opsi} {nilai:.2f}" for opsi, nilai in skor_per_opsi.items()
    )
    print(f"{nama_skenario} -> {cari_pemenang(skor_per_opsi)}")
    print(f"  {rincian}")
  pasien_baru, komisi = hitung_titik_impas_pasien_baru()
  print(f"Komisi per bulan: Rp{komisi:,.0f}")
  print(f"Titik impas: {pasien_baru:,.0f} pasien baru per bulan")


if __name__ == "__main__":
  cetak_hasil()
