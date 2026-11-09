---
title: Layanan database di Oracle Database@AWS
minutes: 22
level: Menengah
badge: lengkap
summary: Exadata Database Service, ExaDB-XS, dan Autonomous Database Serverless.
objectives:
  - Membedakan tiga opsi layanan
  - Memilih opsi sesuai kebutuhan
  - Menjelaskan komponen yang harus dibuat per opsi
---
## Kenapa topik ini diuji
Soal skenario hampir selalu berpangkal pada "layanan mana yang tepat".

## Konsep inti
| Layanan | Ciri | Yang harus dibuat |
|---|---|---|
| Exadata Database Service on Dedicated Infrastructure | Exadata dedicated, kontrol penuh | ODB network → Exadata infrastructure → Exadata VM cluster → database (via OCI) |
| ExaDB-XS (Exadata Database Service on Exascale) | elastis, mulai 8 ECPUs & 300 GB, bayar sesuai pakai | ODB network → Exascale storage vault → Exascale VM cluster → database |
| Autonomous Database Serverless (ADB-S) | tanpa infrastruktur, auto-scale | ODB network → Autonomous Database langsung |

Semua berjalan pada infrastruktur Oracle yang dikelola OCI di dalam AWS; aplikasi mengakses lewat ODB peering dari VPC.

## Jebakan
- ADB-S tidak memerlukan Exadata infrastructure atau VM cluster — sering jadi jebakan soal.
- ExaDB-XS cocok untuk mulai kecil; dedicated Exadata untuk kebutuhan penuh/kontrol maksimal.
- Layanan dedicated memerlukan kapasitas terpasang, bukan elastis per detik.
- Fitur yang tersedia berbeda antar layanan (mis. kontrol parameter, patching).

## Latihan
1. Layanan tanpa provisioning infrastruktur?
2. Komponen khas ExaDB-XS sebelum database dibuat?

<details><summary>Jawaban</summary>
<p><b>1.</b> Autonomous Database Serverless (ADB-S).</p>
<p><b>2.</b> Exascale storage vault dan Exascale VM cluster.</p>
</details>
