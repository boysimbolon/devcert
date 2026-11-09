---
title: Session Bean: Sinkron, Asinkron, dan Interceptor
minutes: 25
level: Menengah
badge: lengkap
summary: Menulis business method, memakai @Asynchronous, lifecycle callback, dan memisahkan concern dengan interceptor.
objectives:
  - Memilih tipe session bean sesuai kebutuhan state
  - Menulis method @Asynchronous dengan return Future
  - Menerapkan @AroundInvoke interceptor dan binding-nya
---
## Kenapa topik ini diuji
Interceptor dan async adalah dua fitur yang sering ditanyakan dalam bentuk "apa outputnya" atau "kapan method jalan". Detail kecil seperti siapa yang membuat thread menentukan jawabannya.

## Konsep inti
```java
@Stateless
@Local
public class LaporanBean {

    @Asynchronous
    public Future<String> buatLaporan(String id) {
        // dijalankan container di thread terpisah, tidak menahan pemanggil
        return new AsyncResult<>("selesai:" + id);
    }

    @Asynchronous
    public void kirimEmail(String to) { /* fire and forget */ }

    @Schedule(hour = "*", minute = "*/5", persistent = false)
    public void sapuTahunan() { }
}
```

- `@Asynchronous` hanya pada session bean (dan MDB tidak perlu). Return type harus `void` atau `Future<T>`.
- Method async **tidak boleh** memakai transaksi yang sama dengan pemanggil; transaksi baru dimulai di method itu.
- Interceptor memisahkan cross-cutting concern:

```java
@InterceptorBinding
@Retention(RUNTIME) @Target({METHOD, TYPE})
public @interface Terlacak { }

@Terlacak
@Interceptor
@Priority(Interceptor.Priority.APPLICATION)
public class TerlacakInterceptor {
    @AroundInvoke
    public Object lacak(InvocationContext ctx) throws Exception {
        long t = System.nanoTime();
        try { return ctx.proceed(); }
        finally { System.out.println(ctx.getMethod().getName() + " " + (System.nanoTime() - t) + "ns"); }
    }
}

@Stateless
public class PesananBean {
    @Terlacak public void proses() { }
}
```

Interceptor bisa dideklarasikan dengan `@Interceptors(NamaKelas.class)` (langsung) atau lewat binding (lebih fleksibel). Urutan eksekusi diatur `@Priority`; interceptor class-level jalan sebelum method-level.

## Jebakan ujian
- `@Asynchronous` pada `@Singleton` dengan `@Lock(WRITE)` bisa membuat method async antre, bukan paralel.
- `Future.get()` memblokir; `isDone()` tidak.
- Interceptor pada `@AroundInvoke` hanya untuk business method, bukan callback lifecycle (`@PostConstruct` punya `@AroundConstruct` untuk CDI).
- Exception dari method async tidak dilempar ke pemanggil - muncul saat `Future.get()` sebagai `ExecutionException`.
- `@Schedule` default `persistent = true` hanya pada EJB timer service yang mendukung; di banyak container default-nya non-persistent.

## Latihan
1. Bolehkah `@Asynchronous` mengembalikan `String` langsung?
2. Apa yang terjadi bila dua interceptor punya `@Priority` sama?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tidak. Harus <code>void</code> atau <code>Future&lt;T&gt;</code>.</p>
<p><b>2.</b> Urutannya tidak terdefinisi secara ketat; tetapkan prioritas berbeda untuk hasil deterministik.</p>
</details>
