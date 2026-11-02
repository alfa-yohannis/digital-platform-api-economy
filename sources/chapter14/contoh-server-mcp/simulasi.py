# Simulasi jadwal sintetis Bab 14; jalankan python simulasi.py.
"""Pisahkan logika latihan dari SDK agar aturan dapat diperiksa tanpa jaringan."""

import json
from datetime import date

FASILITAS_LATIHAN = "klinik-uji-jakarta"
JADWAL = (
  {"id_slot": "uji-01", "tanggal": "2027-01-09", "jam": "09:00"},
  {"id_slot": "uji-02", "tanggal": "2027-01-09", "jam": "10:00"},
)


def cari_jadwal(tanggal: str, fasilitas: str) -> list[dict]:
  """Batasi pencarian pada fasilitas sintetis dan tanggal ISO yang sah."""
  date.fromisoformat(tanggal)
  if fasilitas != FASILITAS_LATIHAN:
    raise ValueError("Fasilitas di luar ruang latihan")
  return [dict(slot) for slot in JADWAL if slot["tanggal"] == tanggal]


def pratinjau_janji(id_slot: str) -> dict:
  """Tampilkan akibat yang diusulkan tanpa membuat atau menyimpan pemesanan."""
  for slot in JADWAL:
    if slot["id_slot"] == id_slot:
      return {
        "status": "pratinjau",
        "fasilitas": FASILITAS_LATIHAN,
        "slot": dict(slot),
        "membuat_pemesanan": False,
        "langkah_berikutnya": "Tinjauan manusia di aplikasi yang berwenang",
      }
  raise ValueError("Slot sintetis tidak ditemukan")


def main():
  """Cetak contoh agar mahasiswa dapat memeriksa hasil tanpa memasang SDK."""
  print(json.dumps(cari_jadwal("2027-01-09", FASILITAS_LATIHAN), indent=2))
  print(json.dumps(pratinjau_janji("uji-01"), indent=2))


if __name__ == "__main__":
  main()
