---
title: Mengambil data lewat konektor
minutes: 22
level: Menengah
badge: lengkap
summary: Query, iterasi result set, dan pemetaan tipe yang benar.
objectives:
  - Menjalankan query dan membaca hasil dengan aman
  - Memetakan tipe MySQL ke tipe bahasa aplikasi
  - Menangani banyak baris tanpa menghabiskan memori
---
## Kenapa topik ini diuji
Soal menyodorkan potongan kode konektor dan menanyakan hasil atau kesalahannya.

## Konsep inti
```java
try (Connection c = ds.getConnection();
     PreparedStatement ps = c.prepareStatement(
         "SELECT id, nama, total FROM pesanan WHERE pelanggan_id = ?")) {
    ps.setLong(1, 42);
    try (ResultSet rs = ps.executeQuery()) {
        while (rs.next()) {
            long id = rs.getLong("id");
            String nama = rs.getString("nama");
            BigDecimal total = rs.getBigDecimal("total");
        }
    }
}
```

```python
cur = conn.cursor(dictionary=True)
cur.execute("SELECT id, nama, total FROM pesanan WHERE pelanggan_id = %s", (42,))
for row in cur.fetchall():
    print(row["id"], row["total"])
cur.close()
```

Pemetaan tipe yang sering salah:

| MySQL | Java/Python | Catatan |
|---|---|---|
| `BIGINT UNSIGNED` | BigInteger / int | bisa melebihi `Long.MAX_VALUE` |
| `DECIMAL` | BigDecimal / Decimal | jangan pakai float |
| `TINYINT(1)` | boolean | konvensi boolean |
| `DATETIME` | LocalDateTime | tanpa zona waktu |
| `TIMESTAMP` | Instant/OffsetDateTime | dikonversi sesuai zona sesi |
| `BIT(1)` | boolean/byte[] | tergantung driver |
| `JSON` | String/objek | parsing di aplikasi |

## Jebakan
- `SELECT *` lalu memetakan berdasarkan posisi kolom; urutan bisa berubah setelah ALTER TABLE.
- Mengambil seluruh hasil dengan `fetchall()` untuk tabel besar.
- Memakai `Float`/`double` untuk uang.
- Lupa bahwa koneksi harus ditutup; di Java, `try-with-resources` wajib.

## Latihan
1. Tipe Java apa untuk `DECIMAL(12,2)` uang?
2. Mengapa `SELECT *` berisiko pada kode aplikasi?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>BigDecimal</code>.</p>
<p><b>2.</b> Karena perubahan skema (kolom baru/urutan) bisa memecahkan pemetaan berbasis posisi dan menambah data yang tidak perlu.</p>
</details>
