---
title: Stream dan lambda
minutes: 24
level: Menengah
badge: lengkap
summary: Pipeline, lazy evaluation, source, intermediate vs terminal operation.
objectives:
  - Menjelaskan sifat lazy stream
  - Membedakan operasi intermediate dan terminal
  - Memakai primitive stream
---
## Kenapa topik ini diuji
Tanpa terminal operation, stream tidak melakukan apa pun — ini soal favorit.

## Konsep inti
```java
var hasil = Stream.of("a", "bb", "ccc")
    .filter(s -> s.length() > 1)     // lazy
    .map(String::toUpperCase)        // lazy
    .sorted()                        // stateful
    .toList();                       // terminal
System.out.println(hasil);           // [BB, CCC]

IntStream.rangeClosed(1, 5).sum();   // 15
Stream.iterate(1, n -> n * 2).limit(4).forEach(System.out::print); // mencetak 1248
```

Aturan: satu stream hanya dipakai sekali (terminal kedua → `IllegalStateException`).

## Jebakan
- `peek` bukan terminal; tanpa terminal tidak ada eksekusi.
- Stream tidak mengubah sumber (`sorted` pada stream list tidak mengurutkan list).
- Infinite stream tanpa `limit` menggantung.
- Autoboxing `IntStream` ↔ `Stream<Integer>` perlu `boxed()`.

## Latihan
1. Mengapa `stream.peek(System.out::println);` mencetak kosong?
2. Apa yang terjadi bila terminal dipanggil dua kali?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena tidak ada terminal operation, pipeline tidak dieksekusi.</p>
<p><b>2.</b> <code>IllegalStateException</code> — stream sudah dikonsumsi.</p>
</details>
