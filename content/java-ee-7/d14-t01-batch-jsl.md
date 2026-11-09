---
title: Job Batch dengan JSL
minutes: 22
level: Menengah
badge: lengkap
summary: Struktur job XML, step chunk vs batchlet, dan listener.
objectives:
  - Menulis JSL dengan step, chunk, dan batchlet
  - Menentukan ukuran chunk dan checkpoint
  - Menambahkan listener job dan step
---
## Kenapa topik ini diuji
Batch 1.0 menguji kemampuan membaca XML job dan memetakan komponen ke elemen.

## Konsep inti
```xml
<!-- META-INF/batch-jobs/imporPesanan.xml -->
<job id="imporPesanan" xmlns="http://xmlns.jcp.org/xml/ns/javaee" version="1.0">
  <listeners>
    <listener ref="id.contoh.JobListener"/>
  </listeners>

  <step id="baca" next="tulis">
    <chunk item-count="100" checkpoint-policy="item" time-limit="60">
      <reader ref="id.contoh.PembacaCsv"/>
      <processor ref="id.contoh.Prosesor"/>
      <writer ref="id.contoh.PenulisDb"/>
    </chunk>
  </step>

  <step id="tulis">
    <batchlet ref="id.contoh.PembersihBatchlet"/>
  </step>
</job>
```

- **Chunk**: reader, processor, writer per item, commit per `item-count`. Cocok untuk data besar.
- **Batchlet**: satu pemanggilan `process()`, untuk task tunggal seperti kirim rekap email.
- `checkpoint-policy="item"` memungkinkan restart dari item terakhir yang sudah commit.
- `next` menentukan alur; tanpa itu step berjalan berurutan.
- `split` dan `flow` untuk paralelisasi.

## Jebakan ujian
- `item-count` adalah jumlah item per commit, bukan jumlah baris yang dibaca sekaligus.
- Batchlet wajib mengembalikan `String` dari method `process()`.
- `reader`/`writer` dapat memakai `@Inject` bila CDI aktif.
- Listener step menerima `StepContext`; listener job menerima `JobContext`.
- Nama file JSL harus sama dengan `job id`.

## Latihan
1. Elemen mana untuk memproses per item dengan commit berkala?
2. Apa return type `process()` pada batchlet?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>&lt;chunk&gt;</code> dengan <code>item-count</code>.</p>
<p><b>2.</b> <code>String</code> (exit status).</p>
</details>
