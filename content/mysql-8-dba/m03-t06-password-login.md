---
title: Keamanan password dan login
minutes: 20
level: Menengah
badge: lengkap
summary: validate_password, masa berlaku, penguncian akun, dan kebijakan login.
objectives:
  - Mengaktifkan dan mengatur komponen validate_password
  - Mengatur expiry dan account locking
  - Menggunakan password history
---
## Kenapa topik ini diuji
Kebijakan password sering muncul karena komponennya harus dipasang dulu di 8.0.

## Konsep inti
```sql
INSTALL COMPONENT 'file://component_validate_password';

SET PERSIST validate_password.policy = MEDIUM;
SET PERSIST validate_password.length = 12;
SET PERSIST validate_password.mixed_case_count = 1;
SET PERSIST validate_password.number_count = 1;
SET PERSIST validate_password.special_char_count = 1;

ALTER USER 'app'@'%' PASSWORD EXPIRE INTERVAL 90 DAY;
ALTER USER 'app'@'%' PASSWORD HISTORY 5;
ALTER USER 'app'@'%' PASSWORD REUSE INTERVAL 365 DAY;

ALTER USER 'app'@'%' FAILED_LOGIN_ATTEMPTS 5 PASSWORD_LOCK_TIME 1;
```

```ini
[mysqld]
default_password_lifetime = 90
disconnect_on_expired_password = ON
```

```sql
SELECT user, host, account_locked, password_lifetime FROM mysql.user;
```

## Jebakan
- Mengira `validate_password` adalah plugin lama — di 8.0 dipasang sebagai **component**.
- `FAILED_LOGIN_ATTEMPTS` tanpa `PASSWORD_LOCK_TIME` tidak mengunci permanen.
- Password expire membuat koneksi aplikasi gagal tanpa pesan jelas di log aplikasi.
- Menyetel `policy=STRONG` lalu pembuatan user gagal karena password sederhana.

## Latihan
1. Perintah memasang komponen validate_password?
2. Variabel apa yang menentukan lama penguncian?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>INSTALL COMPONENT 'file://component_validate_password';</code></p>
<p><b>2.</b> <code>PASSWORD_LOCK_TIME</code> pada <code>ALTER USER</code> (dalam hari).</p>
</details>
