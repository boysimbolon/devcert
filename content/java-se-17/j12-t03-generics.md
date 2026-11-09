---
title: Generics dan wildcard
minutes: 22
level: Menengah
badge: lengkap
summary: Tipe generik, bounded type, wildcard, dan type erasure.
objectives:
  - Menulis kelas/method generik
  - Membedakan extends dan super pada wildcard
  - Menjelaskan akibat type erasure
---
## Kenapa topik ini diuji
Soal menanyakan method call mana yang compile dengan wildcard.

## Konsep inti
```java
class Kotak<T extends Number> { T isi; }

static double jumlah(List<? extends Number> l) {   // baca aman
    double s = 0; for (Number n : l) s += n.doubleValue(); return s;
}
static void tambah(List<? super Integer> l) { l.add(1); }   // tulis aman

// PECS: Producer Extends, Consumer Super
```

Erase: `List<String>` dan `List<Integer>` sama-sama `List` saat runtime → `new T[]` dan `instanceof List<String>` tidak boleh.

## Jebakan
- `List<Object>` bukan supertype `List<String>`; gunakan `List<?>`.
- Tidak bisa `add` ke `List<? extends Number>` (kecuali `null`).
- Overload yang hanya beda generic parameter → sama setelah erasure, compile error.
- `@SafeVarargs` diperlukan untuk var-args generik.

## Latihan
1. Wildcard untuk membaca koleksi angka?
2. Mengapa `new T()` tidak bisa?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>List&lt;? extends Number&gt;</code>.</p>
<p><b>2.</b> Karena tipe generik dihapus saat kompilasi (<em>type erasure</em>) sehingga tidak diketahui saat runtime.</p>
</details>
