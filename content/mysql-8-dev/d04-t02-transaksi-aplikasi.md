---
title: Mengendalikan transaksi di aplikasi
minutes: 22
level: Menengah
badge: lengkap
summary: Transaksi per koneksi, retry deadlock, dan transaksi terdistribusi (XA).
objectives:
  - Mengelola batas transaksi dari kode aplikasi
  - Menangani deadlock dengan retry
  - Memahami kapan XA diperlukan
---
## Kenapa topik ini diuji
Soal menanyakan di mana transaksi dimulai dan apa yang terjadi saat deadlock.

## Konsep inti
```java
try (Connection c = ds.getConnection()) {
    c.setAutoCommit(false);
    try (PreparedStatement a = c.prepareStatement("UPDATE stok SET qty=qty-1 WHERE id=?")) {
        a.setInt(1, id); a.executeUpdate();
    }
    try (PreparedStatement b = c.prepareStatement("INSERT INTO pesanan(id,item) VALUES(?,?)")) {
        b.setLong(1, idPesanan); b.setInt(2, id); b.executeUpdate();
    }
    c.commit();
} // auto-rollback bila exception sebelum commit
```

Deadlock (errno 1213) bukan kesalahan permanen — ulangi:

```java
for (int attempt = 1; attempt <= 3; attempt++) {
    try { kerjakanTransaksi(); break; }
    catch (SQLException e) {
        if (e.getErrorCode() != 1213) throw e;
        Thread.sleep(50L * attempt);
    }
}
```

Transaksi terdistribusi lintas sumber (XA) dipakai bila satu unit kerja menyentuh dua server MySQL atau sistem lain; lebih mahal dan rawan in-doubt.

## Jebakan
- Menjalankan beberapa pernyataan pada koneksi berbeda lalu menganggapnya satu transaksi.
- Menangkap `SQLException` lalu tetap `commit()`.
- Retry tanpa batas → memperparah kemacetan.
- Transaksi panjang menahan lock dan memperlambat purge undo.

## Latihan
1. Kode error untuk deadlock?
2. Mengapa dua koneksi tidak bisa satu transaksi?

<details><summary>Jawaban</summary>
<p><b>1.</b> 1213 (SQLSTATE 40001).</p>
<p><b>2.</b> Karena transaksi terikat pada satu koneksi/sesi; lintas koneksi membutuhkan XA atau pola kompensasi.</p>
</details>
