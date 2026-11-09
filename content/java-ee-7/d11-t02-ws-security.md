---
title: Standar Keamanan Web Service
minutes: 20
level: Menengah
badge: lengkap
summary: WS-Security, token, signature, dan enkripsi pesan SOAP.
objectives:
  - Menjelaskan keamanan level pesan vs level transport
  - Mengenali standar WS-Security, WS-Policy, dan SAML
  - Memilih konfigurasi untuk menandatangani dan mengenkripsi pesan
---
## Kenapa topik ini diuji
Ini domain hafalan standar. Soal memberi kebutuhan, misalnya pesan harus utuh end-to-end lewat perantara, lalu menanyakan mekanismenya.

## Konsep inti
Dua lapisan yang harus dibedakan:

- **Transport** - TLS/HTTPS. Melindungi per hop dan berakhir di gateway.
- **Message** - WS-Security. Bertahan melewati perantara karena header keamanan ikut di dalam pesan.

Standar yang sering disebut:

| Standar | Fungsi |
|---|---|
| WS-Security | UsernameToken, signature, enkripsi XML |
| WS-Policy | mendeklarasikan kewajiban (signed, encrypted) |
| WS-Trust | penerbitan dan pertukaran token |
| WS-SecureConversation | sesi aman berulang |
| SAML | assertion identitas untuk federasi/SSO |

```xml
<wsp:Policy wsu:Id="SignedPolicy">
  <sp:SignedParts>
    <sp:Body/>
  </sp:SignedParts>
</wsp:Policy>
```

## Jebakan ujian
- TLS melindungi titik-ke-titik; WS-Security melindungi end-to-end. Ini pasangan yang paling sering ditanyakan.
- Enkripsi XML mengenkripsi sebagian elemen, bukan seluruh pesan.
- UsernameToken bisa plaintext atau digest; tanpa TLS rawan disadap.
- SAML membawa identitas/atribut, bukan aturan otorisasi aplikasi.
- REST dan WebSocket tidak memakai WS-Security; keduanya memakai token/OAuth.

## Latihan
1. Mekanisme mana yang tetap aman walau pesan melewati tiga perantara?
2. Standar apa untuk menyatakan kewajiban signed/encrypted pada WSDL?

<details><summary>Jawaban</summary>
<p><b>1.</b> WS-Security (level pesan).</p>
<p><b>2.</b> WS-Policy.</p>
</details>
