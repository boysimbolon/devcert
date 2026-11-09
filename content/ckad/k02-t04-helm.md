---
title: Dasar Helm
minutes: 20
level: Menengah
badge: lengkap
summary: Chart, values, install/upgrade/rollback, dan render template.
objectives:
  - Memasang dan memperbarui release
  - Menimpa values
  - Melihat manifest hasil render
---
## Konsep inti
```bash
helm create web
helm lint web
helm template web ./web -f values-prod.yaml
helm install web ./web --namespace prod --create-namespace -f values-prod.yaml
helm upgrade web ./web --set image.tag=1.28
helm history web -n prod
helm rollback web 1 -n prod
helm list -A
helm uninstall web -n prod
```

Struktur chart: `Chart.yaml`, `values.yaml`, `templates/`, `charts/`. Template memakai Go template dengan `.Values`, `.Release`, `.Chart`.

## Jebakan
- `helm upgrade --install` aman untuk CI (idempotent).
- `--set` menimpa values file; urutan prioritas: `--set` > `-f` terakhir > `values.yaml`.
- `helm rollback` butuh nomor revisi, bukan nama.
- Namespace harus ada atau pakai `--create-namespace`.

## Latihan
1. Perintah melihat manifest tanpa instalasi?
2. Perintah kembali ke revisi pertama?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>helm template</code>.</p>
<p><b>2.</b> <code>helm rollback &lt;release&gt; 1 -n &lt;ns&gt;</code>.</p>
</details>
