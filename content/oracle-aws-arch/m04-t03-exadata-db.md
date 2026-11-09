---
title: Membuat Exadata Database dan komponennya
minutes: 20
level: Menengah
badge: lengkap
summary: CDB, PDB, koneksi, dan langkah setelah provisioning.
objectives:
  - Membuat database pada VM cluster
  - Menjelaskan CDB/PDB dalam konteks ini
  - Menyiapkan koneksi aplikasi
---
## Kenapa topik ini diuji
Soal praktis: apa yang dibuat via OCI vs AWS, dan bagaimana aplikasi terhubung.

## Konsep inti
```text
Exadata VM cluster
  └─ CDB (database)
       ├─ PDB1 (aplikasi A)
       └─ PDB2 (aplikasi B)
```

Langkah konseptual:

```text
1. Buat database (CDB) pada VM cluster via OCI
2. Tentukan nama, versi, karakter set, TDE (wajib di cloud)
3. Buat PDB untuk tiap aplikasi
4. Siapkan TNS/service name, buka akses jaringan
5. Uji koneksi dari instance di VPC
```

## Jebakan
- TDE tidak bisa dimatikan pada layanan cloud Oracle; siapkan wallet/keystore.
- Satu CDB dengan banyak PDB memudahkan konsolidasi, tetapi berbagi resource.
- Karakter set tidak bisa diubah setelah dibuat.
- Nama service/TNS harus cocok dengan DNS yang dikonfigurasi.

## Latihan
1. Objek untuk memisahkan aplikasi dalam satu CDB?
2. Enkripsi apa yang wajib pada database cloud Oracle?

<details><summary>Jawaban</summary>
<p><b>1.</b> PDB (pluggable database).</p>
<p><b>2.</b> Transparent Data Encryption (TDE) untuk data at rest.</p>
</details>
