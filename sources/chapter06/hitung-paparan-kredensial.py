# Kegunaan: paparan kredensial dan beban catatan Bab 6. Cara pakai: jalankan via python.
"""Membandingkan akibat kredensial yang bocor, sesudah konstanta diganti tim.

Angka bawaan mengikuti asumsi latihan Medikara pada Bab 6. Skrip ini hanya
berhitung dan tidak menyentuh sistem apa pun, sehingga aman dipakai tanpa izin
uji. Organisasi nyata mengganti konstanta dengan data yang sudah dianonimkan.
"""

# Fakta bersama dari Bab 1, Bab 3, Bab 4, dan Bab 5.
TARIF_PER_JAM_RUPIAH = 60_000
JUMLAH_KLINIK_MITRA = 40
KUOTA_PER_HARI_PER_KLINIK = 300
HASIL_LABORATORIUM_PER_HARI = 240
JAM_LAYANAN_PER_HARI = 12
PANGGILAN_MEDIKARA_PLUS_PER_BULAN = 84_000
JUMLAH_LABORATORIUM_MITRA = 3

# Asumsi latihan Bab 6, ganti dengan angka organisasi.
JAM_GANTI_KREDENSIAL_PER_MITRA = 2
HARI_TIDAK_TERDETEKSI = 30
LAJU_PENYALAHGUNA_PER_DETIK = 5
BATAS_LAJU_PER_DETIK = 1
MENIT_MASA_BERLAKU_TOKEN = 15
HARI_PER_BULAN = 30
DETIK_PER_JAM = 3_600
MENIT_PER_JAM = 60
BYTE_PER_CATATAN_RINGKAS = 500
BYTE_PER_CATATAN_DENGAN_ISI = 50_000
BYTE_PER_GB = 1_000_000_000
BULAN_PER_TAHUN = 12


def biaya_ganti_kredensial(jumlah_mitra):
  """Menghitung biaya pergantian, karena kredensial bersama memaksa semua ikut."""
  return jumlah_mitra * JAM_GANTI_KREDENSIAL_PER_MITRA * TARIF_PER_JAM_RUPIAH


def permintaan_dalam_jam_layanan(laju_per_detik):
  """Menghitung isi yang dapat ditarik bila tidak ada kuota yang menghentikan."""
  return laju_per_detik * DETIK_PER_JAM * JAM_LAYANAN_PER_HARI


def catatan_per_bulan():
  """Menghitung batas atas catatan: Medikara+ ditambah kuota penuh semua klinik."""
  kapasitas_klinik = JUMLAH_KLINIK_MITRA * KUOTA_PER_HARI_PER_KLINIK * HARI_PER_BULAN
  return PANGGILAN_MEDIKARA_PLUS_PER_BULAN + kapasitas_klinik


def main():
  """Mencetak angka yang dipakai naskah, supaya tim dapat memeriksa ulang."""
  print("Ganti kredensial bersama (Rp):", biaya_ganti_kredensial(JUMLAH_KLINIK_MITRA))
  print("Ganti kredensial satu mitra (Rp):", biaya_ganti_kredensial(1))
  print("Ganti kredensial 3 laboratorium (Rp):",
        biaya_ganti_kredensial(JUMLAH_LABORATORIUM_MITRA))

  hasil_per_klinik = HASIL_LABORATORIUM_PER_HARI // JUMLAH_KLINIK_MITRA
  print("Hasil per klinik per hari:", hasil_per_klinik)
  print("Hasil di luar hak bila hanya scope:",
        HASIL_LABORATORIUM_PER_HARI - hasil_per_klinik)

  print("Paparan kredensial 30 hari (panggilan):",
        HARI_TIDAK_TERDETEKSI * KUOTA_PER_HARI_PER_KLINIK)
  print("Paparan token curian (panggilan, paling banyak):",
        KUOTA_PER_HARI_PER_KLINIK)

  print("Tanpa batas, 12 jam:",
        permintaan_dalam_jam_layanan(LAJU_PENYALAHGUNA_PER_DETIK))
  print("Dengan batas laju, 12 jam:",
        permintaan_dalam_jam_layanan(BATAS_LAJU_PER_DETIK))
  print("Dengan kuota habis dalam (detik):",
        KUOTA_PER_HARI_PER_KLINIK / LAJU_PENYALAHGUNA_PER_DETIK)

  token_per_lab = JAM_LAYANAN_PER_HARI * MENIT_PER_JAM // MENIT_MASA_BERLAKU_TOKEN
  print("Token per laboratorium per hari:", token_per_lab)
  print("Token 3 laboratorium per hari:", token_per_lab * JUMLAH_LABORATORIUM_MITRA)

  jumlah_catatan = catatan_per_bulan()
  print("Catatan per bulan:", jumlah_catatan)
  print("GB per tahun, catatan ringkas:",
        jumlah_catatan * BYTE_PER_CATATAN_RINGKAS * BULAN_PER_TAHUN / BYTE_PER_GB)
  print("GB per tahun, catatan berisi isi klinis:",
        jumlah_catatan * BYTE_PER_CATATAN_DENGAN_ISI * BULAN_PER_TAHUN / BYTE_PER_GB)


if __name__ == "__main__":
  main()
