# Sumber Bab 07

Salin templat sebelum mengisi. Contoh Medikara memakai data latihan dan bukan bukti organisasi nyata.

| Berkas | Kegunaan |
| :-- | :-- |
| [penilaian-kesiapan-interoperabilitas.md](penilaian-kesiapan-interoperabilitas.md) | Lembar kerja Aktivitas: skala, contoh terisi, ruang isian, dan pertanyaan tinjauan |
| [contoh-kesenjangan-medikara.csv](contoh-kesenjangan-medikara.csv) | Contoh delapan baris kesenjangan Medikara, sama dengan tabel kasus penilaian pada Bab 7 |
| [pemetaan-simrs-fhir.csv](pemetaan-simrs-fhir.csv) | Contoh pemetaan 13 kolom SIMRS ke elemen HL7 FHIR R4, untuk pendalaman teknis Aktivitas |
| [contoh-resource-fhir.md](contoh-resource-fhir.md) | Contoh sintetis `resource` Patient dan Encounter, salinan listing pada Bab 7 |
| [hitung-kesiapan-interoperabilitas.py](hitung-kesiapan-interoperabilitas.py) | Menghitung skor kesiapan dan cakupan pemetaan dari kedua berkas CSV |

CSV memakai UTF-8 dan koma. Hapus komentar `#` di awal saat impor ke spreadsheet. Periksa satuan angka dan bedakan bukti, asumsi, serta target.

Cara menjalankan skrip dari folder ini:

```
python hitung-kesiapan-interoperabilitas.py
```

Skrip hanya membaca CSV lokal dan tidak memanggil server. Skor yang dihasilkan adalah alat percakapan tim, bukan penilaian kepatuhan resmi.

Contoh `resource` tidak boleh dikirim ke lingkungan produksi. Konfigurasi nyata memerlukan kredensial resmi, tinjauan keamanan, dan izin organisasi. Data pasien atau karyawan nyata tidak boleh dipakai.
