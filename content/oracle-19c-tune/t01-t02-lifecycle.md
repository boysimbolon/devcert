---
title: Fase dalam siklus tuning
minutes: 20
level: Menengah
badge: lengkap
summary: Dari desain sampai operasi berjalan: di mana tuning masih mungkin dan di mana sudah mahal.
objectives:
  - Menyebutkan fase siklus hidup aplikasi
  - Menentukan aktivitas tuning yang tepat per fase
  - Menjelaskan biaya perubahan di fase akhir
---
## Kenapa topik ini diuji
Soal menanyakan pada fase mana masalah tertentu seharusnya diselesaikan.

## Konsep inti
| Fase | Aktivitas tuning |
|---|---|
| Desain | model data, normalisasi, tipe data, partisi |
| Pengembangan | SQL yang baik, index, bind variable, plan stability |
| Pengujian | Real Application Testing, SPA, Database Replay |
| Deployment | parameter, memory, baseline AWR |
| Operasi | ADDM, ASH, SQL Tuning Advisor, SQL Plan Management |

Semakin akhir fase, semakin mahal perbaikannya: mengubah model data setelah produksi bisa berarti migrasi besar.

## Jebakan
- Menunda tuning SQL sampai produksi (biaya tertinggi).
- Mengabaikan baseline saat deployment sehingga tidak ada pembanding.
- Menganggap tuning hanya aktivitas reaktif saat ada insiden.
- Mengubah desain tanpa menguji dengan beban nyata.

## Latihan
1. Fase termurah untuk memperbaiki desain indeks?
2. Mengapa baseline penting di fase deployment?

<details><summary>Jawaban</summary>
<p><b>1.</b> Fase desain/pengembangan.</p>
<p><b>2.</b> Sebagai pembanding obyektif ketika performa berubah setelah perubahan konfigurasi atau aplikasi.</p>
</details>
