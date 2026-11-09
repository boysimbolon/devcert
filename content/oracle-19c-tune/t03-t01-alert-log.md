---
title: Alert log untuk memantau performa
minutes: 18
level: Dasar
badge: lengkap
summary: Mencari error, ORA-00600, perubahan parameter, dan kejadian penting.
objectives:
  - Menemukan lokasi alert log
  - Membaca pola penting
  - Memakai ADRCI untuk menelusuri
---
## Kenapa topik ini diuji
Soal menanyakan di mana mencari error tertentu dan alat apa untuk membacanya.

## Konsep inti
```sql
SELECT value FROM v$diag_info WHERE name = 'Diag Trace';
SELECT value FROM v$diag_info WHERE name = 'Diag Alert';
```

```bash
adrci
show homes
set home diag/rdbms/orcl/ORCL
show alert -tail 50
show alert -p "message_text like '%ORA-00600%'"
```

Isi penting alert log: startup/shutdown, perubahan parameter, error ORA-, tablespace penuh, switch logfile, deadlock.

## Jebakan
- Alert log berbentuk XML di `alert/` dan teks di `trace/`.
- Rotasi otomatis membuat file lama terpisah.
- `ORA-00600/07445` butuh trace file pendamping, bukan hanya alert log.
- Alert log tidak memuat statistik performa; itu tugas AWR.

## Latihan
1. Alat CLI untuk membaca alert log?
2. Di mana daftar trace file berada?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>adrci</code>.</p>
<p><b>2.</b> Direktori <code>Diag Trace</code> (lihat <code>v$diag_info</code>).</p>
</details>
