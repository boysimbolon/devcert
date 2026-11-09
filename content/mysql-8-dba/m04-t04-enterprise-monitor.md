---
title: MySQL Enterprise Monitor
minutes: 16
level: Menengah
badge: lengkap
summary: Apa yang dipantau MEM, advisory, dan cara membaca aktivitas server.
objectives:
  - Menjelaskan komponen MEM (Service Manager, agent)
  - Memakai advisory untuk menemukan masalah
  - Menghubungkan MEM dengan query analyzer
---
## Kenapa topik ini diuji
MEM hanya ada di Enterprise, dan diuji pada tingkat konsep: apa yang dilakukannya dan bagaimana ia membantu DBA.

## Konsep inti
Arsitektur:

- **Service Manager** — server pusat (aplikasi web + repositori).
- **Agent** — dipasang di host MySQL, mengirim metrik.
- Data disimpan di **MEM repository** (MySQL terpisah).

Yang disediakan:

| Fitur | Fungsi |
|---|---|
| Dashboard | grafik status, koneksi, buffer pool |
| Advisors | aturan otomatis yang memberi peringatan (mis. buffer pool terlalu kecil) |
| Query Analyzer | query teratas berdasarkan waktu, mirip slow log tetapi historis |
| Events | catatan kejadian: restart, perubahan konfigurasi |
| Replication monitor | lag, error, thread status |

```text
Alur: MySQL -> agent -> Service Manager (repository) -> browser DBA
```

## Jebakan
- Mengira MEM menggantikan `performance_schema`; ia melengkapinya dengan data historis dan advisory.
- Agent butuh akun MySQL dengan privilege tertentu; tanpa itu metrik tidak lengkap.
- Repository adalah instance MySQL terpisah — butuh backup sendiri.
- MEM tidak tersedia di Community; di ujian muncul sebagai konsep.

## Latihan
1. Komponen apa yang dipasang di host MySQL?
2. Apa fungsi advisor?

<details><summary>Jawaban</summary>
<p><b>1.</b> Agent (Service Manager ada di server terpisah).</p>
<p><b>2.</b> Menjalankan aturan yang mendeteksi konfigurasi/situasi berisiko dan memberi rekomendasi, misalnya buffer pool terlalu kecil.</p>
</details>
