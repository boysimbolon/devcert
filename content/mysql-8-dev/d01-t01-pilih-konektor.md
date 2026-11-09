---
title: Memilih konektor untuk aplikasi
minutes: 20
level: Dasar
badge: lengkap
summary: Connector/J, Python, .NET, ODBC, C++ — kapan dipakai dan apa bedanya dengan X DevAPI.
objectives:
  - Memilih konektor sesuai bahasa aplikasi
  - Membedakan konektor klasik (SQL) dan X DevAPI (NoSQL)
  - Mengetahui konektor mana yang mendukung fitur tertentu
---
## Kenapa topik ini diuji
Soal pertama domain ini selalu tentang pemetaan: bahasa/stack tertentu → konektor mana.

## Konsep inti
| Konektor | Untuk | Catatan |
|---|---|---|
| Connector/J | Java (JDBC) | paling banyak dipakai, mendukung pooling, TLS, prepared statement server-side |
| Connector/Python | Python (DB-API 2.0) | punya `mysql.connector` dan `mysqlx` |
| Connector/NET | C#/.NET | ADO.NET, Entity Framework |
| Connector/ODBC | aplikasi apa pun via ODBC | Excel, BI tools, PHP ODBC |
| Connector/C++ | C++ (JDBC-like/X DevAPI) | juga basis beberapa konektor lain |
| libmysqlclient | C | klien native, dasar banyak library |
| X DevAPI (mysqlx) | document store | port 33060, JSON/dokumen |

Dua jalur koneksi yang berbeda secara protokol:

```text
Klasik  : port 3306, protokol MySQL, SQL, driver JDBC/DB-API
X DevAPI: port 33060, protokol X, CRUD dokumen + SQL, driver mysqlx
```

Contoh string koneksi:

```text
jdbc:mysql://db.internal:3306/appdb?sslMode=REQUIRED&serverTimezone=Asia/Jakarta
mysql-connector-python: host=db.internal, user=app, database=appdb, ssl_ca=ca.pem
```

## Jebakan
- Mengira X DevAPI menggantikan konektor klasik; keduanya hidup berdampingan.
- Memakai Connector/ODBC untuk aplikasi Java (butuh JDBC).
- Lupa bahwa port 33060 harus dibuka terpisah untuk document store.
- Mengandalkan `mysqlx` untuk transaksi kompleks lintas koleksi; dukungannya lebih terbatas dari SQL.

## Latihan
1. Aplikasi C# memakai ORM Entity Framework — konektor mana?
2. Perbedaan port 3306 dan 33060?

<details><summary>Jawaban</summary>
<p><b>1.</b> Connector/NET (ADO.NET).</p>
<p><b>2.</b> 3306 = protokol MySQL klasik (SQL); 33060 = protokol X untuk X DevAPI/document store.</p>
</details>
