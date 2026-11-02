# MCP lokal Bab 14; jalankan python server.py setelah pemasangan.
"""Ekspos dua kemampuan sintetis memakai SDK resmi MCP lini 2.x."""

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
from simulasi import cari_jadwal, pratinjau_janji

server = MCPServer("Medikara: latihan baca dan pratinjau")


@server.tool()
def cari_slot(tanggal: str, fasilitas: str) -> list[dict]:
  """Cari jadwal sintetis; fasilitas hanya klinik-uji-jakarta."""
  try:
    return cari_jadwal(tanggal, fasilitas)
  except ValueError as error:
    raise ToolError(str(error)) from error


@server.tool()
def tinjau_slot(id_slot: str) -> dict:
  """Baca pratinjau tanpa memesan atau menulis data."""
  try:
    return pratinjau_janji(id_slot)
  except ValueError as error:
    raise ToolError(str(error)) from error


if __name__ == "__main__":
  server.run(transport="stdio")
