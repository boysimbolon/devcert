---
title: Menangani nilai khusus
minutes: 20
level: Menengah
badge: lengkap
summary: NULL, zero date, unsigned overflow, dan tipe yang tidak punya padanan langsung.
objectives:
  - Menangani NULL dengan benar di kode
  - Mengenali nilai yang tidak bisa dipetakan langsung
  - Menghindari perbandingan yang salah dengan NULL
---
## Kenapa topik ini diuji
Nilai khusus adalah sumber bug paling halus: NULL yang menjadi 0, tanggal nol yang menjadi exception.

## Konsep inti
- **NULL** bukan 0 dan bukan string kosong. `NULL = NULL` menghasilkan `NULL`, bukan true. Gunakan `IS NULL` / `<=>`.
- `rs.getInt()` pada kolom NULL mengembalikan **0**, sehingga harus dicek `rs.wasNull()`.
- **Zero date** (`0000-00-00`) hanya mungkin bila `sql_mode` mengizinkan; driver modern melempar exception.
- **BIGINT UNSIGNED** bisa > 9.2e18 → butuh BigInteger.
- **ENUM/SET** dipetakan sebagai string; nilai di luar daftar ditolak (strict mode).

```java
int umur = rs.getInt("umur");
Integer umurAtauNull = rs.wasNull() ? null : umur;

// perbandingan NULL-safe
// SQL: WHERE kolom <=> ?
```

```sql
SELECT NULL = NULL;        -- NULL
SELECT NULL <=> NULL;      -- 1
SELECT COALESCE(kota, 'tidak diketahui') FROM pelanggan;
```

## Jebakan
- `WHERE kolom != 'x'` tidak mengembalikan baris yang NULL.
- Menyimpan string kosong sebagai pengganti NULL lalu bingung pada agregasi.
- Driver lama mengubah zero date menjadi `0001-01-01`.
- Menjumlahkan kolom NULL menghasilkan NULL, bukan 0 — gunakan `COALESCE`/`IFNULL`.

## Latihan
1. Hasil `SELECT NULL = NULL`?
2. Cara mendeteksi NULL setelah `getInt()`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>NULL</code> (bukan true/false). Bandingkan dengan <code>IS NULL</code> atau <code>&lt;=&gt;</code>.</p>
<p><b>2.</b> Panggil <code>rs.wasNull()</code> segera setelah membaca kolom.</p>
</details>
