/* DevCert — mesin ujian latihan */
(function () {
  "use strict";
  var raw = document.getElementById("quizData");
  if (!raw) return;
  var DATA = JSON.parse(raw.textContent);
  var QS = DATA.questions, N = QS.length;
  var PASS = DATA.pass || 63, MIN = DATA.minutes || 60, PLABEL = DATA.passLabel || "nilai lulus";
  var DOM = DATA.domTitles || {};
  var CERT = DATA.cert || "cert";
  var BESTKEY = "devcert.quiz." + CERT;

  var startEl = document.getElementById("qStart");
  var runEl = document.getElementById("qRun");
  var resEl = document.getElementById("qResult");
  var btnStart = document.getElementById("startQuiz");
  var btnSubmit = document.getElementById("qSubmit");
  var btnPrev = document.getElementById("qPrev");
  var btnNext = document.getElementById("qNext");
  var elCount = document.getElementById("qCount");
  var elTimer = document.getElementById("qTimer");
  var elDom = document.getElementById("qDom");
  var elText = document.getElementById("qText");
  var elOpts = document.getElementById("qOpts");
  var elGrid = document.getElementById("qGrid");

  var order = [], answers = [], cur = 0, left = 0, tick = null, submitted = false;

  function shuffle(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  function fmt(s) {
    var m = Math.floor(s / 60), r = s % 60;
    return (m < 10 ? "0" : "") + m + ":" + (r < 10 ? "0" : "") + r;
  }

  function start() {
    order = shuffle(QS.map(function (_, i) { return i; }));
    answers = new Array(N).fill(null);
    cur = 0; left = MIN * 60; submitted = false;
    startEl.hidden = true; resEl.hidden = true; runEl.hidden = false;
    document.body.classList.add("quiz-on");
    buildGrid(); render(); startTimer();

  }

  function startTimer() {
    elTimer.textContent = fmt(left);
    elTimer.classList.remove("warn");
    clearInterval(tick);
    tick = setInterval(function () {
      left--;
      elTimer.textContent = fmt(left);
      if (left <= 300) elTimer.classList.add("warn");
      if (left <= 0) { clearInterval(tick); finish(true); }
    }, 1000);
  }

  function buildGrid() {
    elGrid.innerHTML = order.map(function (_, i) {
      return '<button type="button" class="qdot" data-i="' + i + '">' + (i + 1) + "</button>";
    }).join("");
    elGrid.querySelectorAll(".qdot").forEach(function (b) {
      b.addEventListener("click", function () { cur = +b.dataset.i; render(); });
    });
  }

  function paintGrid() {
    elGrid.querySelectorAll(".qdot").forEach(function (b, i) {
      b.classList.toggle("answered", answers[i] !== null);
      b.classList.toggle("current", i === cur);
    });
  }

  function render() {
    var q = QS[order[cur]];
    elCount.textContent = "Soal " + (cur + 1) + " / " + N;
    elDom.textContent = DOM[q.d] || q.d;
    elText.textContent = q.q;
    elOpts.innerHTML = q.o.map(function (opt, i) {
      var sel = answers[cur] === i ? " selected" : "";
      return '<button type="button" class="qopt' + sel + '" data-i="' + i + '">' +
        '<span class="qkey">' + "ABCD"[i] + '</span><span>' + opt.replace(/</g, "&lt;") + "</span></button>";
    }).join("");
    elOpts.querySelectorAll(".qopt").forEach(function (b) {
      b.addEventListener("click", function () { answers[cur] = +b.dataset.i; render(); });
    });
    btnPrev.disabled = cur === 0;
    btnNext.disabled = cur === N - 1;
    paintGrid();
  }

  btnPrev.addEventListener("click", function () { if (cur > 0) { cur--; render(); } });
  btnNext.addEventListener("click", function () { if (cur < N - 1) { cur++; render(); } });
  btnStart.addEventListener("click", start);
  btnSubmit.addEventListener("click", function () {
    var kosong = answers.filter(function (a) { return a === null; }).length;
    if (kosong > 0 && !confirm(kosong + " soal belum dijawab. Kumpulkan sekarang?")) return;
    finish(false);
  });

  document.addEventListener("keydown", function (e) {
    if (runEl.hidden || submitted) return;
    var tag = (e.target.tagName || "").toLowerCase();
    if (tag === "input" || tag === "textarea") return;
    if (["1", "2", "3", "4"].indexOf(e.key) !== -1) {
      answers[cur] = +e.key - 1; render(); e.preventDefault();
    }
    if (e.key === "ArrowRight" && cur < N - 1) { cur++; render(); }
    if (e.key === "ArrowLeft" && cur > 0) { cur--; render(); }
  });

  function finish(auto) {
    if (submitted) return;
    submitted = true;
    clearInterval(tick);

    var benar = 0, perDom = {};
    order.forEach(function (qi, i) {
      var q = QS[qi];
      var d = q.d;
      if (!perDom[d]) perDom[d] = { total: 0, benar: 0 };
      perDom[d].total++;
      if (answers[i] === q.a) { benar++; perDom[d].benar++; }
    });
    var pct = Math.round((benar / N) * 100);
    var lulus = pct >= PASS;

    var best = 0;
    try { best = parseInt(localStorage.getItem(BESTKEY) || "0", 10) || 0; } catch (e) {}
    if (pct > best) { best = pct; try { localStorage.setItem(BESTKEY, String(pct)); } catch (e) {} }

    var domRows = Object.keys(DOM).filter(function (k) { return perDom[k]; }).map(function (k) {
      var x = perDom[k], p = Math.round((x.benar / x.total) * 100);
      var cls = p >= 70 ? "ok" : (p >= 50 ? "mid" : "low");
      return '<div class="qres-row"><span>' + (DOM[k] || k) + '</span>' +
        '<span class="qres-bar"><i class="' + cls + '" style="width:' + p + '%"></i></span>' +
        '<b>' + x.benar + "/" + x.total + '</b></div>';
    }).join("");

    var review = order.map(function (qi, i) {
      var q = QS[qi], chosen = answers[i];
      var ok = chosen === q.a;
      return '<div class="qrev' + (ok ? " correct" : " wrong") + '">' +
        '<p class="qrev-q"><span class="qtag">' + (ok ? "BENAR" : "SALAH") + "</span> " +
        q.q.replace(/</g, "&lt;") + "</p>" +
        '<p class="qrev-a">Jawabanmu: <b>' + (chosen === null ? "kosong" : "ABCD"[chosen] + ". " + q.o[chosen]) + "</b></p>" +
        (ok ? "" : '<p class="qrev-a">Jawaban benar: <b>' + "ABCD"[q.a] + ". " + q.o[q.a] + "</b></p>") +
        '<p class="qrev-e">' + q.e.replace(/</g, "&lt;") + "</p></div>";
    }).join("");

    resEl.hidden = false; runEl.hidden = true;
    resEl.innerHTML =
      '<div class="qscore ' + (lulus ? "pass" : "fail") + '">' +
        '<span class="qscore-num">' + pct + '%</span>' +
        '<span class="qscore-lbl">' + benar + " dari " + N + " soal benar · " + (lulus ? "LULUS" : "BELUM LULUS") +
        " (" + PLABEL + " " + PASS + "%)" + "</span>" +
        (auto ? '<span class="qscore-lbl">Waktu habis — dikumpulkan otomatis.</span>' : "") +
        '<span class="qscore-lbl">Rekor terbaikmu: ' + best + "%</span>" +
      "</div>" +
      '<div class="qactions"><button class="btn primary" id="qRetry" type="button">Ulangi ujian</button>' +
      '<a class="btn ghost" href="/sertifikasi/' + CERT + '/">Kembali ke silabus</a>' +
      '<a class="btn ghost" href="#pembahasan">Lihat pembahasan</a></div>' +
      '<h2 class="section-title">Performa per domain</h2><div class="qres">' + domRows + "</div>" +
      '<h2 class="section-title" id="pembahasan">Pembahasan</h2><div class="qreview">' + review + "</div>" +
      '<div class="qactions"><button class="btn ghost" id="qRetry2" type="button">Ulangi ujian</button></div>';

    resEl.querySelectorAll("#qRetry, #qRetry2").forEach(function (b) { b.addEventListener("click", start); });

  }
})();
