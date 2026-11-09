---
title: Aritmatika pada data tanggal
minutes: 20
level: Dasar
badge: lengkap
summary: Tanggal dikurangi tanggal jadi jumlah hari, dan penambahan hari/pecahan hari.
objectives:
  - Menghitung selisih dua tanggal
  - Menambah/mengurangi hari dan jam
  - Membedakan DATE dan TIMESTAMP dalam aritmatika
---
## Kenapa topik ini diuji
Soal aritmatika tanggal hampir selalu muncul, termasuk hasil pecahan hari.

## Konsep inti
```sql
SELECT SYSDATE, SYSDATE + 1 AS besok, SYSDATE - 7 AS seminggu_lalu FROM dual;

SELECT hire_date, ROUND(SYSDATE - hire_date) AS hari_kerja FROM employees;

-- menambah jam: 1 hari = 1, jadi 12 jam = 0.5
SELECT SYSDATE + 12/24 AS dua_belas_jam FROM dual;

SELECT MONTHS_BETWEEN(SYSDATE, hire_date) AS bulan FROM employees;
SELECT ADD_MONTHS(hire_date, 3) FROM employees;
SELECT NEXT_DAY(SYSDATE, 'SENIN') FROM dual;
```

Aturan: `date + number` = tanggal + hari; `date - date` = jumlah hari (bisa desimal).

## Jebakan
- Menjumlahkan dua tanggal tidak bermakna dan menghasilkan error.
- Hasil `date - date` bisa pecahan; gunakan `ROUND`/`TRUNC` bila butuh hari bulat.
- `MONTHS_BETWEEN` bisa negatif/pecahan; tidak membulatkan otomatis.
- `SYSDATE` mengikuti zona waktu server, bukan klien.

## Latihan
1. Hasil `SYSDATE - hire_date`?
2. Bagaimana menambah 6 jam ke sebuah tanggal?

<details><summary>Jawaban</summary>
<p><b>1.</b> Jumlah hari (bisa pecahan) antara kedua tanggal.</p>
<p><b>2.</b> <code>tanggal + 6/24</code>.</p>
</details>
