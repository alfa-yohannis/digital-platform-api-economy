# Kegunaan: memeriksa kontrak Bab 09. Cara pakai: python periksa-kontrak.py kontrak.yaml
"""Memeriksa kebiasaan kontrak dan mencetak ringkasan bagi pembaca non-teknis.

Skrip memeriksa apa yang dapat diperiksa mesin, yaitu kelengkapan tiap operasi.
Akibatnya, tinjauan bersama dapat memakai waktunya untuk arti dan aturan bisnis.
Lulus skrip ini tidak berarti kontrak benar. Skrip hanya membaca berkas lokal dan
tidak memanggil server. Pemasangan yang dibutuhkan: pip install pyyaml
"""

import sys
from pathlib import Path

import yaml

METODE_HTTP = ("get", "post", "put", "patch", "delete")
BIDANG_OPERASI_WAJIB = ("operationId", "summary", "security", "responses")
MEDIA_GALAT = "application/problem+json"
AWAL_KODE_BERHASIL = "2"
AWAL_KODE_GALAT = ("4", "5")
KODE_KELUAR_GAGAL = 1


def ambil_rujukan(kontrak, simpul):
  """Mengikuti $ref internal, karena respons galat biasanya ditulis sekali saja."""
  if "$ref" not in simpul:
    return simpul
  hasil = kontrak
  for bagian in simpul["$ref"].removeprefix("#/").split("/"):
    hasil = hasil[bagian]
  return hasil


def daftar_operasi(kontrak):
  """Mengumpulkan operasi supaya semua pemeriksaan memakai urutan yang sama."""
  hasil = []
  for jalur, butir_jalur in kontrak.get("paths", {}).items():
    for metode in METODE_HTTP:
      if metode in butir_jalur:
        hasil.append((metode.upper(), jalur, butir_jalur[metode]))
  return hasil


def periksa_operasi(kontrak, metode, jalur, operasi):
  """Mengembalikan temuan satu operasi; daftar kosong berarti tidak ada temuan."""
  label = f"{metode} {jalur}"
  temuan = [
    f"{label}: bidang {bidang} belum ada"
    for bidang in BIDANG_OPERASI_WAJIB
    if bidang not in operasi
  ]
  respons = operasi.get("responses", {})
  kode_galat = [kode for kode in respons if str(kode).startswith(AWAL_KODE_GALAT)]
  if not kode_galat:
    temuan.append(f"{label}: belum ada arti gagal")
  for kode in kode_galat:
    isi = ambil_rujukan(kontrak, respons[kode]).get("content", {})
    if MEDIA_GALAT not in isi:
      temuan.append(f"{label}: galat {kode} tidak memakai {MEDIA_GALAT}")
  return temuan


def daftar_scope(operasi):
  """Menggabungkan scope, karena satu operasi dapat menerima beberapa skema."""
  hasil = []
  for syarat in operasi.get("security", []):
    for nama_scope in syarat.values():
      hasil.extend(nama_scope)
  return ", ".join(hasil) or "-"


def cetak_ringkasan(kontrak):
  """Mencetak operasi, scope, dan kode supaya kontrak terbaca tanpa membuka YAML."""
  print(f"{kontrak['info']['title']}, versi {kontrak['info']['version']}")
  for metode, jalur, operasi in daftar_operasi(kontrak):
    respons = [str(kode) for kode in operasi.get("responses", {})]
    berhasil = [kode for kode in respons if kode.startswith(AWAL_KODE_BERHASIL)]
    galat = [kode for kode in respons if kode.startswith(AWAL_KODE_GALAT)]
    print(f"- {metode} {jalur}: {operasi.get('summary', '(tanpa ringkasan)')}")
    print(f"  scope: {daftar_scope(operasi)}")
    print(f"  berhasil: {', '.join(berhasil)}; gagal: {', '.join(galat)}")


def utama():
  """Menjalankan pemeriksaan; kode keluar bukan nol memudahkan pemeriksaan otomatis."""
  if len(sys.argv) != 2:
    print("Pakai: python periksa-kontrak.py kontrak.yaml")
    return KODE_KELUAR_GAGAL
  kontrak = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8"))
  cetak_ringkasan(kontrak)
  temuan = []
  for metode, jalur, operasi in daftar_operasi(kontrak):
    temuan.extend(periksa_operasi(kontrak, metode, jalur, operasi))
  print(f"\nTemuan: {len(temuan)}")
  for butir in temuan:
    print(f"- {butir}")
  return KODE_KELUAR_GAGAL if temuan else 0


if __name__ == "__main__":
  sys.exit(utama())
