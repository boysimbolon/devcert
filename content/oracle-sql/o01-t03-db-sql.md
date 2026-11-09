---
title: Hubungan basis data dan SQL
minutes: 18
level: Dasar
badge: lengkap
summary: Peran SQL sebagai bahasa non-prosedural, kategori perintah, dan objek DUAL.
objectives:
  - Menyebutkan kategori perintah SQL
  - Menjelaskan sifat non-prosedural
  - Memakai DUAL untuk ekspresi
---
## Kenapa topik ini diuji
Soal dasar memastikan kamu tahu SQL menyatakan **apa**, bukan **bagaimana**, dan kapan DUAL dipakai.

## Konsep inti
Kategori:

| Kategori | Perintah |
|---|---|
| DML | SELECT, INSERT, UPDATE, DELETE, MERGE |
| DDL | CREATE, ALTER, DROP, TRUNCATE, RENAME |
| DCL | GRANT, REVOKE |
| TCL | COMMIT, ROLLBACK, SAVEPOINT |

SQL bersifat **non-prosedural**: kamu menyebut hasil yang diinginkan, optimizer memilih cara. Ini sebabnya rencana eksekusi bisa berubah walau query sama.

```sql
SELECT 2 + 3 AS hasil FROM dual;
SELECT SYSDATE FROM dual;
SELECT 'Halo' || ' ' || 'Dunia' AS salam FROM dual;
```

`DUAL` adalah tabel satu baris satu kolom milik `SYS`, dipakai untuk ekspresi yang tidak butuh tabel.

## Jebakan
- `SELECT 2+3;` tanpa `FROM dual` gagal di Oracle.
- DDL memicu commit implisit dan tidak bisa di-rollback.
- `TRUNCATE` adalah DDL, bukan DML.
- SQL tidak menjamin urutan tanpa `ORDER BY`.

## Latihan
1. Kategori perintah untuk GRANT?
2. Mengapa SELECT tanpa FROM gagal?

<details><summary>Jawaban</summary>
<p><b>1.</b> DCL (Data Control Language).</p>
<p><b>2.</b> Oracle mensyaratkan klausa FROM; gunakan <code>FROM dual</code> untuk ekspresi.</p>
</details>
