---
title: Kuorum manajer dan pemulihan
minutes: 18
level: Menengah
badge: lengkap
summary: Menjaga ketersediaan kontrol plane dan memulihkan cluster.
objectives:
  - Menghitung kuorum
  - Menangani kehilangan manajer
  - Memulihkan dari backup
---
## Konsep inti
```bash
docker node ls                          # kolom MANAGER STATUS: Leader/Reachable/Unreachable
docker node promote node3
docker node demote node2
docker swarm init --force-new-cluster   # pada manajer yang tersisa
```

Kuorum: 3 manajer tahan 1 gagal; 5 manajer tahan 2 gagal. Jika kuorum hilang, perubahan state ditolak (service tidak bisa di-update) meski container yang berjalan tetap hidup.

`--force-new-cluster` memulihkan cluster dari satu manajer yang tersisa, tetapi state mungkin tertinggal dan node lain harus join ulang.

## Jebakan
- Menambah manajer genap tidak menambah toleransi (4 manajer tetap tahan 1).
- Kehilangan kuorum ≠ container berhenti; hanya kontrol plane yang membeku.
- `--force-new-cluster` menghapus konfigurasi lain; gunakan sebagai upaya terakhir.
- Backup state swarm tidak tersedia sebagai perintah resmi; lindungi disk manajer.

## Latihan
1. Toleransi kegagalan dengan 5 manajer?
2. Apa yang terjadi bila kuorum hilang?

<details><summary>Jawaban</summary>
<p><b>1.</b> Dua manajer.</p>
<p><b>2.</b> Perubahan state ditolak; container yang sudah berjalan tetap jalan.</p>
</details>
