---
title: Desain ODB network
minutes: 22
level: Menengah
badge: lengkap
summary: Jaringan privat tempat infrastruktur Exadata berada, subnet, dan peering ke VPC.
objectives:
  - Menjelaskan fungsi ODB network
  - Merencanakan CIDR dan subnet
  - Menentukan kapan memakai beberapa ODB network
---
## Kenapa topik ini diuji
Domain networking (15%) menguji perencanaan CIDR dan konsekuensi desain jaringan.

## Konsep inti
**ODB network** adalah jaringan privat khusus dalam satu Availability Zone tempat Exadata infrastructure berada. Aplikasi di VPC menjangkaunya lewat **ODB peering**.

Pertimbangan desain:

```text
- Pilih AZ sesuai aplikasi (latensi)
- Rencanakan CIDR ODB network & subnet, hindari tumpang tindih dengan VPC
- Tentukan peer network CIDR (rute yang diizinkan masuk)
- Satu ODB network dapat di-peer ke banyak VPC (hingga 125 koneksi peering)
- Pisahkan ODB network per lingkungan bila butuh isolasi (dev/test/prod)
```

## Jebakan
- CIDR bertumpang tindih dengan VPC → tidak bisa di-peer tanpa redesign.
- ODB network bersifat per-AZ; aplikasi lintas AZ butuh desain tambahan.
- Peering bukan transit otomatis; butuh rute dan (bila perlu) Transit Gateway.
- Menambah ODB network menambah kompleksitas operasional, bukan otomatis lebih aman.

## Latihan
1. Apa itu ODB network?
2. Berapa banyak koneksi peering yang didukung per ODB network?

<details><summary>Jawaban</summary>
<p><b>1.</b> Jaringan privat dalam satu AZ tempat infrastruktur Exadata berjalan, yang di-peer ke VPC.</p>
<p><b>2.</b> Hingga 125 koneksi ODB peering.</p>
</details>
