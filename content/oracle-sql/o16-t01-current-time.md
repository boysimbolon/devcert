---
title: CURRENT_DATE, CURRENT_TIMESTAMP, LOCALTIMESTAMP
minutes: 20
level: Menengah
badge: lengkap
summary: Perbedaan zona waktu antar fungsi waktu di Oracle.
objectives:
  - Membedakan ketiga fungsi
  - Menjelaskan pengaruh zona waktu sesi
  - Memilih fungsi yang tepat
---
## Kenapa topik ini diuji
Soal menanyakan nilai mana yang berubah bila `SESSIONTIMEZONE` diubah.

## Konsep inti
| Fungsi | Tipe hasil | Zona waktu |
|---|---|---|
| `SYSDATE` | DATE | zona server |
| `CURRENT_DATE` | DATE | zona **sesi** |
| `SYSTIMESTAMP` | TIMESTAMP WITH TIME ZONE | zona server |
| `CURRENT_TIMESTAMP` | TIMESTAMP WITH TIME ZONE | zona sesi |
| `LOCALTIMESTAMP` | TIMESTAMP (tanpa TZ) | waktu lokal sesi |

```sql
ALTER SESSION SET TIME_ZONE = '-05:00';
SELECT SYSDATE, CURRENT_DATE, CURRENT_TIMESTAMP, LOCALTIMESTAMP FROM dual;
```

## Jebakan
- `CURRENT_DATE` mengembalikan DATE (tanpa zona) tetapi nilainya mengikuti zona sesi.
- `LOCALTIMESTAMP` menghilangkan informasi zona waktu.
- Mengubah `TIME_ZONE` tidak mengubah `SYSDATE`.
- Perbandingan antar fungsi berbeda zona bisa menyesatkan.

## Latihan
1. Fungsi mana yang mengikuti zona waktu sesi dan menyertakan zona?
2. Apakah SYSDATE berubah saat TIME_ZONE diubah?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>CURRENT_TIMESTAMP</code>.</p>
<p><b>2.</b> Tidak; SYSDATE memakai zona server.</p>
</details>
