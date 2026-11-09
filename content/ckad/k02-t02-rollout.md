---
title: Rolling update dan rollback
minutes: 22
level: Menengah
badge: lengkap
summary: Status rollout, riwayat revisi, undo, dan pause.
objectives:
  - Memantau rollout
  - Melakukan rollback ke revisi tertentu
  - Menghentikan rollout yang bermasalah
---
## Konsep inti
```bash
kubectl rollout status deployment/web
kubectl rollout history deployment/web
kubectl rollout history deployment/web --revision=2
kubectl rollout undo deployment/web
kubectl rollout undo deployment/web --to-revision=1
kubectl rollout pause deployment/web
kubectl rollout resume deployment/web
kubectl annotate deployment/web kubernetes.io/change-cause="naik ke 1.28"
```

## Jebakan
- `rollout undo` membuat revisi baru (nomor bertambah), bukan menghapus riwayat.
- Tanpa `--record`/annotation `change-cause`, riwayat hanya berisi nomor.
- `rollout status` bisa menggantung bila Pod tidak pernah siap; batasi dengan `--timeout=60s`.
- `pause` menahan perubahan, tetapi `undo` saat paused tidak berjalan sampai `resume`.

## Latihan
1. Perintah kembali ke revisi 1?
2. Mengapa perubahan cause penting?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>kubectl rollout undo deployment/web --to-revision=1</code>.</p>
<p><b>2.</b> Agar riwayat revisi bisa dibaca manusia saat perlu rollback.</p>
</details>
