---
title: Membatasi jumlah baris
minutes: 18
level: Dasar
badge: lengkap
summary: ROWNUM dan FETCH FIRST, serta mengapa keduanya berbeda.
objectives:
  - Memakai FETCH FIRST (12c+)
  - Memakai ROWNUM dengan benar
  - Menghindari jebakan ROWNUM pada ORDER BY
---
## Kenapa topik ini diuji
`ROWNUM` punya perilaku khusus yang sering menjadi jawaban salah.

## Konsep inti
```sql
-- Oracle 12c+
SELECT last_name, salary FROM employees
 ORDER BY salary DESC
 FETCH FIRST 5 ROWS ONLY;

SELECT last_name FROM employees
 ORDER BY salary DESC
 OFFSET 5 ROWS FETCH NEXT 5 ROWS ONLY;

-- klasik
SELECT * FROM (SELECT last_name, salary FROM employees ORDER BY salary DESC)
 WHERE ROWNUM <= 5;
```

`ROWNUM` diberikan **sebelum** `ORDER BY`, sehingga `WHERE ROWNUM <= 5 ORDER BY ...` mengambil 5 baris acak lalu mengurutkannya.

## Jebakan
- `ROWNUM <= 5` dengan ORDER BY di query yang sama = baris salah.
- `ROWNUM = 5` tidak pernah mengembalikan baris (karena baris ke-5 baru diberi nomor setelah 1-4 lolos).
- `FETCH FIRST` butuh `ORDER BY` agar deterministik.
- `OFFSET` tanpa `ORDER BY` tidak stabil.

## Latihan
1. Mengapa `WHERE ROWNUM = 5` kosong?
2. Cara benar mengambil 5 gaji tertinggi?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena ROWNUM diberikan saat baris lolos filter; tidak ada baris yang bisa menjadi nomor 5 tanpa nomor 1-4 lebih dulu.</p>
<p><b>2.</b> Subquery dengan ORDER BY lalu filter ROWNUM di luar, atau <code>ORDER BY ... FETCH FIRST 5 ROWS ONLY</code>.</p>
</details>
