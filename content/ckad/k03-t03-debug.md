---
title: Debugging dengan kubectl
minutes: 22
level: Menengah
badge: lengkap
summary: exec, debug ephemeral container, port-forward, dan status Pod.
objectives:
  - Masuk ke container dan menyalin berkas
  - Memakai ephemeral container
  - Mendiagnosis status Pod
---
## Konsep inti
```bash
kubectl exec -it web -- sh
kubectl exec web -- cat /etc/config/app.yaml
kubectl cp web:/var/log/app.log ./app.log
kubectl debug -it web --image=busybox:1.36 --target=web
kubectl debug node/ckad-control-plane -it --image=busybox:1.36
kubectl port-forward svc/web 8080:80
kubectl get pod web -o jsonpath='{.status.containerStatuses[*].state}'
kubectl describe pod web
```

Status umum: `ImagePullBackOff` (nama/tag/registry/kredensial), `CrashLoopBackOff` (aplikasi keluar), `Pending` (resource/affinity/PVC), `CreateContainerConfigError` (ConfigMap/Secret hilang).

## Jebakan
- Image minimal (distroless/scratch) tidak punya shell → gunakan `kubectl debug`.
- Ephemeral container tidak bisa dihapus tanpa membuat ulang Pod.
- `port-forward` hanya untuk diagnosis, bukan solusi produksi.
- `kubectl cp` butuh `tar` di dalam container.

## Latihan
1. Cara men-debug image tanpa shell?
2. Arti `CreateContainerConfigError`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>kubectl debug</code> dengan ephemeral container.</p>
<p><b>2.</b> Container gagal dibuat karena referensi ConfigMap/Secret tidak ada.</p>
</details>
