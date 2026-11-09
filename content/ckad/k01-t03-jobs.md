---
title: Job dan CronJob
minutes: 20
level: Menengah
badge: lengkap
summary: Tugas sekali jalan, paralelisme, retry, dan jadwal.
objectives:
  - Menulis Job dengan benar
  - Mengatur paralelisme dan retry
  - Menulis CronJob
---
## Konsep inti
```yaml
apiVersion: batch/v1
kind: Job
metadata: { name: hitung }
spec:
  completions: 4
  parallelism: 2
  backoffLimit: 3
  ttlSecondsAfterFinished: 120
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: kerja
          image: busybox:1.36
          command: ["sh", "-c", "echo memproses; sleep 2"]
---
apiVersion: batch/v1
kind: CronJob
metadata: { name: laporan }
spec:
  schedule: "*/5 * * * *"
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 2
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: cetak
              image: busybox:1.36
              command: ["sh", "-c", "date"]
```

## Jebakan
- `restartPolicy` pada Job hanya boleh `Never` atau `OnFailure` (bukan `Always`).
- `backoffLimit` menghitung kegagalan Pod; 0 = tanpa retry.
- `concurrencyPolicy`: `Allow` (default), `Forbid`, `Replace`.
- CronJob memakai zona waktu controller manager; `timeZone` didukung pada versi baru.
- Job yang selesai tetap ada sampai dihapus (gunakan `ttlSecondsAfterFinished`).

## Latihan
1. Restart policy yang valid untuk Job?
2. Arti `parallelism: 2` dengan `completions: 4`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>Never</code> atau <code>OnFailure</code>.</p>
<p><b>2.</b> Dua Pod berjalan bersamaan, total empat penyelesaian sukses dibutuhkan.</p>
</details>
