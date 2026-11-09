---
title: Batch API dan JobOperator
minutes: 22
level: Menengah
badge: lengkap
summary: Menjalankan, menghentikan, dan melanjutkan job batch secara programatik.
objectives:
  - Memakai JobOperator untuk start, stop, dan restart
  - Menginjeksi BatchProperty ke komponen
  - Membaca status eksekusi
---
## Kenapa topik ini diuji
Soal menanyakan API mana untuk memulai job dan bagaimana parameter sampai ke step.

## Konsep inti
```java
@Stateless
public class PemicuBatch {

    @Resource(lookup = "java:comp/DefaultBatchEnvironment")
    javax.batch.operations.JobOperator operator;

    public long mulai() throws Exception {
        java.util.Properties p = new java.util.Properties();
        p.setProperty("namaFile", "/data/pesanan.csv");
        return operator.start("imporPesanan", p);      // executionId
    }

    public void hentikan(long id) throws Exception { operator.stop(id); }
    public void lanjutkan(long id) throws Exception { operator.restart(id); }
    public java.util.List<Long> berjalan() throws Exception {
        return operator.getRunningExecutions("imporPesanan");
    }
}
```

```java
public class PembacaCsv implements javax.batch.api.chunk.ItemReader {
    @Inject @BatchProperty(name = "namaFile") String namaFile;
    public void open(java.io.Serializable cp) { }
    public Object readItem() { return null; }
    public void close() { }
}
```

- `executionId` dipakai untuk stop, restart, dan query status.
- Restart melanjutkan dari checkpoint terakhir, bukan dari awal.
- `@BatchProperty` mengikat properti job XML ke field; nilainya String kecuali dikonversi.
- Job repository butuh tabel DB; container biasanya menyiapkan skema default.

## Jebakan ujian
- Java EE 7 memakai paket `javax.batch.*`; `jakarta.batch.*` baru pada versi setelahnya.
- `restart` hanya untuk job yang gagal atau berhenti, bukan yang sedang berjalan.
- `@BatchProperty` dengan nilai kosong menghasilkan string kosong, bukan null.
- JobOperator di-inject lewat `@Resource`, bukan `@Inject`.
- Status eksekusi: STARTING, STARTED, COMPLETED, FAILED, STOPPED, ABANDONED.

## Latihan
1. API untuk melanjutkan job yang gagal?
2. Dari mana nilai `@BatchProperty` berasal?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>JobOperator.restart(executionId)</code>.</p>
<p><b>2.</b> Properti yang dikirim saat <code>start()</code> dan atribut pada JSL.</p>
</details>
