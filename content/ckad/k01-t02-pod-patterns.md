---
title: Pod, init container, dan pola multi-container
minutes: 22
level: Menengah
badge: lengkap
summary: Sidecar, init container, dan komunikasi antar container dalam Pod.
objectives:
  - Menulis manifest Pod lengkap
  - Memakai init container
  - Menjelaskan pola sidecar/ambassador/adapter
---
## Konsep inti
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app
  labels: { app: demo }
spec:
  initContainers:
    - name: siapkan
      image: busybox:1.36
      command: ["sh", "-c", "echo siap > /data/status"]
      volumeMounts: [{ name: data, mountPath: /data }]
  containers:
    - name: web
      image: nginx:1.27
      ports: [{ containerPort: 80 }]
      volumeMounts: [{ name: data, mountPath: /usr/share/nginx/html }]
    - name: log-agent
      image: busybox:1.36
      command: ["sh", "-c", "tail -f /var/log/nginx/access.log"]
      volumeMounts: [{ name: logs, mountPath: /var/log/nginx }]
  volumes:
    - name: data
      emptyDir: {}
    - name: logs
      emptyDir: {}
```

Init container berjalan **berurutan** sampai sukses sebelum container utama dimulai. Container dalam satu Pod berbagi network namespace (bisa `localhost`) dan volume.

## Jebakan
- Init container gagal terus → Pod berstatus `Init:CrashLoopBackOff`, bukan `Running`.
- Container dalam Pod yang sama **tidak** bisa memakai nama container sebagai hostname; gunakan `localhost`.
- `kubectl exec -c <container>` wajib bila ada beberapa container.
- Dua container tidak boleh memakai `containerPort` yang sama pada port host yang sama.
- Pod tidak bisa diubah sebagian; banyak perubahan butuh `kubectl replace --force`.

## Latihan
1. Bagaimana container sidecar mengakses aplikasi di Pod yang sama?
2. Status apa bila init container gagal?

<details><summary>Jawaban</summary>
<p><b>1.</b> Lewat <code>localhost</code> dan port yang sama.</p>
<p><b>2.</b> <code>Init:CrashLoopBackOff</code> (Pod belum <code>Running</code>).</p>
</details>
