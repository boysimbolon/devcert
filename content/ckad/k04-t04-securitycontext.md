---
title: SecurityContext
minutes: 22
level: Menengah
badge: lengkap
summary: runAsUser, fsGroup, readOnlyRootFilesystem, dan capabilities.
objectives:
  - Menetapkan user dan group
  - Mengunci filesystem root
  - Mengatur capability
---
## Konsep inti
```yaml
spec:
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
  containers:
    - name: app
      image: nginx:1.27
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
          add: ["NET_BIND_SERVICE"]
      volumeMounts:
        - { name: tmp, mountPath: /tmp }
        - { name: cache, mountPath: /var/cache/nginx }
  volumes:
    - { name: tmp, emptyDir: {} }
    - { name: cache, emptyDir: {} }
```

Level Pod berlaku sebagai default; level container menimpa.

## Jebakan
- `readOnlyRootFilesystem: true` membuat nginx gagal start tanpa volume untuk `/var/cache/nginx`, `/var/run`.
- `fsGroup` memengaruhi kepemilikan volume (bukan image).
- `allowPrivilegeEscalation: false` mencegah setuid.
- `runAsNonRoot: true` gagal bila image berjalan sebagai root tanpa `runAsUser`.

## Latihan
1. Field untuk mengatur grup pemilik volume?
2. Mengapa readOnlyRootFilesystem membuat aplikasi crash?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>fsGroup</code>.</p>
<p><b>2.</b> Karena aplikasi perlu menulis ke path di root filesystem; sediakan emptyDir untuk path tersebut.</p>
</details>
