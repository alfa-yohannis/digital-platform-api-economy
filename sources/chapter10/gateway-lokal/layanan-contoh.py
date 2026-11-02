# Kegunaan: layanan tiruan di belakang gateway Bab 10. Cara pakai: dijalankan oleh docker compose.
"""Menjawab setiap GET dengan data sintetis, supaya kebijakan gateway dapat diuji.

Layanan ini tidak memeriksa token. Akibatnya, bila permintaan tanpa token dijawab 401,
penolakan itu pasti berasal dari gateway. Layanan produksi tetap wajib memeriksa hak
atas objek, seperti pada Bab 6. Layanan ini tidak boleh dipakai di luar latihan.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

ALAMAT_DENGAR = "0.0.0.0"
PORT_DENGAR = 8000
KODE_BERHASIL = 200
JAWABAN_SINTETIS = {"sumber": "layanan-contoh", "slot": [], "catatan": "data sintetis"}


class PenanganContoh(BaseHTTPRequestHandler):
  """Menangani GET, karena pengujian kebijakan gateway tidak perlu mengubah data."""

  def do_GET(self):
    """Mengirim JSON tetap, sehingga perbedaan jawaban hanya berasal dari gateway."""
    isi_jawaban = json.dumps(JAWABAN_SINTETIS).encode("utf-8")
    self.send_response(KODE_BERHASIL)
    self.send_header("Content-Type", "application/json")
    self.send_header("Content-Length", str(len(isi_jawaban)))
    self.end_headers()
    self.wfile.write(isi_jawaban)


if __name__ == "__main__":
  HTTPServer((ALAMAT_DENGAR, PORT_DENGAR), PenanganContoh).serve_forever()
