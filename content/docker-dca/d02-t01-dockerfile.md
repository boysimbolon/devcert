---
title: Instruksi Dockerfile
minutes: 26
level: Menengah
badge: lengkap
summary: FROM, RUN, COPY/ADD, CMD/ENTRYPOINT, ARG/ENV, EXPOSE, USER, HEALTHCHECK.
objectives:
  - Memilih instruksi yang tepat
  - Membedakan CMD dan ENTRYPOINT
  - Menjelaskan ARG vs ENV
---
## Kenapa topik ini diuji
Domain 20%: soal menanyakan instruksi mana untuk kebutuhan tertentu dan perilaku saat container start.

## Konsep inti
```dockerfile
FROM eclipse-temurin:17-jre
ARG VERSION=1.0
ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY target/app.jar app.jar
RUN useradd -r app && chown -R app $APP_HOME
USER app
EXPOSE 8080
HEALTHCHECK CMD curl -f http://localhost:8080/health || exit 1
ENTRYPOINT ["java", "-jar", "app.jar"]
CMD ["--profile=prod"]
```

| Instruksi | Fungsi |
|---|---|
| `FROM` | image dasar (wajib, kecuali `scratch`) |
| `RUN` | eksekusi saat build, menghasilkan layer |
| `COPY` | salin dari build context |
| `ADD` | seperti COPY + URL + auto-extract tar |
| `CMD` | perintah/argumen default (bisa ditimpa) |
| `ENTRYPOINT` | executable utama (sulit ditimpa) |
| `ENTRYPOINT` + `CMD` | CMD menjadi argumen default |
| `ARG` | variabel build-time (tidak ada saat runtime) |
| `ENV` | variabel yang tersedia saat build **dan** runtime |
| `EXPOSE` | dokumentasi port (tidak membuka port) |
| `USER` | pengguna untuk RUN/CMD berikutnya |
| `VOLUME` | deklarasi titik mount |

## Jebakan
- `CMD` bentuk shell (`CMD java -jar app.jar`) dijalankan lewat `/bin/sh -c` sehingga sinyal tidak diteruskan; gunakan bentuk exec (array JSON).
- `RUN cd /app` tidak berpengaruh pada instruksi berikutnya — pakai `WORKDIR`.
- `ADD` dengan URL tidak mengekstrak; hanya tar lokal yang diekstrak.
- `ARG` sebelum `FROM` hanya bisa dipakai di `FROM` (perlu dideklarasikan ulang setelahnya).
- `EXPOSE` tidak mem-publish port; butuh `-p`.

## Latihan
1. Instruksi mana yang bisa ditimpa saat `docker run image lain`?
2. Perbedaan ARG dan ENV?

<details><summary>Jawaban</summary>
<p><b>1.</b> <code>CMD</code>.</p>
<p><b>2.</b> <code>ARG</code> hanya saat build; <code>ENV</code> tersedia saat build dan runtime.</p>
</details>
