# Periksa alat MCP dalam memori: python periksa-demo.py.
"""Periksa batas fasilitas, galat, dan sifat pratinjau tanpa API produksi."""

import asyncio
from mcp import Client
from server import server


async def main():
  """Uji melalui klien protokol agar schema dan pemanggilan ikut diperiksa."""
  async with Client(server, raise_exceptions=True) as client:
    hasil = await client.call_tool("cari_slot", {
      "tanggal": "2027-01-09", "fasilitas": "klinik-uji-jakarta"
    })
    assert not hasil.is_error, hasil
    assert "uji-01" in str(hasil), hasil
    pratinjau = await client.call_tool("tinjau_slot", {"id_slot": "uji-01"})
    assert not pratinjau.is_error, pratinjau
    assert "pratinjau" in str(pratinjau), pratinjau
    ditolak = await client.call_tool("cari_slot", {
      "tanggal": "2027-01-09", "fasilitas": "fasilitas-di-luar-izin"
    })
    assert ditolak.is_error, ditolak
    assert "Fasilitas di luar ruang latihan" in str(ditolak), ditolak
    hilang = await client.call_tool("tinjau_slot", {"id_slot": "tidak-ada"})
    assert hilang.is_error, hilang
    assert "Slot sintetis tidak ditemukan" in str(hilang), hilang
  print("Lolos: pencarian, pratinjau, penolakan fasilitas, dan slot tidak ada.")


if __name__ == "__main__":
  asyncio.run(main())
