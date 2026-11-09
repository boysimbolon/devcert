---
title: Menerbitkan port
minutes: 18
level: Dasar
badge: lengkap
summary: -p, -P, rentang port, dan perbedaan run vs service.
objectives:
  - Menerbitkan port dengan format tepat
  - Menjelaskan -P dan EXPOSE
  - Menghindari bentrok port
---
## Konsep inti
```bash
docker run -d -p 8080:80 nginx           # host:container
docker run -d -p 127.0.0.1:8080:80 nginx # hanya localhost host
docker run -d -p 8080:80/udp nginx
docker run -d -P nginx                   # publish semua port EXPOSE ke acak
docker port <container>
```

Pada swarm: `--publish published=8080,target=80,mode=ingress|host`.

## Jebakan
- `-p 80:80` membuka ke semua interface host (0.0.0.0), bukan hanya localhost.
- Tanpa EXPOSE pun `-p` tetap bekerja; EXPOSE hanya dokumentasi.
- Dua container dengan port host sama → `port is already allocated`.
- `-P` butuh `EXPOSE` di image agar ada yang dipublish.

## Latihan
1. Format agar port hanya diakses dari host itu sendiri?
2. Perintah melihat port yang dipublikasikan container?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>-p 127.0.0.1:8080:80</code>.</p>
<p><b>2.</b> <code>docker port &lt;container&gt;</code>.</p>
</details>
