---
title: Inheritance, abstract, sealed, dan polymorphism
minutes: 24
level: Menengah
badge: lengkap
summary: Override, covariant return, casting, instanceof, dan pattern matching.
objectives:
  - Menerapkan aturan override
  - Menggunakan sealed class
  - Menentukan objek vs tipe referensi
---
## Kenapa topik ini diuji
Soal menyodorkan hierarki dan menanyakan method mana yang dipanggil atau apakah cast aman.

## Konsep inti
```java
sealed interface Shape permits Circle, Square {}
record Circle(double r) implements Shape {}
record Square(double s) implements Shape {}

Shape sh = new Circle(2);
if (sh instanceof Circle c && c.r() > 1) {
    System.out.println("lingkaran besar " + c.r());
}
```

Aturan override: nama & parameter sama, return tipe sama atau kovarian, akses tidak boleh lebih ketat, tidak boleh melempar checked exception baru/lebih luas.

Sealed: `permits` membatasi subclass; subclass harus `final`, `sealed`, atau `non-sealed`.

## Jebakan
- Variabel `Shape` hanya bisa memanggil method yang dideklarasikan di `Shape`.
- Cast ke tipe yang salah → `ClassCastException` saat runtime, bukan compile.
- `@Override` tidak wajib tetapi membantu menangkap kesalahan.
- Static method tidak di-override, hanya disembunyikan.

## Latihan
1. Apakah `Shape sh = new Circle(2); sh.r()` compile?
2. Apa tiga modifier wajib pada subclass sealed?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tidak; <code>r()</code> bukan anggota <code>Shape</code>.</p>
<p><b>2.</b> <code>final</code>, <code>sealed</code>, atau <code>non-sealed</code>.</p>
</details>
