# Kegunaan: pemeriksa panduan gaya Bab 13. Cara pakai: lihat README.md di folder ini.
"""Memeriksa enam butir panduan gaya yang dapat dinilai mesin pada kontrak OpenAPI.

Butir GAYA-07 dan GAYA-08 sengaja tidak diperiksa, karena tujuan data dan hak atas
objek memerlukan tinjauan manusia dan uji perilaku. Akibatnya, nol temuan hanya
berarti kebiasaan tertulis dipenuhi, bukan kontrak aman atau bermakna. Skrip hanya
membaca berkas lokal. Pemasangan yang dibutuhkan: pip install pyyaml
"""

import re
import sys
from pathlib import Path

import yaml

METODE_HTTP = ("get", "post", "put", "patch", "delete")
POLA_JALUR = re.compile(r"^(/([a-z0-9]+(-[a-z0-9]+)*|\{[a-zA-Z]+\}))+$")
MEDIA_GALAT = "application/problem+json"
AWAL_KODE_GALAT = ("4", "5")
NAMA_KUNCI_IDEMPOTENSI = "Idempotency-Key"
NAMA_PARAMETER_BATAS = "batas"
KODE_KELUAR_GAGAL = 1


def ambil_rujukan(kontrak, simpul):
  """Mengikuti $ref internal, karena respons galat biasanya ditulis sekali saja."""
  if "$ref" not in simpul:
    return simpul
  hasil = kontrak
  for bagian in simpul["$ref"].removeprefix("#/").split("/"):
    hasil = hasil[bagian]
  return hasil


def nama_parameter(kontrak, operasi):
  """Mengumpulkan nama parameter operasi dengan huruf kecil agar mudah dibandingkan."""
  return {
    ambil_rujukan(kontrak, parameter)["name"].lower()
    for parameter in operasi.get("parameters", [])
  }


def periksa_jalur(jalur):
  """GAYA-01: bentuk jalur seragam memudahkan klien membaca seluruh API."""
  if POLA_JALUR.match(jalur):
    return []
  return [f"GAYA-01 {jalur}: jalur memakai huruf kecil dan tanda hubung"]


def periksa_kelengkapan(label, operasi):
  """GAYA-02 dan GAYA-03: operasi tanpa identitas atau scope sulit ditinjau."""
  temuan = []
  if "operationId" not in operasi or "summary" not in operasi:
    temuan.append(f"GAYA-02 {label}: operationId atau summary belum ada")
  if "security" not in operasi:
    temuan.append(f"GAYA-03 {label}: security dan scope belum disebut")
  return temuan


def periksa_galat(kontrak, label, operasi):
  """GAYA-04: format galat tunggal mencegah klien menulis pengurai per rumah sakit."""
  temuan = []
  for kode, respons in operasi.get("responses", {}).items():
    if not str(kode).startswith(AWAL_KODE_GALAT):
      continue
    isi = ambil_rujukan(kontrak, respons).get("content", {})
    if MEDIA_GALAT not in isi:
      temuan.append(f"GAYA-04 {label} {kode}: galat tidak memakai {MEDIA_GALAT}")
  return temuan


def periksa_idempotensi(kontrak, metode, label, operasi):
  """GAYA-05: POST tanpa kunci idempotensi dapat membuat janji ganda saat diulang."""
  if metode != "post":
    return []
  if NAMA_KUNCI_IDEMPOTENSI.lower() in nama_parameter(kontrak, operasi):
    return []
  return [f"GAYA-05 {label}: POST tidak menerima {NAMA_KUNCI_IDEMPOTENSI}"]


def periksa_batas(kontrak, metode, jalur, label, operasi):
  """GAYA-06: daftar tanpa batas membebani server, tetapi butir ini tidak mutlak."""
  if metode != "get" or "{" in jalur:
    return []
  if NAMA_PARAMETER_BATAS in nama_parameter(kontrak, operasi):
    return []
  return [f"GAYA-06 {label}: daftar sebaiknya punya parameter {NAMA_PARAMETER_BATAS}"]


def periksa_kontrak(kontrak):
  """Mengumpulkan temuan dan jumlah operasi supaya laporan dapat dibandingkan."""
  temuan = []
  jumlah_operasi = 0
  for jalur, butir_jalur in kontrak.get("paths", {}).items():
    temuan.extend(periksa_jalur(jalur))
    for metode in METODE_HTTP:
      if metode not in butir_jalur:
        continue
      jumlah_operasi += 1
      operasi = butir_jalur[metode]
      label = f"{metode.upper()} {jalur}"
      temuan.extend(periksa_kelengkapan(label, operasi))
      temuan.extend(periksa_galat(kontrak, label, operasi))
      temuan.extend(periksa_idempotensi(kontrak, metode, label, operasi))
      temuan.extend(periksa_batas(kontrak, metode, jalur, label, operasi))
  return jumlah_operasi, temuan


def main():
  """Mengembalikan kode keluar gagal bila ada temuan, supaya alur otomatis berhenti."""
  jalur_kontrak = Path(sys.argv[1])
  kontrak = yaml.safe_load(jalur_kontrak.read_text(encoding="utf-8"))
  jumlah_operasi, temuan = periksa_kontrak(kontrak)
  print(f"{jalur_kontrak.name}: {jumlah_operasi} operasi, {len(temuan)} temuan")
  for butir in temuan:
    print(f"  {butir}")
  print("Nol temuan tidak membuktikan API aman. GAYA-07 dan GAYA-08 ditinjau manusia.")
  sys.exit(KODE_KELUAR_GAGAL if temuan else 0)


if __name__ == "__main__":
  main()
