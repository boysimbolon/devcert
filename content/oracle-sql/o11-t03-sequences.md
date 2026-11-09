---
title: Mengelola sequence
minutes: 18
level: Dasar
badge: lengkap
summary: NEXTVAL, CURRVAL, cache, dan perilaku unik tanpa rollback.
objectives:
  - Membuat sequence dengan parameter benar
  - Memakai NEXTVAL/CURRVAL
  - Menjelaskan mengapa nomor bisa bolong
---
## Kenapa topik ini diuji
Soal menanyakan nilai berikutnya atau mengapa ada celah pada nomor.

## Konsep inti
```sql
CREATE SEQUENCE seq_dept
  START WITH 300 INCREMENT BY 10
  MAXVALUE 99999 CACHE 20 NOCYCLE;

SELECT seq_dept.NEXTVAL FROM dual;
SELECT seq_dept.CURRVAL FROM dual;   -- nilai terakhir di sesi ini

INSERT INTO departments (department_id, department_name)
VALUES (seq_dept.NEXTVAL, 'RISET');

SELECT sequence_name, last_number, cache_size FROM user_sequences;
```

## Jebakan
- `CURRVAL` sebelum `NEXTVAL` pada sesi itu → ORA-08002.
- Sequence tidak ter-rollback: nomor yang terpakai hilang meski transaksi batal.
- `CACHE` besar mempercepat tetapi bisa melompati nomor saat instance restart.
- Sequence tidak menjamin urutan tanpa celah dan tidak terkait tabel tertentu.

## Latihan
1. Mengapa nomor sequence bisa bolong?
2. Kapan CURRVAL bisa dipakai?

<details><summary>Jawaban</summary>
<p><b>1.</b> Karena NEXTVAL tidak ikut rollback, dan cache bisa hilang saat restart.</p>
<p><b>2.</b> Setelah NEXTVAL dipanggil di sesi yang sama.</p>
</details>
