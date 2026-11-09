---
title: Arsitektur Oracle Database@AWS
minutes: 22
level: Menengah
badge: lengkap
summary: Exadata milik Oracle di dalam data center AWS, dikelola OCI, dipesan lewat AWS.
objectives:
  - Menjelaskan komponen arsitektur
  - Menjelaskan pembagian tanggung jawab Oracle vs pelanggan
  - Membedakan letak kontrol (AWS vs OCI)
---
## Kenapa topik ini diuji
Domain 20% ini menuntut pemahaman "siapa mengelola apa" dan alur kontrolnya.

## Konsep inti
```text
AWS Region
 └─ Availability Zone
     ├─ Amazon VPC (aplikasi/EC2)
     └─ ODB network  <-- Exadata infrastructure (dikelola OCI)
          ├─ Exadata VM cluster / Exascale VM cluster
          └─ Autonomous VM cluster
```

Prinsip:

- **Infrastruktur Oracle berjalan di dalam data center AWS**, dekat aplikasi.
- **Kontrol permintaan lewat AWS** (konsol/CLI/API `odb:`), yang memanggil OCI.
- **OCI mengelola** infrastruktur Exadata dan layanan database.
- **Pelanggan mengelola** database, skema, jaringan ODB, IAM, dan integrasi.
- Backup dapat diarahkan ke **Amazon S3**.

## Jebakan
- Mengira database berjalan "di OCI region" secara fisik — perangkatnya di data center AWS.
- Bingung dua konsol: provisioning infrastruktur di AWS, operasi database tertentu di OCI.
- Lupa bahwa ODB network adalah objek terpisah dari VPC.
- Menganggap dukungan tunggal; support bersifat kolaboratif Oracle + AWS.

## Latihan
1. Siapa yang mengelola infrastruktur Exadata?
2. Di mana database secara fisik berjalan?

<details><summary>Jawaban</summary>
<p><b>1.</b> OCI (Oracle), sementara pelanggan mengelola database dan konfigurasi.</p>
<p><b>2.</b> Di dalam data center AWS, pada Availability Zone yang dipilih.</p>
</details>
