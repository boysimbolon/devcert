---
title: MySQL Enterprise Authentication
minutes: 20
level: Menengah
badge: lengkap
summary: Login terpusat lewat PAM, LDAP, Kerberos, dan FIDO — beserta alur autentikasinya.
objectives:
  - Menjelaskan mengapa autentikasi terpusat dipakai
  - Menyebutkan plugin Enterprise yang tersedia
  - Mengonfigurasi akun untuk plugin tersebut
---
## Kenapa topik ini diuji
Soal pemetaan kebutuhan: "perusahaan memakai Active Directory, plugin mana?" Jawabannya plugin Enterprise, bukan fitur bawaan Community.

## Konsep inti
| Plugin | Sumber identitas |
|---|---|
| `authentication_pam` | PAM (Unix, LDAP via PAM) |
| `authentication_ldap_simple` / `_sasl` | LDAP/Active Directory langsung |
| `authentication_kerberos` | Kerberos ticket (Enterprise) |
| `authentication_fido` | FIDO2/WebAuthn (8.0.30+) |
| `authentication_oci` | OCI IAM (untuk HeatWave/OCI) |

```sql
CREATE USER 'budi'@'%' IDENTIFIED WITH authentication_ldap_simple
  AS 'uid=budi,ou=people,dc=contoh,dc=id';

-- dua faktor: password + FIDO
ALTER USER 'admin'@'localhost'
  IDENTIFIED WITH authentication_fido;
```

```ini
[mysqld]
plugin-load-add = authentication_ldap_simple.so
authentication_ldap_simple_server_host = ldap.contoh.id
authentication_ldap_simple_bind_base_dn = ou=people,dc=contoh,dc=id
```

## Jebakan
- Plugin Enterprise tidak tersedia di Community — deployment gagal bila dipaksakan.
- Akun LDAP tidak punya password lokal; jangan harap `IDENTIFIED BY` bekerja.
- Bila server LDAP mati, login admin juga bisa terkunci; sediakan akun darurat lokal.
- `auth_socket` berbeda dari PAM: yang pertama hanya memetakan user OS.

## Latihan
1. Plugin untuk login memakai Active Directory langsung?
2. Mengapa perlu akun darurat lokal?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>authentication_ldap_simple</code> (atau <code>authentication_pam</code> bila lewat PAM).</p>
<p><b>2.</b> Agar tidak terkunci total saat server identitas tidak tersedia.</p>
</details>
