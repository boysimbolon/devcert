---
title: Scope, var, encapsulation, immutability
minutes: 22
level: Menengah
badge: lengkap
summary: Cakupan variabel, local variable type inference, dan desain objek aman.
objectives:
  - Membedakan scope blok, method, dan kelas
  - Memakai var sesuai aturan
  - Merancang kelas immutable
---
## Kenapa topik ini diuji
`var` punya batasan yang sering dijadikan opsi jawaban salah.

## Konsep inti
```java
var list = new ArrayList<String>();   // boleh
// var x;                            // salah: butuh inisialisasi
// var a = null;                     // salah: null tidak punya tipe
// void m(var v) {}                  // salah: parameter tidak boleh var
// var x = 1, y = 2;                 // salah: satu deklarasi satu var
```

Kelas immutable:

```java
public final class Saldo {
    private final long nilai;
    private final List<String> riwayat;
    public Saldo(long nilai, List<String> riwayat) {
        this.nilai = nilai;
        this.riwayat = List.copyOf(riwayat);   // defensive copy
    }
    public long nilai() { return nilai; }
    public List<String> riwayat() { return riwayat; } // sudah tak berubah
}
```

## Jebakan
- `var` hanya untuk variabel lokal, enhanced-for, dan lambda param (dengan tipe lain di lambda).
- Shadowing variabel lokal di blok dalam → compile error bila nama sama.
- Field `final` bukan berarti objeknya immutable bila berisi koleksi mutable.
- Getter yang mengembalikan referensi internal membocorkan mutabilitas.

## Latihan
1. Tiga larangan `var` yang sering diuji?
2. Bagaimana membuat kelas benar-benar immutable dengan list?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tanpa inisialisasi, diinisialisasi <code>null</code>, dan sebagai parameter method/field.</p>
<p><b>2.</b> Salin defensif saat konstruktor dan jangan kembalikan referensi internal (gunakan <code>List.copyOf</code>).</p>
</details>
