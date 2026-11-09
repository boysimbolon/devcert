---
title: Identity and Access Management
minutes: 20
level: Menengah
badge: lengkap
summary: IAM AWS untuk API odb, IAM OCI untuk resource, dan berbagi lintas akun.
objectives:
  - Menjelaskan dua lapis IAM
  - Menyebutkan izin AWS yang diperlukan
  - Memakai AWS RAM untuk berbagi
---
## Kenapa topik ini diuji
Domain keamanan (15%) menguji siapa boleh melakukan apa di dua cloud.

## Konsep inti
| Lapis | Mengatur |
|---|---|
| AWS IAM | akses ke API `odb:` dan konsol AWS; SCP di level organisasi |
| OCI IAM | akses ke resource OCI (infrastruktur, database, backup) |
| AWS RAM | berbagi resource (ODB network/infrastruktur) antar akun |

Praktik: prinsip least privilege, role terpisah untuk admin infrastruktur vs DBA, MFA, dan audit perubahan izin.

## Jebakan
- Izin AWS tidak otomatis memberi izin OCI, dan sebaliknya.
- SCP bisa memblokir aksi meski kebijakan IAM mengizinkan.
- Berbagi resource tanpa meninjau akses di akun penerima.
- Akun root dipakai untuk operasi rutin.

## Latihan
1. Layanan AWS untuk berbagi resource antar akun?
2. Mengapa butuh izin di dua sistem?

<details><summary>Jawaban</summary>
<p><b>1.</b> AWS Resource Access Manager (AWS RAM).</p>
<p><b>2.</b> Karena kontrol permintaan di AWS, sedangkan resource dikelola OCI.</p>
</details>
