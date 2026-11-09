---
title: Class, record, field, dan initializer
minutes: 24
level: Menengah
badge: lengkap
summary: Urutan inisialisasi, static vs instance, constructor, dan aturan record.
objectives:
  - Memprediksi urutan inisialisasi kelas
  - Menulis record dengan compact constructor
  - Membedakan static dan instance initializer
---
## Kenapa topik ini diuji
Urutan eksekusi static → instance → constructor adalah soal klasik.

## Konsep inti
```java
class A {
    static { System.out.println("static A"); }
    { System.out.println("init A"); }
    A() { System.out.println("ctor A"); }
}

record Point(int x, int y) {
    Point {                       // compact constructor
        if (x < 0) throw new IllegalArgumentException();
    }
    int sum() { return x + y; }
}
```

Urutan: static field & static block (sekali per kelas, saat pertama dipakai) → instance field & instance block (per objek, sebelum constructor) → body constructor.

Record: field otomatis `private final`, accessor `x()`, `equals/hashCode/toString`, tidak bisa `extends` kelas lain, boleh implement interface, tidak boleh punya field instance tambahan.

## Jebakan
- Static block berjalan saat kelas *diinisialisasi*, bukan saat objek dibuat/dideklarasikan.
- Record tidak bisa mendeklarasikan field instance tambahan; static field boleh.
- Compact constructor tidak boleh menulis `this.x = x`.
- Constructor `this(...)` dan `super(...)` harus baris pertama.

## Latihan
1. Berapa kali static block berjalan untuk 3 objek?
2. Apakah record boleh menambah field instance?

<details><summary>Jawaban</summary>
<p><b>1.</b> Sekali (per classloader).</p>
<p><b>2.</b> Tidak; hanya komponen record dan field static.</p>
</details>
