---
title: Arsitektur dan Lifecycle JSF
minutes: 24
level: Menengah
badge: lengkap
summary: Enam fase JSF, immediate=true, dan kapan model diperbarui.
objectives:
  - Menyebutkan urutan enam fase lifecycle JSF
  - Menjelaskan efek immediate pada validasi
  - Menentukan kapan navigation rule dievaluasi
---
## Kenapa topik ini diuji
JSF punya lifecycle yang paling sering diuji setelah transaksi EJB. Soal menanyakan di fase mana validasi terjadi dan mengapa action tidak terpanggil.

## Konsep inti
1. **Restore View** - bangun / pulihkan komponen view (state disimpan di `UIViewRoot`).
2. **Apply Request Values** - nilai input masuk; konversi dasar; `immediate=true` memproses validasi di sini.
3. **Process Validations** - konverter dan validator berjalan; gagal maka langsung Render Response.
4. **Update Model Values** - nilai dipindah ke managed bean.
5. **Invoke Application** - action method dipanggil, navigasi dihitung.
6. **Render Response** - HTML dibuat; pada postback, state disimpan.

```java
@Named @ViewScoped
public class PesananForm implements java.io.Serializable {
    private String nama;
    public String simpan() { return "sukses?faces-redirect=true"; }
    public void batal() { nama = null; }
    public String getNama() { return nama; }
    public void setNama(String n) { this.nama = n; }
}
```

```xml
<h:form>
  <h:inputText value="#{pesananForm.nama}" required="true"
               requiredMessage="Nama wajib diisi"/>
  <h:commandButton value="Simpan" action="#{pesananForm.simpan}"/>
  <h:commandButton value="Batal" action="#{pesananForm.batal}" immediate="true"/>
  <h:messages/>
</h:form>
```

## Jebakan ujian
- Validasi gagal membuat lifecycle langsung ke Render Response; action tidak dipanggil.
- `immediate="true"` melewati validasi untuk komponen itu dan memproses di fase 2, biasanya untuk tombol batal.
- Tanpa `<h:messages/>` atau `<h:message/>`, pesan validasi tidak tampil walau validasi berjalan.
- Bean harus `Serializable` untuk scope yang di-passivate (`@SessionScoped`, `@ViewScoped`).
- `faces-redirect=true` menerapkan Post/Redirect/Get sehingga refresh tidak mengirim ulang form.

## Latihan
1. Tombol "Batal" tidak boleh memicu validasi. Atribut apa yang dipakai?
2. Di fase mana method action dipanggil?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>immediate="true"</code>.</p>
<p><b>2.</b> Fase 5, Invoke Application.</p>
</details>
