---
title: Kustomize
minutes: 20
level: Menengah
badge: lengkap
summary: Overlay, patch, dan penamaan tanpa template.
objectives:
  - Membuat kustomization dasar
  - Menambal manifest dengan patch
  - Menerapkan dengan kubectl -k
---
## Konsep inti
```yaml
# kustomization.yaml (overlay prod)
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
namespace: prod
namePrefix: prod-
resources:
  - ../../base
images:
  - name: nginx
    newTag: "1.28"
commonLabels:
  env: prod
patches:
  - path: replica-patch.yaml
```

```yaml
# replica-patch.yaml
apiVersion: apps/v1
kind: Deployment
metadata: { name: web }
spec: { replicas: 6 }
```

```bash
kubectl kustomize overlays/prod      # render
kubectl apply -k overlays/prod
```

## Jebakan
- `namePrefix` mengubah nama resource; selector pada Service ikut disesuaikan otomatis, tetapi referensi manual di ConfigMap tidak.
- Patch tanpa `metadata.name` yang cocok tidak berefek.
- `kubectl apply -k` butuh direktori berisi `kustomization.yaml`.
- Field `commonLabels` juga menambah label ke selector (hati-hati pada Deployment yang sudah ada).

## Latihan
1. Perintah menerapkan overlay Kustomize?
2. Apa efek `namePrefix` pada Service dan Deployment?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>kubectl apply -k &lt;direktori&gt;</code>.</p>
<p><b>2.</b> Nama objek diberi prefiks dan referensi internal yang dikenal Kustomize ikut disesuaikan.</p>
</details>
