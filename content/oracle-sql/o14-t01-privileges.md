---
title: System privilege vs object privilege
minutes: 18
level: Menengah
badge: lengkap
summary: Hak tingkat sistem dan tingkat objek, serta bedanya dalam pemakaian.
objectives:
  - Membedakan system dan object privilege
  - Menyebutkan contoh tiap jenis
  - Menjelaskan hak yang dibutuhkan untuk operasi umum
---
## Kenapa topik ini diuji
Soal sering menanyakan privilege mana yang diperlukan untuk sebuah operasi.

## Konsep inti
| Jenis | Contoh | Cakupan |
|---|---|---|
| System | CREATE TABLE, CREATE SESSION, CREATE VIEW, ALTER DATABASE | seluruh database |
| Object | SELECT, INSERT, UPDATE, DELETE, EXECUTE, REFERENCES | objek tertentu |

```sql
GRANT CREATE SESSION, CREATE TABLE TO app;
GRANT SELECT, INSERT ON hr.employees TO app;
GRANT EXECUTE ON hr.proc_gaji TO app;

SELECT * FROM session_privs;      -- system privilege saya
SELECT * FROM user_tab_privs;     -- object privilege saya
```

`CREATE SESSION` wajib agar user bisa login — kesalahan umum saat membuat user baru.

## Jebakan
- User baru tanpa `CREATE SESSION` tidak bisa konek sama sekali.
- Object privilege tidak memberi hak untuk membuat objek baru.
- `ALL PRIVILEGES` pada objek tidak termasuk `GRANT OPTION`.
- Privilege lewat role tidak terlihat di `SESSION_PRIVS` bila role belum aktif.

## Latihan
1. Privilege minimal agar user bisa login?
2. Jenis privilege untuk SELECT pada tabel tertentu?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>CREATE SESSION</code>.</p>
<p><b>2.</b> Object privilege.</p>
</details>
