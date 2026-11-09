---
title: Collectors: grouping, partitioning, reduction
minutes: 24
level: Menengah
badge: lengkap
summary: groupingBy, partitioningBy, mapping, teeing, dan stream paralel.
objectives:
  - Menulis groupingBy dengan downstream collector
  - Membedakan groupingBy dan partitioningBy
  - Menjelaskan risiko stream paralel
---
## Kenapa topik ini diuji
Soal meminta struktur hasil koleksi dari `groupingBy` bertingkat.

## Konsep inti
```java
record Karyawan(String dept, String nama, int gaji, boolean aktif) {}

Map<String, Long> perDept = data.stream()
    .collect(Collectors.groupingBy(Karyawan::dept, Collectors.counting()));

Map<Boolean, List<Karyawan>> part = data.stream()
    .collect(Collectors.partitioningBy(Karyawan::aktif));   // selalu 2 kunci

Map<String, Integer> total = data.stream()
    .collect(Collectors.groupingBy(Karyawan::dept,
             Collectors.summingInt(Karyawan::gaji)));

String ringkas = data.stream().collect(Collectors.teeing(
    Collectors.counting(), Collectors.averagingInt(Karyawan::gaji),
    (n, avg) -> n + " orang, rata-rata " + avg));
```

## Jebakan
- `partitioningBy` selalu menghasilkan dua entri (`true`/`false`), `groupingBy` hanya kunci yang ada.
- `groupingBy` default memakai `HashMap`; urutan hasil tidak terjamin.
- `toMap` dengan kunci duplikat → `IllegalStateException` (butuh merge function).
- Stream paralel untuk data kecil biasanya lebih lambat dan berisiko race pada state bersama.

## Latihan
1. Collector untuk membagi dua kelompok berdasarkan boolean?
2. Mengapa `toMap` bisa gagal pada kunci duplikat?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>Collectors.partitioningBy</code>.</p>
<p><b>2.</b> Karena tidak ada cara menentukan nilai mana yang dipakai; sediakan merge function.</p>
</details>
