---
title: Mengelola synonym
minutes: 18
level: Dasar
badge: lengkap
summary: Nama alternatif untuk objek, privat dan publik.
objectives:
  - Membuat synonym privat dan publik
  - Menghapus synonym
  - Menjelaskan manfaatnya
---
## Kenapa topik ini diuji
Soal kecil: siapa yang bisa memakai synonym publik, dan bagaimana menghapusnya.

## Konsep inti
```sql
CREATE SYNONYM emp FOR employees;
CREATE PUBLIC SYNONYM karyawan FOR hr.employees;

SELECT * FROM emp;
DROP SYNONYM emp;
DROP PUBLIC SYNONYM karyawan;

SELECT synonym_name, table_owner, table_name FROM user_synonyms;
```

| Jenis | Cakupan |
|---|---|
| Privat | hanya pembuatnya |
| Publik | semua user (butuh hak) |

Manfaat: menyembunyikan skema/nama panjang, memudahkan migrasi, dan memberi nama lokal untuk objek bersama.

## Jebakan
- Synonym publik tidak menghapus hak akses; privilege tetap diperlukan.
- `DROP PUBLIC SYNONYM` butuh hak khusus.
- Synonym bisa menunjuk objek yang sudah dihapus → error saat dipakai.
- Synonym tidak memvalidasi objek saat dibuat (kecuali objek lokal yang tidak ada).

## Latihan
1. Synonym mana yang bisa dipakai semua user?
2. Apakah synonym memberi akses tanpa GRANT?

<details><summary>Jawaban</summary>
<p><b>1.</b> Public synonym.</p>
<p><b>2.</b> Tidak; privilege pada objek tetap wajib.</p>
</details>
