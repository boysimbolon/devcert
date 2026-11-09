---
title: UNION dan UNION ALL
minutes: 18
level: Menengah
badge: lengkap
summary: Menggabungkan hasil, menghapus duplikat atau tidak, dan dampak performa.
objectives:
  - Membedakan UNION dan UNION ALL
  - Menjelaskan biaya penghapusan duplikat
  - Memilih operator sesuai kebutuhan
---
## Kenapa topik ini diuji
Soal menanyakan jumlah baris hasil, yang berbeda antara UNION dan UNION ALL.

## Konsep inti
```sql
SELECT department_id FROM employees
UNION
SELECT department_id FROM departments;

SELECT department_id FROM employees
UNION ALL
SELECT department_id FROM departments;
```

| Operator | Duplikat | Biaya |
|---|---|---|
| `UNION` | dihapus (sort/hash) | lebih mahal |
| `UNION ALL` | dipertahankan | lebih murah |

Gunakan `UNION ALL` bila duplikat memang tidak mungkin atau tidak masalah — hampir selalu lebih cepat.

## Jebakan
- Mengira UNION ALL lebih lambat; justru sebaliknya.
- UNION menghapus duplikat termasuk antar-SELECT, bukan hanya dalam satu SELECT.
- Jumlah/tipe kolom harus sama.
- `ORDER BY` hanya di akhir.

## Latihan
1. Operator mana yang lebih cepat dan mengapa?
2. Apakah UNION menghapus duplikat dalam satu SELECT juga?

<details><summary>Jawaban</summary>
<p><b>1.</b> UNION ALL, karena tidak perlu mengurutkan/menghapus duplikat.</p>
<p><b>2.</b> Ya, hasil akhirnya unik secara keseluruhan.</p>
</details>
