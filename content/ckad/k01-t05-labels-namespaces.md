---
title: Label, selector, dan namespace
minutes: 18
level: Dasar
badge: lengkap
summary: Menandai objek, memfilter, dan memisahkan lingkungan.
objectives:
  - Memakai label dan selector
  - Memfilter dengan kubectl
  - Bekerja dengan namespace
---
## Konsep inti
```bash
kubectl label pod app tier=backend env=prod --overwrite
kubectl get pods -l 'env=prod,tier!=frontend'
kubectl get pods -l 'env in (prod,staging)'
kubectl get all -n dev
kubectl config set-context --current --namespace=dev

kubectl create namespace dev --dry-run=client -o yaml | kubectl apply -f -
```

Selector pada Service/Deployment memakai `matchLabels` (kesetaraan) atau `matchExpressions` (`In`, `NotIn`, `Exists`, `DoesNotExist`).

## Jebakan
- Selector Service yang tidak cocok dengan label Pod → endpoint kosong (koneksi gagal).
- `kubectl get pods` hanya namespace aktif; gunakan `-A` untuk semua.
- Label berbeda dari annotation: label dipakai selector, annotation untuk metadata.
- Mengubah label Pod bisa memutus Service tanpa error.

## Latihan
1. Arti `-l 'env in (prod,staging)'`?
2. Mengapa Service bisa punya endpoint kosong?

<details><summary>Jawaban</summary>
<p><b>1.</b> Memfilter objek dengan label <code>env</code> bernilai <code>prod</code> atau <code>staging</code>.</p>
<p><b>2.</b> Karena selector-nya tidak cocok dengan label Pod mana pun.</p>
</details>
