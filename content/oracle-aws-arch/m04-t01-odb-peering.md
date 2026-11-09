---
title: Membuat ODB network dan ODB peering
minutes: 22
level: Menengah
badge: lengkap
summary: Membuat koneksi privat VPC ↔ ODB network, peer CIDR, dan rute.
objectives:
  - Membuat ODB peering
  - Menentukan peer network CIDR
  - Memilih manajemen rute implisit atau manual
---
## Kenapa topik ini diuji
Domain 20% provisioning: soal menanyakan langkah wajib setelah peering dibuat.

## Konsep inti
ODB peering = koneksi yang dibuat user agar trafik VPC dan ODB network dirutekan secara privat.

```text
Langkah:
1. Buat ODB network (pilih AZ, CIDR)
2. Buat ODB peering ke VPC (same-account atau cross-account)
3. Tentukan peer network CIDR (rute yang diterima ODB network)
4. Perbarui route table VPC (atau pakai implicit route management)
5. Konfigurasi DNS, lalu uji koneksi
```

Detail yang diuji:

- Peer network CIDR bisa dari `/0` sampai `/32`, termasuk supernet; **longest-prefix match** berlaku.
- Default route `0.0.0.0/0` pada peering **bukan** berarti ODB network menjadi default gateway VPC.
- Setiap peering adalah resource terpisah yang bisa dibuat/dihapus sendiri.
- Maksimum 125 peering per ODB network.

## Jebakan
- Lupa route table → trafik tidak sampai walau peering "Available".
- Peer CIDR terlalu sempit sehingga subnet aplikasi tidak tercakup.
- Cross-account peering butuh izin/berbagi resource (AWS RAM) di sisi yang tepat.
- Menghapus peering memutus semua database di belakangnya.

## Latihan
1. Apa dua hal yang harus diperbarui setelah membuat peering?
2. Apa arti longest-prefix match pada peer CIDR?

<details><summary>Jawaban</summary>
<p><b>1.</b> Route table VPC dan konfigurasi DNS.</p>
<p><b>2.</b> Rute paling spesifik yang menang; supernet hanya menangani trafik yang tidak ditangani rute lebih spesifik.</p>
</details>
