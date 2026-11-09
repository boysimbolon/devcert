---
title: Konfigurasi DNS untuk Oracle Database@AWS
minutes: 20
level: Menengah
badge: lengkap
summary: Route 53, resolusi nama dari VPC ke ODB network, dan kesalahan umum.
objectives:
  - Menjelaskan peran DNS pada koneksi VPC → database
  - Mengonfigurasi resolusi setelah peering
  - Mendiagnosis nama yang tidak resolve
---
## Kenapa topik ini diuji
Koneksi jaringan bisa benar tetapi aplikasi tetap gagal karena DNS; soal sering menanyakan langkah tambahan setelah peering.

## Konsep inti
Setelah ODB peering dibuat, **resolusi DNS harus dikonfigurasi** agar nama host database dapat di-resolve dari VPC. Amazon Route 53 dipakai sebagai layanan DNS.

Langkah konseptual:

```text
1. Buat ODB peering (VPC <-> ODB network)
2. Pastikan route table VPC mengarah ke peering
3. Konfigurasi DNS: zona/privat resolver untuk nama database
4. Uji dengan nslookup/dig dari instance di VPC
5. Uji koneksi (mis. tnsping / sqlplus)
```

## Jebakan
- Peering aktif tanpa DNS → nama tidak resolve, koneksi gagal.
- Perubahan DNS butuh waktu propagasi/cache.
- Menggunakan IP langsung menghindari DNS tetapi rapuh saat failover.
- Resolver privat per-VPC harus di-attach dengan benar.

## Latihan
1. Langkah jaringan yang sering terlupa setelah peering?
2. Layanan DNS AWS yang dipakai?

<details><summary>Jawaban</summary>
<p><b>1.</b> Konfigurasi resolusi DNS untuk nama database.</p>
<p><b>2.</b> Amazon Route 53.</p>
</details>
