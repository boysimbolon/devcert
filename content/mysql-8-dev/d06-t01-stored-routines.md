---
title: Membuat dan menjalankan stored routine
minutes: 22
level: Menengah
badge: lengkap
summary: Procedure vs function, parameter, dan karakteristik yang wajib dipahami.
objectives:
  - Membuat procedure dan function
  - Membedakan IN, OUT, dan INOUT
  - Menentukan karakteristik dan hak eksekusi
---
## Kenapa topik ini diuji
Soal stored routine menguji sintaks dan perbedaan procedure/function, termasuk pemanggilan.

## Konsep inti
```sql
DELIMITER //
CREATE PROCEDURE tambah_stok(IN p_id INT, IN p_qty INT, OUT p_total INT)
  SQL SECURITY INVOKER
BEGIN
  UPDATE stok SET qty = qty + p_qty WHERE id = p_id;
  SELECT qty INTO p_total FROM stok WHERE id = p_id;
END //

CREATE FUNCTION hitung_pajak(nilai DECIMAL(12,2)) RETURNS DECIMAL(12,2)
  DETERMINISTIC
  RETURN ROUND(nilai * 0.11, 2) //
DELIMITER ;

CALL tambah_stok(1, 5, @total);
SELECT @total;
SELECT hitung_pajak(100000);
```

Perbedaan:

| Aspek | Procedure | Function |
|---|---|---|
| Pemanggilan | `CALL` | di dalam ekspresi SQL |
| Return | `OUT`/`INOUT` | `RETURNS` satu nilai |
| Dipakai di SELECT | tidak | ya |
| Karakteristik | boleh `MODIFIES SQL DATA` | harus `DETERMINISTIC`/`NO SQL`/`READS SQL DATA` |

`SQL SECURITY DEFINER` menjalankan dengan hak pembuat; `INVOKER` dengan hak pemanggil.

## Jebakan
- Lupa `DELIMITER` sehingga body terpotong di titik koma pertama.
- Function tanpa `DETERMINISTIC` bisa ditolak pada binary logging tertentu.
- `SELECT ... INTO var` yang mengembalikan banyak baris → error.
- Parameter `OUT` tidak otomatis terisi bila tidak ada baris cocok.

## Latihan
1. Bagaimana memanggil procedure dengan parameter OUT?
2. Kapan memakai `SQL SECURITY DEFINER`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>CALL nama_proc(nilai, @variabel);</code> lalu baca <code>@variabel</code>.</p>
<p><b>2.</b> Saat pemanggil tidak boleh punya akses langsung ke tabel tetapi perlu menjalankan logika itu.</p>
</details>
