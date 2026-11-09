---
title: Primitif, wrapper, Math, dan casting
minutes: 22
level: Dasar
badge: lengkap
summary: Delapan tipe primitif, autoboxing, promotion, dan aturan casting yang diuji.
objectives:
  - Menyebutkan ukuran dan rentang tipe primitif
  - Memprediksi hasil promotion dan casting
  - Menghindari jebakan autoboxing dan Math
---
## Kenapa topik ini diuji
Hampir setiap soal kode memuat ekspresi aritmetika; salah membaca promotion = salah jawab.

## Konsep inti
| Tipe | Ukuran | Catatan |
|---|---|---|
| `byte`/`short`/`int`/`long` | 8/16/32/64 bit | default literal bilangan bulat = `int` |
| `float`/`double` | 32/64 bit | default literal desimal = `double` |
| `char` | 16 bit unsigned | `'A'` = 65 |
| `boolean` | — | tidak bisa dikonversi ke angka |

```java
int a = 5, b = 2;
double d = a / b;          // 2.0  (pembagian int dulu)
double e = (double) a / b; // 2.5
byte x = 10, y = 20;
byte z = (byte) (x + y);   // butuh cast: hasil int

Integer i1 = 127, i2 = 127;
System.out.println(i1 == i2);   // true  (cache -128..127)
Integer j1 = 128, j2 = 128;
System.out.println(j1 == j2);   // false
```

Math: `Math.round(2.5)` = 3 (long), `Math.round(-2.5)` = -2, `Math.floor(-2.5)` = -3.0, `Math.abs(Integer.MIN_VALUE)` tetap negatif (overflow).

## Jebakan
- `char + char` menghasilkan `int`, bukan `char`.
- `float f = 3.5;` gagal compile (double ke float perlu `f` suffix).
- Autoboxing di dalam kondisi `?:` atau `==` bisa melempar NPE.
- `x++` vs `++x` di dalam argumen method (evaluasi kiri-ke-kanan).

## Latihan
1. Hasil `5 / 2` dan `5 / 2.0`?
2. Mengapa `Integer a=1000, b=1000; a==b` bisa false?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>2</code> dan <code>2.5</code>.</p>
<p><b>2.</b> Karena nilai di luar cache -128..127 dibuat objek baru, sehingga referensi berbeda.</p>
</details>
