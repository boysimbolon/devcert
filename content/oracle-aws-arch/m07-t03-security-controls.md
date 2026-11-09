---
title: Kontrol keamanan
minutes: 20
level: Menengah
badge: lengkap
summary: Isolasi jaringan, audit, patching, dan pemisahan tugas.
objectives:
  - Menyebutkan kontrol keamanan utama
  - Menerapkan isolasi jaringan
  - Merancang audit perubahan
---
## Kenapa topik ini diuji
Soal menanyakan kontrol mana untuk risiko tertentu.

## Konsep inti
| Risiko | Kontrol |
|---|---|
| Akses tidak sah dari internet | ODB network privat + peering, tanpa endpoint publik |
| Perubahan konfigurasi tak terlacak | CloudTrail, audit database |
| Celah versi | patching terjadwal (dikelola OCI) |
| Penyalahgunaan hak | least privilege, pemisahan tugas, MFA |
| Data sensitif terlihat | Data Safe masking/audit, view terbatas |

## Jebakan
- Mengandalkan security group saja tanpa memeriksa rute dan peering.
- Audit aktif tetapi tidak ditinjau.
- Satu akun admin untuk semua fungsi.
- Patching tanpa jendela uji.

## Latihan
1. Kontrol untuk melacak perubahan API?
2. Kontrol untuk mengurangi risiko penyalahgunaan hak?

<details><summary>Jawaban</summary>
<p><b>1.</b> AWS CloudTrail (plus audit database untuk aktivitas SQL).</p>
<p><b>2.</b> Least privilege, pemisahan tugas, dan MFA.</p>
</details>
