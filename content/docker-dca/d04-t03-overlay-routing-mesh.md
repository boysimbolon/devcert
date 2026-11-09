---
title: Overlay network dan routing mesh
minutes: 24
level: Menengah
badge: lengkap
summary: Jaringan lintas node, ingress mesh, dan publish mode host.
objectives:
  - Membuat overlay network
  - Menjelaskan routing mesh
  - Memilih ingress atau host publish
---
## Konsep inti
```bash
docker network create -d overlay --attachable appnet

docker service create --name web --network appnet --publish published=80,target=8080 --replicas 3 nginx
docker service create --name agent --publish published=9000,target=9000,mode=host --mode global agent
```

**Routing mesh (ingress)**: port yang dipublish didengar di **semua** node swarm; trafik masuk ke node mana pun diteruskan ke task yang tersedia. `mode=host` melewati mesh sehingga port hanya terbuka di node yang menjalankan task.

Overlay memakai VXLAN (UDP 4789) dan control plane gossip (7946).

## Jebakan
- Overlay non-attachable tidak bisa dipakai `docker run` di luar swarm.
- `mode=host` dengan beberapa replika pada node yang sama → bentrok port.
- Ingress mesh tidak memberi load balancing aplikasi (hanya L3/L4).
- Overlay butuh port 4789/7946 terbuka antar node.

## Latihan
1. Mode publish agar port hanya di node task?
2. Protokol enkapsulasi overlay?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>mode=host</code>.</p>
<p><b>2.</b> VXLAN (UDP 4789).</p>
</details>
