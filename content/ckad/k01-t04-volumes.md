---
title: Volume untuk aplikasi
minutes: 22
level: Menengah
badge: lengkap
summary: emptyDir, ConfigMap/Secret volume, PVC, dan StorageClass.
objectives:
  - Memilih jenis volume
  - Menulis PVC dan memakainya
  - Memakai subPath
---
## Konsep inti
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata: { name: data }
spec:
  accessModes: ["ReadWriteOnce"]
  resources: { requests: { storage: 1Gi } }
---
apiVersion: v1
kind: Pod
metadata: { name: db }
spec:
  containers:
    - name: app
      image: nginx:1.27
      volumeMounts:
        - { name: data, mountPath: /var/lib/data }
        - { name: config, mountPath: /etc/app/config.yaml, subPath: config.yaml }
  volumes:
    - name: data
      persistentVolumeClaim: { claimName: data }
    - name: config
      configMap: { name: app-config }
```

| Volume | Umur data |
|---|---|
| `emptyDir` | selama Pod ada |
| `hostPath` | selama node ada (tidak portabel) |
| PVC | independen dari Pod |
| `configMap`/`secret` | mengikuti objek |
| `projected` | gabungan beberapa sumber |

## Jebakan
- PVC `Pending` bisa berarti tidak ada PV/StorageClass yang cocok, **atau** StorageClass ber-mode `WaitForFirstConsumer` yang baru mengikat setelah ada Pod memakainya. Cek `kubectl describe pvc`.
- `subPath` mencegah direktori tujuan tertimpa seluruhnya.
- `ReadWriteOnce` mengikat ke satu node, bukan satu Pod.
- Menghapus Pod tidak menghapus PVC (data tetap ada, biaya tetap jalan).

## Latihan
1. Volume sementara yang hilang bersama Pod?
2. Mengapa memakai subPath saat mount ConfigMap?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>emptyDir</code>.</p>
<p><b>2.</b> Agar hanya satu berkas yang dipasang, bukan menimpa seluruh direktori tujuan.</p>
</details>
