---
title: Concurrency Utilities di Java EE
minutes: 22
level: Menengah
badge: lengkap
summary: ManagedExecutorService, ManagedThreadFactory, dan mengapa thread mentah dilarang.
objectives:
  - Menjelaskan larangan membuat thread di container
  - Memilih utilitas concurrency yang tepat
  - Memakai ContextService untuk memindahkan konteks
---
## Kenapa topik ini diuji
Java EE melarang `new Thread()` di komponen terkelola karena merusak lifecycle. Soal menguji alternatif yang benar.

## Konsep inti
| Utilitas | Kegunaan |
|---|---|
| ManagedExecutorService | menjalankan task asinkron |
| ManagedScheduledExecutorService | task terjadwal atau berulang |
| ManagedThreadFactory | membuat thread terkelola untuk API yang butuh ThreadFactory |
| ContextService | membungkus objek agar membawa konteks container |

```java
@Stateless
public class LaporanBean {

    @Resource(lookup = "java:comp/DefaultManagedExecutorService")
    ManagedExecutorService executor;

    @Resource(lookup = "java:comp/DefaultManagedScheduledExecutorService")
    ManagedScheduledExecutorService penjadwal;

    @Resource
    ContextService contextService;

    public Future<Integer> hitungAsync() {
        return executor.submit(() -> 42);
    }

    public void tiapMenit(Runnable r) {
        penjadwal.scheduleAtFixedRate(
            contextService.createContextualProxy(r, Runnable.class),
            0, 60, java.util.concurrent.TimeUnit.SECONDS);
    }
}
```

- `@Asynchronous` pada EJB adalah cara paling sederhana; utilitas ini untuk kontrol lebih besar.
- `ManagedExecutorService` bisa didefinisikan lewat `@ManagedExecutorDefinition` atau `web.xml`.
- Konteks keamanan tidak otomatis terbawa; gunakan `ContextService` bila perlu propagasi.

## Jebakan ujian
- `new Thread()` di EJB atau servlet melanggar spesifikasi.
- `synchronized` pada objek container-managed tidak menjamin apa pun karena instance bisa berbeda.
- `Future.get()` memblokir thread pemanggil; selalu beri timeout.
- Executor default dipakai bersama aplikasi lain.
- Exception di dalam task tidak otomatis ter-log; bungkus dengan try/catch.

## Latihan
1. Apa pengganti `new Thread` di dalam EJB?
2. Utilitas untuk propagasi konteks keamanan ke task?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ManagedExecutorService</code> atau <code>@Asynchronous</code>.</p>
<p><b>2.</b> <code>ContextService</code>.</p>
</details>
