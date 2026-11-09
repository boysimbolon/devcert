---
title: Menggunakan prepared statement
minutes: 20
level: Dasar
badge: lengkap
summary: Parameter binding, prepared statement server-side, dan eksekusi berulang.
objectives:
  - Menulis prepared statement yang aman
  - Membedakan emulasi klien dan server-side
  - Memakai ulang statement untuk banyak eksekusi
---
## Kenapa topik ini diuji
Ini pertahanan utama terhadap SQL injection, dan sering muncul sebagai soal kode.

## Konsep inti
```sql
PREPARE stmt FROM 'SELECT id, nama FROM pelanggan WHERE kota = ? AND aktif = ?';
SET @kota = 'Bandung', @aktif = 1;
EXECUTE stmt USING @kota, @aktif;
DEALLOCATE PREPARE stmt;
```

Di aplikasi (Java):

```java
try (PreparedStatement ps = c.prepareStatement(
        "INSERT INTO pesanan (pelanggan_id, total) VALUES (?, ?)")) {
    for (Pesanan p : daftar) {
        ps.setLong(1, p.pelangganId());
        ps.setBigDecimal(2, p.total());
        ps.addBatch();
    }
    ps.executeBatch();
}
```

Dua mode pada Connector/J:

- `useServerPrepStmts=false` (default lama): driver menyusun SQL dengan escaping — aman tetapi bukan prepare di server.
- `useServerPrepStmts=true`: server menyiapkan statement; lebih efisien bila dieksekusi berulang.

## Jebakan
- Menggabungkan identifier (nama tabel) sebagai parameter — tidak bisa; gunakan whitelist.
- Lupa `addBatch`/`executeBatch` lalu mengira sudah efisien.
- Menyiapkan statement baru di dalam loop (boros); siapkan sekali di luar.
- `BETWEEN ? AND ?` dengan tipe string pada kolom tanggal.

## Latihan
1. Mengapa parameter tidak bisa dipakai untuk nama tabel?
2. Kapan server-side prepare lebih menguntungkan?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena parameter hanya untuk nilai; identifier harus menjadi bagian teks query dan divalidasi whitelist.</p>
<p><b>2.</b> Saat statement yang sama dieksekusi berkali-kali dalam satu koneksi.</p>
</details>
