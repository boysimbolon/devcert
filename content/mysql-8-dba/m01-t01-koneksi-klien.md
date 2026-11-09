---
title: Konfigurasi koneksi klien ke server
minutes: 20
level: Dasar
badge: lengkap
summary: Bagaimana mysqld menerima koneksi, memilih port dan socket, serta mengatur batas koneksi.
objectives:
  - Menjelaskan fase koneksi (handshake, autentikasi, TLS)
  - Mengonfigurasi bind-address, port, dan socket
  - Mengatur max_connections dan timeout yang relevan
---
## Kenapa topik ini diuji
Soal arsitektur hampir selalu mulai dari sini: "klien tidak bisa konek, apa penyebabnya?" Jawabannya ada pada bind address, socket, atau batas koneksi.

## Konsep inti
Fase koneksi:

1. **TCP handshake** ke `bind-address:port` (default 3306).
2. **Server greeting** berisi versi dan capability.
3. **Autentikasi** dengan plugin yang sesuai (caching_sha2_password default di 8.0).
4. **TLS** dinegosiasikan bila klien meminta atau server mewajibkan.
5. Koneksi menjadi **thread** yang melayani sampai selesai; thread diambil dari thread cache bila tersedia.

```ini
[mysqld]
bind-address = 0.0.0.0          # 127.0.0.1 = hanya lokal (lebih aman)
port = 3306
socket = /var/lib/mysql/mysql.sock
max_connections = 200
wait_timeout = 600              # koneksi idle diputus
interactive_timeout = 600
skip_name_resolve = ON          # hindari DNS reverse lookup (lebih cepat)
```

Variabel penting:

| Variabel | Fungsi |
|---|---|
| `max_connections` | jumlah koneksi bersamaan |
| `max_user_connections` | batas per akun |
| `wait_timeout` | batas idle non-interaktif |
| `thread_cache_size` | thread yang dipakai ulang |
| `back_log` | antrean koneksi sebelum ditolak |

Status yang dipakai mendiagnosis:

```sql
SHOW STATUS LIKE 'Threads_connected';
SHOW STATUS LIKE 'Max_used_connections';
SHOW STATUS LIKE 'Aborted_connects';    -- gagal handshake/auth
SHOW VARIABLES LIKE 'max_connections';
```

## Jebakan
- `bind-address=127.0.0.1` lalu bingung mengapa klien remote gagal — itu disengaja.
- `Aborted_connects` tinggi biasanya karena kredensial salah atau TLS tidak cocok, bukan karena `max_connections`.
- `skip-networking` mematikan TCP sama sekali; hanya socket lokal yang jalan.
- Klien memakai socket berbeda (mis. `/tmp/mysql.sock` vs `/var/lib/mysql/mysql.sock`) sehingga gagal walau server hidup.

## Latihan
1. Koneksi lokal jalan lewat socket, koneksi remote gagal. Variabel apa yang perlu diperiksa?
2. Apa arti `Max_used_connections` jauh di bawah `max_connections`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>bind-address</code> dan apakah <code>skip-networking</code> aktif; lalu firewall dan izin akun (host di <code>mysql.user</code>).</p>
<p><b>2.</b> Beban puncak masih jauh dari batas; menaikkan <code>max_connections</code> belum perlu.</p>
</details>
