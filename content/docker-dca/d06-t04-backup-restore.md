---
title: Backup dan restore volume
minutes: 20
level: Menengah
badge: lengkap
summary: Menyalin data volume dengan container bantu dan memulihkannya.
objectives:
  - Membuat arsip volume
  - Memulihkan ke volume lain
  - Menjadwalkan backup
---
## Konsep inti
```bash
# backup
docker run --rm -v pgdata:/data -v "$PWD":/backup alpine \
  tar czf /backup/pgdata-$(date +%F).tar.gz -C /data .

# restore ke volume baru
docker volume create pgdata_restore
docker run --rm -v pgdata_restore:/data -v "$PWD":/backup alpine \
  sh -c 'cd /data && tar xzf /backup/pgdata-2026-11-09.tar.gz'

# verifikasi
docker run --rm -v pgdata_restore:/data alpine ls -l /data
```

Untuk database, hentikan penulisan atau gunakan dump logis agar arsip konsisten.

## Jebakan
- Menyalin file database aktif bisa menghasilkan backup rusak.
- Arsip tar menyimpan UID/GID; restore ke environment lain bisa menyebabkan masalah izin.
- Backup ke host path harus punya ruang cukup dan disimpan di luar host.
- Restore ke volume yang sudah berisi data bisa bercampur — gunakan volume kosong.

## Latihan
1. Mengapa perlu menghentikan penulisan saat backup volume database?
2. Volume tujuan restore sebaiknya bagaimana?

<details><summary>Jawaban</summary>
<p><b>1.</b> Agar arsip konsisten (tidak menyalin file setengah tertulis).</p>
<p><b>2.</b> Kosong/baru, agar tidak bercampur dengan data lama.</p>
</details>
