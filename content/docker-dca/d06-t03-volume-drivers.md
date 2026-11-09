---
title: Volume driver dan NFS
minutes: 20
level: Menengah
badge: lengkap
summary: Driver local, NFS, dan volume lintas node.
objectives:
  - Membuat volume dengan driver
  - Memasang NFS sebagai backend
  - Menilai opsi untuk swarm
---
## Konsep inti
```bash
docker volume create --driver local \
  --opt type=nfs --opt o=addr=10.0.0.20,rw,nfsvers=4 \
  --opt device=:/export/pgdata nfsdata

docker run -d --name db -v nfsdata:/var/lib/postgresql/data postgres:16
docker volume inspect nfsdata
```

Driver pihak ketiga (rekomendasi: plugin volume) memungkinkan EBS, Azure Disk, Portworx, dan sejenisnya. Pada swarm, volume lokal tidak ikut berpindah node.

## Jebakan
- Volume `local` dengan opsi NFS tetap terikat pada node (bukan otomatis tersedia di semua node kecuali didefinisikan di sana).
- NFS locking bisa bermasalah untuk database; uji sebelum produksi.
- Plugin volume harus dipasang di setiap node swarm.
- Menghapus volume NFS tidak menghapus data di server NFS.

## Latihan
1. Mengapa volume lokal bermasalah pada swarm?
2. Opsi driver untuk NFS?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena data hanya ada di node tempat volume dibuat; task yang pindah tidak melihat datanya.</p>
<p><b>2.</b> <code>--driver local --opt type=nfs ...</code> atau plugin volume khusus.</p>
</details>
