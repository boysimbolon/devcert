---
title: Entity dan Pemetaan ORM
minutes: 25
level: Menengah
badge: lengkap
summary: Membuat entity, memetakan relasi satu-ke-banyak dan banyak-ke-banyak, serta memilih owning side.
objectives:
  - Menulis entity dengan @Entity, @Id, dan tipe identitas
  - Memetakan relasi dan menentukan owning side lewat mappedBy
  - Mengatur cascade, fetch, dan orphanRemoval dengan sadar
---
## Kenapa topik ini diuji
Pemetaan relasi adalah sumber bug paling umum di aplikasi JPA: data dobel, foreign key null, atau query N+1. Ujian menanyakan siapa pemilik relasi dan apa efek cascade.

## Konsep inti
- `@Entity` menandai kelas; butuh konstruktor tanpa argumen (boleh `protected`) dan tidak boleh `final`.
- `@Id` wajib. `@GeneratedValue(strategy=...)`: `AUTO`, `IDENTITY`, `SEQUENCE`, `TABLE`.
- `@Table`, `@Column`, `@Transient`, `@Temporal`, `@Enumerated` mengatur pemetaan kolom.
- Sisi **owning** adalah yang punya kolom foreign key. `mappedBy` menandai sisi **inverse** - tidak punya kolom.

| Relasi | Owning side tipikal | Catatan |
|---|---|---|
| `@OneToMany` / `@ManyToOne` | `@ManyToOne` | paling umum; `mappedBy` di koleksi |
| `@OneToOne` | sisi dengan FK | sisi lain `mappedBy` |
| `@ManyToMany` | sisi yang mendeklarasikan `@JoinTable` | butuh tabel penghubung |

```java
@Entity
@Table(name = "pesanan")
public class Pesanan {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY, optional = false)
    @JoinColumn(name = "pelanggan_id")
    private Pelanggan pelanggan;

    @OneToMany(mappedBy = "pesanan", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<ItemPesanan> item = new ArrayList<>();

    public void tambahItem(ItemPesanan i) { item.add(i); i.setPesanan(this); }
}

@Entity
public class ItemPesanan {
    @Id @GeneratedValue private Long id;
    @ManyToOne(fetch = FetchType.LAZY) @JoinColumn(name = "pesanan_id")
    private Pesanan pesanan;   // owning side: punya kolom FK
}
```

`cascade` menyebarkan operasi (`PERSIST`, `MERGE`, `REMOVE`, `REFRESH`, `DETACH`) dari induk ke anak. `orphanRemoval = true` menghapus anak yang dilepas dari koleksi - bedanya dengan `CascadeType.REMOVE`: yang satu berbasis "tidak lagi dirujuk", yang lain berbasis operasi hapus induk.

## Jebakan ujian
- Lupa `mappedBy` pada `@OneToMany` membuat JPA menganggap relasi join table terpisah - hasilnya tabel tak terduga.
- `@ManyToOne` default-nya `EAGER`; `@OneToMany` default `LAZY`. Soal sering menanyakan default ini.
- Menyimpan anak tanpa mengisi sisi owning (`item.setPesanan(this)`) menghasilkan FK null.
- `@Transient` (JPA) berbeda dari `transient` (Java) - yang pertama tidak dipetakan, yang kedua tidak diserialisasi.
- `@Basic(optional=false)` bukan jaminan constraint di DB; itu urusan DDL/skema.

## Latihan
1. Pada relasi dua arah `Pesanan`-`ItemPesanan`, sisi mana yang memiliki foreign key?
2. Apa perbedaan `cascade = REMOVE` dan `orphanRemoval = true`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>ItemPesanan</code> lewat <code>@ManyToOne</code> + <code>@JoinColumn</code>; <code>Pesanan</code> adalah sisi inverse dengan <code>mappedBy</code>.</p>
<p><b>2.</b> <code>REMOVE</code> menghapus anak saat induk dihapus. <code>orphanRemoval</code> menghapus anak saat ia dilepas dari koleksi induk.</p>
</details>
