---
title: EL dan Integrasi JSF dengan CDI
minutes: 20
level: Menengah
badge: lengkap
summary: @Named vs @ManagedBean, scope JSF vs CDI, dan injeksi ke bean halaman.
objectives:
  - Memilih @Named dengan scope CDI untuk aplikasi Java EE 7
  - Membedakan @ViewScoped JSF dan CDI
  - Mengakses properti bean dari EL
---
## Kenapa topik ini diuji
Java EE 7 menyatukan JSF dan CDI secara longgar. Soal menanyakan bean mana yang dikelola siapa, dan mengapa injeksi gagal.

## Konsep inti
Aspek penting:

- `@ManagedBean` dikelola JSF, injeksi lewat `@ManagedProperty`.
- `@Named` dikelola CDI, injeksi lewat `@Inject`, dan bisa memakai semua fitur CDI.
- Scope JSF: `@RequestScoped`, `@ViewScoped`, `@SessionScoped`, `@ApplicationScoped` (paket `javax.faces.bean`).
- Scope CDI: `@RequestScoped`, `@SessionScoped`, `@ApplicationScoped`, `@ConversationScoped`, `@Dependent`.
- EL mengakses keduanya dengan `#{namaBean}`.

```java
@Named("pesananForm")
@ViewScoped
public class PesananForm implements java.io.Serializable {
    @Inject PesananService service;
    private String nama;
    public String simpan() { service.simpan(nama); return "daftar"; }
    public String getNama() { return nama; }
    public void setNama(String n) { this.nama = n; }
}
```

- Bean harus punya getter/setter untuk properti yang diikat EL.
- `@Named` tanpa nilai memakai nama kelas dengan huruf pertama kecil.
- Untuk memakai `@Inject`, bean harus dikelola CDI, bukan `@ManagedBean`.

## Jebakan ujian
- `@ManagedProperty` hanya bekerja pada `@ManagedBean`.
- JSF `@ViewScoped` dan CDI tidak kompatibel penuh di Java EE 7.
- `@Dependent` pada `@Named` membuat instance baru per evaluasi EL - bukan yang diinginkan untuk form.
- `@Named` tidak otomatis `@RequestScoped`; default-nya `@Dependent`.
- EL memanggil getter; tanpa getter, properti tidak bisa dibaca.

## Latihan
1. Anotasi injeksi yang bekerja di `@Named` bean?
2. Apa default scope `@Named` tanpa anotasi scope?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>@Inject</code>.</p>
<p><b>2.</b> <code>@Dependent</code>.</p>
</details>
