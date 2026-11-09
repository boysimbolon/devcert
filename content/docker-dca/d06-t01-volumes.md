---
title: Volume
minutes: 22
level: Dasar
badge: lengkap
summary: Volume terkelola Docker, siklus hidup, dan pemakaiannya.
objectives:
  - Membuat dan memakai volume
  - Menjelaskan siklus hidup volume
  - Memeriksa isi volume
---
## Kenapa topik ini diuji
Domain Storage 10%: soal menanyakan di mana data tetap ada setelah container dihapus.

## Konsep inti
```bash
docker volume create pgdata
docker run -d --name db -v pgdata:/var/lib/postgresql/data postgres:16
docker volume ls
docker volume inspect pgdata
docker run --rm -v pgdata:/data alpine ls -l /data
docker volume rm pgdata            # hanya bila tidak dipakai
```

Volume disimpan di area Docker (`/var/lib/docker/volumes` pada default), dikelola Docker, dan **tidak** terhapus saat container dihapus.

## Jebakan
- `docker rm -v` hanya menghapus anonymous volume; named volume tetap.
- `docker volume rm` gagal bila volume masih dipakai container (aktif atau berhenti).
- Volume yang di-mount ke path berisi data image akan menutupi isi image tersebut.
- Backup volume butuh container bantu; tidak ada `docker volume export`.

## Latihan
1. Apakah volume hilang saat container dihapus?
2. Perintah melihat detail lokasi volume?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tidak (named volume tetap ada).</p>
<p><b>2.</b> <code>docker volume inspect</code>.</p>
</details>
