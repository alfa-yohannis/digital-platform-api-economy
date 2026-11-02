# Kegunaan: menghitung code_challenge PKCE S256. Cara pakai: python hitung-pkce.py
"""Menunjukkan mengapa code_challenge aman dikirim lewat pengalihan.

Server otorisasi hanya menerima hasil hash saat pengalihan. Akibatnya, pihak
yang menangkap kode otorisasi tidak dapat menebusnya tanpa code_verifier asli.
Skrip ini hanya berhitung di komputer sendiri, tanpa memanggil server apa pun.
"""

import base64
import hashlib
import secrets

# Contoh uji RFC 7636 Lampiran B. Nilainya publik, jangan dipakai di produksi.
CONTOH_VERIFIER_RFC = "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
CONTOH_CHALLENGE_RFC = "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM"
# RFC 7636 menganjurkan 32 oktet acak, menjadi 43 karakter setelah dikodekan.
JUMLAH_OKTET_ACAK = 32


def buat_code_verifier():
  """Membuat rahasia baru per transaksi, agar nilai lama tidak dapat dipakai."""
  return secrets.token_urlsafe(JUMLAH_OKTET_ACAK)


def hitung_code_challenge(code_verifier):
  """Menghitung S256: base64url dari SHA-256, tanpa tanda =.

  Tanda = yang tersisa membuat pencocokan selalu gagal.
  """
  ringkasan = hashlib.sha256(code_verifier.encode("ascii")).digest()
  hasil_kode = base64.urlsafe_b64encode(ringkasan).decode("ascii")
  return hasil_kode.rstrip("=")


def cocokkan_saat_tebus_kode(code_verifier, code_challenge_tersimpan):
  """Meniru pemeriksaan server otorisasi saat kode otorisasi ditebus."""
  hasil_hitung = hitung_code_challenge(code_verifier)
  return secrets.compare_digest(hasil_hitung, code_challenge_tersimpan)


def main():
  """Menguji contoh RFC, lalu memperlihatkan penolakan bagi penangkap kode."""
  hasil_contoh = hitung_code_challenge(CONTOH_VERIFIER_RFC)
  print("Contoh RFC 7636 cocok:", hasil_contoh == CONTOH_CHALLENGE_RFC)

  verifier_baru = buat_code_verifier()
  challenge_baru = hitung_code_challenge(verifier_baru)
  print("Panjang code_verifier baru:", len(verifier_baru), "karakter")
  print("Pemilik asli diterima:",
        cocokkan_saat_tebus_kode(verifier_baru, challenge_baru))

  # Penangkap kode tidak memegang verifier, sehingga hanya dapat menebak.
  verifier_tebakan = buat_code_verifier()
  print("Penangkap kode diterima:",
        cocokkan_saat_tebus_kode(verifier_tebakan, challenge_baru))


if __name__ == "__main__":
  main()
