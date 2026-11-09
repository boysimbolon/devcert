---
title: NVL, NULLIF, dan COALESCE
minutes: 18
level: Dasar
badge: lengkap
summary: Mengganti NULL, membandingkan nilai, dan memilih nilai pertama yang tidak NULL.
objectives:
  - Memakai NVL dan NVL2
  - Menjelaskan NULLIF
  - Memilih COALESCE untuk banyak argumen
---
## Kenapa topik ini diuji
Tiga fungsi ini muncul berulang, dan perbedaannya halus.

## Konsep inti
```sql
SELECT NVL(commission_pct, 0)          AS komisi,
       NVL2(commission_pct, 'ada', 'tidak') AS status,
       NULLIF(10, 10)                  AS n1,   -- NULL
       NULLIF(10, 20)                  AS n2,   -- 10
       COALESCE(NULL, NULL, 'x', 'y')  AS c     -- 'x'
  FROM employees;
```

| Fungsi | Perilaku |
|---|---|
| `NVL(a,b)` | b bila a NULL; 2 argumen saja |
| `NVL2(a,b,c)` | b bila a tidak NULL, c bila NULL |
| `NULLIF(a,b)` | NULL bila a = b, selain itu a |
| `COALESCE(a,b,c,...)` | nilai tidak NULL pertama |

Tipe data harus kompatibel; `NVL(number, 'teks')` memicu konversi implisit.

## Jebakan
- `NVL` hanya dua argumen; untuk banyak gunakan `COALESCE`.
- `NULLIF` berguna mencegah pembagian nol: `x / NULLIF(y,0)`.
- `COALESCE` mengevaluasi argumen berurutan dan berhenti di yang pertama tidak NULL.
- Tipe hasil `COALESCE` mengikuti aturan presedensi tipe.

## Latihan
1. Fungsi untuk mencegah pembagian nol?
2. Bedakan NVL dan COALESCE.

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>NULLIF(pembagi, 0)</code>.</p>
<p><b>2.</b> NVL hanya dua argumen; COALESCE menerima banyak dan mengembalikan yang pertama tidak NULL.</p>
</details>
