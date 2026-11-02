# Kegunaan: memanggil API gempa terbaru BMKG yang terbuka tanpa akun, lalu menampilkan
# kode status HTTP, jenis isi, dan isi JSON-nya. Cara pakai: python panggil-api-publik.py
# Untuk melihat kode 404: python panggil-api-publik.py autogempaa.json (sengaja salah ketik).
"""Pendalaman teknis Bab 01: membaca request dan response dari satu API publik.

Skrip ini hanya memakai pustaka standar Python 3, sehingga tidak perlu memasang paket.
Data berasal dari BMKG (Badan Meteorologi, Klimatologi, dan Geofisika), dan setiap
pemakaian data itu wajib mencantumkan BMKG sebagai sumbernya.

Skrip memanggil API satu kali untuk setiap kali dijalankan, tidak dalam putaran,
agar tidak membebani server milik pihak lain. Padanannya dengan curl:

  curl -i https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json
  curl -i https://data.bmkg.go.id/DataMKG/TEWS/autogempaa.json
"""

import json
import sys
import urllib.error
import urllib.request

# Alamat dasar data gempa BMKG. Nama berkas di ujungnya menentukan data yang diminta.
ALAMAT_DASAR = "https://data.bmkg.go.id/DataMKG/TEWS/"
# Berkas bawaan berisi satu kejadian gempa terbaru.
BERKAS_BAWAAN = "autogempa.json"
# Batas tunggu, agar skrip tidak menggantung bila jaringan atau server lambat.
BATAS_TUNGGU_DETIK = 10
# Identitas peminta. Sebagian server menolak request yang tidak menyebut identitasnya.
IDENTITAS_PEMINTA = "IT40613-bab01-pendalaman/1.0"
# Kode status yang menandakan request berhasil dan isinya dapat dibaca.
KODE_BERHASIL = 200
# Kunci JSON yang ditampilkan, dipilih yang mudah dibaca rekan non-teknis.
KUNCI_YANG_DITAMPILKAN = ("Tanggal", "Jam", "Magnitude", "Kedalaman", "Wilayah",
                          "Potensi")


def kirim_request(alamat):
  """Mengirim satu request GET, lalu mengembalikan kode, jenis isi, dan isi.

  Kode 4xx dan 5xx dikembalikan sebagai hasil biasa, bukan sebagai galat,
  karena justru kode itulah yang ingin dibaca pada pendalaman ini.
  """
  header = {"Accept": "application/json", "User-Agent": IDENTITAS_PEMINTA}
  request = urllib.request.Request(alamat, headers=header)
  try:
    response = urllib.request.urlopen(request, timeout=BATAS_TUNGGU_DETIK)
  except urllib.error.HTTPError as galat_http:
    jenis_isi = galat_http.headers.get("Content-Type")
    return galat_http.code, jenis_isi, galat_http.read()
  with response:
    jenis_isi = response.headers.get("Content-Type")
    return response.status, jenis_isi, response.read()


def tampilkan_gempa(isi_response):
  """Mengurai isi JSON, lalu menampilkan kunci terpilih dari data gempa.

  Struktur JSON BMKG bertingkat: objek Infogempa berisi objek gempa. Bila isinya
  bukan JSON atau strukturnya berubah, skrip menampilkan pesan yang jelas, bukan
  berhenti dengan galat yang membingungkan pembaca non-teknis.
  """
  try:
    data = json.loads(isi_response)
  except json.JSONDecodeError:
    print("Isi response bukan JSON yang sah.")
    return
  gempa = data.get("Infogempa", {}).get("gempa")
  if gempa is None:
    print("Struktur JSON tidak dikenali. Isi mentahnya:")
    print(json.dumps(data, indent=2, ensure_ascii=False))
    return
  for kunci in KUNCI_YANG_DITAMPILKAN:
    print(f"  {kunci:<10}: {gempa.get(kunci, '-')}")
  print("Sumber data: BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)")


def main():
  """Membaca nama berkas dari argumen, memanggil API, lalu melaporkan hasilnya.

  Kegagalan jaringan dilaporkan dengan status keluar 1, sehingga mudah dibedakan
  dari response yang memang membawa kode 4xx atau 5xx.
  """
  nama_berkas = sys.argv[1] if len(sys.argv) > 1 else BERKAS_BAWAAN
  alamat = ALAMAT_DASAR + nama_berkas
  print(f"Request : GET {alamat}")
  try:
    kode_status, jenis_isi, isi_response = kirim_request(alamat)
  except (urllib.error.URLError, TimeoutError) as galat_jaringan:
    print(f"Tidak ada response. Periksa sambungan internet: {galat_jaringan}")
    sys.exit(1)
  print(f"Response: kode status {kode_status}, jenis isi {jenis_isi}")
  if kode_status == KODE_BERHASIL:
    tampilkan_gempa(isi_response)
  else:
    print("Request tidak berhasil. Kode 4xx berarti ada yang salah di sisi peminta,")
    print("sedangkan kode 5xx berarti ada masalah di sisi penyedia.")


if __name__ == "__main__":
  main()
