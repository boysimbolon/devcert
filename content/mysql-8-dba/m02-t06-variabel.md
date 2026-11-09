---
title: Mengonfigurasi variabel MySQL
minutes: 20
level: Menengah
badge: lengkap
summary: Scope global dan session, variabel dinamis, serta cara mengaudit nilai.
objectives:
  - Membedakan variabel global, session, dan status
  - Menentukan variabel yang bisa diubah online
  - Mengaudit variabel yang menyimpang dari baseline
---
## Kenapa topik ini diuji
Soal sering meminta membedakan mana yang bisa diubah tanpa restart, dan mana yang berpengaruh per sesi.

## Konsep inti
Tiga kategori:

- **Variabel** (`@@`) — konfigurasi, bisa global/session, sebagian read-only.
- **Status** (`SHOW STATUS`) — penghitung runtime, tidak bisa di-set.
- **System variables** dari `performance_schema` — untuk observability.

```sql
-- global vs session
SELECT @@global.sort_buffer_size, @@session.sort_buffer_size;

-- mengubah untuk sesi ini saja
SET SESSION sql_mode = 'STRICT_ALL_TABLES,NO_ENGINE_SUBSTITUTION';

-- mengubah global + sesi berjalan
SET GLOBAL max_connections = 400;

-- melihat variabel yang berbeda dari default
SELECT VARIABLE_NAME, VARIABLE_SOURCE, SET_TIME
  FROM performance_schema.variables_info
 WHERE VARIABLE_SOURCE <> 'COMPILED' ORDER BY VARIABLE_NAME LIMIT 20;
```

Variabel penting per area:

| Area | Variabel |
|---|---|
| Transaksi | `transaction_isolation`, `autocommit` |
| Query | `long_query_time`, `sql_mode` |
| Replikasi | `server_id`, `gtid_mode`, `binlog_format` |
| InnoDB | `innodb_buffer_pool_size`, `innodb_flush_log_at_trx_commit` |
| Keamanan | `require_secure_transport`, `validate_password.*` |

## Jebakan
- Mengubah variabel `SESSION` lalu mengira semua koneksi berubah.
- Variabel read-only (`innodb_log_file_size` di beberapa versi) tetap butuh restart.
- `sql_mode` berbeda antara aplikasi dan CLI → perilaku query berbeda.
- Lupa bahwa `SET PERSIST` mengubah nilai saat restart, bisa mengejutkan saat rollback.

## Latihan
1. Bagaimana melihat variabel mana yang diubah dari default?
2. Apakah perubahan `SET SESSION` memengaruhi koneksi lain?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>performance_schema.variables_info</code> dengan <code>VARIABLE_SOURCE &lt;&gt; 'COMPILED'</code>.</p>
<p><b>2.</b> Tidak; hanya sesi itu, dan hilang saat koneksi ditutup.</p>
</details>
