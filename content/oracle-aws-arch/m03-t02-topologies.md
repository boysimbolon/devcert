---
title: Topologi jaringan yang didukung
minutes: 22
level: Menengah
badge: lengkap
summary: Satu VPC, banyak VPC, Transit Gateway, dan AWS Cloud WAN.
objectives:
  - Memilih topologi sesuai jumlah VPC/akun
  - Menjelaskan peran Transit Gateway
  - Mengenali batasan tiap topologi
---
## Kenapa topik ini diuji
Soal desain memberi jumlah akun/VPC dan menanyakan topologi yang tepat.

## Konsep inti
| Topologi | Kapan dipakai |
|---|---|
| Peering langsung VPC ↔ ODB network | satu/beberapa VPC sederhana |
| Banyak VPC via Transit Gateway | hub-and-spoke, banyak akun |
| AWS Cloud WAN | jaringan global banyak region/akun |
| Cross-account peering | ODB network di akun A, VPC di akun B |

Catatan penting: peering bersifat **non-transitif**. Untuk banyak VPC, rute harus lewat Transit Gateway atau VPC routing yang dirancang khusus.

```text
VPC-A ─┐
VPC-B ─┼─ TGW ── ODB peering ── ODB network
VPC-C ─┘
```

## Jebakan
- Menganggap peering VPC-A→ODB otomatis membuka VPC-B.
- Overlapping CIDR memaksa NAT/redesign.
- Transit Gateway menambah hop dan biaya.
- Cloud WAN memerlukan kebijakan jaringan global; tidak otomatis.

## Latihan
1. Topologi untuk 20 VPC di 6 akun?
2. Mengapa peering langsung tidak cukup untuk banyak VPC?

<details><summary>Jawaban</summary>
<p><b>1.</b> Transit Gateway (atau Cloud WAN jika lintas region).</p>
<p><b>2.</b> Karena peering tidak transitif; tiap VPC butuh koneksi/rute sendiri.</p>
</details>
