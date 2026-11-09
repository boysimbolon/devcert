---
title: Menumpuk beberapa fungsi
minutes: 18
level: Menengah
badge: lengkap
summary: Evaluasi dari dalam ke luar, tipe hasil antara, dan kesalahan umum.
objectives:
  - Menulis fungsi bertumpuk dengan benar
  - Menentukan tipe hasil antara
  - Menghindari konflik tipe
---
## Kenapa topik ini diuji
Soal memberi ekspresi bertumpuk dan menanyakan hasil akhir; kesalahan biasanya pada tipe antara.

## Konsep inti
```sql
SELECT UPPER(SUBSTR(last_name, 1, 3)) AS inisial FROM employees;

SELECT TO_CHAR(ADD_MONTHS(hire_date, 6), 'DD-MON-YYYY') AS tgl FROM employees;

SELECT ROUND(NVL(commission_pct, 0) * salary, 2) AS komisi FROM employees;

SELECT NVL(TO_CHAR(manager_id), 'TIDAK ADA') FROM employees;
```

Aturan: evaluasi **dalam ke luar**; tipe hasil fungsi dalam menentukan fungsi luar.

## Jebakan
- `NVL(number, 'teks')` memaksa konversi implisit yang bisa gagal.
- `TO_CHAR(NULL)` menghasilkan NULL, bukan string kosong.
- Menumpuk `TO_DATE(TO_CHAR(...))` biasanya tidak perlu dan bisa mengubah nilai.
- Fungsi pada kolom di WHERE menghalangi index.

## Latihan
1. Urutan evaluasi `UPPER(SUBSTR(x,1,3))`?
2. Mengapa `NVL(nomor, 'TIDAK ADA')` bermasalah?

<details><summary>Jawaban</summary>
<p><b>1.</b> SUBSTR lebih dulu, hasilnya diteruskan ke UPPER.</p>
<p><b>2.</b> Karena tipe argumen harus kompatibel; number dan string memicu konversi implisit yang bisa error (ORA-01722).</p>
</details>
