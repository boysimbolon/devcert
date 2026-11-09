---
title: Sintaks JSP, JSTL, dan Expression Language
minutes: 22
level: Menengah
badge: lengkap
summary: Mengganti scriptlet dengan EL dan tag JSTL untuk loop, kondisi, dan format.
objectives:
  - Menulis EL dengan scope dan operator
  - Memakai c:forEach, c:if, c:choose, fmt:formatDate
  - Menghindari scriptlet dalam kode produksi
---
## Kenapa topik ini diuji
Soal menyukai EL karena banyak jebakan halus: perbedaan `${x}` dan `${x.y}`, scope resolution, serta `empty`.

## Konsep inti
```jsp
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>

<c:if test="${not empty sessionScope.user}">
  <p>Halo ${sessionScope.user.nama}</p>
</c:if>

<c:choose>
  <c:when test="${pesanan.total > 1000000}">VIP</c:when>
  <c:otherwise>Reguler</c:otherwise>
</c:choose>

<table>
  <c:forEach var="p" items="${pesananList}" varStatus="s">
    <tr class="${s.index % 2 == 0 ? 'genap' : 'ganjil'}">
      <td>${s.count}</td>
      <td><c:out value="${p.nama}"/></td>
      <td><fmt:formatNumber value="${p.total}" type="currency" currencySymbol="Rp"/></td>
      <td><fmt:formatDate value="${p.tanggal}" pattern="dd MMM yyyy"/></td>
    </tr>
  </c:forEach>
</table>
```

- EL mencari atribut berurutan: page → request → session → application.
- `${empty x}` benar untuk `null`, string kosong, koleksi kosong.
- `${x.y}` memanggil getter `getY()`; `${x['y']}` untuk nama dinamis.
- `<c:out>` meng-escape HTML - wajib untuk data pengguna (mencegah XSS).
- `${pageContext.request.contextPath}` untuk path aplikasi.

## Jebakan ujian
- `${x}` pada objek memanggil `toString()`; untuk properti pakai `${x.prop}`.
- EL tidak punya `if` sebagai ekspresi; gunakan `c:choose` atau ternary di atribut.
- `c:forEach` dengan `varStatus` menyediakan `index` (0-based), `count` (1-based).
- JSTL 1.2 memakai URI `http://java.sun.com/jsp/jstl/core` (bukan `jakarta`).
- EL diabaikan bila `isELIgnored="true"` pada directive page.

## Latihan
1. Apa hasil `${empty daftar}` bila `daftar` adalah `List` kosong?
2. Tag apa untuk meng-escape output pengguna?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>true</code>.</p>
<p><b>2.</b> <code>&lt;c:out&gt;</code> (atau <code>fn:escapeXml</code>).</p>
</details>
