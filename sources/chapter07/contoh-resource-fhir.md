<!-- Kegunaan: contoh sintetis resource Patient dan Encounter Bab 7. Cara pakai: baca sebagai latihan, jangan kirim ke server nyata. -->
# Contoh resource HL7 FHIR R4 (data sintetis)

Seluruh nilai pada berkas ini dikarang. Nomor, nama, dan rujukan tidak mewakili pasien, tenaga kesehatan, atau fasilitas nyata. Contoh tidak diuji pada server SATUSEHAT. Spesifikasi berlaku dibaca pada dokumentasi SATUSEHAT dan spesifikasi HL7 FHIR R4.

## Patient

```json
{
  "resourceType": "Patient",
  "identifier": [
    {
      "use": "official",
      "system": "https://fhir.kemkes.go.id/id/patient-ihs-number",
      "value": "P00000000001"
    }
  ],
  "name": [{ "use": "official", "text": "Pasien Sintetis" }],
  "gender": "male",
  "birthDate": "1985-11-02"
}
```

## Encounter

```json
{
  "resourceType": "Encounter",
  "status": "arrived",
  "class": {
    "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
    "code": "AMB",
    "display": "ambulatory"
  },
  "subject": { "reference": "Patient/P00000000001" },
  "period": { "start": "2026-11-02T01:15:00+00:00" },
  "location": [
    { "location": { "reference": "Location/LOK-SINTETIS-01" } }
  ],
  "serviceProvider": { "reference": "Organization/ORG-SINTETIS-01" }
}
```

## Yang perlu diperhatikan

- `Patient.gender` berisi `male`, bukan `L`, karena elemen ini terikat pada daftar kode dengan kekuatan *required*.
- `Encounter.status` dan `Encounter.class` wajib pada spesifikasi dasar R4.
- `Patient.identifier` dan `Patient.name` boleh kosong pada spesifikasi dasar R4, tetapi wajib menurut panduan SATUSEHAT.
- `Encounter.period.start` memakai UTC+00. Pukul 08.15 WIB ditulis 01:15.
- `Encounter.subject` menunjuk Patient, sehingga satu pasien dapat dirujuk oleh banyak kunjungan.
