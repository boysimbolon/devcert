---
title: Monitoring dan observability
minutes: 20
level: Menengah
badge: lengkap
summary: CloudWatch, EventBridge, CloudTrail, dan alat OCI untuk database.
objectives:
  - Menyebutkan alat monitoring yang tersedia
  - Menentukan metrik yang penting
  - Menggabungkan monitoring AWS dan OCI
---
## Kenapa topik ini diuji
Soal menanyakan layanan AWS mana untuk metrik, event, dan audit API.

## Konsep inti
| Kebutuhan | Alat |
|---|---|
| Metrik & alarm | Amazon CloudWatch |
| Event/otomatisasi | Amazon EventBridge |
| Audit panggilan API | AWS CloudTrail |
| Performa database (AWR, ASH, SQL) | OCI Database Management / alat Oracle |

Praktik: alarm pada CPU/storage/latensi/koneksi, dashboard per aplikasi, dan korelasi event AWS dengan metrik database.

## Jebakan
- CloudWatch tidak menggantikan AWR/ASH untuk tuning SQL.
- CloudTrail mencatat API, bukan query SQL.
- Metrik tanpa baseline sulit ditafsirkan.
- EventBridge hanya bereaksi pada event; butuh aturan yang dirancang.

## Latihan
1. Alat untuk alarm metrik?
2. Alat untuk audit pemanggilan API?

<details><summary>Jawaban</summary>
<p><b>1.</b> Amazon CloudWatch.</p>
<p><b>2.</b> AWS CloudTrail.</p>
</details>
