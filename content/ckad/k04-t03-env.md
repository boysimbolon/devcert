---
title: Environment variable lanjutan
minutes: 18
level: Dasar
badge: lengkap
summary: valueFrom, fieldRef, resourceFieldRef, dan urutan prioritas.
objectives:
  - Memakai env dari field Pod
  - Menggabungkan env dan envFrom
  - Menghindari konflik nama
---
## Konsep inti
```yaml
env:
  - name: POD_NAME
    valueFrom: { fieldRef: { fieldPath: metadata.name } }
  - name: NODE_NAME
    valueFrom: { fieldRef: { fieldPath: spec.nodeName } }
  - name: MEMORY_LIMIT
    valueFrom: { resourceFieldRef: { containerName: web, resource: limits.memory } }
  - name: STATIS
    value: "42"
envFrom:
  - configMapRef: { name: app-config }
  - secretRef: { name: db-pass }
```

## Jebakan
- `env` menimpa nilai dari `envFrom` bila nama sama.
- `fieldRef` hanya mendukung field tertentu (`metadata.name`, `metadata.namespace`, `spec.nodeName`, `status.podIP`).
- Variabel dari Secret akan terlihat di `kubectl describe pod`? Tidak nilainya, tetapi nama variabelnya terlihat.
- Mengubah env butuh recreate Pod (bukan update in-place).

## Latihan
1. Cara mendapatkan nama Pod sebagai env?
2. Mana yang menang bila nama env sama di `env` dan `envFrom`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>fieldRef</code> ke <code>metadata.name</code>.</p>
<p><b>2.</b> <code>env</code> eksplisit.</p>
</details>
