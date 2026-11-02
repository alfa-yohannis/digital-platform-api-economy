# Bandingkan biaya sambungan langsung dan lapisan: python hitung-beban-integrasi.py
"""Menghitung beban integrasi untuk Latihan 1 dan kotak pendalaman Bab 4.

Skrip ini ada agar tim tidak berdebat dari perasaan. Tim mengganti konstanta di
awal berkas dengan angka organisasinya, lalu membaca titik impasnya. Angka bawaan
adalah asumsi latihan Medikara Health, bukan data organisasi nyata.
"""

JUMLAH_SISTEM_SUMBER = 5
BIAYA_PER_SAMBUNGAN_JUTA = 45
BIAYA_LAPISAN_BERSAMA_JUTA = 300
DAFTAR_JUMLAH_TUJUAN = (1, 2, 3, 4, 6, 8)
BATAS_PENCARIAN_TITIK_IMPAS = 50
JUMLAH_SISTEM_CONTOH_GRAF = 9
INDEKS_SAMBUNGAN = 0
INDEKS_BIAYA = 1


def hitung_biaya_langsung(jumlah_sumber, jumlah_tujuan):
  """Tiap sumber disambung ke tiap tujuan, sehingga biaya tumbuh berlipat."""
  sambungan = jumlah_sumber * jumlah_tujuan
  return sambungan, sambungan * BIAYA_PER_SAMBUNGAN_JUTA


def hitung_biaya_lapisan(jumlah_sumber, jumlah_tujuan):
  """Tiap sistem cukup satu sambungan, tetapi lapisannya juga punya biaya."""
  sambungan = jumlah_sumber + jumlah_tujuan
  biaya = sambungan * BIAYA_PER_SAMBUNGAN_JUTA + BIAYA_LAPISAN_BERSAMA_JUTA
  return sambungan, biaya


def hitung_batas_pasangan(jumlah_sistem):
  """Batas atas graf lengkap. Anggaran tidak boleh disusun dari angka ini."""
  return jumlah_sistem * (jumlah_sistem - 1) // 2


def cari_titik_impas(jumlah_sumber):
  """Mencari jumlah tujuan terkecil agar lapisan lebih murah.

  Bila tidak ditemukan, fungsi mengembalikan None. Akibatnya tim tahu bahwa
  lapisan bersama tidak layak pada asumsi biaya yang sedang dipakai.
  """
  for jumlah_tujuan in range(1, BATAS_PENCARIAN_TITIK_IMPAS + 1):
    langsung = hitung_biaya_langsung(jumlah_sumber, jumlah_tujuan)
    lapisan = hitung_biaya_lapisan(jumlah_sumber, jumlah_tujuan)
    if lapisan[INDEKS_BIAYA] < langsung[INDEKS_BIAYA]:
      return jumlah_tujuan
  return None


def cetak_perbandingan():
  """Mencetak satu baris per skenario agar mudah disalin ke tabel Latihan 1."""
  for jumlah_tujuan in DAFTAR_JUMLAH_TUJUAN:
    langsung = hitung_biaya_langsung(JUMLAH_SISTEM_SUMBER, jumlah_tujuan)
    lapisan = hitung_biaya_lapisan(JUMLAH_SISTEM_SUMBER, jumlah_tujuan)
    print(
      f"{jumlah_tujuan} tujuan: "
      f"langsung {langsung[INDEKS_SAMBUNGAN]} (Rp{langsung[INDEKS_BIAYA]} juta), "
      f"lapisan {lapisan[INDEKS_SAMBUNGAN]} (Rp{lapisan[INDEKS_BIAYA]} juta)"
    )
  batas = hitung_batas_pasangan(JUMLAH_SISTEM_CONTOH_GRAF)
  print(f"Batas pasangan {JUMLAH_SISTEM_CONTOH_GRAF} sistem: {batas}")
  print(f"Lapisan lebih murah mulai {cari_titik_impas(JUMLAH_SISTEM_SUMBER)} tujuan")


if __name__ == "__main__":
  cetak_perbandingan()
