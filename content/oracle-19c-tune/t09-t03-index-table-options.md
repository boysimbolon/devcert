---
title: Opsi performa index dan tabel
minutes: 20
level: Menengah
badge: lengkap
summary: PCTFREE, INITRANS, kompresi index, dan opsi yang memengaruhi I/O.
objectives:
  - Mengatur PCTFREE dan INITRANS
  - Memakai index compression
  - Menjelaskan trade-off tiap opsi
---
## Kenapa topik ini diuji
Soal menanyakan opsi mana untuk mengurangi I/O atau kontensi.

## Konsep inti
```sql
CREATE TABLE pesanan (
  id NUMBER, pelanggan_id NUMBER, total NUMBER
) PCTFREE 20 INITRANS 4;

CREATE INDEX idx_pesanan ON pesanan(pelanggan_id) PCTFREE 10 INITRANS 4;
ALTER INDEX idx_pesanan REBUILD COMPRESS 2;

ALTER TABLE pesanan MOVE PCTFREE 30;
```

| Opsi | Efek |
|---|---|
| `PCTFREE` tinggi | ruang untuk update, lebih banyak blok |
| `INITRANS` tinggi | mengurangi kontensi blok pada OLTP konkuren |
| `COMPRESS n` | prefix compression pada index, menghemat ruang |
| `NOLOGGING` (saat build) | mempercepat, kurangi redo |

## Jebakan
- `PCTFREE` terlalu tinggi memperbesar tabel dan memperlambat full scan.
- Index compression menambah biaya CPU saat DML.
- `NOLOGGING` mengurangi redo tetapi data tidak terproteksi saat media failure.
- `INITRANS` besar memakan ruang header blok.

## Latihan
1. Opsi untuk mengurangi kontensi blok pada OLTP?
2. Apa efek index compression?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>INITRANS</code> lebih tinggi.</p>
<p><b>2.</b> Menghemat ruang index dengan prefix compression, tetapi menambah CPU saat perubahan.</p>
</details>
