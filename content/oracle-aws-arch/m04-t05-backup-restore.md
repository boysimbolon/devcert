---
title: Backup dan restore Oracle Database@AWS
minutes: 20
level: Menengah
badge: lengkap
summary: RMAN, backup otomatis ADB, penyimpanan di Amazon S3, dan uji restore.
objectives:
  - Menjelaskan opsi backup
  - Menentukan tujuan penyimpanan backup
  - Merencanakan uji restore
---
## Kenapa topik ini diuji
Soal menanyakan ke mana backup disimpan dan siapa yang mengelolanya.

## Konsep inti
| Layanan | Backup |
|---|---|
| Exadata Database Service | RMAN (ke S3/OCI Object Storage), kebijakan otomatis tersedia |
| Autonomous Database | otomatis (retensi dapat diatur) + backup manual sesuai kebutuhan |

Backup dapat diarahkan ke **Amazon S3** yang dirancang untuk durabilitas sangat tinggi; akses dari ODB network dapat memakai integrasi AWS (mis. VPC Lattice) tanpa keluar lewat internet publik.

Prinsip: backup ≠ DR. Uji restore berkala, dan simpan salinan di lokasi/akun berbeda.

## Jebakan
- Backup ada tetapi restore belum pernah diuji.
- Retensi terlalu pendek untuk kebutuhan audit/PITR.
- Backup lintas region memerlukan konfigurasi tambahan.
- Enkripsi backup harus dikelola bersama kunci (kehilangan kunci = backup tidak berguna).

## Latihan
1. Layanan penyimpanan AWS yang umum untuk backup?
2. Mengapa uji restore wajib?

<details><summary>Jawaban</summary>
<p><b>1.</b> Amazon S3.</p>
<p><b>2.</b> Karena backup yang tidak pernah direstore belum terbukti dapat dipulihkan.</p>
</details>
