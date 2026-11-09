---
title: Memberikan privilege pada tabel
minutes: 18
level: Menengah
badge: lengkap
summary: GRANT, WITH GRANT OPTION, REVOKE, dan efek berantai.
objectives:
  - Memberikan dan mencabut privilege tabel
  - Menjelaskan WITH GRANT OPTION
  - Memprediksi efek REVOKE berantai
---
## Kenapa topik ini diuji
Soal memberi urutan grant lalu menanyakan siapa yang kehilangan akses setelah revoke.

## Konsep inti
```sql
GRANT SELECT, INSERT ON hr.employees TO app;
GRANT SELECT ON hr.employees TO app WITH GRANT OPTION;   -- app bisa meneruskan
REVOKE INSERT ON hr.employees FROM app;

-- kolom spesifik
GRANT UPDATE (salary) ON hr.employees TO app;
```

Efek berantai: bila A memberi B dengan `GRANT OPTION`, lalu A dicabut, akses B bisa ikut hilang (cascade).

## Jebakan
- `WITH GRANT OPTION` membuat penerima bisa memberi ke pihak lain.
- REVOKE berantai dapat mencabut akses yang diberikan melalui rantai tersebut.
- Privilege kolom tidak bisa digabung dengan SELECT *.
- `GRANT SELECT ON tabel TO PUBLIC` membuka ke semua user.

## Latihan
1. Apa fungsi WITH GRANT OPTION?
2. Apa risiko grant ke PUBLIC?

<details><summary>Jawaban</summary>
<p><b>1.</b> Penerima boleh memberikan privilege itu kepada user lain.</p>
<p><b>2.</b> Semua user mendapat akses tersebut — sangat luas dan sulit dicabut.</p>
</details>
