---
title: SQL Performance Analyzer
minutes: 20
level: Menengah
badge: lengkap
summary: Membandingkan performa SQL sebelum dan sesudah perubahan.
objectives:
  - Menjelaskan alur SPA
  - Membuat SQL tuning set
  - Membaca laporan perbandingan
---
## Kenapa topik ini diuji
SPA adalah alat uji regresi SQL sebelum perubahan diterapkan; soal menanyakan urutan langkahnya.

## Konsep inti
```text
1. Buat SQL Tuning Set (STS) dari beban nyata
2. Tangkap plan/statistik awal (SQL trial 1)
3. Terapkan perubahan (parameter, statistik, upgrade)
4. Jalankan SQL trial 2
5. Bandingkan (compare report)
```

```sql
-- dari AWR ke STS
BEGIN
  DBMS_SQLTUNE.CREATE_SQLSET('sts_beban');
  DBMS_SQLTUNE.LOAD_SQLSET(sqlset_name => 'sts_beban',
    populate_cursor => DBMS_SQLTUNE.SELECT_WORKLOAD_REPOSITORY(100,110));
END;
/

-- via EM atau DBMS_SQLPA
```

## Jebakan
- STS harus mewakili beban nyata, bukan query pilihan.
- Perubahan lingkungan (data berbeda) mengaburkan hasil.
- SPA menjalankan query; hindari pada beban produksi tanpa izin.
- Hasil "regressed" harus dianalisis per SQL, bukan hanya jumlah.

## Latihan
1. Objek yang menyimpan kumpulan SQL untuk diuji?
2. Kapan SPA dipakai?

<details><summary>Jawaban</summary>
<p><b>1.</b> SQL Tuning Set (STS).</p>
<p><b>2.</b> Sebelum perubahan yang berpotensi mengubah plan (upgrade, parameter, statistik).</p>
</details>
