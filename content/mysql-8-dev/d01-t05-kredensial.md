---
title: Mengamankan kredensial dan koneksi
minutes: 20
level: Menengah
badge: lengkap
summary: Menyimpan kredensial dengan aman, TLS dari klien, dan login path.
objectives:
  - Menghindari kredensial hardcoded
  - Memakai mysql_config_editor dan keyring
  - Mewajibkan TLS dari sisi klien
---
## Kenapa topik ini diuji
Soal keamanan aplikasi menanyakan di mana kredensial boleh disimpan — dan hampir semua jawaban salah adalah "di source code".

## Konsep inti
```bash
# simpan kredensial terenkripsi untuk klien CLI
mysql_config_editor set --login-path=prod --host=db.internal \
  --user=app --password
mysql --login-path=prod appdb -e "SELECT 1"
mysql_config_editor print --all
```

```text
Prioritas penyimpanan kredensial (dari aman ke buruk):
1. Secret manager / vault (Vault, AWS Secrets Manager, Kubernetes Secret + KMS)
2. Variabel environment dari orchestrator
3. File kredensial mode 600 milik user aplikasi
4. File konfigurasi aplikasi (terenkripsi)
5. Hardcoded di source  <-- jangan pernah
```

TLS dari klien:

```bash
mysql --ssl-mode=VERIFY_IDENTITY --ssl-ca=ca.pem -h db.internal -u app -p
```

```text
jdbc:mysql://db.internal:3306/appdb?sslMode=VERIFY_IDENTITY&trustCertificateKeyStoreUrl=file:/etc/app/truststore.jks
```

Akun aplikasi sebaiknya `REQUIRE SSL` sehingga koneksi tanpa TLS ditolak server.

## Jebakan
- `sslMode=PREFERRED` (default) tidak menjamin TLS dipakai.
- Menyimpan password di `~/.my.cnf` world-readable.
- Rotasi password tanpa memperbarui secret di semua instance aplikasi.
- Membagikan satu akun DB untuk semua layanan → sulit diaudit dan dicabut.

## Latihan
1. Mode TLS mana yang memverifikasi identitas server?
2. Perintah menyimpan kredensial CLI terenkripsi?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>VERIFY_IDENTITY</code> (memeriksa sertifikat dan hostname).</p>
<p><b>2.</b> <code>mysql_config_editor set --login-path=nama ...</code> yang menulis ke file terenkripsi <code>.mylogin.cnf</code>.</p>
</details>
