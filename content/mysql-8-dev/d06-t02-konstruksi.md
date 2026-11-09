---
title: Konstruksi pemrograman dalam stored routine
minutes: 22
level: Menengah
badge: lengkap
summary: Variabel, IF/CASE, loop, cursor, dan handler.
objectives:
  - Menulis alur kendali di dalam routine
  - Memakai cursor dengan benar
  - Menangani kondisi dengan handler
---
## Kenapa topik ini diuji
Soal memberi potongan procedure dan menanyakan hasil atau kesalahannya.

## Konsep inti
```sql
DELIMITER //
CREATE PROCEDURE laporan_kota()
BEGIN
  DECLARE selesai INT DEFAULT 0;
  DECLARE v_kota VARCHAR(50);
  DECLARE cur CURSOR FOR SELECT DISTINCT kota FROM pelanggan;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET selesai = 1;

  CREATE TEMPORARY TABLE tmp_kota (kota VARCHAR(50), jumlah INT);

  OPEN cur;
  baca: LOOP
    FETCH cur INTO v_kota;
    IF selesai = 1 THEN LEAVE baca; END IF;

    INSERT INTO tmp_kota
    SELECT v_kota, COUNT(*) FROM pelanggan WHERE kota = v_kota;
  END LOOP;
  CLOSE cur;
END //
DELIMITER ;
```

Blok yang tersedia: `BEGIN...END`, `IF/ELSEIF/ELSE`, `CASE`, `LOOP`, `WHILE`, `REPEAT`, `LEAVE`/`ITERATE`, `DECLARE ... HANDLER`.

Aturan urutan deklarasi dalam blok: variabel → kondisi → cursor → handler.

## Jebakan
- Urutan deklarasi salah → error sintaks.
- Handler `NOT FOUND` harus `CONTINUE`, bukan `EXIT`, untuk loop cursor.
- Variabel routine berbeda dari variabel sesi (`@x`).
- `ITERATE` hanya di dalam loop berlabel.

## Latihan
1. Urutan deklarasi yang benar dalam blok?
2. Mengapa handler memakai CONTINUE pada cursor?

<details><summary>Jawaban</summary>
<p><b>1.</b> Variabel, lalu kondisi, lalu cursor, lalu handler.</p>
<p><b>2.</b> Agar eksekusi tidak keluar dari blok saat cursor habis, melainkan lanjut ke pengecekan flag selesai.</p>
</details>
