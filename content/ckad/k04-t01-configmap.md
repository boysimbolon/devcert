---
title: ConfigMap
minutes: 22
level: Dasar
badge: lengkap
summary: Membuat ConfigMap dari literal, file, atau env; memakainya sebagai env dan volume.
objectives:
  - Membuat ConfigMap dengan tiga cara
  - Mengonsumsi sebagai env dan volume
  - Menangani perubahan konfigurasi
---
## Konsep inti
```bash
kubectl create configmap app-config --from-literal=LOG_LEVEL=debug
kubectl create configmap app-file --from-file=config.yaml
kubectl create configmap app-env --from-env-file=app.env
kubectl get cm app-config -o yaml
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata: { name: app-config }
data:
  LOG_LEVEL: debug
  config.yaml: |
    server:
      port: 8080
```

Pemakaian:

```yaml
env:
  - name: LOG_LEVEL
    valueFrom: { configMapKeyRef: { name: app-config, key: LOG_LEVEL } }
envFrom:
  - configMapRef: { name: app-config }
volumes:
  - name: cfg
    configMap: { name: app-config, items: [{ key: config.yaml, path: config.yaml }] }
```

## Jebakan
- Env dari ConfigMap **tidak** ikut berubah saat ConfigMap diubah; butuh restart Pod.
- Volume ConfigMap diperbarui otomatis (kecuali `subPath`).
- Pod gagal start (`CreateContainerConfigError`) bila key ConfigMap tidak ada dan `optional` tidak diset.
- `--from-env-file` berbeda dari `--from-file` (yang membuat satu key per file).

## Latihan
1. Cara mengonsumsi semua key sebagai env?
2. Apakah env dari ConfigMap ter-update otomatis?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>envFrom: [{ configMapRef: { name: ... } }]</code>.</p>
<p><b>2.</b> Tidak; perlu restart Pod (volume yang otomatis).</p>
</details>
