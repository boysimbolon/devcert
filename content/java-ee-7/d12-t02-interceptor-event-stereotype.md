---
title: Interceptor, Event, dan Stereotype CDI
minutes: 22
level: Menengah
badge: lengkap
summary: Memisahkan concern lintas potong, komunikasi longgar lewat event, dan pengelompokan anotasi.
objectives:
  - Menulis interceptor dengan binding sendiri
  - Memancarkan dan mengamati event, termasuk yang transaksional
  - Membuat stereotype untuk konfigurasi berulang
---
## Kenapa topik ini diuji
Soal menguji urutan dan cakupan: event sinkron vs asinkron, dan mengapa interceptor tidak jalan.

## Konsep inti
```java
@InterceptorBinding
@Retention(RUNTIME) @Target({METHOD, TYPE})
public @interface Diaudit { }

@Diaudit
@Interceptor
@Priority(Interceptor.Priority.APPLICATION)
public class AuditInterceptor {
    @Inject AuditLog log;
    @AroundInvoke
    public Object catat(InvocationContext ctx) throws Exception {
        log.tulis("masuk " + ctx.getMethod().getName());
        return ctx.proceed();
    }
}

public class PesananDibuat { public final long id; public PesananDibuat(long id){this.id=id;} }

@ApplicationScoped
public class Penerbit {
    @Inject Event<PesananDibuat> event;
    public void buat(long id) {
        event.fire(new PesananDibuat(id));
        event.fireAsync(new PesananDibuat(id));
    }
}

@ApplicationScoped
public class Pendengar {
    public void pada(@Observes PesananDibuat e) { }
    public void setelahCommit(@Observes(during = TransactionPhase.AFTER_SUCCESS) PesananDibuat e) { }
}

@Stereotype @RequestScoped @Named
@Retention(RUNTIME) @Target(TYPE)
public @interface Halaman { }
```

## Jebakan ujian
- Interceptor hanya jalan bila bean dipanggil lewat proxy, bukan self-invocation.
- `@Priority` menentukan urutan; tanpa itu interceptor tidak aktif di CDI 1.1.
- `AFTER_SUCCESS` hanya terpanggil bila transaksi commit.
- Event asinkron butuh penanganan exception terpisah lewat `CompletionStage`.
- Stereotype membawa scope; menambah scope lain di bean bisa konflik.

## Latihan
1. Mengapa interceptor tidak berjalan saat method memanggil method lain di bean yang sama?
2. Fase transaksi apa untuk bereaksi setelah data benar-benar tersimpan?

<details><summary>Jawaban</summary>
<p><b>1.</b> Pemanggilan internal tidak melewati proxy, jadi rantai interceptor dilewati.</p>
<p><b>2.</b> <code>TransactionPhase.AFTER_SUCCESS</code>.</p>
</details>
