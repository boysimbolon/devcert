---
title: Pengadaan (procurement) Oracle Database@AWS
minutes: 20
level: Menengah
badge: lengkap
summary: Private offer vs public offer, kontrak, dan konsekuensi komersialnya.
objectives:
  - Membedakan private offer dan public offer
  - Menjelaskan alur kontrak
  - Menyebutkan konsekuensi saat kontrak berakhir
---
## Kenapa topik ini diuji
Soal menanyakan cara membeli layanan dan apa yang terjadi saat kontrak berakhir.

## Konsep inti
| Jalur | Cara | Catatan |
|---|---|---|
| Private offer | negosiasi harga/EULA dengan Oracle → Oracle membuat penawaran untuk akun AWS tertentu → diterima di AWS Marketplace | umum untuk komitmen besar/dedicated |
| Public offer | langganan langsung di AWS Marketplace | tersedia untuk ExaDB-XS |

Setelah diterima: aktivasi akun OCI, lalu dashboard Oracle Database@AWS terbuka. Biaya masuk ke tagihan AWS dan dapat dihitung terhadap komitmen AWS; lisensi Oracle tetap berlaku (mis. Oracle Support Rewards).

Saat private offer berakhir: pelanggan otomatis pindah ke harga publik produk atau berhenti berlangganan — perlu perencanaan perpanjangan.

## Jebakan
- Dashboard tidak tersedia sebelum private offer diterima.
- Private offer ditujukan ke **akun AWS tertentu**; akun lain tidak melihatnya.
- Berakhirnya kontrak bisa mengubah biaya secara tiba-tiba.
- Pembelian di AWS tidak menghapus kewajiban lisensi Oracle yang ada.

## Latihan
1. Jalur pembelian yang biasanya butuh negosiasi dengan Oracle?
2. Apa yang terjadi saat private offer kedaluwarsa?

<details><summary>Jawaban</summary>
<p><b>1.</b> Private offer di AWS Marketplace.</p>
<p><b>2.</b> Berpindah otomatis ke harga publik atau berhenti berlangganan.</p>
</details>
