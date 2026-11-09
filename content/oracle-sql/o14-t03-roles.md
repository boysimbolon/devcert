---
title: Privilege vs role
minutes: 18
level: Menengah
badge: lengkap
summary: Mengelompokkan privilege dalam role, mengaktifkan, dan default role.
objectives:
  - Membuat role dan memberi privilege
  - Memberikan role ke user
  - Mengatur default role
---
## Kenapa topik ini diuji
Perbedaan memberi privilege langsung vs lewat role adalah soal konsep yang sering keluar.

## Konsep inti
```sql
CREATE ROLE baca_hr;
GRANT SELECT ON hr.employees TO baca_hr;
GRANT baca_hr TO app;

ALTER USER app DEFAULT ROLE baca_hr;   -- aktif otomatis saat login
ALTER USER app DEFAULT ROLE ALL;

SET ROLE baca_hr;                       -- aktifkan manual
SET ROLE NONE;                          -- matikan semua role

SELECT role FROM session_roles;
```

| Aspek | Privilege langsung | Role |
|---|---|---|
| Pengelolaan | satu per satu | terkelompok |
| Aktif | selalu | perlu default/aktifkan |
| Pencabutan | per privilege | satu perintah |

## Jebakan
- Role tidak otomatis aktif tanpa `DEFAULT ROLE` atau `SET ROLE`.
- `SET ROLE` memengaruhi sesi berjalan saja.
- Role bisa diberi ke role lain (nested), tetapi lacak agar tidak membingungkan.
- Object privilege lewat role yang belum aktif tidak berlaku.

## Latihan
1. Bagaimana membuat role aktif otomatis saat login?
2. Apakah pemberian role langsung aktif?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ALTER USER ... DEFAULT ROLE nama_role;</code></p>
<p><b>2.</b> Tidak; perlu DEFAULT ROLE atau SET ROLE.</p>
</details>
