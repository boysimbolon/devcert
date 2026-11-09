---
title: Menulis dan Menjalankan JPQL
minutes: 22
level: Menengah
badge: lengkap
summary: Query berbasis entity, join fetch, agregasi, constructor expression, dan named query.
objectives:
  - Menulis SELECT, UPDATE, DELETE JPQL yang benar
  - Menghindari N+1 dengan JOIN FETCH
  - Memakai parameter, named query, dan constructor expression
---
## Kenapa topik ini diuji
JPQL menguji pemahaman model, bukan SQL. Soal menanyakan hasil query, penyebab `LazyInitializationException`, dan perbedaan join biasa dengan join fetch.

## Konsep inti
JPQL bekerja pada **entity dan field**, bukan tabel dan kolom. Nama entity peka huruf besar-kecil di beberapa provider, jadi gunakan persis seperti deklarasi kelas.

```java
// parameter binding - selalu, jangan konkatenasi string
List<Pesanan> hasil = em.createQuery(
    "SELECT p FROM Pesanan p WHERE p.status = :st ORDER BY p.tanggal DESC", Pesanan.class)
    .setParameter("st", Status.BARU)
    .setMaxResults(20)
    .getResultList();

// JOIN FETCH menyelesaikan N+1
List<Pelanggan> pel = em.createQuery(
    "SELECT DISTINCT c FROM Pelanggan c JOIN FETCH c.pesanan WHERE c.aktif = true", Pelanggan.class)
    .getResultList();

// constructor expression
List<Ringkasan> ring = em.createQuery(
    "SELECT NEW id.app.Ringkasan(p.kode, COUNT(i), SUM(i.harga)) " +
    "FROM Pesanan p JOIN p.item i GROUP BY p.kode HAVING COUNT(i) > 2", Ringkasan.class)
    .getResultList();

// bulk update - tidak memicu callback entity, cache bisa basi
int n = em.createQuery("UPDATE Pesanan p SET p.status = :s WHERE p.tanggal < :t")
          .setParameter("s", Status.KEDALUWARSA)
          .setParameter("t", batas).executeUpdate();
```

Named query dideklarasikan sekali dan biasanya lebih cepat karena bisa di-precompile provider:

```java
@Entity
@NamedQuery(name = "Pesanan.aktif", query = "SELECT p FROM Pesanan p WHERE p.status = :s")
public class Pesanan { }
```

## Jebakan ujian
- `JOIN FETCH` pada koleksi `@OneToMany` butuh `DISTINCT` untuk menghindari duplikat induk.
- Bulk `UPDATE`/`DELETE` melewati lifecycle callback dan tidak menyegarkan entity yang sudah managed.
- `LazyInitializationException` terjadi saat mengakses koleksi LAZY di luar transaksi/persistence context.
- JPQL tidak mengenal `SELECT *`; tulis `SELECT p FROM Pesanan p`.
- `:param` untuk parameter bernama, `?1` untuk posisional; mencampur keduanya tidak boleh.

## Latihan
1. Mengapa query dengan `JOIN FETCH` mengembalikan induk ganda?
2. Apakah `@PreUpdate` dipanggil pada bulk update JPQL?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena setiap baris anak menghasilkan satu baris hasil; solusinya <code>SELECT DISTINCT</code> atau <code>HINT_PASS_DISTINCT_THROUGH</code> pada provider yang mendukung.</p>
<p><b>2.</b> Tidak. Bulk operation langsung ke DB dan melewati callback serta cache.</p>
</details>
