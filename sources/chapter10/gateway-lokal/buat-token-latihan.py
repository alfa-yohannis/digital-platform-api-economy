# Kegunaan: membuat JWT latihan untuk gateway lokal Bab 10. Cara pakai: python buat-token-latihan.py
"""Mencetak JWT HS256 yang diterima jwt-auth pada apisix.yaml.

Skrip memakai pustaka bawaan Python, supaya mahasiswa tidak perlu memasang paket. Klaim
key menentukan consumer, sehingga batas laju dan kuota dihitung per klinik. Rahasianya
hanya untuk latihan. Rahasia produksi tidak boleh ditulis di berkas yang diberi versi.
"""

import base64
import hashlib
import hmac
import json
import time

KUNCI_KONSUMEN = "klinik-mitra-01"
RAHASIA_LATIHAN = "rahasia-latihan-bab-10-jangan-dipakai-di-produksi"
MASA_BERLAKU_DETIK = 900  # 15 menit, mengikuti pemisalan token pada Bab 6.
KEPALA_TOKEN = {"alg": "HS256", "typ": "JWT"}


def kode_base64url(data_biner):
  """Mengubah data ke base64url tanpa tanda sama dengan, sesuai bentuk JWT."""
  return base64.urlsafe_b64encode(data_biner).rstrip(b"=").decode("ascii")


def kode_json(objek):
  """Mengubah objek ke JSON ringkas, karena tanda tangan dihitung atas teksnya."""
  teks = json.dumps(objek, separators=(",", ":")).encode("utf-8")
  return kode_base64url(teks)


def buat_token(waktu_sekarang):
  """Menyusun kepala, isi, dan tanda tangan, lalu menggabungkannya dengan titik."""
  isi_token = {"key": KUNCI_KONSUMEN, "exp": waktu_sekarang + MASA_BERLAKU_DETIK}
  bagian_tertanda = f"{kode_json(KEPALA_TOKEN)}.{kode_json(isi_token)}"
  tanda_tangan = hmac.new(
    RAHASIA_LATIHAN.encode("utf-8"),
    bagian_tertanda.encode("ascii"),
    hashlib.sha256,
  ).digest()
  return f"{bagian_tertanda}.{kode_base64url(tanda_tangan)}"


if __name__ == "__main__":
  print(buat_token(int(time.time())))
