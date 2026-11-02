# Bandingkan polling dan webhook untuk Latihan 1: python hitung-pemberitahuan.py
"""Menghitung beban pemberitahuan hasil laboratorium bagi klinik mitra.

Skrip ini ada agar pilihan polling atau webhook dibaca dari angka, bukan dari
selera. Tim mengganti konstanta di awal berkas dengan angka organisasinya. Angka
bawaan adalah asumsi latihan Medikara Health, bukan data organisasi nyata.
"""

JUMLAH_KLINIK = 40
KUNJUNGAN_PER_HARI_PER_KLINIK = 60
PORSI_KUNJUNGAN_DENGAN_HASIL = 0.10
JAM_LAYANAN_PER_HARI = 12
MENIT_PER_JAM = 60
PANGGILAN_PEMESANAN_PER_KLINIK = 180
KUOTA_PER_KLINIK_PER_HARI = 300
DAFTAR_SELANG_MENIT = (1, 5, 6)
PORSI_GAGAL_KIRIMAN_PERTAMA = 0.02
REKONSILIASI_PER_JAM = 1


def hitung_hasil_per_hari():
  """Jumlah hasil baru menentukan berapa pemberitahuan yang benar-benar perlu."""
  kunjungan = JUMLAH_KLINIK * KUNJUNGAN_PER_HARI_PER_KLINIK
  return round(kunjungan * PORSI_KUNJUNGAN_DENGAN_HASIL)


def hitung_polling(selang_menit):
  """Polling menghabiskan permintaan walaupun tidak ada hasil baru."""
  per_jam = MENIT_PER_JAM // selang_menit
  per_klinik = per_jam * JAM_LAYANAN_PER_HARI
  total = per_klinik * JUMLAH_KLINIK
  tunda_rata_rata_menit = selang_menit / 2
  return total, per_klinik, tunda_rata_rata_menit


def hitung_webhook():
  """Webhook mengikuti jumlah hasil, tetapi tetap butuh rekonsiliasi."""
  hasil = hitung_hasil_per_hari()
  kiriman = hasil + round(hasil * PORSI_GAGAL_KIRIMAN_PERTAMA)
  per_klinik = REKONSILIASI_PER_JAM * JAM_LAYANAN_PER_HARI
  rekonsiliasi = per_klinik * JUMLAH_KLINIK
  return kiriman, rekonsiliasi, per_klinik


def nilai_kuota(panggilan_per_klinik):
  """Kuota dipakai bersama pemesanan, sehingga keduanya dijumlahkan."""
  total = panggilan_per_klinik + PANGGILAN_PEMESANAN_PER_KLINIK
  keterangan = "aman" if total <= KUOTA_PER_KLINIK_PER_HARI else "melampaui"
  return total, keterangan


def cetak_perbandingan():
  """Mencetak satu baris per skenario agar mudah disalin ke tabel Latihan 1."""
  hasil = hitung_hasil_per_hari()
  print(f"Hasil baru: {hasil} per hari, {hasil // JAM_LAYANAN_PER_HARI} per jam")
  for selang_menit in DAFTAR_SELANG_MENIT:
    total, per_klinik, tunda = hitung_polling(selang_menit)
    panggilan_klinik, keterangan = nilai_kuota(per_klinik)
    print(
      f"Polling {selang_menit} menit: {total} per hari, tunda {tunda} menit, "
      f"klinik {panggilan_klinik}/{KUOTA_PER_KLINIK_PER_HARI} ({keterangan})"
    )
  kiriman, rekonsiliasi, per_klinik = hitung_webhook()
  panggilan_klinik, keterangan = nilai_kuota(per_klinik)
  print(
    f"Webhook: {kiriman + rekonsiliasi} per hari "
    f"({kiriman} kiriman, {rekonsiliasi} rekonsiliasi), "
    f"klinik {panggilan_klinik}/{KUOTA_PER_KLINIK_PER_HARI} ({keterangan})"
  )


if __name__ == "__main__":
  cetak_perbandingan()
