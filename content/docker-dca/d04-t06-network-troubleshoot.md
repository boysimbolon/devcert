---
title: Troubleshooting jaringan
minutes: 20
level: Menengah
badge: lengkap
summary: Diagnosa konektivitas: iptables, DNS, rute, dan tool dalam container.
objectives:
  - Menguji konektivitas bertahap
  - Memeriksa aturan NAT
  - Mengenali masalah umum
---
## Konsep inti
```bash
docker network inspect appnet --format '{{json .Containers}}'
docker exec web ip addr show eth0
docker exec web getent hosts api
docker run --rm --network container:web nicolaka/netshoot nslookup api
docker logs <container> --tail 50
sudo iptables -t nat -L DOCKER -n | head
```

Urutan diagnosa: container up? → IP ada? → DNS resolve? → port listening di dalam? → aturan NAT/publish? → firewall host/cloud?

## Jebakan
- Port terbuka di container tetapi tidak di host = masalah publish, bukan aplikasi.
- Aplikasi yang listen di `127.0.0.1` di dalam container tidak bisa dijangkau lewat publish.
- `iptables` yang dimatikan/diubah bisa memutus NAT Docker.
- Firewall cloud (security group) sering menjadi penyebab di luar host.

## Latihan
1. Mengapa `-p 8080:80` tetap gagal bila aplikasi listen di 127.0.0.1:80?
2. Tool untuk DNS/IP test cepat di container?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena publish meneruskan ke IP container, bukan loopback di dalamnya.</p>
<p><b>2.</b> <code>nicolaka/netshoot</code> (atau <code>alpine</code> dengan <code>nslookup</code>/<code>ping</code>).</p>
</details>
