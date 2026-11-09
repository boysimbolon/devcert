---
title: Thread, Runnable, Callable, dan executor
minutes: 24
level: Menengah
badge: lengkap
summary: Membuat worker, mengelola siklus hidup, dan mengambil hasil Future.
objectives:
  - Membuat thread dengan Runnable dan Callable
  - Membedakan executor service
  - Mengambil hasil dari Future
---
## Kenapa topik ini diuji
Soal menanyakan API yang tepat untuk menjalankan tugas dan mengambil hasil.

## Konsep inti
```java
Runnable r = () -> System.out.println("jalan " + Thread.currentThread().getName());
new Thread(r).start();

ExecutorService pool = Executors.newFixedThreadPool(2);
Future<Integer> f = pool.submit(() -> 6 * 7);     // Callable<Integer>
System.out.println(f.get());                       // 42
pool.shutdown();
```

| API | Keterangan |
|---|---|
| `newSingleThreadExecutor` | satu worker, antrean tak terbatas |
| `newFixedThreadPool(n)` | n worker |
| `newCachedThreadPool` | membuat thread sesuai beban, bisa membengkak |
| `newScheduledThreadPool` | tugas terjadwal |
| `newVirtualThreadPerTaskExecutor` (21+) | bukan Java 17 — pakai `Executors.newCachedThreadPool` di 17 |

Siklus hidup thread: NEW → RUNNABLE → (BLOCKED/WAITING/TIMED_WAITING) → TERMINATED.

## Jebakan
- `run()` dipanggil langsung = berjalan di thread pemanggil, bukan thread baru.
- `Future.get()` memblokir dan melempar `ExecutionException` bila tugas gagal.
- ExecutorService tidak otomatis berhenti; `shutdown()` tetap perlu.
- Thread tidak bisa di-restart setelah selesai.

## Latihan
1. API untuk tugas yang mengembalikan nilai?
2. Mengapa `t.run()` bukan cara memulai thread?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>Callable</code> lewat <code>ExecutorService.submit</code>.</p>
<p><b>2.</b> Karena dieksekusi sinkron di thread saat ini; gunakan <code>t.start()</code>.</p>
</details>
