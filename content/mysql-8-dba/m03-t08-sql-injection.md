---
title: Mencegah serangan SQL injection
minutes: 20
level: Menengah
badge: lengkap
summary: Prepared statement, hak akses minimal, dan peran server dalam mitigasi.
objectives:
  - Menjelaskan mengapa prepared statement mencegah injeksi
  - Mengurangi dampak lewat privilege minimal
  - Mengenali konfigurasi server yang memperparah
---
## Kenapa topik ini diuji
Soal security sering menyodorkan potongan kode dan menanyakan apakah rentan.

## Konsep inti
Rentan — query disusun dari input:

```sql
-- JANGAN: input pengguna digabung ke teks query
SET @q = CONCAT("SELECT * FROM users WHERE name = '", @input, "'");
PREPARE s FROM @q;
EXECUTE s;
```

Aman — teks query tetap, nilai diikat:

```sql
PREPARE s FROM 'SELECT * FROM users WHERE name = ?';
SET @nama = 'budi';
EXECUTE s USING @nama;
```

Peran server (bukan pengganti perbaikan aplikasi):

- Akun aplikasi hanya `SELECT/INSERT/UPDATE/DELETE` pada schema aplikasi — tanpa `DROP`, `FILE`, `PROCESS`.
- `local_infile=OFF` menutup jalur pemuatan file.
- `sql_mode` ketat menolak input aneh.
- WAF di depan aplikasi (di luar MySQL).

```sql
SHOW GRANTS FOR 'app'@'%';
SELECT @@sql_mode, @@local_infile;
```

## Jebakan
- Mengandalkan escaping string sebagai satu-satunya pertahanan.
- Memberi akun aplikasi `FILE` atau `SUPER` "supaya tidak error".
- Nama tabel/kolom tidak bisa diparameterkan — wajib whitelist.
- Prosedur `SQL SECURITY DEFINER` berprivilege tinggi dipanggil dari input pengguna.

## Latihan
1. Mengapa parameter binding mencegah injeksi?
2. Bagian query mana yang tidak bisa diparameterkan?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena nilai dikirim terpisah dari teks query sehingga tidak ditafsirkan sebagai sintaks SQL.</p>
<p><b>2.</b> Nama tabel, nama kolom, dan arah ORDER BY — harus divalidasi dengan whitelist.</p>
</details>
