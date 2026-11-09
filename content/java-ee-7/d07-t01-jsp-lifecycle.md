---
title: Siklus Hidup JSP
minutes: 20
level: Dasar
badge: lengkap
summary: Dari file .jsp menjadi servlet - translation, init, service, destroy.
objectives:
  - menjelaskan fase lifecycle JSP
  - Menentukan kapan kode Java di JSP dikompilasi
  - Membedakan _jspInit, _jspService, _jspDestroy
---
## Kenapa topik ini diuji
JSP adalah servlet yang digenerate. Soal menanyakan pada fase apa error sintaks muncul dan method apa yang bisa ditimpa.

## Konsep inti
1. **Translation** - container mengubah `.jsp` menjadi kelas Java (servlet). Error sintaks muncul di sini, bukan saat runtime.
2. **Compilation** - kelas hasil terjemahan dikompilasi.
3. **Initialization** - `jspInit()` dipanggil sekali.
4. **Service** - `_jspService()` dipanggil per request; nama berawalan garis bawah sehingga tidak bisa ditimpa.
5. **Destruction** - `jspDestroy()` sekali saat aplikasi berhenti.

```jsp
<%-- deklarasi: jadi field/method kelas --%>
<%! private int hitungan = 0; %>

<%-- scriptlet: kode di dalam _jspService --%>
<%
  hitungan++;
  String user = (String) session.getAttribute("user");
%>

<%-- expression: dicetak ke output --%>
<p>Halo <%= user != null ? user : "tamu" %> (kunjungan <%= hitungan %>)</p>
```

- JSP di-compile ulang otomatis saat file berubah (development), dan itu mahal.
- `<%@ page contentType="text/html;charset=UTF-8" %>` mengatur header.
- Scriptlet sebaiknya dihindari; gunakan EL dan JSTL.

## Jebakan ujian
- `_jspService` tidak bisa ditimpa karena nama dengan garis bawah; `jspInit`/`jspDestroy` bisa.
- Variabel `hitungan` pada deklarasi adalah field servlet → dibagi semua request (race).
- Error kompilasi JSP tampil sebagai 500 dengan pesan translation.
- `isThreadSafe="false"` membuat container mensinkronkan akses (lambat, jarang dipakai).
- JSP hilang dari `WEB-INF` tetap dapat diakses lewat forward, tetapi tidak lewat URL langsung.

## Latihan
1. Di fase mana kesalahan `<%= x %>` tanpa deklarasi `x` ditemukan?
2. Mengapa field pada `<%! %>` berbahaya?

<details><summary>Jawaban</summary>
<p><b>1.</b> Fase translation/compilation - hasilnya error 500 saat pertama diakses.</p>
<p><b>2.</b> Field itu milik satu instance servlet yang dipakai banyak thread; nilainya bisa saling menimpa.</p>
</details>
