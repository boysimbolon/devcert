---
title: Membuat tabel
minutes: 20
level: Dasar
badge: lengkap
summary: CREATE TABLE dengan DEFAULT, constraint inline, dan opsi storage dasar.
objectives:
  - Menulis CREATE TABLE lengkap
  - Memakai DEFAULT dan constraint inline
  - Menghindari kesalahan umum
---
## Kenapa topik ini diuji
Soal meminta DDL yang benar; kesalahan kecil (koma, tipe) membuat opsi jawaban gugur.

## Konsep inti
```sql
CREATE TABLE pelanggan (
  id        NUMBER(8)      CONSTRAINT pk_pelanggan PRIMARY KEY,
  email     VARCHAR2(120)  CONSTRAINT uq_email UNIQUE,
  nama      VARCHAR2(80)   NOT NULL,
  aktif     CHAR(1)        DEFAULT 'Y' CHECK (aktif IN ('Y','N')),
  dibuat    DATE           DEFAULT SYSDATE,
  dept_id   NUMBER(4)      REFERENCES departments(department_id)
);
```

Bentuk constraint: inline (di kolom) atau out-of-line (`CONSTRAINT nama PRIMARY KEY (kolom)`). Beri nama constraint agar mudah diubah/dihapus.

## Jebakan
- Constraint tanpa nama mendapat nama sistem (`SYS_C…`) sehingga sulit di-drop.
- `DEFAULT` tidak berlaku untuk NULL eksplisit yang dimasukkan.
- `CHECK` tidak bisa memakai subquery.
- Tabel tanpa PK menyulitkan replikasi dan update selektif.

## Latihan
1. Mengapa constraint sebaiknya diberi nama?
2. Apakah DEFAULT dipakai saat INSERT menyebut NULL?

<details><summary>Jawaban</summary>
<p><b>1.</b> Agar mudah dirujuk pada ALTER/DROP dan pesan error lebih jelas.</p>
<p><b>2.</b> Tidak; NULL eksplisit tetap NULL (kecuali kolom NOT NULL sehingga error).</p>
</details>
