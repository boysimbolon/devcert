---
title: Mengenali risiko keamanan umum
minutes: 18
level: Dasar
badge: lengkap
summary: Akun longgar, port terbuka, privilege berlebih, dan data tanpa enkripsi.
objectives:
  - Menyebutkan risiko utama pada instalasi MySQL
  - Memeriksa konfigurasi berbahaya
  - Memprioritaskan perbaikan
---
## Kenapa topik ini diuji
Soal tipe "risiko mana yang paling serius" atau "apa langkah pertama mengamankan server baru".

## Konsep inti
Risiko yang berulang:

1. **Akun tanpa password / `'root'@'%'`** — akses penuh dari mana saja.
2. **Port 3306 terbuka ke internet** — target pemindaian otomatis.
3. **Privilege berlebih** — aplikasi memakai akun `root`.
4. **Tanpa TLS** — kredensial dan data lewat jaringan terbuka.
5. **Data tidak terenkripsi** di disk/backup.
6. **Log berisi data sensitif** (`general_log` menyimpan nilai parameter).
7. **Plugin auth lama** dengan hash lemah.
8. **Tidak ada backup teruji** — risiko ketersediaan.

Pemeriksaan cepat:

```sql
SELECT user, host, plugin FROM mysql.user WHERE host <> 'localhost';
SELECT user, host FROM mysql.user WHERE authentication_string = '';
SHOW VARIABLES LIKE 'require_secure_transport';
SHOW VARIABLES LIKE 'local_infile';
SHOW VARIABLES LIKE 'general_log';
```

```bash
ss -tlnp | grep 3306
mysql_secure_installation
```

## Jebakan
- Mengira `bind-address` di firewall sudah cukup padahal MySQL mendengar di semua interface.
- `local_infile=ON` membuka jalur pemuatan file dari klien.
- Menyimpan kredensial aplikasi di file world-readable.
- Menganggap backup tidak perlu dienkripsi karena "hanya di server".

## Latihan
1. Apa risiko utama membuka 3306 ke publik?
2. Mengapa `local_infile` sebaiknya dimatikan?

<details><summary>Jawaban</summary>
<p><b>1.</b> Server dapat dipindai dan diserang brute force/eksploit; MySQL seharusnya hanya diakses dari jaringan aplikasi.</p>
<p><b>2.</b> Karena memungkinkan klien memuat file dari sisi klien, yang dapat disalahgunakan untuk membaca data lokal.</p>
</details>
