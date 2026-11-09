---
title: Overloading dan var-args
minutes: 20
level: Menengah
badge: lengkap
summary: Aturan pemilihan method, widening vs boxing, dan var-args.
objectives:
  - Menentukan method mana yang dipilih saat overloading
  - Menjelaskan urutan prioritas resolusi
  - Menghindari ambiguity dengan var-args
---
## Kenapa topik ini diuji
Soal memberi beberapa versi method dan menanyakan mana yang dipanggil.

## Konsep inti
Prioritas pemilihan (fase):

```text
1. exact match (subtyping diperbolehkan)
2. widening primitif (int -> long -> float -> double)
3. autoboxing / widening reference
4. var-args
```

```java
void m(int i)   { System.out.println("int"); }
void m(long l)  { System.out.println("long"); }
void m(Integer i) { System.out.println("Integer"); }
m(5);      // int (exact)
m(5L);     // long
m((short)5); // int (widening)

void v(int... a) {}
void v(int a) {}
v(1);      // memilih v(int), bukan var-args
```

## Jebakan
- Widening primitif dipilih sebelum boxing.
- `m(null)` ambigu bila ada `String` dan `Integer` → compile error.
- Var-args hanya boleh satu dan harus parameter terakhir.
- Overload berbeda dari override: parameter harus berbeda.

## Latihan
1. `m(5)` dengan `m(int)` dan `m(Integer)` memilih apa?
2. Mengapa `m(null)` bisa gagal compile?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>m(int)</code> karena exact match lebih diprioritaskan daripada boxing.</p>
<p><b>2.</b> Karena dua referensi tipe berbeda sama-sama cocok sehingga ambigu.</p>
</details>
