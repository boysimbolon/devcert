---
title: Aspek teoretis dan fisik basis data relasional
minutes: 20
level: Dasar
badge: lengkap
summary: Tabel, baris, kolom, kunci, dan bagaimana Oracle menyimpannya secara fisik.
objectives:
  - Menjelaskan model relasional (relasi, tuple, atribut)
  - Membedakan aspek logis dan fisik
  - Menyebutkan objek fisik Oracle
---
## Kenapa topik ini diuji
Soal pembuka menguji istilah: tabel vs segmen, baris vs rowid, kunci primer vs unik.

## Konsep inti
| Teori relasional | Istilah Oracle |
|---|---|
| Relation | table |
| Tuple | row |
| Attribute | column |
| Domain | data type / constraint |
| Primary key | primary key constraint + unique index |

Aspek **logis**: tabel terdiri dari baris dan kolom, tanpa urutan yang dijamin. Aspek **fisik**: Oracle menyimpan baris dalam **blok** di dalam **extent** di dalam **segmen** (satu segmen per tabel), dengan **ROWID** sebagai alamat fisik baris.

```sql
SELECT rowid, employee_id, last_name FROM employees WHERE employee_id = 100;
-- ROWID menunjukkan file, blok, dan slot baris
```

Karena tabel tidak berurutan, hasil query tanpa `ORDER BY` tidak dijamin urutannya.

## Jebakan
- Menganggap baris tersimpan sesuai urutan INSERT.
- Mengira `ROWID` bisa berubah — ia stabil kecuali baris dipindah (mis. `ALTER TABLE ... MOVE`).
- Menyamakan primary key dengan index: constraint-nya logis, index-nya fisik dan dibuat otomatis.
- Menganggap NULL sebagai 0 atau string kosong.

## Latihan
1. Apa padanan "tuple" di Oracle?
2. Mengapa urutan hasil tanpa ORDER BY tidak bisa diandalkan?

<details><summary>Jawaban</summary>
<p><b>1.</b> Baris (row).</p>
<p><b>2.</b> Karena tabel adalah himpunan baris tanpa urutan bawaan; urutan bergantung pada rencana eksekusi.</p>
</details>
