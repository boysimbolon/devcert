---
title: Data dictionary views
minutes: 20
level: Menengah
badge: lengkap
summary: USER_, ALL_, dan DBA_ views untuk memeriksa objek dan hak.
objectives:
  - Membedakan prefix USER_, ALL_, DBA_
  - Menemukan informasi objek lewat dictionary
  - Menghindari kesalahan query umum
---
## Kenapa topik ini diuji
Soal menanyakan view mana yang tepat untuk informasi tertentu.

## Konsep inti
| Prefix | Cakupan |
|---|---|
| `USER_` | objek milik user saat ini |
| `ALL_` | objek yang bisa diakses user |
| `DBA_` | semua objek (butuh privilege) |
| `V$` | dynamic performance views |

```sql
SELECT table_name, num_rows FROM user_tables;
SELECT column_name, data_type FROM user_tab_columns WHERE table_name='EMPLOYEES';
SELECT constraint_name, constraint_type FROM user_constraints;
SELECT index_name, uniqueness FROM user_indexes;
SELECT view_name FROM user_views;
SELECT privilege FROM user_sys_privs;
DESC user_tables;
```

## Jebakan
- `USER_TABLES` tidak menampilkan tabel milik user lain (walau bisa diakses).
- Nama objek di dictionary disimpan **huruf besar** kecuali dibuat dengan tanda kutip.
- `NUM_ROWS` hanya terisi setelah statistik dikumpulkan.
- `ALL_TABLES` bisa sangat besar; filter dengan `OWNER`.

## Latihan
1. View untuk tabel milik sendiri?
2. Mengapa `WHERE table_name='employees'` tidak menemukan apa pun?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>USER_TABLES</code>.</p>
<p><b>2.</b> Karena nama disimpan huruf besar; gunakan <code>'EMPLOYEES'</code> atau <code>UPPER(...)</code>.</p>
</details>
