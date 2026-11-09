---
title: Service dan replica
minutes: 22
level: Menengah
badge: lengkap
summary: Membuat service, menerbitkan port, dan menskalakan replika.
objectives:
  - Membuat service di swarm
  - Menerbitkan port dengan benar
  - Menskalakan dan memeriksa service
---
## Konsep inti
```bash
docker service create --name web --replicas 3 --publish published=80,target=80 nginx:1.25
docker service ls
docker service ps web
docker service inspect --pretty web
docker service scale web=5
docker service logs -f web
docker service rm web
```

Service adalah deklarasi state yang dijaga oleh swarm: bila container mati, manajer membuat pengganti di node yang tersedia.

Mode:
- **replicated** (default): jumlah replika ditentukan.
- **global**: satu task per node (cocok untuk agen monitoring).

## Jebakan
- `--publish 80:80` sama dengan `published=80,target=80`; pada ingress mesh, port didengar di **semua** node.
- `docker run` tidak sama dengan `docker service create` — yang pertama tidak dijadwalkan ulang.
- Menghapus service menghapus task dan container-nya.
- `docker service ps` menampilkan riwayat task (termasuk yang gagal).

## Latihan
1. Mode service untuk satu container per node?
2. Perintah menskalakan ke 5 replika?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>--mode global</code>.</p>
<p><b>2.</b> <code>docker service scale web=5</code>.</p>
</details>
