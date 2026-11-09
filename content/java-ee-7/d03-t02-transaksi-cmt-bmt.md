---
title: Transaksi Container-Managed vs Bean-Managed
minutes: 24
level: Menengah
badge: lengkap
summary: Enam atribut CMT, kapan memakai BMT, dan aturan rollback yang menjebak banyak kandidat.
objectives:
  - Menjelaskan efek REQUIRED, REQUIRES_NEW, MANDATORY, NEVER, SUPPORTS, NOT_SUPPORTED
  - Menulis BMT dengan UserTransaction atau SessionContext
  - Menerapkan aturan rollback exception
---
## Kenapa topik ini diuji
Ini domain dengan soal paling teknis: diberikan dua EJB yang saling memanggil, tentukan apakah perubahan tersimpan. Hampir selalu soal tentang atribut transaksi dan rollback.

## Konsep inti
| Atribut | Perilaku |
|---|---|
| `REQUIRED` (default) | gabung transaksi berjalan, buat baru bila tidak ada |
| `REQUIRES_NEW` | suspend transaksi berjalan, selalu buat baru |
| `SUPPORTS` | gabung bila ada, jalan tanpa transaksi bila tidak ada |
| `NOT_SUPPORTED` | suspend transaksi berjalan, jalan tanpa transaksi |
| `MANDATORY` | wajib ada transaksi, jika tidak → `TransactionRequiredException` |
| `NEVER` | tidak boleh ada transaksi, jika ada → `EJBTransactionRequiredException` |

**Rollback otomatis** terjadi bila method melempar **runtime exception** atau `RemoteException`. **Checked exception** tidak memicu rollback kecuali dianotasi `@ApplicationException(rollback = true)`.

```java
@Stateless
public class PesananBean {

    @Resource SessionContext ctx;

    @TransactionAttribute(TransactionAttributeType.REQUIRED)
    public void pesan(Pesanan p) {
        // CMT: commit di akhir method
    }

    // BMT: kontrol manual
    @TransactionAttribute(TransactionAttributeType.NOT_SUPPORTED)
    public void prosesManual(Pesanan p) throws Exception {
        javax.transaction.UserTransaction ut = ctx.getUserTransaction();
        ut.begin();
        try {
            // lakukan sesuatu
            ut.commit();
        } catch (RuntimeException e) {
            ut.rollback();
            throw e;
        }
    }

    @TransactionAttribute(TransactionAttributeType.REQUIRES_NEW)
    public void catatLog(String s) { /* commit terpisah walau pemanggil rollback */ }
}
```

`@TransactionAttribute` hanya boleh di method bisnis session bean/MDB, bukan di `@PostConstruct` atau method `static`.

## Jebakan ujian
- `REQUIRES_NEW` di method yang sama (self-invocation) tidak berlaku - proxy tidak dilewati. Panggil lewat bean lain atau `SessionContext.getBusinessObject()`.
- Checked exception tidak me-rollback transaksi secara default: baris yang sudah di-persist bisa tetap commit.
- `setRollbackOnly()` menandai transaksi untuk rollback tanpa melempar exception.
- MDB mendukung CMT; `@TransactionAttribute` hanya `REQUIRED` atau `NOT_SUPPORTED`.
- BMT: `UserTransaction` tidak boleh dipakai setelah transaksi di-commit atau di-rollback.

## Latihan
1. Method A (`REQUIRED`) memanggil method B (`REQUIRES_NEW`) lalu A melempar exception. Apakah data B tersimpan?
2. Exception apa yang otomatis me-rollback transaksi CMT?

<details><summary>Jawaban</summary>
<p><b>1.</b> Ya. Transaksi B sudah commit sebelum A gagal.</p>
<p><b>2.</b> Runtime exception dan <code>RemoteException</code>; checked exception hanya bila dianotasi <code>@ApplicationException(rollback=true)</code>.</p>
</details>
