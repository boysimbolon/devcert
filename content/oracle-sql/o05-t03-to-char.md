---
title: TO_CHAR, TO_NUMBER, dan TO_DATE
minutes: 22
level: Menengah
badge: lengkap
summary: Format model untuk tanggal dan angka, serta konversi balik.
objectives:
  - Memakai format model tanggal dan angka
  - Mengonversi string ke tanggal/angka
  - Menghindari format yang salah
---
## Kenapa topik ini diuji
Soal sering meminta keluaran dengan format tertentu — jawabannya bergantung pada format model.

## Konsep inti
```sql
SELECT TO_CHAR(SYSDATE, 'DD-MON-YYYY HH24:MI:SS') AS tgl FROM dual;
SELECT TO_CHAR(SYSDATE, 'Day, DD "of" Month YYYY') FROM dual;

SELECT TO_CHAR(1234567.891, '9,999,999.99') AS n1,
       TO_CHAR(0.25, '0.00%')              AS n2,
       TO_CHAR(-1234, 'S9999')             AS n3
  FROM dual;

SELECT TO_DATE('15-03-2026','DD-MM-YYYY') FROM dual;
SELECT TO_NUMBER('1,234.56','9,999.99')   FROM dual;
```

Elemen format penting: `YYYY`, `MM`, `MON`, `DD`, `HH24`, `MI`, `SS`, `DAY`, `9`, `0`, `,`, `.`, `$`, `FM` (menghapus spasi).

## Jebakan
- `YYYY` vs `RRRR` (RRRR lebih aman untuk abad).
- `MI` = menit; `MM` = bulan.
- Format model harus cocok dengan string; kelebihan/kekurangan elemen → ORA-01861/ORA-01722.
- `TO_CHAR` pada kolom tanggal di WHERE menghalangi index.

## Latihan
1. Elemen untuk jam 24-jam dan menit?
2. Mengapa `TO_CHAR(kolom_tanggal) = '2026'` buruk untuk performa?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>HH24</code> dan <code>MI</code>.</p>
<p><b>2.</b> Karena fungsi diterapkan pada kolom sehingga index tanggal tidak dipakai; bandingkan dengan rentang tanggal.</p>
</details>
