---
title: Managed Executor dan Pola Asinkron
minutes: 20
level: Menengah
badge: lengkap
summary: Mengonfigurasi pool sendiri, timeout, dan pola hasil gabungan.
objectives:
  - Mendefinisikan ManagedExecutorService dengan anotasi definisi
  - Menggabungkan beberapa Future
  - Menangani timeout dan pembatalan
---
## Kenapa topik ini diuji
Soal skenario: banyak task paralel dengan batas waktu. Jawabannya menggabungkan executor dengan `invokeAll` dan `Future`.

## Konsep inti
```java
@ManagedExecutorDefinition(
    name = "java:app/concurrent/LaporanPool",
    maxAsync = 8,
    context = "java:app/concurrent/Propagasi")
public class KonfigurasiConcurrency { }

@Stateless
public class ParalelBean {

    @Resource(lookup = "java:app/concurrent/LaporanPool")
    ManagedExecutorService pool;

    public long total(List<Callable<Long>> tugas) throws Exception {
        List<Future<Long>> hasil = pool.invokeAll(tugas, 30, java.util.concurrent.TimeUnit.SECONDS);
        long sum = 0;
        for (Future<Long> f : hasil) {
            if (!f.isCancelled()) sum += f.get();
        }
        return sum;
    }
}
```

- `invokeAll(..., timeout)` membatalkan task yang belum selesai saat waktu habis.
- Lifecycle executor milik container; aplikasi tidak boleh menutupnya.
- Antrean penuh menghasilkan `RejectedExecutionException`; tangani agar request tidak gagal.

## Jebakan ujian
- `maxAsync` membatasi jumlah task paralel, bukan ukuran antrean.
- `invokeAll` mengembalikan Future dalam urutan yang sama dengan input, termasuk yang dibatalkan.
- `Future.cancel(true)` hanya mengirim interrupt; task yang tidak responsif tetap berjalan.
- Executor terkelola tidak boleh ditutup manual.
- Konteks transaksi tidak otomatis terbawa ke task.

## Latihan
1. Apa yang terjadi bila task melebihi batas waktu pada `invokeAll`?
2. Apakah transaksi EJB ikut ke task executor?

<details><summary>Jawaban</summary>
<p><b>1.</b> Future-nya ditandai cancelled dan task diinterupsi.</p>
<p><b>2.</b> Tidak otomatis; konteks transaksi tidak dipropagasi.</p>
</details>
