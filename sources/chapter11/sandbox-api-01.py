# Kegunaan: sandbox lokal API-01 dengan data sintetis untuk pendalaman Bab 11. Cara pakai: python sandbox-api-01.py
"""Menjawab empat operasi API-01 di komputer sendiri, tanpa menyentuh sistem apa pun.

Tiap skenario gagal dipicu oleh masukan tertentu, sehingga klinik dapat mengujinya kapan
saja. Akibatnya, kasus gagal tidak perlu menunggu kejadian nyata atau data pasien nyata.
Jalankan hanya pada komputer sendiri. Berkas ini bukan pengganti uji pada SIMRS.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import parse_qs, urlparse

ALAMAT = "127.0.0.1"
PORT = 8011
TIPE_MASALAH = "https://api.medikara.example/masalah/"

TOKEN_SAH = "token-uji-klinik-01"
TOKEN_KEDALUWARSA = "token-uji-kedaluwarsa"
KUOTA_UJI_PER_HARI = 100
DETIK_TUNGGU_KUOTA = 86400
DETIK_TUNGGU_SIMRS = 3600

RUMAH_SAKIT = {"jakarta", "bekasi", "depok", "bogor", "bandung"}
TANGGAL_CONTOH = "2026-11-02"
TANGGAL_SIMRS_DIPERBARUI = "2026-11-03"
SLOT_TERSEDIA = "BKS-20261102-0915"
SLOT_TERISI = "BKS-20261102-0930"
JUMLAH_PASIEN_SINTETIS = 20
PASIEN_SINTETIS = {
  f"PSN-{nomor:05d}" for nomor in range(1, JUMLAH_PASIEN_SINTETIS + 1)}

JUMLAH_PANGGILAN = {"nilai": 0}
JANJI_TEMU = {}


def buat_masalah(kode_status, tipe, judul, rincian):
  """Menyusun jawaban galat menurut RFC 9457, sama dengan kontrak Bab 9."""
  return kode_status, {
    "type": TIPE_MASALAH + tipe,
    "title": judul,
    "status": kode_status,
    "detail": rincian,
  }, {}


def periksa_token(nilai_header):
  """Memeriksa token uji, supaya skenario akses kedaluwarsa dapat dicoba."""
  token = nilai_header.removeprefix("Bearer ").strip()
  if token == TOKEN_KEDALUWARSA:
    return buat_masalah(
      401, "token-tidak-sah", "Akses kedaluwarsa", "Minta token uji baru.")
  if token != TOKEN_SAH:
    return buat_masalah(
      401, "token-tidak-sah", "Token tidak sah", "Periksa token uji.")
  return None


def periksa_kuota():
  """Menghitung panggilan, karena kuota uji lebih kecil daripada kuota produksi."""
  JUMLAH_PANGGILAN["nilai"] += 1
  if JUMLAH_PANGGILAN["nilai"] <= KUOTA_UJI_PER_HARI:
    return None
  status, isi, _ = buat_masalah(
    429, "kuota-habis", "Kuota hari ini habis", "Tunda sesuai Retry-After.")
  return status, isi, {"Retry-After": str(DETIK_TUNGGU_KUOTA)}


def jawab_jadwal(parameter):
  """Menjawab pencarian slot, termasuk 503 yang bukan berarti tidak ada dokter."""
  rumah_sakit = parameter.get("rumahSakit", [""])[0]
  tanggal = parameter.get("tanggal", [""])[0]
  if rumah_sakit not in RUMAH_SAKIT or not tanggal:
    return buat_masalah(
      400, "masukan-tidak-sah", "Masukan tidak sah",
      "Periksa rumahSakit dan tanggal.")
  if tanggal == TANGGAL_SIMRS_DIPERBARUI:
    status, isi, _ = buat_masalah(
      503, "simrs-tidak-tersedia", "Jadwal belum dapat dibaca",
      "SIMRS sedang diperbarui. Bukan berarti tidak ada dokter.")
    return status, isi, {"Retry-After": str(DETIK_TUNGGU_SIMRS)}
  daftar_slot = []
  if rumah_sakit == "bekasi" and tanggal == TANGGAL_CONTOH:
    daftar_slot = [{
      "id": SLOT_TERSEDIA,
      "namaDokter": "dr. Contoh Sintetis",
      "spesialis": "anak",
      "mulai": "2026-11-02T09:15:00+07:00",
      "durasiMenit": 15,
    }]
  isi = {"rumahSakit": rumah_sakit, "tanggal": tanggal, "slot": daftar_slot}
  return 200, isi, {}


def jawab_pemesanan(isi_permintaan, kunci_idempotensi):
  """Membuat janji sintetis. Hanya 201 yang berarti slot sudah terkunci."""
  slot = isi_permintaan.get("slot", "")
  pasien = isi_permintaan.get("pasien", "")
  if not kunci_idempotensi or not slot:
    return buat_masalah(
      400, "masukan-tidak-sah", "Masukan tidak sah",
      "Periksa slot dan Idempotency-Key.")
  if pasien not in PASIEN_SINTETIS:
    return buat_masalah(
      400, "pasien-tidak-dapat-dipakai", "Nomor pasien tidak dapat dipakai",
      "Periksa kartu pasien, jangan menebak.")
  if slot == SLOT_TERISI:
    return buat_masalah(
      409, "slot-terisi", "Slot sudah terisi", "Pilih slot lain.")
  id_janji = f"JT-{len(JANJI_TEMU) + 1:05d}"
  janji = {"id": id_janji, "slot": slot, "pasien": pasien,
           "status": "terkonfirmasi"}
  JANJI_TEMU[id_janji] = janji
  return 201, janji, {"Location": f"/janji-temu/{id_janji}"}


def jawab_satu_janji(id_janji, metode):
  """Membaca atau membatalkan janji. Data janji tetap ada untuk rekonsiliasi."""
  janji = JANJI_TEMU.get(id_janji)
  if janji is None:
    return buat_masalah(
      404, "janji-tidak-ditemukan", "Janji tidak ditemukan",
      "Periksa nomor janji.")
  if metode == "DELETE":
    janji["status"] = "dibatalkan"
  return 200, janji, {}


class PenanganSandbox(BaseHTTPRequestHandler):
  """Menghubungkan alamat dengan fungsi jawaban, satu kelas per server contoh."""

  def kirim_jawaban(self, status, isi, header_tambahan):
    """Mengirim JSON, karena seluruh jawaban kontrak API-01 berbentuk JSON."""
    teks = json.dumps(isi, ensure_ascii=False).encode("utf-8")
    self.send_response(status)
    self.send_header("Content-Type", "application/json; charset=utf-8")
    self.send_header("Content-Length", str(len(teks)))
    for nama, nilai in header_tambahan.items():
      self.send_header(nama, nilai)
    self.end_headers()
    self.wfile.write(teks)

  def baca_isi(self):
    """Membaca isi permintaan. Isi yang rusak diperlakukan sebagai format salah."""
    panjang = int(self.headers.get("Content-Length", 0))
    try:
      return json.loads(self.rfile.read(panjang) or b"{}")
    except json.JSONDecodeError:
      return {}

  def tangani(self, metode):
    """Memeriksa token dan kuota lebih dulu, lalu memilih jawaban menurut alamat."""
    alamat = urlparse(self.path)
    hasil = periksa_token(self.headers.get("Authorization", ""))
    hasil = hasil or periksa_kuota()
    if hasil is None and metode == "GET" and alamat.path == "/jadwal-dokter":
      hasil = jawab_jadwal(parse_qs(alamat.query))
    elif hasil is None and metode == "POST" and alamat.path == "/janji-temu":
      hasil = jawab_pemesanan(
        self.baca_isi(), self.headers.get("Idempotency-Key", ""))
    elif hasil is None and alamat.path.startswith("/janji-temu/"):
      hasil = jawab_satu_janji(alamat.path.rsplit("/", 1)[-1], metode)
    elif hasil is None:
      hasil = buat_masalah(
        404, "janji-tidak-ditemukan", "Alamat tidak ada", "Periksa alamat.")
    self.kirim_jawaban(*hasil)

  def do_GET(self):
    """Menerima GET, nama metode ini ditentukan oleh pustaka http.server."""
    self.tangani("GET")

  def do_POST(self):
    """Menerima POST, nama metode ini ditentukan oleh pustaka http.server."""
    self.tangani("POST")

  def do_DELETE(self):
    """Menerima DELETE, nama metode ini ditentukan oleh pustaka http.server."""
    self.tangani("DELETE")


def utama():
  """Menjalankan server lokal sampai dihentikan dengan Ctrl+C."""
  server = HTTPServer((ALAMAT, PORT), PenanganSandbox)
  print(f"Sandbox berjalan di http://{ALAMAT}:{PORT}")
  server.serve_forever()


if __name__ == "__main__":
  utama()
