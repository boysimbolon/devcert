---
title: Operator INTERSECT
minutes: 16
level: Menengah
badge: lengkap
summary: Irisan dua hasil query, dan perlakuan duplikat.
objectives:
  - Memakai INTERSECT
  - Memahami bahwa duplikat dihapus
  - Menggabungkan dengan ORDER BY
---
## Kenapa topik ini diuji
Soal meminta "baris yang muncul di kedua query" — jawabannya INTERSECT.

## Konsep inti
```sql
SELECT department_id FROM employees
INTERSECT
SELECT department_id FROM departments
ORDER BY department_id;
```

Sifat: hanya baris yang ada di **kedua** hasil, dan duplikat dihapus (seperti DISTINCT).

```text
A = {1,2,3,4}   B = {3,4,5}
A INTERSECT B = {3,4}
```

## Jebakan
- INTERSECT menghapus duplikat; tidak ada versi ALL di Oracle.
- NULL dianggap sama pada INTERSECT (berbeda dari `=`).
- Jumlah/tipe kolom harus cocok seperti operasi set lain.
- Bisa digantikan `EXISTS`/join, tetapi INTERSECT lebih jelas maksudnya.

## Latihan
1. Apakah INTERSECT mempertahankan duplikat?
2. Bagaimana NULL diperlakukan?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tidak; hasilnya unik.</p>
<p><b>2.</b> NULL dianggap sama, sehingga baris NULL bisa muncul di irisan.</p>
</details>
