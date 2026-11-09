---
title: Aturan presedensi operator
minutes: 18
level: Dasar
badge: lengkap
summary: Urutan evaluasi aritmatika, perbandingan, dan logika.
objectives:
  - Menyebutkan urutan presedensi operator
  - Memakai tanda kurung untuk kejelasan
  - Menghindari kesalahan logika AND/OR
---
## Kenapa topik ini diuji
Soal memberi ekspresi tanpa tanda kurung dan menanyakan hasil atau baris yang lolos.

## Konsep inti
Urutan (tinggi ke rendah):

```text
1. Operator aritmatika: * / , lalu + -
2. Konkatenasi: ||
3. Perbandingan: = <> < > <= >=
4. IS [NOT] NULL, LIKE, BETWEEN, IN
5. NOT
6. AND
7. OR
```

```sql
SELECT 2 + 3 * 4 FROM dual;        -- 14
SELECT (2 + 3) * 4 FROM dual;      -- 20

-- AND lebih kuat dari OR
WHERE dept = 10 OR dept = 20 AND salary > 5000
-- dibaca: dept=10 OR (dept=20 AND salary>5000)
```

## Jebakan
- Menganggap AND/OR setara; AND dievaluasi lebih dulu.
- Lupa bahwa `NOT` mengikat lebih kuat dari `AND`.
- Perbandingan string memperhatikan collation dan case.
- `BETWEEN` bersifat inklusif di kedua ujung.

## Latihan
1. Hasil `2 + 3 * 4`?
2. Bagaimana memaksa urutan logika yang berbeda?

<details><summary>Jawaban</summary>
<p><b>1.</b> 14 (perkalian lebih dulu).</p>
<p><b>2.</b> Dengan tanda kurung: <code>(a OR b) AND c</code>.</p>
</details>
