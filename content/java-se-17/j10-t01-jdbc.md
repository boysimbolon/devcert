---
title: JDBC: connection, statement, resultset, transaksi
minutes: 24
level: Menengah
badge: lengkap
summary: PreparedStatement, CallableStatement, ResultSet, dan commit/rollback.
objectives:
  - Membuat koneksi dan mengeksekusi statement
  - Membedakan Statement, PreparedStatement, CallableStatement
  - Mengelola transaksi dan resource
---
## Kenapa topik ini diuji
Soal menanyakan urutan resource dan cara mencegah SQL injection.

## Konsep inti
```java
try (Connection c = DriverManager.getConnection(url, user, pass)) {
    c.setAutoCommit(false);
    try (PreparedStatement ps = c.prepareStatement(
            "SELECT nama FROM pelanggan WHERE kota = ? AND aktif = ?")) {
        ps.setString(1, "Jakarta");
        ps.setBoolean(2, true);
        try (ResultSet rs = ps.executeQuery()) {
            while (rs.next()) System.out.println(rs.getString("nama"));
        }
    }
    c.commit();
} catch (SQLException e) {
    // rollback bila perlu
}
```

`CallableStatement` untuk stored procedure: `{call proc(?, ?)}`, `registerOutParameter`.

## Jebakan
- Tanpa `commit()` saat autocommit=false → perubahan hilang saat close.
- `rs.getString(1)` indeks dimulai dari 1, bukan 0.
- `executeQuery` untuk SELECT, `executeUpdate` untuk DML.
- Menutup Connection menutup statement/resultset; urutan aman: ResultSet → Statement → Connection.
- Concatenate input ke SQL = SQL injection.

## Latihan
1. Statement untuk memanggil stored procedure?
2. Apa yang terjadi bila lupa commit?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>CallableStatement</code>.</p>
<p><b>2.</b> Perubahan tidak tersimpan (bergantung driver, umumnya rollback saat close).</p>
</details>
