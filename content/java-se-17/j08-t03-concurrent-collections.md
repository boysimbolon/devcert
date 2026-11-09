---
title: Koleksi konkuren dan stream paralel
minutes: 22
level: Menengah
badge: lengkap
summary: ConcurrentHashMap, CopyOnWriteArrayList, BlockingQueue, dan parallel stream.
objectives:
  - Memilih koleksi aman untuk akses bersamaan
  - Menjelaskan jebakan parallel stream
  - Menghindari ConcurrentModificationException
---
## Kenapa topik ini diuji
Soal menanyakan koleksi mana yang tepat dan apa risiko stream paralel.

## Konsep inti
```java
var map = new ConcurrentHashMap<String, Integer>();
map.merge("a", 1, Integer::sum);          // atomik

var list = new CopyOnWriteArrayList<String>();   // aman untuk baca-dominan
var q = new LinkedBlockingQueue<String>();
q.put("a");                                // blocking bila penuh
String v = q.take();                       // blocking bila kosong

long total = data.parallelStream().mapToLong(Double::longValue).sum();
```

`ConcurrentHashMap` tidak mengizinkan `null` key/value dan iterator-nya *weakly consistent* (tidak melempar CME).

## Jebakan
- `Collections.synchronizedMap` masih butuh sinkronisasi saat iterasi.
- Parallel stream memakai `ForkJoinPool.commonPool`; jangan untuk I/O atau data kecil.
- State mutable yang dibagi dalam `forEach` paralel → hasil salah.
- `HashMap` di banyak thread bisa merusak struktur internal.

## Latihan
1. Map aman untuk update bersamaan tanpa lock eksternal?
2. Mengapa parallel stream buruk untuk panggilan I/O?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ConcurrentHashMap</code>.</p>
<p><b>2.</b> Karena memakai commonPool dengan thread terbatas sehingga I/O memblokir task lain.</p>
</details>
