---
title: Perlindungan data
minutes: 20
level: Menengah
badge: lengkap
summary: TDE, enkripsi transit, manajemen kunci, dan Data Safe.
objectives:
  - Menjelaskan enkripsi at rest dan in transit
  - Mengelola kunci enkripsi
  - Memakai alat perlindungan data Oracle
---
## Kenapa topik ini diuji
Soal menanyakan kontrol enkripsi wajib dan siapa memegang kunci.

## Konsep inti
| Kontrol | Fungsi |
|---|---|
| TDE (Transparent Data Encryption) | enkripsi kolom/tablespace at rest (wajib di cloud Oracle) |
| TLS | enkripsi koneksi klien → database |
| Manajemen kunci (OCI Vault/KMS) | menyimpan master key, rotasi |
| Oracle Data Safe | penilaian keamanan, masking, audit |
| Backup terenkripsi | melindungi salinan backup |

## Jebakan
- Kehilangan akses ke kunci berarti data (dan backup) tidak dapat dibuka.
- Enkripsi at rest tidak melindungi dari user dengan hak penuh di database — perlu audit/least privilege.
- TLS tanpa validasi sertifikat tetap rentan MITM.
- Masking harus diuji agar data produksi tidak bocor ke non-produksi.

## Latihan
1. Enkripsi data at rest di Oracle?
2. Layanan untuk penilaian keamanan dan masking?

<details><summary>Jawaban</summary>
<p><b>1.</b> TDE.</p>
<p><b>2.</b> Oracle Data Safe.</p>
</details>
