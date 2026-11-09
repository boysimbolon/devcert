---
title: InnoDB Cluster dan Group Replication
minutes: 20
level: Menengah
badge: lengkap
summary: Arsitektur cluster: Group Replication, MySQL Shell AdminAPI, dan MySQL Router.
objectives:
  - Menjelaskan tiga komponen InnoDB Cluster
  - Membedakan single-primary dan multi-primary
  - Menjelaskan peran quorum
---
## Kenapa topik ini diuji
HA modern MySQL dibangun dari tiga komponen yang harus disebutkan dengan benar.

## Konsep inti
| Komponen | Fungsi |
|---|---|
| **Group Replication** | replikasi sinkron berbasis Paxos antar anggota grup |
| **MySQL Shell AdminAPI** | membuat dan mengelola cluster (`dba.*`) |
| **MySQL Router** | routing koneksi aplikasi ke primary/replica |

Mode:

- **Single-primary** — satu anggota menerima tulis, sisanya baca; default dan paling aman.
- **Multi-primary** — semua bisa menulis; risiko konflik lebih tinggi.

Quorum: mayoritas anggota harus hidup. Tiga anggota → toleransi satu mati. Dua anggota → tidak ada toleransi (tidak disarankan).

```text
Aplikasi -> MySQL Router -> primary (tulis) / secondary (baca)
                          -> Group Replication (konsistensi)
                          -> MySQL Shell (administrasi)
```

## Jebakan
- Cluster 2 anggota dianggap HA padahal tidak ada mayoritas.
- Router bukan load balancer umum; ia mengarahkan sesuai peran.
- Multi-primary membutuhkan penanganan konflik aplikasi.
- Group Replication mensyaratkan GTID, `binlog_format=ROW`, dan PK pada semua tabel.

## Latihan
1. Komponen mana yang menghadap aplikasi?
2. Berapa anggota minimum untuk toleransi satu kegagalan?

<details><summary>Jawaban</summary>
<p><b>1.</b> MySQL Router.</p>
<p><b>2.</b> Tiga anggota — mayoritas dua tetap hidup.</p>
</details>
