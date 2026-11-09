---
title: Membuat dan menjalankan trigger
minutes: 20
level: Menengah
badge: lengkap
summary: BEFORE/AFTER, NEW/OLD, dan batasan yang harus dipatuhi.
objectives:
  - Menulis trigger untuk validasi dan audit
  - Memakai NEW dan OLD dengan tepat
  - Mengetahui batasan trigger di MySQL
---
## Kenapa topik ini diuji
Soal trigger biasanya soal perilaku: kapan jalan dan apa yang tidak boleh dilakukan.

## Konsep inti
```sql
CREATE TRIGGER trg_pesanan_audit
AFTER INSERT ON pesanan
FOR EACH ROW
INSERT INTO audit_log (tabel, aksi, ref_id, dibuat)
VALUES ('pesanan', 'INSERT', NEW.id, NOW());

CREATE TRIGGER trg_stok_validasi
BEFORE UPDATE ON stok
FOR EACH ROW
BEGIN
  IF NEW.qty < 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Stok tidak boleh negatif';
  END IF;
END;
```

Aturan:

- `BEFORE` bisa mengubah `NEW`; `AFTER` tidak.
- `OLD` tersedia pada UPDATE/DELETE; `NEW` pada INSERT/UPDATE.
- Satu tabel hanya boleh punya satu trigger per event+timing.
- Trigger tidak boleh melakukan `COMMIT`/`ROLLBACK` atau DDL pada tabel yang sama.

## Jebakan
- Memakai trigger untuk logika bisnis berat → tersembunyi dan sulit dilacak.
- Trigger `AFTER` yang memodifikasi tabel yang sama → error/loop.
- Replikasi berbasis STATEMENT bisa bermasalah dengan trigger non-deterministik.
- Lupa bahwa trigger jalan juga saat bulk update.

## Latihan
1. Timing mana yang bisa mengubah nilai kolom baru?
2. Bisakah trigger memanggil COMMIT?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>BEFORE</code> (lewat <code>SET NEW.kolom = ...</code>).</p>
<p><b>2.</b> Tidak; trigger tidak boleh mengendalikan transaksi.</p>
</details>
