---
title: Tipe data INTERVAL
minutes: 20
level: Menengah
badge: lengkap
summary: INTERVAL YEAR TO MONTH dan DAY TO SECOND, serta aritmatika tanggal.
objectives:
  - Menulis literal interval
  - Menambah/mengurangi interval dari tanggal
  - Membedakan dua jenis interval
---
## Kenapa topik ini diuji
Soal memberi ekspresi dengan interval dan menanyakan hasil atau tipenya.

## Konsep inti
```sql
SELECT SYSDATE + INTERVAL '3' MONTH   AS plus3m,
       SYSDATE + INTERVAL '10' DAY    AS plus10d,
       SYSDATE + INTERVAL '2 03:30:00' DAY TO SECOND AS plus2d3h
  FROM dual;

SELECT INTERVAL '1-6' YEAR TO MONTH AS satu_setengah_tahun FROM dual;

SELECT INTERVAL '90' MINUTE AS sembilan_puluh_menit FROM dual;

SELECT hire_date,
       (SYSDATE - hire_date) DAY TO SECOND AS selisih
  FROM employees;
```

| Tipe | Menyimpan |
|---|---|
| `INTERVAL YEAR TO MONTH` | tahun dan bulan |
| `INTERVAL DAY TO SECOND` | hari, jam, menit, detik |

## Jebakan
- `INTERVAL '1' YEAR` dan `INTERVAL '12' MONTH` setara, tetapi tipe hasil bisa berbeda.
- Aritmatika dua DATE menghasilkan NUMBER, bukan INTERVAL; perlu CAST.
- Format literal salah → ORA-01867.
- Interval bisa negatif.

## Latihan
1. Tipe interval untuk 2 tahun 6 bulan?
2. Bagaimana menambahkan 90 menit ke tanggal?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>INTERVAL YEAR TO MONTH</code> (mis. <code>INTERVAL '2-6' YEAR TO MONTH</code>).</p>
<p><b>2.</b> <code>tanggal + INTERVAL '90' MINUTE</code> (atau <code>+ 90/1440</code>).</p>
</details>
