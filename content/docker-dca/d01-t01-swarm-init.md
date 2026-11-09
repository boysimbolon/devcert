---
title: Menyiapkan cluster swarm
minutes: 22
level: Menengah
badge: lengkap
summary: Inisialisasi swarm, join token, dan kuorum manajer.
objectives:
  - Menginisialisasi swarm mode
  - Menambahkan worker dan manajer
  - Menghitung kuorum
---
## Kenapa topik ini diuji
Domain Orchestration 25% — soal hampir selalu mulai dari "bagaimana node bergabung".

## Konsep inti
```bash
docker swarm init --advertise-addr 10.0.0.5
# output memberi perintah join untuk worker dan manager

docker swarm join --token SWMTKN-1-xxx 10.0.0.5:2377      # worker
docker swarm join --token SWMTKN-1-yyy 10.0.0.5:2377      # manager

docker node ls
docker swarm join-token worker          # lihat token
docker swarm join-token --rotate manager
docker node promote node2
docker node demote node2
docker swarm leave --force
```

Kuorum Raft: `(N/2)+1`. 3 manajer → toleransi 1 gagal; 5 → 2 gagal. Jumlah manajer ganjil disarankan (3 atau 5).

Port yang dipakai: **2377** (manajemen swarm), **7946** TCP/UDP (gossip), **4789** UDP (VXLAN overlay).

## Jebakan
- `--advertise-addr` penting pada host multi-NIC; salah pilih = node lain tidak bisa join.
- Enam manajer bukan lebih baik: kuorum jadi lebih rapuh.
- Worker tidak bisa menjalankan `docker service` (bukan manajer).
- `docker swarm leave` pada manajer terakhir butuh `--force`.

## Latihan
1. Berapa manajer minimum agar tahan 1 kegagalan?
2. Port apa untuk trafik overlay?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tiga (kuorum 2).</p>
<p><b>2.</b> UDP 4789.</p>
</details>
