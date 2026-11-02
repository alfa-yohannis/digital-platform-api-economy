# Kegunaan: memeriksa kecocokan alur Arazzo dengan kontrak Bab 9.
# Cara pakai: python periksa-alur-arazzo.py (memerlukan PyYAML)
"""Memeriksa bahwa alur Arazzo hanya menyebut operasi yang benar-benar ada di kontrak.

Pemeriksaan ini sengaja sempit dan hanya membaca berkas lokal. Lulus berarti rujukan
operasi dan parameter cocok. Lulus tidak membuktikan alur aman dijalankan oleh agen,
karena Arazzo menyerahkan keamanan kepada pelaksana.
"""

import sys
from pathlib import Path

import yaml

FOLDER_INI = Path(__file__).resolve().parent
BERKAS_ALUR = FOLDER_INI / "alur-janji-temu.arazzo.yaml"
BERKAS_KONTRAK = FOLDER_INI.parent / "chapter09" / "kontrak-api-01-janji-temu.yaml"
METODE_HTTP = ("get", "put", "post", "delete", "patch")
KELUAR_GAGAL = 1
RUJUKAN_LOKAL = "#/"


def baca_yaml(jalur):
  """Membaca satu berkas YAML sebagai UTF-8, karena komentarnya berbahasa Indonesia."""
  return yaml.safe_load(jalur.read_text(encoding="utf-8"))


def selesaikan_parameter(parameter, kontrak):
  """Mengikuti $ref ke komponen kontrak, supaya nama parameter dapat dibandingkan."""
  rujukan = parameter.get("$ref", "")
  if not rujukan.startswith(RUJUKAN_LOKAL):
    return parameter
  hasil = kontrak
  for bagian in rujukan[len(RUJUKAN_LOKAL):].split("/"):
    hasil = hasil[bagian]
  return hasil


def kumpulkan_operasi(kontrak):
  """Membuat peta operationId ke nama parameternya, termasuk parameter tingkat jalur."""
  operasi = {}
  for isi_jalur in kontrak["paths"].values():
    bersama = isi_jalur.get("parameters", [])
    for metode in METODE_HTTP:
      if metode not in isi_jalur:
        continue
      isi_operasi = isi_jalur[metode]
      semua = bersama + isi_operasi.get("parameters", [])
      nama = {selesaikan_parameter(item, kontrak)["name"] for item in semua}
      operasi[isi_operasi["operationId"]] = nama
  return operasi


def periksa_langkah(langkah, operasi):
  """Mengembalikan daftar temuan pada satu langkah alur."""
  temuan = []
  nama_operasi = langkah["operationId"]
  if nama_operasi not in operasi:
    temuan.append(f"{langkah['stepId']}: operasi {nama_operasi} tidak ada di kontrak")
    return temuan
  for parameter in langkah.get("parameters", []):
    if parameter["name"] not in operasi[nama_operasi]:
      temuan.append(f"{langkah['stepId']}: parameter {parameter['name']} tidak dikenal")
  if not langkah.get("successCriteria"):
    temuan.append(f"{langkah['stepId']}: tanpa kriteria berhasil")
  return temuan


def main():
  """Mencetak hasil tiap langkah, lalu keluar dengan kode gagal bila ada temuan."""
  alur = baca_yaml(BERKAS_ALUR)
  kontrak = baca_yaml(BERKAS_KONTRAK)
  operasi = kumpulkan_operasi(kontrak)
  jumlah_temuan = 0
  for alur_kerja in alur["workflows"]:
    for langkah in alur_kerja["steps"]:
      temuan = periksa_langkah(langkah, operasi)
      jumlah_temuan += len(temuan)
      status = "lulus" if not temuan else "; ".join(temuan)
      print(f"{langkah['stepId']} -> {langkah['operationId']}: {status}")
  print(f"Kontrak memuat {len(operasi)} operasi. Temuan: {jumlah_temuan}.")
  if jumlah_temuan:
    sys.exit(KELUAR_GAGAL)


if __name__ == "__main__":
  main()
