---
title: Menghapus kolom dan menandai UNUSED
minutes: 18
level: Menengah
badge: lengkap
summary: DROP COLUMN, SET UNUSED, dan kapan memilih yang mana.
objectives:
  - Menghapus kolom secara langsung
  - Menandai kolom sebagai UNUSED
  - Menghapus kolom UNUSED
---
## Kenapa topik ini diuji
`SET UNUSED` adalah fitur khas Oracle dan sering muncul di soal DDL.

## Konsep inti
```sql
ALTER TABLE employees DROP COLUMN commission_pct;
ALTER TABLE employees SET UNUSED COLUMN commission_pct;
ALTER TABLE employees DROP UNUSED COLUMNS;

SELECT column_name FROM user_tab_columns WHERE table_name='EMPLOYEES';
SELECT * FROM user_unused_col_tabs;
```

Perbedaan:

| Aksi | Efek | Waktu |
|---|---|---|
| `DROP COLUMN` | menghapus data & metadata segera | bisa lama pada tabel besar |
| `SET UNUSED` | menonaktifkan kolom, data masih ada sampai `DROP UNUSED` | cepat |

Kolom UNUSED tidak muncul di `SELECT *` dan tidak bisa dipakai, tetapi masih memakan ruang.

## Jebakan
- Kolom UNUSED tidak bisa dikembalikan; hanya bisa di-drop.
- `DROP COLUMN` pada tabel besar bisa mengunci lama.
- Batas jumlah kolom termasuk kolom UNUSED.
- Menghapus kolom yang dipakai constraint bisa gagal tanpa `CASCADE CONSTRAINTS`.

## Latihan
1. Mana yang lebih cepat pada tabel besar?
2. Apakah kolom UNUSED muncul di SELECT *?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>SET UNUSED</code> — hanya mengubah metadata.</p>
<p><b>2.</b> Tidak.</p>
</details>
