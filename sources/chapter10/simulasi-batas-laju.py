# Kegunaan: mengulang hitungan batas laju dan kuota Bab 6 dan Bab 10. Cara pakai: python simulasi-batas-laju.py
"""Menyimulasikan token bucket dan kuota pada penarikan data 5 permintaan per detik.

Simulasi berjalan di memori dan tidak memanggil sistem apa pun. Tujuannya menunjukkan
bahwa batas laju hanya memperlambat, sedangkan kuota menghentikan. Akibatnya, kedua
batas dipasang bersama. Angka masukan adalah pemisalan latihan.
"""

LAJU_MASUK_PER_DETIK = 5
DURASI_DETIK = 12 * 3600
BATAS_LAJU_PER_DETIK = 1
KAPASITAS_EMBER = 1
KUOTA_PER_HARI = 300
JUMLAH_SALINAN_GATEWAY = 2


def hitung_tanpa_batas(laju_masuk, durasi):
  """Menghitung seluruh permintaan, sebagai pembanding bagi kedua batas."""
  return laju_masuk * durasi


def hitung_token_bucket(laju_masuk, batas_laju, kapasitas, durasi):
  """Menjalankan token bucket per langkah waktu dengan bilangan bulat.

  Satu detik dibagi menjadi laju_masuk langkah, dan satu permintaan datang tiap langkah.
  Satu token bernilai laju_masuk satuan, sehingga tidak ada galat pembulatan pecahan.
  """
  satuan_per_token = laju_masuk
  batas_satuan = kapasitas * satuan_per_token
  satuan_tersedia = batas_satuan
  jumlah_diterima = 0
  for _ in range(laju_masuk * durasi):
    if satuan_tersedia >= satuan_per_token:
      satuan_tersedia -= satuan_per_token
      jumlah_diterima += 1
    satuan_tersedia = min(batas_satuan, satuan_tersedia + batas_laju)
  return jumlah_diterima


def hitung_detik_sampai_kuota_habis(laju_masuk, kuota):
  """Menghitung kapan kuota habis, karena sesudahnya setiap permintaan dijawab 429."""
  return kuota / laju_masuk


def format_angka(nilai):
  """Mencetak angka dengan pemisah ribuan titik, sesuai penulisan pada bab."""
  return f"{nilai:,.0f}".replace(",", ".")


def cetak_ringkasan():
  """Mencetak empat keadaan yang dibandingkan pada bab."""
  tanpa_batas = hitung_tanpa_batas(LAJU_MASUK_PER_DETIK, DURASI_DETIK)
  dengan_laju = hitung_token_bucket(
    LAJU_MASUK_PER_DETIK, BATAS_LAJU_PER_DETIK, KAPASITAS_EMBER, DURASI_DETIK
  )
  detik_habis = hitung_detik_sampai_kuota_habis(LAJU_MASUK_PER_DETIK, KUOTA_PER_HARI)
  print(f"Tanpa batas selama 12 jam : {format_angka(tanpa_batas)} permintaan")
  print(f"Batas laju 1 per detik    : {format_angka(dengan_laju)} permintaan")
  print(f"Kuota {KUOTA_PER_HARI} per hari      : habis setelah {detik_habis:.0f} detik")
  kuota_efektif = KUOTA_PER_HARI * JUMLAH_SALINAN_GATEWAY
  print(f"Dua salinan penghitung lokal: sekitar {kuota_efektif} per hari")


if __name__ == "__main__":
  cetak_ringkasan()
