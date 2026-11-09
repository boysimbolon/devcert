---
title: Parameter yang memengaruhi optimizer
minutes: 20
level: Menengah
badge: lengkap
summary: optimizer_mode, optimizer_features_enable, cursor_sharing, dan optimizer_index_caching.
objectives:
  - Menyebutkan parameter optimizer utama
  - Menjelaskan risiko mengubahnya
  - Memilih parameter untuk kasus khusus
---
## Kenapa topik ini diuji
Soal menanyakan parameter mana yang mengubah pemilihan plan, dan risikonya.

## Konsep inti
| Parameter | Efek |
|---|---|
| `optimizer_mode` | `ALL_ROWS` (default OLAP-ish) vs `FIRST_ROWS_n` |
| `optimizer_features_enable` | memakai perilaku optimizer versi tertentu |
| `cursor_sharing` | `EXACT`/`FORCE` untuk mengurangi hard parse |
| `optimizer_index_cost_adj` | menaikkan/menurunkan kecenderungan memakai index |
| `optimizer_dynamic_sampling` | sampling saat statistik minim |
| `db_file_multiblock_read_count` | memengaruhi biaya full scan |

```sql
SHOW PARAMETER optimizer;
ALTER SESSION SET optimizer_mode = FIRST_ROWS(10);
ALTER SYSTEM SET optimizer_features_enable = '19.1.0' SCOPE=SPFILE;
```

## Jebakan
- `optimizer_features_enable` menurunkan perilaku optimizer — bisa menyembunyikan fitur baru.
- `cursor_sharing=FORCE` bisa menyebabkan plan buruk karena bind peeking.
- Mengubah parameter global untuk satu query buruk adalah solusi jangka pendek.
- `optimizer_index_cost_adj` bukan pengganti statistik yang benar.

## Latihan
1. Parameter untuk mengurangi hard parse?
2. Risiko `optimizer_features_enable`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>cursor_sharing</code> (atau perbaiki bind di aplikasi).</p>
<p><b>2.</b> Optimizer memakai aturan versi lama sehingga fitur perbaikan plan baru tidak aktif.</p>
</details>
