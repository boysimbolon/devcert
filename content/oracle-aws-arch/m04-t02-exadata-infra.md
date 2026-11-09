---
title: Provisioning Exadata infrastructure dan VM cluster
minutes: 22
level: Menengah
badge: lengkap
summary: Exadata infrastructure, Exadata VM cluster, dan Autonomous VM cluster.
objectives:
  - Menjelaskan urutan provisioning
  - Membedakan Exadata VM cluster dan Autonomous VM cluster
  - Menentukan ukuran awal
---
## Kenapa topik ini diuji
Soal menanyakan urutan objek: infrastruktur → cluster → database.

## Konsep inti
```text
ODB network
  └─ Exadata infrastructure (kapasitas fisik: shape, storage)
       ├─ Exadata VM cluster         (untuk Exadata Database Service)
       └─ Autonomous VM cluster      (untuk Autonomous Database dedicated)
            └─ database / ACDB
```

Poin uji:

- Infrastruktur dibuat di konsol AWS; database dibuat dengan alat OCI.
- Satu infrastructure dapat menampung beberapa VM cluster (tergantung kapasitas/shape).
- **Autonomous VM cluster** dipakai untuk Autonomous Database on Dedicated Exadata Infrastructure.
- Untuk ExaDB-XS, komponennya **Exascale storage vault** + **Exascale VM cluster** (bukan infrastruktur dedicated klasik).

## Jebakan
- Membuat VM cluster sebelum infrastruktur tersedia.
- Menyamakan Autonomous VM cluster dengan Exadata VM cluster.
- Kapasitas infrastructure menentukan jumlah cluster; tidak bisa ditambah tanpa ekspansi.
- Patching mengikuti jadwal OCI; perlu perencanaan downtime.

## Latihan
1. Objek yang dibuat sebelum VM cluster?
2. VM cluster mana untuk Autonomous Database dedicated?

<details><summary>Jawaban</summary>
<p><b>1.</b> ODB network dan Exadata infrastructure.</p>
<p><b>2.</b> Autonomous VM cluster.</p>
</details>
