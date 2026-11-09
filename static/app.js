(() => {
  const API = "/api";
  const main = document.getElementById("main");
  const navRoot = document.querySelector("nav");
  let state = { m: null, quiz: null, answers: {}, examMode: false };
  // Global bridge used by inline handlers generated in the views.
  window.ZCU = window.ZCU || {};

  // All in-app hash links (sidebar + content) go through the router.
  document.addEventListener("click", (e) => {
    const a = e.target.closest('a[href^="#/university"]');
    if (!a) return;
    e.preventDefault();
    route(a.getAttribute("href").slice(1));
  });

  // Mark the sidebar entry that matches the current route (including subroutes).
  function setActiveNav(route) {
    const links = [...navRoot.querySelectorAll("a[data-route]")];
    let best = null;
    for (const a of links) {
      const r = a.dataset.route;
      if (route === r || route.startsWith(r + "/")) {
        if (!best || r.length > best.dataset.route.length) best = a;
      }
    }
    for (const a of links) {
      const on = a === best;
      a.classList.toggle("active", on);
      if (on) a.setAttribute("aria-current", "page");
      else a.removeAttribute("aria-current");
    }
  }

  async function api(path, body) {
    const opt = { headers: { "Content-Type": "application/json" } };
    if (body) opt.method = "POST", opt.body = JSON.stringify(body);
    const r = await fetch(API + path, opt);
    if (!r.ok) throw new Error((await r.json().catch(() => ({}))).detail || r.statusText);
    return r.json();
  }

  function page(title, sub, html) {
    main.innerHTML = `<div class="page"><h1>${title}</h1><div class="sub">${sub}</div>${html}</div>`;
    document.title = title.includes("ZiCore University") ? title : `${title} · ZiCore University`;
    setActiveNav(location.hash.slice(1));
    main.focus({ preventScroll: true });
  }
  function card(title, big, lbl, cls = "") {
    return `<div class="card"><h3>${title}</h3><div class="big ${cls}">${big}</div><div class="lbl">${lbl}</div></div>`;
  }
  function bar(pct, cls = "") { return `<div class="bar"><div style="width:${Math.max(0, Math.min(100, pct))}%"></div></div>`; }

  async function route(r) {
    if (!r) r = "/university/dashboard";
    if (location.hash.slice(1) !== r) history.pushState(null, "", "#" + r);
    setActiveNav(r);
    document.getElementById("main").innerHTML = '<div class="loader">…</div>';
    try {
      if (r.endsWith("/dashboard")) return await dashboard();
      if (r.match(/\/foundation\/course\/.+/i)) return await courseView(0, r.split("/course/")[1]);
      if (r.match(/\/foundation\/module\/.+/i)) return await moduleView(0, r.split("/module/")[1]);
      if (r.match(/\/engineering-core\/course\/.+/i)) return await courseView(2, r.split("/course/")[1]);
      if (r.match(/\/engineering-core\/module\/.+/i)) return await moduleView(2, r.split("/module/")[1]);
      if (r.match(/\/career-cores\/course\/.+/i)) return await courseView(3, r.split("/course/")[1]);
      if (r.match(/\/career-cores\/module\/.+/i)) return await moduleView(3, r.split("/module/")[1]);
      if (r.endsWith("/foundation") || r.endsWith("/foundation/")) return await levelView(0, r.endsWith("/foundation") || r.endsWith("/foundation/"));
      if (r.endsWith("/engineering-core") || r.endsWith("/engineering-core/")) return await levelView(2, true);
      if (r.endsWith("/career-cores") || r.endsWith("/career-cores/")) return await levelView(3, true);
      if (r.endsWith("/core") || r.endsWith("/core/")) return await levelView(2, true);
      if (r.endsWith("/careers")) return await careers();
      if (r.endsWith("/modules")) return await modules();
      if (r.endsWith("/evaluations")) return await evaluations();
      if (r.endsWith("/progress")) return await progress();
      if (r.endsWith("/professional")) return await professional();
      if (r.endsWith("/health-manager")) return await health();
      if (r.endsWith("/research")) return await research();
      if (r.endsWith("/portfolio")) return await portfolio();
      return dashboard();
    } catch (err) { page("Error", "", `<div class="card"><span class="badge bad">ERR</span> ${err.message}</div>`); }
  }

  async function dashboard() {
    const [d, prog, mastery, cred] = await Promise.all([
      api("/student/dashboard"), api("/progress"), api("/mastery"), api("/credits"),
    ]);
    const initials = d.program.split(/\s+/).filter(w => w !== "&").map(w => w[0]).join("").slice(0, 4).toUpperCase();
    page("ZiCore University", "University of Engineering, Science, Space & Advanced Technology",
      `<div class="grid g4">
        ${card("Program", initials, "Aerospace & Space Systems")}
        ${card("Level", "Nivel 4", "Advanced Engineering · 5 carreras")}
        ${card("Progress", d.progress + "%", "Del programa completo")}
        ${card("GPA", d.gpa + " / 10", "Zi GPA Engine")}
      </div>
      <div class="grid g4" style="margin-top:16px">
        ${card("Mastery", (d.mastery||0) + "%", "Knowledge Graph")}
        ${card("Credits", d.credits + "%", "240 académicos")}
        ${card("Professional", d.professional + "%", "Readiness Score")}
        ${card("Health", d.health, "Zi Health Manager", "text")}
      </div>
      <div class="grid g2" style="margin-top:16px">
        <div class="card"><h3>Progreso de módulos</h3><div class="big">${prog.modules_done} / ${prog.modules_total}</div><div class="lbl">Módulos dominados (≥70%)</div>${bar(prog.percent)}</div>
        <div class="card"><h3>Ruta académica</h3><div class="prog-path">
          ${["FOUNDATION","ENGINEERING CORE","5 CAREERS","SPECIALIZATION","RESEARCH"].map((s, i) => `<span class="prog-step ${i<2?"done":i===2?"cur":""}">${s}</span>`).join("→")}
        </div>
        <p class="muted" style="font-size:12px">Todos los estudiantes construyen primero Zi Foundation y el Tronco Común antes de elegir carrera.</p></div>
      </div>`);
  }

  const LV_INFO = {
    0: { title: "Nivel 0 · Zi Foundation", sub: "Matemáticas fundamentales en progresión estricta", base: "/university/foundation" },
    2: { title: "Nivel 2 · Engineering Core", sub: "Tronco común compartido por las cinco carreras", base: "/university/engineering-core" },
    3: { title: "Nivel 3 · Career Cores", sub: "Núcleo propio de cada carrera, después del tronco común", base: "/university/career-cores" },
  };

  function courseCard(level, c, href) {
    const opened = c.locked;
    const flag = !opened ? '<span class="badge warn">BLOQUEADO</span>'
      : (c.done === c.total && c.total > 0 ? '<span class="badge ok">COMPLETADO</span>' : '<span class="badge info">ACTIVO</span>');
    return `<div class="card level-card" style="border-left-color:${c.color}">
      <div class="row-between">
        <h3 class="card-title">${c.code} · ${c.name}</h3>${flag}
      </div>
      <div class="mono" style="font-size:11px;color:${c.color}">${c.name_en} · ${c.credits} créd.</div>
      <p style="font-size:12px;color:var(--mut);margin:8px 0">${c.desc}</p>
      <div style="font-size:12px;margin:6px 0">${c.mode === "sessions" ? "Sesiones" : "Módulos"} ${c.done}/${c.total} · Dominio ${c.mastery}%</div>
      ${bar(c.mastery)}
      ${opened ? `<a class="ghost link-btn" style="margin-top:8px" href="#${href}">Entrar al curso →</a>` : ''}
    </div>`;
  }

  async function levelView(level, isRoot) {
    const info = LV_INFO[level];
    const data = await api("/level/" + level);
    let gate = "";
    if (data.entry === false) {
      const det = data.entry_detail || {};
      const pend = (det.pending || []).map(p => `Módulos de ${p.course}: ${p.current}/${p.required}%`).join(" · ");
      gate = `<div class="card" style="background:var(--panel2);margin-bottom:14px">
        <h3>Nivel bloqueado</h3>
        <p style="font-size:13px;color:var(--mut)">Completa el nivel anterior para abrir este. ${pend || ""}</p>
        <div style="display:flex;gap:10px;margin-top:10px;flex-wrap:wrap">
          ${level === 2 ? '<a class="ghost link-btn" href="#/university/foundation">Ir a Zi Foundation</a>' : '<a class="ghost link-btn" href="#/university/engineering-core">Ir a Engineering Core</a>'}
        </div>
      </div>`;
    }
    if (level === 3 && data.careers) {
      const blocks = data.careers.map(c => `<div class="card" style="margin:14px 0;border-left:3px solid ${c.color}">
        <h3 class="card-title">${c.code} · ${c.name}</h3>
        <div class="mono" style="font-size:12px;color:${c.color}">${c.name_en}</div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px;margin-top:12px">
          ${c.courses.map(co => courseCard(3, co, info.base + "/course/" + co.id)).join("")}
        </div>
      </div>`).join("");
      page(info.title, info.sub, gate + `<div class="card">${blocks}</div>`);
      return;
    }
    page(info.title, info.sub, gate + `<div class="card">
      <div class="prog-path">${(data.sequence || []).map(x => x.toUpperCase()).join(" → ")}</div>
      <p class="muted" style="font-size:12px;margin:10px 0 16px">Cada curso desbloquea al siguiente al superar el dominio requerido.</p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px">
        ${(data.courses || []).map((c, i) => courseCard(level, c, info.base + "/course/" + c.id)).join("")}
      </div>
    </div>`);
  }

  async function courseView(level, cid) {
    const c = await api("/level/" + level + "/course/" + cid);
    window.ZCU._curCourse = c.id;
    if (c.mode === "sessions") return sessionCourse(level, c);
    const info = LV_INFO[level];
    const lab = level === 3 ? `<div class="card" style="background:var(--panel2);margin-bottom:16px">
         <h3>Aplicación en ZICORE</h3>
         <p style="font-size:13px;color:var(--mut)">Cada módulo de esta carrera incluye una lección <b>“Aplicación en ZICORE”</b> que conecta la teoría con el subsistema real del sistema operativo aeroespacial.</p>
         <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px">
           <a class="ghost link-btn" target="_blank" rel="noopener" href="https://aerospace.zicore.space/aerospace">Aerospace OS</a>
           <a class="ghost link-btn" target="_blank" rel="noopener" href="https://aerospace.zicore.space/rendezvous">Simulador Rendezvous</a>
           <a class="ghost link-btn" target="_blank" rel="noopener" href="https://materializer.zicore.space">Materializer 3D</a>
         </div>
       </div>` : "";
    page(`${c.code} · ${c.name}`, c.name_en,
      `<div class="card" style="border-left:3px solid ${c.color};margin-bottom:16px">
         <p style="font-size:13px;color:var(--mut)">${c.desc}</p>
         <div style="display:flex;gap:16px;margin-top:10px;font-size:12px;flex-wrap:wrap" class="muted">
           <span>Créditos: ${c.credits}</span>
           <span>Dominio requerido: ${c.required}%</span>
           <span>Gate: ${c.gate && c.gate.type !== 'open' ? (c.unlocked ? '<span class="badge ok">desbloqueado</span>' : `<span class="badge warn">requiere ${c.gate.prereq_course} ${c.gate.current}/${c.gate.required}%</span>`) : '<span class="badge ok">libre</span>'}</span>
         </div>
       </div>
       ${lab}
       <div style="display:grid;gap:12px">
       ${c.modules.map(m => {
         return `<div class="card" style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap">
           <div style="flex:1;min-width:200px">
             <h3 class="card-title">${m.order}. ${m.name}</h3>
             <div style="font-size:12px;color:var(--mut);margin-top:4px">Lecciones: ${m.lessons_done}/${m.lessons.length} · Dominio: ${m.score ?? "—"}${m.score != null ? "%" : ""}</div>
             <div style="font-size:12px;margin-top:6px">${bar(m.score || 0)}</div>
           </div>
           <a class="ghost link-btn" href="#${info.base}/module/${m.id}">Abrir módulo</a>
         </div>`;
       }).join("")}
       </div>`);
  }

  async function moduleView(level, mid) {
    const m = await api("/level/" + level + "/module/" + mid);
    const info = LV_INFO[level];
    const isDone = (m.progress && m.progress.lessons_done) || 0;
    page(`Módulo ${m.name}`, `Curso: ${m.course_id} · Dominio: ${m.mastery.score ?? "sin evaluar"}${m.mastery.score != null ? "%" : ""}`,
      `<div class="card" style="margin-bottom:16px">
         <h3>Lecciones</h3>
         <div style="display:grid;gap:12px;margin-top:10px">
         ${m.lessons.map((l, i) => `<div class="qrow" style="margin-bottom:0">
           <details>
             <summary style="cursor:pointer;font-weight:600">${i + 1}. ${l.title} <span class="tag">${i + 1 <= isDone ? "leída" : "pendiente"}</span></summary>
             <div class="reading">${l.body}</div>
             <button class="ghost" style="margin-top:12px" onclick="window.ZCU.readLesson(${level},'${mid}', ${l.id})">Marcar lección leída</button>
           </details>
         </div>`).join("")}
         </div>
       </div>
       <div class="card" style="background:var(--panel2)">
         <h3>Evaluación del módulo</h3>
         <p style="font-size:13px;color:var(--mut);margin-bottom:10px">${m.lessons.length} lecciones · ${m.mastery.score != null ? `Última evaluación: ${m.mastery.score}% (${m.mastery.level})` : "Aún no has evaluado este módulo."}</p>
         <button onclick="window.ZCU.evalL0(${level},'${mid}')">Comenzar evaluación</button>
         <span id="quiz-${mid}"></span>
       </div>`);
  }

  async function quizL0(level, mid, name) {
    const zone = document.getElementById("quiz-" + mid);
    if (!zone) return;
    let quiz, answers = {};
    try { quiz = await api("/university/evaluation/start", { module_id: mid }); }
    catch (e) { zone.innerHTML = `<span class="badge bad">ERR</span> ${e.message}`; return; }
    quiz.questions.forEach(a => answers[a.id] = "");
    function render() {
      zone.innerHTML = `<div style="margin-top:12px;font-size:13px;color:var(--mut)">${quiz.questions.length} preguntas · 0–100 · dominio ≥70%</div>
        ${quiz.questions.map((a, i) => `<div class="qrow"><div class="q">${i + 1}. ${a.q}</div>
          ${a.options ? Object.entries(a.options).map(([k, v]) =>
            `<label class="opt"><input type="radio" name="q${a.id}" ${answers[a.id] === k ? "checked" : ""} data-k="${k}" onchange="window.ZCU.setA(${a.id},'${k}')"> ${k}. ${v}</label>`).join("") : ""}
        </div>`).join("")}
        <button onclick="window.ZCU.subm(${level},'${mid}')">Entregar evaluación</button>`;
    }
    window.ZCU.setA = (id, k) => { answers[id] = k; };
    window.ZCU.subm = async (lv, m) => {
      const payload = Object.entries(answers).map(([id, a]) => ({ question_id: +id, answer: a }));
      const res = await api("/university/evaluation/submit", { module_id: m, answers: payload });
      const details = res.wrong && res.wrong.length ? `<div style="margin-top:12px">${res.wrong.map(w =>
        `<div class="qrow" style="border-color:var(--bad)"><div class="q">✗ ${w.question}</div>
         <div style="font-size:12px;color:var(--mut)">Tu respuesta: <span class="badge bad">${w.given || "—"}</span> · Correcta: <span class="badge ok">${w.key}</span></div>
         ${w.explanation ? `<div style="font-size:12px;margin-top:6px" class="muted">${w.explanation}</div>` : ""}</div>`).join("")}</div>` : "";
      zone.innerHTML = `<div class="card" style="background:var(--panel);margin-top:12px">
        <h3>Resultado</h3>
        <div class="big">${res.score} / 100</div>
        <div class="lbl">${res.level} ${res.mastered ? '<span class="badge ok">DOMINIO</span>' : '<span class="badge warn">REFORZAR</span>'}</div>
        <p style="margin-top:10px">Correctas: ${res.right} / ${res.total}</p>
        ${details}
        <button class="ghost" style="margin-top:12px" onclick="window.ZCU.evalL0(${lv},'${m}')">Re-evaluar</button>
        <button style="margin-left:8px" onclick="window.ZCU.courseBack('${m.course_id || ""}')">Volver al curso</button>
      </div>`;
    };
    render();
  }
  window.ZCU.evalL0 = (lv, mid) => { quizL0(lv, mid, ""); };

  // ---------- COURSES BY SESSIONS (niveles > sesiones + examen final) ----------
  async function sessionCourse(level, c) {
    window.ZCU._curCourse = c.id;
    const blocks = c.levels.map(lev => {
      const sessHtml = lev.sessions.map((s, i) => {
        const badge = s.mastered ? '<span class="badge ok">DOMINADA</span>'
          : (s.open ? '<span class="badge">PENDIENTE</span>' : '<span class="badge warn">BLOQUEADA</span>');
        return `<div class="card" style="margin-bottom:8px">
          <div class="row-between">
            <h4 style="font-size:13px;margin:0">Sesión ${i + 1}. ${s.title}</h4>${badge}
          </div>
          <details style="margin-top:6px"><summary style="cursor:pointer;font-size:12px;color:var(--acc)">Ver contenido</summary>
            <div class="reading">${s.body}</div>
            <div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap">
              <button class="ghost" onclick="window.ZCU.readSession(${level},'${s.id}')">Marcar leída</button>
              ${s.open ? `<button onclick="window.ZCU.sessionExam(${level},'${s.id}')">Examen de sesión</button>` : ""}
            </div>
          </details>
          ${s.score != null ? `<div style="font-size:12px;margin-top:6px">${bar(s.score)}</div>` : ""}
          <span id="quiz-${s.id}"></span>
        </div>`;
      }).join("");
      const fin = lev.final;
      const finalBtn = fin.open ? `<button onclick="window.ZCU.finalExam(${level},'${c.id}',${lev.no})">Examen final del nivel ${lev.no}</button>`
        : `<span class="badge warn">Examen final bloqueado</span>`;
      return `<div class="card" style="border-left:3px solid ${c.color};margin:14px 0">
        <div class="row-between">
          <h3 class="card-title" style="margin:0">Nivel ${lev.no} · ${lev.name}</h3>
          ${lev.done ? '<span class="badge ok">COMPLETADO</span>' : ''}
        </div>
        <div style="font-size:12px;color:var(--mut);margin:4px 0 8px">${lev.credits} créditos al aprobar</div>
        ${sessHtml}
        <div style="margin-top:12px;padding-top:10px;border-top:1px dashed var(--mut)">
          ${finalBtn}
          ${fin.score != null ? `<span style="margin-left:10px;font-size:12px">Final: ${fin.score}% ${fin.mastered ? '<span class="badge ok">APROBADO</span>' : ""}</span>` : ""}
          <span id="finquiz-${c.id}-${lev.no}"></span>
        </div>
      </div>`;
    }).join("");
    page(`${c.code} · ${c.name}`, `${c.name_en} · ${c.credits_total} créditos · ${c.credits_earned} obtenidos`,
      `<div class="card" style="border-left:3px solid ${c.color};margin-bottom:10px">
         <p style="font-size:13px;color:var(--mut)">${c.desc}</p>
         <div style="font-size:12px" class="muted">Dominio exigido del curso: ${c.required}%</div>
       </div>
       ${blocks}
       <div class="card" style="background:var(--panel2);margin-top:14px"><h3>Cómo se gana el curso</h3>
       <p style="font-size:13px;color:var(--mut)">Aprueba cada sesión (≥70%) para desbloquear el examen final del nivel. Aprueba el final (≥70%) para ganar sus créditos. Al completar los 4 niveles el curso queda dominado y desbloquea el siguiente.</p></div>`);
  }

  async function quizRunner(zone, startPath, body, submitPath, onDone) {
    let quiz, answers = {};
    try { quiz = await api(startPath, body); }
    catch (e) { zone.innerHTML = `<span class="badge bad">ERR</span> ${e.message}`; return; }
    quiz.questions.forEach(a => answers[a.id] = "");
    function render() {
      zone.innerHTML = `<div style="margin-top:10px;font-size:12px;color:var(--mut)">${quiz.questions.length} preguntas · dominio ≥70%</div>
        ${quiz.questions.map((a, i) => `<div class="qrow"><div class="q">${i + 1}. ${a.q}</div>
          ${a.options ? Object.entries(a.options).map(([k, v]) =>
            `<label class="opt"><input type="radio" name="q${a.id}" data-k="${k}" onchange="window.ZCU.setA(${a.id},'${k}')"> ${k}. ${v}</label>`).join("") : ""}
        </div>`).join("")}
        <button style="margin-top:10px" onclick="window.ZCU.doSubmit()">Entregar examen</button>`;
    }
    window.ZCU.setA = (id, k) => { answers[id] = k; };
    window.ZCU.doSubmit = async () => {
      const payload = Object.entries(answers).map(([id, a]) => ({ question_id: +id, answer: a }));
      const res = await api(submitPath, Object.assign({}, body, { answers: payload }));
      const details = res.wrong && res.wrong.length ? `<div style="margin-top:10px">${res.wrong.map(w =>
        `<div class="qrow" style="border-color:var(--bad)"><div class="q">✗ ${w.question}</div>
         <div style="font-size:12px;color:var(--mut)">Tu respuesta: <span class="badge bad">${w.given || "—"}</span> · Correcta: <span class="badge ok">${w.key}</span></div>
         ${w.explanation ? `<div style="font-size:12px;margin-top:6px" class="muted">${w.explanation}</div>` : ""}</div>`).join("")}</div>` : "";
      zone.innerHTML = `<div class="card" style="background:var(--panel);margin-top:12px">
        <h3>Resultado</h3>
        <div class="big">${res.score} / 100</div>
        <div class="lbl">${res.level} ${res.mastered ? '<span class="badge ok">¡NIVEL SUPERADO!</span>' : '<span class="badge warn">REFORZAR</span>'}</div>
        <p style="margin-top:10px">Correctas: ${res.right} / ${res.total}</p>
        ${details}
        <button class="ghost" style="margin-top:12px" onclick="${onDone.again}">Re-evaluar</button>
        <button style="margin-left:8px" onclick="${onDone.refresh}">Ver progreso</button>
      </div>`;
    };
    render();
  }

  function sessionExam(level, sid) {
    const zone = document.getElementById("quiz-" + sid);
    if (!zone) return;
    quizRunner(zone, `/level/${level}/session/${sid}/exam`, { module_id: sid },
      `/level/${level}/session/${sid}/submit`,
      { again: `window.ZCU.sessionExam(${level},'${sid}')`, refresh: `route(LV_INFO[${level}].base + '/course/' + window.ZCU._curCourse)` });
  }

  function finalExam(level, cid, n) {
    const zone = document.getElementById(`finquiz-${cid}-${n}`);
    if (!zone) return;
    quizRunner(zone, `/level/${level}/course/${cid}/final/${n}/exam`, { module_id: `${cid}_fin${n}` },
      `/level/${level}/course/${cid}/final/${n}/submit`,
      { again: `window.ZCU.finalExam(${level},'${cid}',${n})`, refresh: `route(LV_INFO[${level}].base + '/course/' + window.ZCU._curCourse)` });
  }
  window.ZCU.sessionExam = sessionExam;
  window.ZCU.finalExam = finalExam;
  window.ZCU.readSession = async (level, sid) => {
    await api(`/level/${level}/session/${sid}/read`, {});
    route(LV_INFO[level].base + "/course/" + window.ZCU._curCourse);
  };

  window.ZCU.readLesson = async (lv, mid, lid) => {
    await api("/level/" + lv + "/module/" + mid + "/read", { lesson_id: lid });
    moduleView(lv, mid);
  };
  window.ZCU.courseBack = (cid) => { };
  window.ZCU.refreshBack = async (lv, m) => { };  // patched per module below

  // patch back-navigation to know its course + level
  const _origCView = moduleView;
  moduleView = async function (level, mid) {
    const m = await api("/level/" + level + "/module/" + mid);
    window.ZCU.courseBack = () => route(LV_INFO[level].base + "/course/" + m.course_id);
    window.ZCU.refreshBack = async () => moduleView(level, mid);
    return _origCView(level, mid);
  };

  async function careers() {
    const data = await api("/careers");
    page("Carreras de Ingeniería", "Cinco carreras construidas sobre el tronco común",
      data.map(c => `<div class="card level-card" style="border-left-color:${c.color};margin-bottom:14px">
        <h3>${c.name_es}</h3>
        <div class="mono" style="font-size:12px;color:${c.color}">${c.name_en} · ${c.code}</div>
        <p style="font-size:13px;margin:8px 0;color:var(--mut)">${c.focus}</p>
        <details><summary style="cursor:pointer;color:var(--acc);font-size:12px">Ver plan de estudios</summary>
        <table style="margin-top:10px"><tr><th>Materia</th><th>Nivel</th><th>Cr</th></tr>
        ${c.courses.map(co => `<tr><td>${co.name}</td><td class="mono">${co.level}</td><td>${co.credits}</td></tr>`).join("")}
        </table></details></div>`).join(""));
  }

  async function modules() {
    const data = await api("/careers");
    const mastery = await api("/mastery");
    const mmap = {}; mastery.forEach(m => mmap[m.module_id] = m);
    const rows = [];
    for (const c of data) for (const co of c.courses) {
      const mid = `${c.id}_${co.id}_1`;
      const m = mmap[mid];
      rows.push(`<tr><td>${c.code}</td><td>${co.name}</td><td class="mono">${mid}</td>
        <td>${m ? `<span class="badge ${m.mastered ? "ok" : "warn"}">${m.level}</span>` : '<span class="badge">—</span>'}</td>
        <td><button class="ghost" onclick="window.ZCU.eval('${mid}')">Evaluar</button></td></tr>`);
    }
    page("Módulos", "Cada materia se divide en módulos independientes con evaluación",
      `<div class="card"><div style="overflow-x:auto"><table><tr><th>Car</th><th>Materia</th><th>Module</th><th>Dominio</th><th></th></tr>${rows.join("")}</table></div></div>`);
  }

  async function evaluations() {
    page("Evaluaciones", "Zi Academic Evaluation Engine · 0–100",
      `<div class="card" id="evbox">
        <div class="field"><label>ID de módulo</label><input id="evmid" placeholder="p.ej. computational_45_1">
        <button style="margin-top:8px" onclick="window.ZCU.eval(document.getElementById('evmid').value)">Comenzar evaluación</button></div>
        <div class="muted" style="font-size:12px;margin-top:6px">Puedes copiar un Module ID desde la vista Módulos.</div>
        <div id="quizzone"></div>
      </div>`);
    window.ZCU.quizZone = () => document.getElementById("quizzone");
  }

  async function quizFlow(moduleId) {
    const zone = window.ZCU.quizZone ? window.ZCU.quizZone() : null;
    if (!zone) return;
    let quiz, answers = {};
    try { quiz = await api("/university/evaluation/start", { module_id: moduleId }); }
    catch (e) { zone.innerHTML = `<span class="badge bad">ERR</span> ${e.message}`; return; }
    const cat = {};
    quiz.questions.forEach(a => answers[a.id] = "");
    function render() {
      zone.innerHTML = `<p class="mono" style="margin-bottom:14px">Evaluación de <b>${moduleId}</b> · ${quiz.questions.length} preguntas · tipo de dominio: 0–100</p>
        ${quiz.questions.map((a, i) => `<div class="qrow"><div class="q">${i + 1}. ${a.q}</div>
          ${a.options ? Object.entries(a.options).map(([k, v]) =>
            `<label class="opt"><input type="radio" name="q${a.id}" ${answers[a.id] === k ? "checked" : ""} data-k="${k}" onchange="window.ZCU.setA(${a.id},'${k}')"> ${k}. ${v}</label>`).join("") : ""
          }</div>`).join("")}
        <button onclick="window.ZCU.submit('${moduleId}')">Entregar evaluación</button>`;
    }
    window.ZCU.setA = (id, k) => { answers[id] = k; };
    window.ZCU.submit = async (mid) => {
      const payload = Object.entries(answers).map(([id, a]) => ({ question_id: +id, answer: a }));
      const res = await api("/university/evaluation/submit", { module_id: mid, answers: payload });
      zone.innerHTML = `<div class="card" style="background:var(--panel2)">
        <h3>Resultado</h3>
        <div class="big">${res.score} / 100</div>
        <div class="lbl">${res.level} ${res.mastered ? '<span class="badge ok">DOMINIO</span>' : ""}</div>
        <p style="margin-top:10px">Correctas: ${res.right} / ${res.total}</p>
        <p style="margin-top:6px">${res.recommendation}</p>
        <p style="margin-top:10px" class="mono small muted">Error analysis: ${JSON.stringify(res.errors) || "ninguno"}</p>
        <button class="ghost" style="margin-top:12px" onclick="window.ZCU.eval('${mid}')">Re-evaluar (recuperación)</button>
      </div>`;
    };
    render();
  }
  window.ZCU.eval = (mid) => { evaluations(); setTimeout(() => quizFlow(mid), 60); };

  async function progress() {
    const mastery = await api("/mastery");
    const prog = await api("/progress");
    page("Progreso y Maestría", "Zi Academic Knowledge Graph · retención y dominio",
      `<div class="grid g2">
        <div class="card"><h3>Avance general</h3><div class="big">${prog.percent}%</div><div class="lbl">${prog.modules_done}/${prog.modules_total} módulos dominados</div></div>
        <div class="card"><h3>Knowledge Graph</h3>${bar(prog.percent)}</div>
      </div>
      <div class="card" style="margin-top:16px"><table><tr><th>Módulo</th><th>Score</th><th>Nivel</th><th>Intentos</th><th>Estado</th></tr>
      ${mastery.map(m => `<tr><td class="mono">${m.module_id}</td><td>${m.score}</td><td>${m.level}</td><td>${m.attempts}</td>
        <td>${m.mastered ? '<span class="badge ok">Dominado</span>' : '<span class="badge warn">Reforzar</span>'}</td></tr>`).join("") || '<tr><td colspan="5" class="muted">Sin evaluaciones aún.</td></tr>'}
      </table></div>`);
  }

  async function professional() {
    page("Zi Professional Track", "Ruta transversal desde los primeros niveles · Knowledge + Skills + Portfolio",
      `<div class="grid g3" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
        ${card("Python Freelancing", "Nivel 1", "Ingresos durante la formación")}
        ${card("Data Analysis", "Nivel 1", "Procesa y reporta datos")}
        ${card("Technical Documentation", "Nivel 1", "Escribe informes técnicos")}
        ${card("CAD & Simulation", "Nivel 2", "Modelado y simulación")}
        ${card("AI-assisted Workflows", "Nivel 2", "Automatización con IA")}
        ${card("Professional Portfolio", "76%", "Zi Professional Readiness Score")}
      </div>
      <div class="card" style="margin-top:16px"><h3>Zi Professional Readiness Score</h3>
        ${bar(76, "")}
        <div style="display:flex;justify-content:space-between;font-size:12px" class="muted"><span>Technical · Problem solving · Comms · Docs · Projects · Portfolio · Tools</span><span>76%</span></div>
      </div>`);
  }

  async function health() {
    const d = await api("/health-manager/dashboard");
    page("Zi Health Manager", "Sistema de bienestar y seguimiento preventivo · <b>no es diagnóstico médico</b>",
      `<div class="grid g2">
        <div class="card"><h3>Estado de hoy</h3>
          <div class="health-row"><span class="hname">Sueño</span><div class="hbar"><div style="width:${(d.today.sleep_h || 7) / 10 * 100}%;background:var(--acc)"></div></div><span class="mono">${d.today.sleep_h || 7}h</span></div>
          <div class="health-row"><span class="hname">Recovery</span><div class="hbar"><div style="width:${d.recovery === "Baja" ? 30 : 70}%;background:${d.recovery === "Baja" ? "var(--bad)" : "var(--warn)"}"></div></div><span>${d.recovery}</span></div>
          <div class="health-row"><span class="hname">Carga de estudio</span><div class="hbar"><div style="width:60%;background:var(--acc2)"></div></div><span class="badge ${d.load === "RECOVERY RECOMMENDED" ? "bad" : d.load === "HIGH LOAD" ? "warn" : "ok"}">${d.load}</span></div>
          <div class="health-row"><span class="hname">Check-ins</span><div class="hbar"><div style="width:${(d.today.checkins || 0) * 20}%;background:var(--ok)"></div></div><span>${d.today.checkins || 0}</span></div>
        </div>
        <div class="card"><h3>Daily Health Check</h3>
          <div class="field"><label>¿Cómo te sientes hoy?</label>
          <select id="mood">${["Excelente", "Bien", "Normal", "Cansado", "Estresado", "Agotado"].map(m => `<option ${d.today.mood === m ? "selected" : ""}>${m}</option>`).join("")}</select></div>
          <div class="field"><label>Horas de sueño</label><input id="sleeph" type="number" step="0.5" value="${d.today.sleep_h || 7}"></div>
          <div class="field"><label>Horas de estudio hoy</label><input id="studyh" type="number" step="0.5" value="${d.today.study_h || 6}"></div>
          <button onclick="window.ZCU.checkin()">Registrar check-in</button>
          <button class="ghost" style="margin-left:8px" onclick="window.ZCU.breakp()">+ Pausa</button>
        </div>
      </div>
      ${card("Zi Mentor", "Recomendaciones adaptativas", "Explica · ejercicios · análisis de errores · planes de estudio", "text")}` +
      `<div class="card" style="margin-top:16px"><h3>Recomendaciones de bienestar</h3><div id="rec"></div></div>`);
    api("/health-manager/recommendations").then(r => {
      document.getElementById("rec").innerHTML = r.recommendations.map(x => `<div style="margin:6px 0;font-size:13px">▪ ${x}</div>`).join("");
    }).catch(() => {});
    window.ZCU.checkin = async () => {
      await api("/health-manager/checkin", { mood: document.getElementById("mood").value, sleep_h: +document.getElementById("sleeph").value, study_h: +document.getElementById("studyh").value });
      health();
    };
    window.ZCU.breakp = async () => { await api("/health-manager/break", { kind: "break", val: "50/10" }); health(); };
  }

  async function research() {
    page("Zi Research Institute", "De Estudiante → Ingeniero → Especialista → Investigador",
      `<div class="grid g4">
        ${card("Research Projects", "0", "Grupos y publicaciones")}
        ${card("ZiLabs", "9", "Física · Computación · Simulación · Aeroespacial · Propulsión · Nuclear · Space · IA · Robótica")}
        ${card("Capstone", "Pendiente", "Proyectos de integración", "text")}
        ${card("Interdisciplinary", "✔", "Nuclear+Propulsión+Space · IA+Órbita+Space")}
      </div>
      <div class="card" style="margin-top:16px"><h3>Ruta de investigación</h3>
      <div class="prog-path">${["STUDENT","ENGINEER","SPECIALIST","RESEARCHER"].map((s,i)=>`<span class="prog-step ${i<1?"cur":""}">${s}</span>`).join("→")}</div>
      <p class="muted" style="font-size:12px;margin-top:8px">Disponible tras completar la carrera y la especialización (Comprehensive Assessment).</p></div>`);
  }

  async function portfolio() {
    const p = await api("/university/portfolio");
    page("Zi Student Portfolio", "Proyectos aprobados → portafolio, certificados y competencias",
      `<div class="grid g2">${card("Proyectos", p.projects.length, "Aprobados pasan automáticamente al portafolio")}
      ${card("Competencias registradas", p.masteries.length, "Knowledge graph")}</div>
      <div class="card" style="margin-top:16px"><table><tr><th>Proyecto</th><th>Estado</th></tr>
      ${p.projects.map(x => `<tr><td>${x.title}</td><td>${x.status}</td></tr>`).join("") || '<tr><td colspan="2" class="muted">Sin proyectos aún.</td></tr>'}</table></div>`);
  }

  // boot
  window.addEventListener("popstate", () => route(location.hash.slice(1) || "/university/dashboard"));
  const initial = location.hash.slice(1)
    || (location.pathname.startsWith("/university/") ? location.pathname : "/university/dashboard");
  history.replaceState(null, "", "#" + initial);
  route(initial);
})();