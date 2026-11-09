---
title: Node label dan constraint penempatan
minutes: 20
level: Menengah
badge: lengkap
summary: Menandai node dan mengendalikan penempatan task.
objectives:
  - Menambahkan label ke node
  - Menulis constraint penempatan
  - Memakai drain untuk pemeliharaan
---
## Konsep inti
```bash
docker node update --label-add tier=db node1
docker node inspect --format '{{.Spec.Labels}}' node1

docker service create --name db --constraint 'node.labels.tier==db' postgres:16
docker service create --name ap --placement-pref 'spread=node.labels.zone' nginx

docker node update --availability drain node1    # kosongkan untuk maintenance
docker node update --availability active node1
```

Availability: `active` (bisa menerima task), `pause` (tidak menerima task baru), `drain` (task dipindahkan keluar).

Constraint bawaan: `node.role==manager`, `node.hostname==node1`, `node.labels.<key>==<value>`, `engine.labels.<key>`.

## Jebakan
- Label harus ada di node sebelum task dijadwalkan; constraint tidak cocok = task `pending`.
- `drain` memindahkan task, tetapi volume lokal tidak ikut pindah.
- `--constraint` berbeda dari `--placement-pref` (pref hanya preferensi, bukan syarat).
- Label node bukan label container (`docker run --label`).

## Latihan
1. Perintah mengosongkan node untuk maintenance?
2. Apa yang terjadi bila tidak ada node yang cocok dengan constraint?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>docker node update --availability drain node1</code>.</p>
<p><b>2.</b> Task tetap <code>pending</code> sampai ada node yang cocok.</p>
</details>
