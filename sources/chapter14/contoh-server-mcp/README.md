# Server MCP latihan Bab 14

Contoh memakai SDK Python resmi lini **2.x** dengan `MCPServer`; versi yang diverifikasi adalah **2.3.0**. Python 3.11 atau lebih baru diperlukan. Dua tool memakai jadwal sintetis: `cari_slot` dan `tinjau_slot`. Keduanya hanya membaca; tidak ada pemesanan atau pemanggilan API rumah sakit.

## Menjalankan

Dari folder ini:

```powershell
python simulasi.py
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
.venv/Scripts/python periksa-demo.py
.venv/Scripts/python server.py
```

Pada Linux atau macOS gunakan `.venv/bin/python`. Server berkomunikasi melalui stdin/stdout dan menunggu klien MCP; tidak mencetak antarmuka web. Hentikan dengan Ctrl+C. Host yang mendukung stdio menjalankan interpreter virtual environment dengan argumen jalur absolut `server.py`. Contoh tidak memerlukan API key model AI.

`periksa-demo.py` memakai klien SDK dalam memori. Empat pemeriksaan harus lulus: pencarian sah, pratinjau, penolakan fasilitas di luar latihan, dan penolakan slot yang tidak ada. Galat dua kasus terakhir merupakan hasil yang diharapkan. Paket `mcp` 2.3.0 menyatakan revisi protokol terbarunya 2026-07-28.

## Pengujian dengan MCP Inspector (opsional)

Dokumentasi SDK menyebut perintah `uv run mcp dev server.py` untuk membuka MCP Inspector, dan Inspector memerlukan `npx` dari Node.js. Status: langkah ini belum dijalankan pada pemeriksaan Bab 14, karena `npx` tidak tersedia pada mesin pemeriksaan. Keempat pemeriksaan di atas berjalan tanpa Inspector. Tim yang memakai Inspector mencatat versinya, karena dukungan revisi protokol perlu diperiksa sendiri.

## Percobaan

1. Panggil `cari_slot` dengan tanggal `2027-01-09` dan fasilitas `klinik-uji-jakarta`.
2. Panggil `tinjau_slot` dengan `id_slot` bernilai `uji-01`.
3. Periksa `membuat_pemesanan: false`. Ulangi panggilan dan amati bahwa tidak ada keadaan pemesanan yang berubah.
4. Coba fasilitas atau slot lain dan jelaskan alasan penolakannya.

Tanggal tetap merupakan data latihan, bukan jadwal layanan nyata. Daftar fasilitas di kode merupakan pembatas demonstrasi, bukan autentikasi. Tidak ada implementasi persetujuan transaksi produksi pada contoh ini. Penambahan tool yang mengubah keadaan memerlukan identitas, otorisasi objek, pratinjau, persetujuan yang sesuai risiko, idempotensi, serta audit di layanan bisnis.

Referensi: [SDK resmi](https://py.sdk.modelcontextprotocol.io/), [pengujian](https://py.sdk.modelcontextprotocol.io/get-started/testing/), dan [spesifikasi MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28). Contoh lama yang mengimpor `mcp.server.fastmcp` memakai lini berbeda; jangan mencampurkan instruksinya.
