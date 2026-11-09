---
title: Autonomous Container Database dan Autonomous Database
minutes: 20
level: Menengah
badge: lengkap
summary: ACDB sebagai wadah, ADB sebagai database, dan pilihan serverless vs dedicated.
objectives:
  - Menjelaskan hubungan ACDB dan ADB
  - Membedakan ADB serverless dan dedicated
  - Menentukan kapan memakai masing-masing
---
## Kenapa topik ini diuji
Soal menanyakan objek mana yang dibuat lebih dulu pada Autonomous Database.

## Konsep inti
```text
Autonomous VM cluster
  └─ ACDB (Autonomous Container Database)
       ├─ ADB 1
       └─ ADB 2
```

| Opsi | Infrastruktur | Catatan |
|---|---|---|
| ADB Serverless (ADB-S) | tidak perlu VM cluster | dibuat langsung setelah ODB network |
| ADB on Dedicated | Autonomous VM cluster + ACDB | kontrol lebih, kapasitas terjamin |

ADB menangani patching, tuning, dan backup otomatis; pengguna fokus pada skema dan workload.

## Jebakan
- ADB-S tidak memerlukan ACDB; ADB dedicated memerlukan ACDB.
- Satu ACDB dapat menampung beberapa ADB, berbagi resource.
- Mengubah opsi (serverless ↔ dedicated) bukan migrasi sepele.
- Fitur yang bisa diubah pada ADB lebih terbatas dibanding Exadata Database Service.

## Latihan
1. Objek sebelum ADB pada dedicated?
2. Apakah ADB-S memerlukan Autonomous VM cluster?

<details><summary>Jawaban</summary>
<p><b>1.</b> Autonomous VM cluster, lalu ACDB.</p>
<p><b>2.</b> Tidak.</p>
</details>
