---
title: Objek, nested class, dan siklus hidup
minutes: 22
level: Menengah
badge: lengkap
summary: Instansiasi, referensi, nested/inner class, dan garbage collection.
objectives:
  - Menjelaskan perbedaan inner, static nested, local, anonymous class
  - Menentukan kapan objek layak GC
  - Memprediksi output konstruktor pada nested class
---
## Kenapa topik ini diuji
Soal menanyakan urutan inisialisasi dan apakah objek masih bisa diakses (eligible for GC).

## Konsep inti
```java
class Outer {
    private int x = 1;
    static class Nested { int y = 2; }
    class Inner { int z = x; }        // butuh instance Outer
    void m() {
        class Local {}                 // hanya di dalam method
        Runnable r = new Runnable() {  // anonymous
            public void run() { System.out.println(x); }
        };
    }
}
Outer o = new Outer();
Outer.Inner i = o.new Inner();        // sintaks penting
Outer.Nested n = new Outer.Nested();
```

GC: objek eligible bila tidak ada referensi kuat dari root (stack, static, thread aktif). `System.gc()` hanya *saran*.

## Jebakan
- `new Outer.Inner()` salah; harus `o.new Inner()`.
- Inner class memegang referensi ke outer (bisa mencegah GC pada outer).
- `finalize()` deprecated dan tidak dijamin dipanggil.
- Anonymous class tidak bisa punya konstruktor; memakai initializer blok.

## Latihan
1. Sintaks membuat inner class instance?
2. Apakah `System.gc()` menjamin objek dihapus?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>outer.new Inner()</code>.</p>
<p><b>2.</b> Tidak, hanya permintaan; JVM bebas mengabaikan.</p>
</details>
