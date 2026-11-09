---
title: Produk dan fitur MySQL Enterprise
minutes: 22
level: Dasar
badge: lengkap
summary: Peta produk EE: Backup, Monitor, Audit, Firewall, Authentication, Thread Pool, dan HeatWave.
objectives:
  - Memetakan produk Enterprise ke masalah yang diselesaikannya
  - Menjelaskan komponen tiap produk
  - Mengetahui produk mana yang butuh agen
---
## Kenapa topik ini diuji
Soal pemetaan: "kebutuhan X, produk mana?" Ini hafalan terstruktur yang mudah dijamin benar.

## Konsep inti
| Produk | Menyelesaikan | Komponen |
|---|---|---|
| Enterprise Backup (MEB) | backup hot & inkremental | `mysqlbackup`, opsi `--incremental` |
| Enterprise Monitor (MEM) | monitoring & advisory | Service Manager + agent |
| Enterprise Audit | kepatuhan, jejak aktivitas | plugin `audit_log`, filter |
| Enterprise Firewall | memblokir query menyimpang | plugin firewall, allowlist |
| Enterprise Authentication | login terpusat | plugin PAM/LDAP/FIDO |
| Thread Pool | banyak koneksi tanpa kehabisan thread | plugin `thread_pool` |
| Enterprise Encryption | TDE, keyring terpusat | keyring KMIP/OCI Vault |
| HeatWave | analitik in-memory | DB system + node HeatWave |

```ini
# contoh mengaktifkan thread pool
[mysqld]
thread_handling = pool-of-threads
thread_pool_size = 16
```

```sql
INSTALL PLUGIN audit_log SONAME 'audit_log.so';
INSTALL PLUGIN mysql_firewall SONAME 'mysql_firewall.so';
```

## Jebakan
- MEM butuh **agent** di host MySQL; tanpa agent, metrik tidak lengkap.
- Thread Pool mengubah model thread (bukan satu thread per koneksi) → beberapa status variable berubah makna.
- Enterprise Encryption butuh keyring aktif sebelum tabel dienkripsi.
- HeatWave bukan plugin on-prem; ia layanan OCI dengan DB system.

## Latihan
1. Produk mana yang butuh agent terpisah?
2. Plugin apa untuk thread pool?

<details><summary>Jawaban</summary>
<p><b>1.</b> MySQL Enterprise Monitor.</p>
<p><b>2.</b> <code>thread_pool</code> (dengan <code>thread_handling=pool-of-threads</code>).</p>
</details>
