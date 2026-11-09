---
title: Sistem privilege MySQL
minutes: 22
level: Menengah
badge: lengkap
summary: Tabel grant, tingkat privilege, dan urutan pemeriksaan izin.
objectives:
  - Menjelaskan tabel sistem yang menyimpan privilege
  - Membedakan tingkat privilege
  - Memahami mengapa izin tertentu tidak berlaku
---
## Kenapa topik ini diuji
Soal keamanan sering menyodorkan skenario "user tidak bisa X" dan menanyakan penyebabnya.

## Konsep inti
Privilege disimpan di tabel sistem di schema `mysql`:

| Tabel | Cakupan |
|---|---|
| `user` | global |
| `db` | database |
| `tables_priv` | tabel |
| `columns_priv` | kolom |
| `procs_priv` | prosedur/fungsi |
| `role_edges` | role → user |
| `global_grants` | dynamic privileges |

Tingkat privilege: global → database → tabel → kolom → rutin.

```sql
SHOW GRANTS FOR 'app'@'%';
SHOW GRANTS FOR 'app'@'%' USING 'app_read';

GRANT SELECT, INSERT ON appdb.* TO 'app'@'%';
GRANT EXECUTE ON PROCEDURE appdb.hitung TO 'app'@'%';
GRANT BACKUP_ADMIN ON *.* TO 'dba'@'localhost';
```

Pemeriksaan izin bertingkat: MySQL mencocokkan akun **paling spesifik** (`user@host`), lalu menggabungkan privilege dari semua tingkat yang berlaku.

## Jebakan
- Privilege global tidak otomatis memberi izin pada tabel yang dibuat setelahnya? — justru berlaku ke semua; sebaliknya privilege database berlaku ke tabel baru.
- `SHOW GRANTS` tanpa `USING` tidak menampilkan privilege dari role.
- Menghapus user tidak otomatis menghapus baris di tabel grant lain (di 8.0 sudah dibersihkan, tapi role bisa tertinggal).
- `GRANT` pada kolom tidak bisa dipakai bersama `SELECT *`.

## Latihan
1. Tabel mana yang menyimpan privilege level kolom?
2. Bagaimana melihat izin yang berasal dari role?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>mysql.columns_priv</code>.</p>
<p><b>2.</b> <code>SHOW GRANTS FOR user USING role;</code></p>
</details>
