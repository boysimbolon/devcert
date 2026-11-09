---
title: Sintaks JSF dan Tag Library
minutes: 22
level: Menengah
badge: lengkap
summary: Facelets, tag h:, f:, ui:, dan pemilihan komponen input yang tepat.
objectives:
  - Membedakan tag h:, f:, ui:
  - Memakai template Facelets dengan ui:composition
  - Memilih komponen data table dan input
---
## Kenapa topik ini diuji
Soal menyodorkan potongan XHTML dan menanyakan komponen mana yang dirender atau mengapa value tidak muncul.

## Konsep inti
```xml
<!-- template.xhtml -->
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
      xmlns:h="http://xmlns.jcp.org/jsf/html">
<body>
  <ui:insert name="konten"/>
</body>
</html>

<!-- halaman -->
<ui:composition template="/template.xhtml"
                xmlns="http://www.w3.org/1999/xhtml"
                xmlns:ui="http://xmlns.jcp.org/jsf/facelets"
                xmlns:h="http://xmlns.jcp.org/jsf/html"
                xmlns:f="http://xmlns.jcp.org/jsf/core">
  <ui:define name="konten">
    <h:dataTable value="#{daftar.items}" var="p">
      <h:column>#{p.nama}</h:column>
      <h:column>#{p.total}</h:column>
    </h:dataTable>
    <h:form>
      <h:inputText id="judul" value="#{form.judul}"/>
      <h:commandButton value="Kirim" action="#{form.simpan}"/>
    </h:form>
  </ui:define>
</ui:composition>
```

- `h:` komponen UI (inputText, commandButton, dataTable, message).
- `f:` core (f:convertDateTime, f:validator, f:ajax, f:viewParam).
- `ui:` template (composition, define, insert, include, repeat).
- Wajib dibungkus `<h:form>` untuk komponen input/command.
- `f:ajax` untuk partial render: `execute="@this" render="hasil"`.

## Jebakan ujian
- Tanpa `<h:form>`, `h:inputText` tidak mengirim nilai.
- `ui:include` saat build time; `ui:insert`/`ui:define` untuk template; `h:panelGroup` untuk render grup.
- `f:ajax` membutuhkan area render yang id-nya benar (prepend `:form:` bila perlu).
- `h:outputText` bukan input; `h:outputLink` bukan command.
- Tag library harus di-declare namespace di root elemen.

## Latihan
1. Tag untuk partial render dengan AJAX?
2. Apa perbedaan `ui:include` dan `ui:insert`?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>&lt;f:ajax execute="…" render="…"/&gt;</code>.</p>
<p><b>2.</b> <code>ui:include</code> menyisipkan file saat build; <code>ui:insert</code> menandai slot yang diisi <code>ui:define</code>.</p>
</details>
