---
title: Mengelola constraint
minutes: 20
level: Menengah
badge: lengkap
summary: NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK dan opsi deferrable.
objectives:
  - Menambah constraint pada tabel yang sudah ada
  - Mengaktifkan/menonaktifkan constraint
  - Menjelaskan deferrable dan cascade
---
## Kenapa topik ini diuji
Soal menguji jenis constraint dan efek menonaktifkannya.

## Konsep inti
```sql
ALTER TABLE pelanggan ADD CONSTRAINT pk_pel PRIMARY KEY (id);
ALTER TABLE pelanggan ADD CONSTRAINT uq_email UNIQUE (email);
ALTER TABLE pesanan ADD CONSTRAINT fk_pel FOREIGN KEY (pelanggan_id)
  REFERENCES pelanggan(id) ON DELETE CASCADE;
ALTER TABLE pelanggan ADD CONSTRAINT ck_aktif CHECK (aktif IN ('Y','N'));

ALTER TABLE pesanan DISABLE CONSTRAINT fk_pel;
ALTER TABLE pesanan ENABLE CONSTRAINT fk_pel;

SELECT constraint_name, constraint_type, status FROM user_constraints
 WHERE table_name = 'PESANAN';
```

| Tipe | Kode di USER_CONSTRAINTS |
|---|---|
| Primary key | P |
| Unique | U |
| Check | C |
| Foreign key | R |
| Not null | C (dengan search_condition IS NOT NULL) |

## Jebakan
- `DISABLE` pada PK tanpa `KEEP INDEX` akan menghapus index-nya.
- Constraint `DEFERRABLE` memeriksa saat commit, bukan per pernyataan.
- Menambah constraint pada data yang melanggar gagal; gunakan `ENABLE NOVALIDATE` untuk data lama.
- `ON DELETE CASCADE` menghapus anak otomatis — berbahaya bila tidak disadari.

## Latihan
1. Kode constraint_type untuk foreign key?
2. Apa efek `ENABLE NOVALIDATE`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>R</code>.</p>
<p><b>2.</b> Constraint aktif untuk baris baru tanpa memeriksa data lama yang sudah ada.</p>
</details>
