---
title: Qualifier, Producer, dan Disposer
minutes: 24
level: Menengah
badge: lengkap
summary: Menghilangkan ambiguitas injeksi dan membuat objek yang tidak bisa di-inject langsung.
objectives:
  - Menulis qualifier kustom
  - Membuat objek lewat @Produces dan membersihkannya lewat @Disposes
  - Memakai @Alternative untuk implementasi pengganti
---
## Kenapa topik ini diuji
Soal CDI paling sering berupa kode yang gagal deploy: Ambiguous dependencies atau Unsatisfied dependencies. Jawabannya ada di qualifier dan producer.

## Konsep inti
```java
@Qualifier
@Retention(RUNTIME) @Target({FIELD, METHOD, PARAMETER, TYPE})
public @interface Cepat { }

public interface Pengirim { void kirim(String s); }

@Cepat
public class PengirimCepat implements Pengirim {
    public void kirim(String s) { }
}

public class PengirimLambat implements Pengirim {
    public void kirim(String s) { }
}

@ApplicationScoped
public class Pabrik {
    @Produces @Cepat
    public Pengirim buat() { return new PengirimCepat(); }

    @Produces @RequestScoped
    public Koneksi koneksi() { return Koneksi.buka(); }

    public void tutup(@Disposes Koneksi k) { k.close(); }
}

@Stateless
public class Layanan {
    @Inject @Cepat Pengirim cepat;
}
```

- Qualifier adalah anotasi ber-`@Qualifier`; `@Named` juga qualifier bawaan.
- `@Produces` pada field/method menghasilkan objek yang bisa di-`@Inject`.
- `@Disposes` menerima tipe yang sama seperti producer, tanpa qualifier tambahan.
- `@Alternative` + `beans.xml` memungkinkan mengganti implementasi tanpa mengubah kode.

## Jebakan ujian
- Dua implementasi tanpa qualifier menghasilkan `AmbiguousResolutionException`.
- Interface tanpa implementasi menghasilkan `UnsatisfiedResolutionException` saat deploy.
- `@Disposes` hanya untuk objek hasil `@Produces`, bukan sembarang bean.
- Producer pada bean `@Dependent` menghasilkan objek `@Dependent` kecuali diberi scope.
- `@Alternative` harus diaktifkan di `beans.xml`; kalau tidak, diabaikan.

## Latihan
1. Exception apa bila dua implementasi interface di-inject tanpa qualifier?
2. Method apa yang membersihkan hasil producer?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>AmbiguousResolutionException</code> (gagal deploy).</p>
<p><b>2.</b> Method ber-<code>@Disposes</code> dengan parameter tipe hasil producer.</p>
</details>
