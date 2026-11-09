---
title: Bridge dan user-defined bridge
minutes: 22
level: Menengah
badge: lengkap
summary: Default bridge, network buatan sendiri, dan DNS internal.
objectives:
  - Membedakan default bridge dan user-defined
  - Membuat network dan melampirkan container
  - Menjelaskan isolasi
---
## Kenapa topik ini diuji
Domain Networking 15%: soal menanyakan bagaimana dua container saling menemukan.

## Konsep inti
```bash
docker network ls
docker network create appnet
docker run -d --name api --network appnet nginx
docker run -d --name web --network appnet alpine sleep 3600

docker exec web ping -c1 api       # resolve via DNS internal
docker network inspect appnet
docker network connect appnet lain
```

| Jenis | DNS internal | Isolasi |
|---|---|---|
| `bridge` (default) | tidak (kecuali `--link`, usang) | semua container default |
| bridge buatan sendiri | **ya** (127.0.0.11) | hanya anggota |

## Jebakan
- Pada default bridge, container harus saling hubungi lewat IP; nama tidak resolve.
- Container hanya bisa berada di beberapa network; `docker network connect` menambah.
- Network yang masih dipakai container tidak bisa dihapus.
- Nama network tidak sama dengan nama host.

## Latihan
1. Di mana DNS internal Docker berjalan?
2. Mengapa `ping api` gagal pada default bridge?

<details><summary>Jawaban</summary>
<p><b>1.</b> Di dalam network user-defined (resolver 127.0.0.11).</p>
<p><b>2.</b> Karena default bridge tidak menyediakan resolusi nama otomatis.</p>
</details>
