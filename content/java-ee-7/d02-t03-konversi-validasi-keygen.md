---
title: Konversi, Validasi, dan Key Generation
minutes: 20
level: Menengah
badge: lengkap
summary: AttributeConverter dan Bean Validation di sisi entity, plus strategi membangkitkan primary key.
objectives:
  - Menulis AttributeConverter untuk tipe kustom
  - Menerapkan Bean Validation pada field entity dan memicu validasi saat persist
  - Memilih strategi @GeneratedValue dan tahu konsekuensinya
---
## Kenapa topik ini diuji
Java EE 7 menambahkan `AttributeConverter` (JPA 2.1) dan mengintegrasikan Bean Validation 1.1 dengan JPA. Soal menyukai kombinasi "nilai apa yang tersimpan di DB" dan "kapan validasi jalan".

## Konsep inti
**AttributeConverter** memetakan tipe Java kustom ke kolom DB.

```java
@Converter(autoApply = true)
public class StatusConverter implements AttributeConverter<Status, String> {
    public String convertToDatabaseColumn(Status s) { return s == null ? null : s.kode(); }
    public Status convertToEntityAttribute(String kode) { return Status.dari(kode); }
}

@Entity
public class Tugas {
    @Id @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "tugas_seq")
    @SequenceGenerator(name = "tugas_seq", sequenceName = "seq_tugas", allocationSize = 50)
    private Long id;

    @Convert(converter = StatusConverter.class)   // tidak perlu bila autoApply=true
    private Status status;

    @NotNull @Size(min = 3, max = 80)
    private String judul;

    @Email
    private String email;
}
```

**Key generation**

| Strategi | Perilaku | Catatan |
|---|---|---|
| `AUTO` | provider memilih | default, portabel |
| `IDENTITY` | kolom auto-increment DB | insert langsung, id baru diketahui setelah insert |
| `SEQUENCE` | sequence DB | efisien, bisa `allocationSize` untuk pre-allocation |
| `TABLE` | tabel penampung nilai | portabel tapi paling lambat |

**Bean Validation pada entity** dijalankan otomatis pada `pre-persist`, `pre-update`, `pre-remove` (default group `Default`). Pelanggaran → `ConstraintViolationException` yang membungkus `Set<ConstraintViolation<?>>`.

## Jebakan ujian
- `IDENTITY` menghalangi batching insert karena id baru diketahui setelah baris dibuat; `SEQUENCE` lebih baik untuk banyak insert.
- `@Convert` tidak berlaku untuk relasi atau tipe `@Enumerated` (untuk enum gunakan `@Enumerated` atau converter ke kolom string).
- Validasi terjadi saat flush/commit, bukan saat `setJudul()`. Panggil `em.flush()` atau `validator.validate()` untuk memeriksa lebih awal.
- `@NotNull` (Bean Validation) berbeda dari `@Column(nullable=false)` (DDL).
- `allocationSize` pada `SequenceGenerator` menentukan jumlah id yang di-cache; salah mengira id naik satu per satu adalah jebakan klasik.

## Latihan
1. Di mana `ConstraintViolationException` dilempar saat `persist` dipanggil dari EJB CMT?
2. Strategi key mana yang aman untuk insert massal dan mengapa?

<details><summary>Jawaban</summary>
<p><b>1.</b> Saat transaksi flush/commit, bukan saat <code>persist</code> dipanggil.</p>
<p><b>2.</b> <code>SEQUENCE</code> dengan <code>allocationSize</code> besar, karena id bisa diambil di muka sehingga JDBC batch insert tetap bisa dipakai.</p>
</details>
