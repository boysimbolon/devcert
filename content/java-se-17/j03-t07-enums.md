---
title: Enum dengan field, method, dan constructor
minutes: 20
level: Menengah
badge: lengkap
summary: Enum sebagai kelas penuh, urutan inisialisasi, dan abstract method per konstanta.
objectives:
  - Menulis enum dengan state dan perilaku
  - Menjelaskan urutan inisialisasi konstanta
  - Memakai values(), valueOf(), ordinal()
---
## Kenapa topik ini diuji
Soal menanyakan output saat enum punya constructor dan blok inisialisasi.

## Konsep inti
```java
enum Status {
    BARU(1) { boolean boleh() { return true; } },
    SELESAI(2) { boolean boleh() { return false; } };

    private final int kode;
    Status(int kode) { this.kode = kode; System.out.println("ctor " + name()); }
    abstract boolean boleh();
    int kode() { return kode; }
}

System.out.println(Status.valueOf("BARU").kode());  // 1
System.out.println(Status.values().length);          // 2
```

Konstanta dibuat **satu per satu** saat kelas diinisialisasi, berurutan sesuai deklarasi.

## Jebakan
- Constructor enum selalu `private` (atau default) — tidak bisa `public`.
- `valueOf` melempar `IllegalArgumentException` bila nama tidak ada (peka huruf besar).
- Enum tidak bisa `extends` kelas lain (sudah extends `Enum`) tetapi bisa implement interface.
- `ordinal()` mengikuti urutan deklarasi dan rapuh untuk logika bisnis.

## Latihan
1. Berapa kali constructor dipanggil untuk 3 konstanta?
2. Apa yang terjadi pada `Status.valueOf("baru")`?

<details><summary>Jawaban</summary>
<p><b>1.</b> Tiga kali, satu per konstanta saat inisialisasi kelas.</p>
<p><b>2.</b> <code>IllegalArgumentException</code> karena nama tidak cocok.</p>
</details>
