---
title: EntityManager, Transaksi, dan Locking
minutes: 25
level: Menengah
badge: lengkap
summary: Siklus hidup entity, operasi EntityManager, batas transaksi, dan strategi locking optimistis vs pesimistis.
objectives:
  - Membedakan persist, merge, remove, find, getReference
  - Menentukan batas transaksi pada EJB dan entity
  - Memilih locking OPTIMISTIC atau PESSIMISTIC sesuai skenario
---
## Kenapa topik ini diuji
Kesalahan memakai `merge` sebagai pengganti `persist`, atau tidak memahami kapan flush terjadi, adalah dua kesalahan yang paling sering muncul di soal skenario.

## Konsep inti
Entity punya empat status: **new/transient**, **managed**, **detached**, **removed**.

| Operasi | Efek |
|---|---|
| `persist(e)` | transient → managed; insert saat flush |
| `merge(e)` | menyalin state ke instance managed baru (return value!) |
| `remove(e)` | managed → removed; delete saat flush |
| `find(Class, id)` | ambil langsung dari DB, return null bila tidak ada |
| `getReference(Class, id)` | proxy lazy, tidak hit DB sampai diakses |
| `createQuery(...)` | JPQL; `createNamedQuery` untuk named query |

Pada EJB dengan CMT, transaksi dimulai dan di-commit container di sekitar method bisnis. `em.flush()` memaksa sinkronisasi ke DB, tetapi commit tetap di akhir method.

```java
@Stateless
public class PesananRepository {
    @PersistenceContext EntityManager em;

    public Pesanan simpanBaru(Pesanan p) { em.persist(p); return p; }

    public Pesanan ubah(Pesanan detach) {
        return em.merge(detach);   // return value adalah instance managed
    }

    @TransactionAttribute(TransactionAttributeType.REQUIRES_NEW)
    public void catatAudit(String teks) { em.persist(new Audit(teks)); }
}
```

**Locking**

- Optimistis: kolom `@Version`, cek saat commit. `em.lock(e, LockModeType.OPTIMISTIC)` atau `OPTIMISTIC_FORCE_INCREMENT`. Bentrok → `OptimisticLockException`.
- Pesimistis: lock di DB (`SELECT ... FOR UPDATE`). `PESSIMISTIC_READ` (shared), `PESSIMISTIC_WRITE` (exclusive). Bentrok → `PessimisticLockException`, timeout → `LockTimeoutException`.
- Timeout lock: `em.lock(e, LockModeType.PESSIMISTIC_WRITE, Map.of("javax.persistence.lock.timeout", 5000))`.

## Jebakan ujian
- `merge` mengembalikan instance managed; mengabaikan return value membuat perubahan tidak tersimpan.
- `getReference` melempar `EntityNotFoundException` saat diakses bila baris tidak ada - bukan saat dipanggil.
- `find` pada entity yang sudah managed tidak memicu query kedua (identity map).
- Optimistic lock butuh kolom `@Version`; tanpa itu `OPTIMISTIC` praktis tidak mendeteksi konflik.
- `REQUIRES_NEW` men-suspend transaksi berjalan; perubahan pada transaksi luar belum commit dan tidak terlihat oleh transaksi baru.

## Latihan
1. Objek hasil query dilepas ke lapisan presentasi lalu dikirim balik untuk diubah. Operasi apa yang dipakai?
2. Lock apa untuk mencegah dua kasir mengambil nomor urut yang sama?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>merge</code> pada instance detached; gunakan nilai kembaliannya.</p>
<p><b>2.</b> <code>PESSIMISTIC_WRITE</code> pada baris counter, atau optimistis dengan retry bila beban baca tinggi.</p>
</details>
