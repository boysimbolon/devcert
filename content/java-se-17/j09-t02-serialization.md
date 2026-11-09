---
title: Serialisasi objek
minutes: 20
level: Menengah
badge: lengkap
summary: Serializable, serialVersionUID, transient, dan risiko deserialisasi.
objectives:
  - Menulis dan membaca objek terserialisasi
  - Menjelaskan peran transient dan serialVersionUID
  - Mengenali risiko keamanan
---
## Kenapa topik ini diuji
Soal menanyakan field mana yang hilang dan error apa yang muncul saat versi berubah.

## Konsep inti
```java
class Akun implements Serializable {
    private static final long serialVersionUID = 1L;
    private String nama;
    private transient String sandi;   // tidak diserialisasi -> null setelah baca
}

try (var out = new ObjectOutputStream(new FileOutputStream("a.ser"))) {
    out.writeObject(new Akun());
}
try (var in = new ObjectInputStream(new FileInputStream("a.ser"))) {
    Akun a = (Akun) in.readObject();
}
```

Aturan: `static` dan `transient` tidak diserialisasi; superclass non-serializable harus punya constructor tanpa argumen.

## Jebakan
- Mengubah `serialVersionUID` atau struktur tanpa UID → `InvalidClassException`.
- `transient` kembali `null`/`0` setelah deserialisasi.
- Deserialisasi data tak terpercaya berbahaya (gadget chain) — gunakan filter/JSON.
- `NotSerializableException` bila field non-transient tidak `Serializable`.

## Latihan
1. Field mana yang tidak ikut tersimpan?
2. Error saat versi kelas berubah tanpa UID?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>static</code> dan <code>transient</code>.</p>
<p><b>2.</b> <code>InvalidClassException</code>.</p>
</details>
