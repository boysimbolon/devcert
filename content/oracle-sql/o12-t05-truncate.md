---
title: TRUNCATE tabel
minutes: 16
level: Dasar
badge: lengkap
summary: Menghapus semua baris secara cepat, tanpa rollback, dengan reset high-water mark.
objectives:
  - Membandingkan TRUNCATE dan DELETE
  - Menjelaskan efek pada index dan storage
  - Mengetahui batasannya
---
## Kenapa topik ini diuji
Soal menanyakan perbedaan DELETE dan TRUNCATE: kecepatan, rollback, dan trigger.

## Konsep inti
```sql
TRUNCATE TABLE emp_copy;
TRUNCATE TABLE emp_copy DROP STORAGE;
TRUNCATE TABLE emp_copy REUSE STORAGE;
```

| Aspek | DELETE | TRUNCATE |
|---|---|---|
| Jenis | DML | DDL |
| Rollback | bisa | tidak |
| Trigger | jalan | tidak jalan |
| WHERE | bisa | tidak bisa |
| Kecepatan | per baris | sangat cepat |
| High-water mark | tetap | direset |

## Jebakan
- TRUNCATE memicu commit implisit.
- Tidak bisa dipakai bila ada foreign key yang mereferensikan tabel (tanpa CASCADE).
- Tidak menjalankan trigger DELETE.
- Hak yang dibutuhkan berbeda dari DELETE.

## Latihan
1. Bisakah TRUNCATE dibatasi dengan WHERE?
2. Apakah trigger DELETE jalan pada TRUNCATE?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tidak.</p>
<p><b>2.</b> Tidak; TRUNCATE tidak memicu trigger DML.</p>
</details>
