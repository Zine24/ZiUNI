#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ZiCore University — MVP backend (FastAPI + SQLite).
Endpoints:
  /api/university/evaluation/start|answer|submit|result
  /api/university/mastery|progress|credits|recommendations
  /api/university/exercise/generate|exam/generate
  /api/university/portfolio
  /api/health-manager/dashboard|checkin|sleep|activity|break|recommendations|recovery
  /api/careers|/api/structure|/api/levels|/api/courses|/api/modules
"""
import os, re, json, math, time, sqlite3, uuid, random
from pathlib import Path
from datetime import datetime, date
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse, Response
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

from level0 import LEVEL0, SEQUENCE
from level2 import LEVEL2, SEQUENCE2
from level3 import LEVEL3
from sessions_l0 import SESSIONS0

LEVELS = {
    0: {"name": "Zi Foundation", "sub": "Matemáticas fundamentales", "seq": SEQUENCE, "data": LEVEL0, "t": 0, "entry": None},
    2: {"name": "Engineering Core", "sub": "Tronco común de ingeniería", "seq": SEQUENCE2, "data": LEVEL2, "t": 2, "entry": {"level": 0}},
    3: {"name": "Career Cores", "sub": "Núcleo de cada carrera", "seq": None, "data": LEVEL3, "t": 3, "entry": {"level": 2}},
}

# Bump when level0/level2/level3/sessions content changes so the live DB re-seeds.
CONTENT_VERSION = "2"

def _lv_table(level, kind):
    return f"l{LEVELS[level]['t']}_{kind}"

def _course_required(cid):
    for lv in (0, 2):
        d = LEVELS[lv]["data"]
        if cid in d:
            return d[cid]["required"]
    for career in LEVEL3.values():
        if cid in career["courses"]:
            return career["courses"][cid]["required"]
    return 70

def _course_modules_score(cid):
    for lv, meta in LEVELS.items():
        if meta["seq"] and cid in meta["seq"]:
            t = meta["t"]
            mods = q(f"SELECT id FROM l{t}_modules WHERE course_id=?", (cid,))
            vals = []
            for mo in mods:
                m = q(f"SELECT score FROM l{t}_masteries WHERE module_id=?", (mo["id"],), one=True) if False else q("SELECT score FROM masteries WHERE module_id=?", (mo["id"],), one=True)
                vals.append(m["score"] if m and m["score"] is not None else 0)
            if not vals:
                return {"score": 0, "done": 0, "total": 0}
            return {"score": round(sum(vals)/len(vals), 1), "done": sum(1 for v in vals if v >= 70), "total": len(vals)}
    # level3 career courses
    for career in LEVEL3.values():
        if cid in career["courses"]:
            mods = q("SELECT id FROM l3_modules WHERE course_id=?", (cid,))
            vals = []
            for mo in mods:
                m = q("SELECT score FROM masteries WHERE module_id=?", (mo["id"],), one=True)
                vals.append(m["score"] if m and m["score"] is not None else 0)
            if not vals:
                return {"score": 0, "done": 0, "total": 0}
            return {"score": round(sum(vals)/len(vals), 1), "done": sum(1 for v in vals if v >= 70), "total": len(vals)}
    return {"score": 0, "done": 0, "total": 0}

def _level_entry_unlocked(level):
    entry = LEVELS[level]["entry"]
    if not entry:
        return {"unlocked": True, "reason": None}
    prev = entry["level"]
    seq = LEVELS[prev]["seq"]
    if seq is None:
        return {"unlocked": True, "reason": None}
    pending = []
    for cid in seq:
        req = LEVELS[prev]["data"][cid]["required"]
        sc = _course_modules_score(cid)["score"]
        if sc < req:
            pending.append({"course": cid, "current": sc, "required": req})
    return {"unlocked": not pending, "reason": "pending_level", "pending": pending}

BASE = Path(os.environ.get("UNI_BASE", Path(__file__).resolve().parent))
DB = BASE / "data" / "uni.db"
STATIC = BASE / "static"

app = FastAPI(title="ZiCore University", version="0.1.0")

# ---------------- DB helpers ----------------
def conn():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c

def q(sql, args=(), one=False):
    with conn() as c:
        cur = c.execute(sql, args)
        rows = [dict(r) for r in cur.fetchall()]
    return rows[0] if (one and rows) else rows

def x(sql, args=()):
    with conn() as c:
        cur = c.execute(sql, args)
        c.commit()
        return cur.lastrowid

def init_db():
    c = conn()
    c.executescript("""
    CREATE TABLE IF NOT EXISTS careers(
      id TEXT PRIMARY KEY, code TEXT, name_en TEXT, name_es TEXT,
      focus TEXT, color TEXT, levels INTEGER DEFAULT 7);
    CREATE TABLE IF NOT EXISTS courses(
      id INTEGER PRIMARY KEY AUTOINCREMENT, career_id TEXT,
      level TEXT, semester INTEGER, name TEXT, credits INTEGER,
      descr TEXT, seq INTEGER DEFAULT 0);
    CREATE TABLE IF NOT EXISTS modules(
      id TEXT PRIMARY KEY, course_id INTEGER, name TEXT, descr TEXT,
      order_no INTEGER DEFAULT 0, credit_hours INTEGER DEFAULT 2);
    CREATE TABLE IF NOT EXISTS lessons(
      id INTEGER PRIMARY KEY AUTOINCREMENT, module_id TEXT, title TEXT,
      body TEXT, order_no INTEGER DEFAULT 0);
    CREATE TABLE IF NOT EXISTS questions(
      id INTEGER PRIMARY KEY AUTOINCREMENT, module_id TEXT, q TEXT,
      options TEXT, answer TEXT, type TEXT DEFAULT 'multiple',
      difficulty TEXT DEFAULT 'basic', topic TEXT);
    CREATE TABLE IF NOT EXISTS masteries(
      module_id TEXT PRIMARY KEY, score REAL DEFAULT 0, level TEXT,
      attempts INTEGER DEFAULT 0, mastered INTEGER DEFAULT 0,
      error_model TEXT DEFAULT '{}', updated INTEGER DEFAULT 0);
    CREATE TABLE IF NOT EXISTS progress(
      module_id TEXT PRIMARY KEY, status TEXT DEFAULT 'not_started',
      lessons_done INTEGER DEFAULT 0, lessons_total INTEGER DEFAULT 0,
      updated INTEGER DEFAULT 0);
    CREATE TABLE IF NOT EXISTS attempts(
      id INTEGER PRIMARY KEY AUTOINCREMENT, module_id TEXT,
      kind TEXT DEFAULT 'quiz', score REAL, answers TEXT, errors TEXT,
      ts INTEGER);
    CREATE TABLE IF NOT EXISTS projects(
      id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, course_id INTEGER,
      status TEXT DEFAULT 'in_progress', research REAL DEFAULT 0,
      eng REAL DEFAULT 0, impl REAL DEFAULT 0, sim REAL DEFAULT 0,
      docs REAL DEFAULT 0, pres REAL DEFAULT 0, portfolio INTEGER DEFAULT 0,
      ts INTEGER);
    CREATE TABLE IF NOT EXISTS health(
      d TEXT PRIMARY KEY, mood TEXT, sleep_h REAL, activity TEXT,
      breaks INT DEFAULT 0, energy TEXT, study_h REAL DEFAULT 0,
      checkins INTEGER DEFAULT 0, updated INTEGER DEFAULT 0);
    CREATE TABLE IF NOT EXISTS wellness(
      id INTEGER PRIMARY KEY AUTOINCREMENT, kind TEXT, ts INTEGER, val TEXT);
    CREATE TABLE IF NOT EXISTS l0_courses(
      id TEXT PRIMARY KEY, code TEXT, name TEXT, name_en TEXT,
      desc TEXT, credits INTEGER, prereq TEXT, required REAL, color TEXT, seq INTEGER);
    CREATE TABLE IF NOT EXISTS l0_modules(
      id TEXT PRIMARY KEY, course_id TEXT, name TEXT, order_no INTEGER);
    CREATE TABLE IF NOT EXISTS l0_lessons(
      id INTEGER PRIMARY KEY AUTOINCREMENT, module_id TEXT, title TEXT,
      body TEXT, order_no INTEGER);
    CREATE TABLE IF NOT EXISTS l0_questions(
      id INTEGER PRIMARY KEY AUTOINCREMENT, module_id TEXT, q TEXT,
      options TEXT, answer TEXT, type TEXT DEFAULT 'multiple',
      difficulty TEXT DEFAULT 'basic', explanation TEXT);
    CREATE TABLE IF NOT EXISTS l0_levels(
      course_id TEXT, level_no INTEGER, name TEXT, credits REAL,
      PRIMARY KEY(course_id, level_no));
    CREATE TABLE IF NOT EXISTS l0_sessions(
      id TEXT PRIMARY KEY, course_id TEXT, level_no INTEGER,
      title TEXT, body TEXT, order_no INTEGER);
    CREATE TABLE IF NOT EXISTS l0_session_questions(
      id INTEGER PRIMARY KEY AUTOINCREMENT, session_id TEXT, q TEXT,
      options TEXT, answer TEXT, type TEXT DEFAULT 'multiple',
      difficulty TEXT DEFAULT 'basic', explanation TEXT);
    CREATE TABLE IF NOT EXISTS l0_final_questions(
      id INTEGER PRIMARY KEY AUTOINCREMENT, course_id TEXT, level_no INTEGER, q TEXT,
      options TEXT, answer TEXT, type TEXT DEFAULT 'multiple',
      difficulty TEXT DEFAULT 'basic', explanation TEXT);
    CREATE TABLE IF NOT EXISTS l2_courses(
      id TEXT PRIMARY KEY, code TEXT, name TEXT, name_en TEXT,
      desc TEXT, credits INTEGER, prereq TEXT, required REAL, color TEXT, seq INTEGER);
    CREATE TABLE IF NOT EXISTS l2_modules(
      id TEXT PRIMARY KEY, course_id TEXT, name TEXT, order_no INTEGER);
    CREATE TABLE IF NOT EXISTS l2_lessons(
      id INTEGER PRIMARY KEY AUTOINCREMENT, module_id TEXT, title TEXT,
      body TEXT, order_no INTEGER);
    CREATE TABLE IF NOT EXISTS l2_questions(
      id INTEGER PRIMARY KEY AUTOINCREMENT, module_id TEXT, q TEXT,
      options TEXT, answer TEXT, type TEXT DEFAULT 'multiple',
      difficulty TEXT DEFAULT 'basic', explanation TEXT);
    CREATE TABLE IF NOT EXISTS l3_courses(
      id TEXT PRIMARY KEY, career_id TEXT, code TEXT, name TEXT, name_en TEXT,
      desc TEXT, credits INTEGER, prereq TEXT, required REAL, color TEXT, seq INTEGER);
    CREATE TABLE IF NOT EXISTS l3_modules(
      id TEXT PRIMARY KEY, course_id TEXT, name TEXT, order_no INTEGER);
    CREATE TABLE IF NOT EXISTS l3_lessons(
      id INTEGER PRIMARY KEY AUTOINCREMENT, module_id TEXT, title TEXT,
      body TEXT, order_no INTEGER);
    CREATE TABLE IF NOT EXISTS l3_questions(
      id INTEGER PRIMARY KEY AUTOINCREMENT, module_id TEXT, q TEXT,
      options TEXT, answer TEXT, type TEXT DEFAULT 'multiple',
      difficulty TEXT DEFAULT 'basic', explanation TEXT);
    CREATE TABLE IF NOT EXISTS meta(
      k TEXT PRIMARY KEY, v TEXT);
    """)
    c.commit()
    # seed if empty
    n = q("SELECT COUNT(*) AS c FROM careers")[0]["c"]
    if n == 0:
        _seed(c)
        c.commit()
    _ensure_content(c)
    c.commit()
    c.close()

def _seed(c):
    careers = [
      ("computational","CSE","Computational Sciences & Simulation Engineering",
       "Ingeniería en Ciencias Computacionales y Simulación",
       "programación científica, simulación, IA, modelado, análisis de datos, sistemas dinámicos, computación científica","#22d3ee"),
      ("aerospace","ASE","Aerospace & Space Systems Engineering",
       "Ingeniería Aeroespacial y Sistemas Espaciales",
       "aeronáutica, astronáutica, mecánica orbital, satélites, sistemas espaciales, estructuras, aerodinámica, control, diseño de misiones","#f97316"),
      ("propulsion","PRE","Propulsion & Rocket Technology Engineering",
       "Ingeniería de Propulsión y Tecnología de Cohetes",
       "termodinámica, combustión, motores cohete, propulsión química/eléctrica, turbomáquinas, simulación de propulsión","#ef4444"),
      ("nuclear","NEE","Nuclear Engineering & Advanced Energy",
       "Ingeniería Nuclear y Energía Avanzada",
       "física nuclear, reactores, radiación, transferencia térmica, seguridad, materiales, sistemas energéticos avanzados","#a855f7"),
      ("spacesystems","SSE","Advanced Space Systems Engineering",
       "Ingeniería de Sistemas Espaciales Avanzados",
       "arquitectura espacial, sistemas orbitales, energía, comunicaciones, navegación, control, robótica espacial, sistemas autónomos","#10b981"),
    ]
    for cid, code, en, es, foc, color in careers:
        c.execute("INSERT INTO careers(id,code,name_en,name_es,focus,color) VALUES(?,?,?,?,?,?)",(cid,code,en,es,foc,color))
        # seed foundation + core + career courses
        _seed_courses(c, cid)

def _seed_courses(c, cid):
    levels = [
      ("FOUNDATION","Foundation",0,0),
      ("CORE","Common Engineering Core",0,1),
      ("CAREER","Career Engineering",1,2),
      ("ADVANCED","Advanced Engineering",2,3),
      ("SPEC","Specialization",3,4),
      ("RESEARCH","Research",4,5),
    ]
    base_core = [
      ("Matemáticas I: Álgebra","Algebra I",4),
      ("Matemáticas II: Geometría y Trigonometría","Geometry & Trigonometry",4),
      ("Matemáticas III: Pre-Cálculo","Pre-Calculus",4),
      ("Cálculo Diferencial e Integral","Calculus I",5),
      ("Cálculo Multivariable","Calculus II",5),
      ("Álgebra Lineal","Linear Algebra",4),
      ("Ecuaciones Diferenciales","Differential Equations",4),
      ("Probabilidad y Estadística","Probability & Statistics",4),
      ("Física I: Mecánica Clásica","Classical Mechanics",5),
      ("Física II: Electricidad y Magnetismo","Electricity & Magnetism",5),
      ("Termodinámica y Mecánica de Fluidos","Thermodynamics & Fluids",5),
      ("Programación I: Python y Pensamiento Computacional","Programming I: Python",5),
      ("Algoritmos y Estructuras de Datos","Algorithms & Data Structures",5),
      ("Computación Científica y Simulación","Scientific Computing & Simulation",4),
      ("Circuitos y Electrónica","Circuits & Electronics",5),
      ("Ciencias de Materiales","Materials Science",4),
      ("Diseño y Métodos de Ingeniería","Engineering Design & Methods",4),
      ("Sistemas de Control","Control Systems",4),
    ]
    career_courses = {
      "computational": [
        ("IA y Aprendizaje Automático","AI & Machine Learning",5),
        ("Modelado y Sistemas Dinámicos","Modeling & Dynamical Systems",5),
        ("Simulación Física","Physical Simulation",5),
        ("Análisis de Datos y Cómputo Científico","Data Analysis & Scientific Computing",5),
        ("Computación Avanzada","Advanced Computing",4),
      ],
      "aerospace": [
        ("Aerodinámica","Aerodynamics",5),
        ("Mecánica Orbital","Orbital Mechanics",5),
        ("Estructuras Aeroespaciales","Aerospace Structures",5),
        ("Sistemas de Navegación y Control","GN&C Systems",5),
        ("Diseño de Misiones","Mission Design",4),
      ],
      "propulsion": [
        ("Motores Cohete y Combustión","Rocket Engines & Combustion",5),
        ("Propulsión Química y Eléctrica","Chemical & Electric Propulsion",5),
        ("Turbomáquinas y Ciclos de Potencia","Turbomachinery & Power Cycles",5),
        ("Análisis de Ciclos de Propulsión","Propulsion Cycle Analysis",4),
        ("Simulación de Propulsión","Propulsion Simulation",4),
      ],
      "nuclear": [
        ("Física Nuclear","Nuclear Physics",5),
        ("Ingeniería de Reactores","Reactor Engineering",5),
        ("Protección Radiológica","Radiation Protection",4),
        ("Seguridad Nuclear","Nuclear Safety",4),
        ("Sistemas de Energía Avanzada","Advanced Energy Systems",4),
      ],
      "spacesystems": [
        ("Arquitectura de Sistemas Espaciales","Space Systems Architecture",5),
        ("Comunicaciones y Navegación Espacial","Space Comms & Navigation",5),
        ("Robótica Espacial y Sistemas Autónomos","Space Robotics & Autonomy",5),
        ("Energía en el Espacio","Space Power Systems",4),
        ("Integración de Misión","Mission Integration",4),
      ],
    }
    names = {
      "computational":"Computational & Simulation Engineering",
      "aerospace":"Aerospace & Space Systems Engineering",
      "propulsion":"Propulsion & Rocket Technology Engineering",
      "nuclear":"Nuclear Engineering & Advanced Energy",
      "spacesystems":"Advanced Space Systems Engineering",
    }
    idx = 0
    for lvl_code, lvl_name, sem, seq in levels:
        pool = base_core if lvl_code in ("FOUNDATION","CORE") else career_courses.get(cid, [])
        for name_en, name, credits in pool:
            idx += 1
            cur = c.execute("INSERT INTO courses(career_id,level,semester,name,credits,descr,seq) VALUES(?,?,?,?,?,?,?)",
                            (cid, lvl_code, sem, name, credits, f"{lvl_name}: {name} ({name_en})", seq))
            cid_n = cur.lastrowid
            # module + sample lessons
            for m in range(1,4):
                mid = f"{cid}_{cid_n}_{m}"
                c.execute("INSERT INTO modules(id,course_id,name,descr,order_no) VALUES(?,?,?,?,?)",
                          (mid,cid_n,f"{name} · Módulo {m}",f"Módulo {m} de {name}: {lvl_name}",m))
                for i in (1,2):
                    c.execute("INSERT INTO lessons(module_id,title,body,order_no) VALUES(?,?,?,?)",
                              (mid,f"Lección {i}", f"Contenido de la lección {i} del módulo {m}.", i))
            # seed 2 questions per course (module 1)
            mid = f"{cid}_{cid_n}_1"
            c.execute("INSERT INTO questions(module_id,q,options,answer,type,difficulty,topic) VALUES(?,?,?,?,?,?,?)",
                      (mid, f"Concepto clave de {name_en}:",
                       json.dumps({"A":"Opción correcta","B":"Distractor 1","C":"Distractor 2","D":"Distractor 3"}),
                       "A","multiple","basic",name_en))
            c.execute("INSERT INTO questions(module_id,q,options,answer,type,difficulty,topic) VALUES(?,?,?,?,?,?,?)",
                      (mid, f"Problema aplicado de {name_en}:",
                       json.dumps({"A":"Resultado A","B":"Resultado B","C":"Resultado C","D":"Resultado D"}),
                       "B","multiple","intermediate",name_en))
    # health seed today
    today = date.today().isoformat()
    c.execute("INSERT OR IGNORE INTO health(d,mood,sleep_h,activity,energy) VALUES(?,?,?,?,?)",
              (today,"Normal",7.5,"Ligera","Normal"))

def _seed_level(c, level):
    prefix = LEVELS[level]["t"]
    data = LEVELS[level]["data"]
    for idx, cid in enumerate(LEVELS[level]["seq"] or []):
        co = data[cid]
        cols = "id,code,name,name_en,desc,credits,prereq,required,color,seq"
        c.execute(f"INSERT INTO l{prefix}_courses({cols}) VALUES(?,?,?,?,?,?,?,?,?,?)",
                  (cid, co["code"], co["name"], co["name_en"], co["desc"], co["credits"], co.get("prereq"), co["required"], co["color"], idx))
        for mo_i, m in enumerate(co["modules"], 1):
            c.execute(f"INSERT INTO l{prefix}_modules(id,course_id,name,order_no) VALUES(?,?,?,?)",
                      (m["id"], cid, m["name"], mo_i))
            for i, les in enumerate(m.get("lessons", []), 1):
                c.execute(f"INSERT INTO l{prefix}_lessons(module_id,title,body,order_no) VALUES(?,?,?,?)",
                          (m["id"], les["title"], les["body"], i))
            for qrow in m.get("questions", []):
                c.execute(f"INSERT INTO l{prefix}_questions(module_id,q,options,answer,type,difficulty,explanation) VALUES(?,?,?,?,?,?,?)",
                          (m["id"], qrow["q"], json.dumps(qrow["options"]), qrow["answer"], qrow.get("type", "multiple"), qrow.get("difficulty", "basic"), qrow.get("explanation", "")))
    # level 3: seeded from careers structure
    if level == 3:
        for career, meta in LEVEL3.items():
            for idx, cid in enumerate(meta["courses"]):
                co = meta["courses"][cid]
                c.execute("INSERT OR REPLACE INTO l3_courses(id,career_id,code,name,name_en,desc,credits,prereq,required,color,seq) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                          (cid, career, co["code"], co["name"], co["name_en"], co["desc"], co["credits"], co.get("prereq"), co["required"], co["color"], idx))
                for mo_i, m in enumerate(co["modules"], 1):
                    c.execute("INSERT OR REPLACE INTO l3_modules(id,course_id,name,order_no) VALUES(?,?,?,?)",
                              (m["id"], cid, m["name"], mo_i))
                    for i, les in enumerate(m.get("lessons", []), 1):
                        c.execute("INSERT OR REPLACE INTO l3_lessons(module_id,title,body,order_no) VALUES(?,?,?,?)",
                                  (m["id"], les["title"], les["body"], i))
                    for qrow in m.get("questions", []):
                        c.execute("INSERT OR REPLACE INTO l3_questions(module_id,q,options,answer,type,difficulty,explanation) VALUES(?,?,?,?,?,?,?)",
                                  (m["id"], qrow["q"], json.dumps(qrow["options"]), qrow["answer"], qrow.get("type", "multiple"), qrow.get("difficulty", "basic"), qrow.get("explanation", "")))

_CONTENT_TABLES = (
    "l0_courses", "l0_modules", "l0_lessons", "l0_questions",
    "l0_levels", "l0_sessions", "l0_session_questions", "l0_final_questions",
    "l2_courses", "l2_modules", "l2_lessons", "l2_questions",
    "l3_courses", "l3_modules", "l3_lessons", "l3_questions",
)

def _ensure_content(c):
    """Seed content on first run; re-seed when CONTENT_VERSION changes.

    Learner state (masteries/progress/attempts/projects) is keyed by stable
    module/session ids and is intentionally preserved across re-seeds.
    """
    c.commit()
    row = c.execute("SELECT v FROM meta WHERE k='content_version'").fetchone()
    if row and row["v"] == CONTENT_VERSION:
        return
    for t in _CONTENT_TABLES:
        c.execute(f"DELETE FROM {t}")
    _seed_level(c, 0)
    _seed_level(c, 2)
    _seed_level(c, 3)
    _seed_sessions(c)
    c.execute("INSERT OR REPLACE INTO meta(k,v) VALUES('content_version',?)", (CONTENT_VERSION,))
    c.commit()

def _seed_sessions(c):
    n = q("SELECT COUNT(*) AS c FROM l0_sessions")[0]["c"]
    if n > 0:
        return
    for cid, meta in SESSIONS0.items():
        for lev in meta["levels"]:
            c.execute("INSERT OR REPLACE INTO l0_levels(course_id,level_no,name,credits) VALUES(?,?,?,?)",
                      (cid, lev["no"], lev["name"], lev["credits"]))
            for s_i, sess in enumerate(lev["sessions"], 1):
                c.execute("INSERT OR REPLACE INTO l0_sessions(id,course_id,level_no,title,body,order_no) VALUES(?,?,?,?,?,?)",
                          (sess["id"], cid, lev["no"], sess["title"], sess["body"], s_i))
                for qrow in sess.get("exam", []):
                    c.execute("INSERT INTO l0_session_questions(session_id,q,options,answer,type,difficulty,explanation) VALUES(?,?,?,?,?,?,?)",
                              (sess["id"], qrow["q"], json.dumps(qrow["options"]), qrow["answer"], qrow.get("type", "multiple"), qrow.get("difficulty", "basic"), qrow.get("explanation", "")))
            for qrow in lev.get("final", []):
                c.execute("INSERT INTO l0_final_questions(course_id,level_no,q,options,answer,type,difficulty,explanation) VALUES(?,?,?,?,?,?,?,?)",
                          (cid, lev["no"], qrow["q"], json.dumps(qrow["options"]), qrow["answer"], qrow.get("type", "multiple"), qrow.get("difficulty", "basic"), qrow.get("explanation", "")))

init_db()
def _score_to_mastery(s):
    if s < 40: return "No dominado"
    if s < 60: return "Inicial"
    if s < 70: return "Básico"
    if s < 80: return "Competente"
    if s < 90: return "Avanzado"
    return "Dominio"

def _classify_error(a):
    """Clasificación básica de errores según respuesta y tipo."""
    a = (a or "").lower()
    if "unidad" in a or "unit" in a: return "UNIT"
    if any(k in a for k in ("convertir","transform","factor","=")): return "CALCULATION"
    if any(k in a for k in ("supongo","asumo","assume")): return "ASSUMPTION"
    if any(k in a for k in ("if","else","loop","for ","while")): return "PROGRAMMING"
    if "modelo" in a or "model" in a: return "MODEL"
    if "proced" in a or "fórmula" in a or "formula" in a: return "PROCEDURE"
    return "LOGIC"

class AnswerIn(BaseModel):
    module_id: str
    kind: Optional[str] = "quiz"
    answers: List[Dict[str,Any]] = []

class CheckinIn(BaseModel):
    mood: str
    sleep_h: Optional[float] = None
    activity: Optional[str] = None
    energy: Optional[str] = None
    study_h: Optional[float] = None
    breaks: Optional[int] = None

class WellnessIn(BaseModel):
    kind: str
    val: str

@app.get("/api/structure")
def get_structure():
    levels = [
      {"code":"FOUNDATION","label":"Zi Foundation","desc":"Preparación para el estudio formal de ingeniería."},
      {"code":"CORE","label":"Engineering Foundation","desc":"Tronco común de ingeniería."},
      {"code":"CAREER","label":"Career Engineering","desc":"Núcleo de la carrera elegida."},
      {"code":"ADVANCED","label":"Advanced Engineering","desc":"Ingeniería avanzada."},
      {"code":"SPEC","label":"Specialization","desc":"Especialización profesional."},
      {"code":"RESEARCH","label":"Zi Research Institute","desc":"Investigación y R&D."},
    ]
    return {"levels": levels}

@app.get("/api/health")
def get_health():
    return {"status": "ok", "service": "zicore-university", "version": app.version,
            "content_version": CONTENT_VERSION, "levels": sorted(LEVELS.keys()),
            "time": int(time.time())}

@app.get("/api/levels")
def get_levels():
    out = []
    for lv in sorted(LEVELS.keys()):
        meta = LEVELS[lv]
        n = len(meta["seq"]) if meta["seq"] else sum(len(c["courses"]) for c in LEVEL3.values())
        out.append({"level": lv, "name": meta["name"], "sub": meta["sub"],
                    "entry": meta["entry"], "courses": n})
    return {"levels": out}

@app.get("/api/careers")
def get_careers():
    c = q("SELECT id,code,name_en,name_es,focus,color FROM careers ORDER BY id")
    for r in c:
        r["courses"] = q("SELECT id,level,semester,name,credits FROM courses WHERE career_id=? ORDER BY seq", (r["id"],))
    return c

# ---------------- LEVEL 0: Zi Foundation ----------------
def _mastery_of(module_id):
    m = q("SELECT score,mastered,level FROM masteries WHERE module_id=?", (module_id,), one=True)
    if not m: return {"score": None, "mastered": False, "level": None}
    return m

# ---------------- SESSION-BASED COURSES (niveles > sesiones + examen final) ----------------
def _final_key(cid, level_no):
    return f"{cid}_fin{level_no}"

def _s_open(cid, sid):
    row = q("SELECT level_no, order_no FROM l0_sessions WHERE id=?", (sid,), one=True)
    if not row:
        return False
    lev = row["level_no"]; order = row["order_no"]
    if order == 1:
        if lev == 1:
            return True
        pm = q("SELECT score FROM masteries WHERE module_id=?", (_final_key(cid, lev - 1),), one=True)
        return bool(pm and pm["score"] and pm["score"] >= 70)
    prev = q("SELECT id FROM l0_sessions WHERE course_id=? AND level_no=? AND order_no=?", (cid, lev, order - 1), one=True)
    if not prev:
        return False
    pm = q("SELECT score FROM masteries WHERE module_id=?", (prev["id"],), one=True)
    return bool(pm and pm["score"] and pm["score"] >= 70)

def _f_open(cid, level_no):
    sess = q("SELECT id FROM l0_sessions WHERE course_id=? AND level_no=?", (cid, level_no))
    if not sess:
        return False
    for s in sess:
        m = q("SELECT score FROM masteries WHERE module_id=?", (s["id"],), one=True)
        if not (m and m["score"] and m["score"] >= 70):
            return False
    return True

def _graded(key, qs, answers):
    total = len(qs)
    right = 0
    wrong = []
    for a in answers:
        qid = a.get("question_id")
        given = (a.get("answer") or "").strip()
        for rb in qs:
            if rb["id"] == qid:
                if given.upper() == str(rb["answer"]).upper(): right += 1
                else: wrong.append({"question": rb["q"], "given": given, "key": rb["answer"], "explanation": rb.get("explanation") or ""})
    pct = round(right/max(total, 1)*100, 1)
    level = _score_to_mastery(pct)
    errors = {}
    for w in wrong:
        errors.setdefault(_classify_error(w["given"]), 0)
        errors[_classify_error(w["given"])] += 1
    m = q("SELECT error_model FROM masteries WHERE module_id=?", (key,), one=True)
    em = json.loads(m["error_model"]) if m and m["error_model"] else {}
    for k, v in errors.items(): em[k] = em.get(k, 0) + v
    ap = q("SELECT attempts FROM masteries WHERE module_id=?", (key,), one=True)
    att = (ap["attempts"] if ap else 0) + 1
    x("""INSERT INTO masteries(module_id,score,level,attempts,mastered,error_model,updated)
        VALUES(?,?,?,?,?,?,?)
        ON CONFLICT(module_id) DO UPDATE SET score=?, level=?, attempts=?, mastered=?, error_model=?, updated=?""",
      (key, pct, level, att, 1 if pct >= 70 else 0, json.dumps(em), int(time.time()),
       pct, level, att, 1 if pct >= 70 else 0, json.dumps(em), int(time.time())))
    x("INSERT INTO attempts(module_id,kind,score,answers,errors,ts) VALUES(?,?,?,?,?,?)",
      (key, "quiz", pct, json.dumps({"right": right, "total": total}), json.dumps(errors), int(time.time())))
    return {"module_id": key, "score": pct, "level": level, "mastered": pct >= 70,
            "right": right, "total": total, "errors": errors, "wrong": wrong,
            "recommendation": "Reinforcement: revisa la sesión y re-evalúa" if pct < 70 else "Dominio logrado. Continúa."}

def _session_course_payload(level, cid):
    co = LEVELS[level]["data"][cid]
    levels_out = []
    total_credits = 0.0
    earned = 0.0
    for lev in SESSIONS0[cid]["levels"]:
        total_credits += lev["credits"]
        lev_done = True
        sessions_out = []
        for oi, sess in enumerate(lev["sessions"]):
            mas = _mastery_of(sess["id"])
            prog = q("SELECT lessons_done FROM progress WHERE module_id=?", (sess["id"],), one=True)
            sessions_out.append({"id": sess["id"], "title": sess["title"], "body": sess["body"],
                                 "ord_no": lev["no"] * 100 + oi + 1,
                                 "score": mas["score"], "mastered": bool(mas["mastered"]),
                                 "read": (prog["lessons_done"] if prog else 0), "open": _s_open(cid, sess["id"])})
            if not (mas["score"] is not None and mas["score"] >= 70):
                lev_done = False
        fmas = _mastery_of(_final_key(cid, lev["no"]))
        fin_done = bool(fmas["score"] is not None and fmas["score"] >= 70 and _f_open(cid, lev["no"]))
        if fin_done:
            earned += lev["credits"]
        levels_out.append({"no": lev["no"], "name": lev["name"], "credits": lev["credits"],
                           "sessions": sessions_out, "final": {"score": fmas["score"], "mastered": bool(fmas["mastered"]),
                           "open": _f_open(cid, lev["no"])}, "done": lev_done and fin_done})
    return {"id": cid, "code": co["code"], "name": co["name"], "name_en": co["name_en"],
            "desc": co["desc"], "credits": co["credits"], "color": co["color"],
            "required": co["required"], "prereq": co.get("prereq"),
            "mode": "sessions", "unlocked": True, "gate": {"unlocked": True, "type": "open"},
            "levels": levels_out, "credits_total": total_credits, "credits_earned": round(earned, 1)}

@app.post("/api/level/{level}/session/{sid}/exam")
def session_exam_start(level: int, sid: str):
    row = q("SELECT course_id FROM l0_sessions WHERE id=?", (sid,), one=True)
    if not row:
        raise HTTPException(404, "sesión no existe")
    cid = row["course_id"]
    if not _s_open(cid, sid):
        raise HTTPException(403, "sesión bloqueada: aprueba la sesión o el nivel anterior")
    qs = q("SELECT id,q,options,type,difficulty,explanation FROM l0_session_questions WHERE session_id=? ORDER BY id", (sid,))
    if not qs:
        raise HTTPException(404, "sesión sin preguntas")
    return {"started": True, "session_id": sid, "course_id": cid,
            "kind": "session",
            "questions": [{"id": r["id"], "q": r["q"], "options": json.loads(r["options"]) if r["options"] else None,
                           "type": r["type"], "difficulty": r["difficulty"], "explanation": r.get("explanation")} for r in qs]}

@app.post("/api/level/{level}/session/{sid}/submit")
def session_exam_submit(level: int, sid: str, body: AnswerIn):
    row = q("SELECT course_id FROM l0_sessions WHERE id=?", (sid,), one=True)
    if not row:
        raise HTTPException(404, "sesión no existe")
    qs = q("SELECT id,answer,q,type,difficulty,explanation FROM l0_session_questions WHERE session_id=? ORDER BY id", (sid,))
    return _graded(sid, qs, body.answers)

@app.post("/api/level/{level}/session/{sid}/read")
def session_read(level: int, sid: str, body: Optional[dict] = None):
    row = q("SELECT id FROM l0_sessions WHERE id=?", (sid,), one=True)
    if not row:
        raise HTTPException(404, "sesión no existe")
    p = q("SELECT lessons_done FROM progress WHERE module_id=?", (sid,), one=True)
    done = (p["lessons_done"] if p else 0)
    if done == 0:
        x("INSERT OR REPLACE INTO progress(module_id,status,lessons_done,lessons_total,updated) VALUES(?,?,?,?,?)",
          (sid, "completed", 1, 1, int(time.time())))
    return {"ok": True, "read": 1}

@app.post("/api/level/{level}/course/{cid}/final/{n}/exam")
def final_exam_start(level: int, cid: str, n: int):
    if cid not in SESSIONS0:
        raise HTTPException(404, "curso sin sesiones")
    if not _f_open(cid, n):
        raise HTTPException(403, "examen final bloqueado: domina todas las sesiones del nivel")
    qs = q("SELECT id,q,options,type,difficulty,explanation FROM l0_final_questions WHERE course_id=? AND level_no=? ORDER BY id", (cid, n))
    if not qs:
        raise HTTPException(404, "nivel sin preguntas finales")
    return {"started": True, "final_id": _final_key(cid, n), "course_id": cid, "level_no": n,
            "kind": "final",
            "questions": [{"id": r["id"], "q": r["q"], "options": json.loads(r["options"]) if r["options"] else None,
                           "type": r["type"], "difficulty": r["difficulty"], "explanation": r.get("explanation")} for r in qs]}

@app.post("/api/level/{level}/course/{cid}/final/{n}/submit")
def final_exam_submit(level: int, cid: str, n: int, body: AnswerIn):
    if cid not in SESSIONS0:
        raise HTTPException(404, "curso sin sesiones")
    qs = q("SELECT id,answer,q,type,difficulty,explanation FROM l0_final_questions WHERE course_id=? AND level_no=? ORDER BY id", (cid, n))
    return _graded(_final_key(cid, n), qs, body.answers)

def _course_mastery(course_id, mods):
    ids = [m["id"] for m in mods]
    if not ids: return {"score": 0, "mastered": False, "done": 0, "total": 0}
    rows = q(f"SELECT module_id,score FROM masteries WHERE module_id IN ({','.join('?'*len(ids))})", tuple(ids))
    sc = {r["module_id"]: r["score"] for r in rows}
    vals = [sc.get(i, 0) for i in ids]
    done = sum(1 for v in vals if v >= 70)
    avg = round(sum(vals) / len(vals), 1) if vals else 0
    return {"score": avg, "mastered": done == len(ids), "done": done, "total": len(ids)}

def _course_unlocked(cid):
    co = LEVEL0[cid]
    prer = co.get("prereq")
    if not prer: return {"unlocked": True, "required": None, "current": None, "prereq_course": None}
    mods = q("SELECT id FROM l0_modules WHERE course_id=?", (prer,))
    m = _course_mastery(prer, mods)
    req = LEVEL0[prer]["required"]
    return {"unlocked": m["score"] >= req, "required": req, "current": m["score"], "prereq_course": prer}

@app.get("/api/level/0")
def level_zero():
    return level_overview(0)

@app.get("/api/course/{cid}")
def course_detail(cid: str):
    if cid not in LEVEL0: raise HTTPException(404, "curso no existe")
    co = LEVEL0[cid]
    mods = q("SELECT id,name,order_no FROM l0_modules WHERE course_id=? ORDER BY order_no", (cid,))
    mod_items = []
    for mo in mods:
        mas = _mastery_of(mo["id"])
        lessons = q("SELECT id,title,order_no FROM l0_lessons WHERE module_id=? ORDER BY order_no", (mo["id"],))
        done = q("SELECT lessons_done FROM progress WHERE module_id=?", (mo["id"],), one=True)
        mod_items.append({"id": mo["id"], "name": mo["name"], "order": mo["order_no"],
                          "score": mas["score"], "mastered": mas["mastered"],
                          "lessons": [{"id": le["id"], "title": le["title"], "order": le["order_no"]} for le in lessons],
                          "lessons_done": (done["lessons_done"] if done else 0)})
    lock = _course_unlocked(cid)
    return {"id": cid, "code": co["code"], "name": co["name"], "name_en": co["name_en"],
            "desc": co["desc"], "credits": co["credits"], "color": co["color"],
            "required": co["required"], "prereq": co.get("prereq"),
            "unlocked": lock["unlocked"], "gate": lock, "modules": mod_items}

@app.get("/api/module/{mid}")
def module_detail(mid: str):
    row = q("SELECT * FROM l0_modules WHERE id=?", (mid,), one=True)
    if not row: raise HTTPException(404, "módulo no existe")
    lessons = q("SELECT * FROM l0_lessons WHERE module_id=? ORDER BY order_no", (mid,))
    mas = _mastery_of(mid)
    prog = q("SELECT * FROM progress WHERE module_id=?", (mid,), one=True)
    return {"id": mid, "name": row["name"], "course_id": row["course_id"],
            "mastery": mas, "progress": prog or {"lessons_done": 0},
            "lessons": lessons}

class LessonReadIn(BaseModel):
    lesson_id: Optional[int] = None

@app.post("/api/module/{mid}/read")
def module_read(mid: str, body: Optional[LessonReadIn] = None):
    body = body or LessonReadIn()
    row = q("SELECT COUNT(*) AS c FROM l0_lessons WHERE module_id=?", (mid,), one=True)
    total = row["c"]
    p = q("SELECT lessons_done FROM progress WHERE module_id=?", (mid,), one=True)
    done = (p["lessons_done"] if p else 0)
    if body.lesson_id is not None:
        done = min(done + 1, total)
    else:
        done = total
    status = "completed" if done >= total else "in_progress"
    x("""INSERT INTO progress(module_id,status,lessons_done,lessons_total,updated)
        VALUES(?,?,?,?,?)
        ON CONFLICT(module_id) DO UPDATE SET status=?, lessons_done=?, lessons_total=?, updated=?""",
      (mid, status, done, total, int(time.time()), status, done, total, int(time.time())))
    return {"ok": True, "done": done, "total": total}

# ---------------- GENERIC LEVEL ROUTES (L0/L2/L3) ----------------
def _course_gate(level, cid):
    co = None
    if level == 3:
        for career in LEVEL3.values():
            if cid in career["courses"]:
                co = career["courses"][cid]
                break
    else:
        co = LEVELS[level]["data"][cid]
    if co is None:
        return {"unlocked": True, "type": "open", "required": None, "current": None}
    prer = co.get("prereq")
    if not prer:
        return {"unlocked": True, "type": "open", "required": None, "current": None}
    if prer.startswith("foundation:"):
        base = prer.split(":")[1]
        sc = _course_modules_score(base)["score"]
        req = _course_required(base)
        return {"unlocked": sc >= req, "type": "foundation", "prereq_course": base, "required": req, "current": sc}
    if level == 3:
        sc = _course_modules_score(prer)["score"]
        req = _course_required(prer)
        return {"unlocked": sc >= req, "type": "course", "prereq_course": prer, "required": req, "current": sc}
    sc = _course_modules_score(prer)["score"]
    req = _course_required(prer)
    return {"unlocked": sc >= req, "type": "course", "prereq_course": prer, "required": req, "current": sc}

@app.get("/api/level/{level}")
def level_overview(level: int):
    if level not in LEVELS:
        raise HTTPException(404, "nivel no existe")
    meta = LEVELS[level]
    entry = _level_entry_unlocked(level)
    out = {"level": level, "name": meta["name"], "sub": meta["sub"], "entry": entry["unlocked"], "entry_detail": entry}
    if level == 3:
        out["sequence"] = ["careers"]
        out["careers"] = []
        for career, meta3 in LEVEL3.items():
            cmods = []
            for cid, co in meta3["courses"].items():
                cm = _course_modules_score(cid)
                lock = _course_gate(3, cid)
                cmods.append({"id": cid, "code": co["code"], "name": co["name"], "name_en": co["name_en"],
                              "desc": co["desc"], "credits": co["credits"], "color": co["color"],
                              "required": co["required"], "prereq": co.get("prereq"),
                              "mastery": cm["score"], "done": cm["done"], "total": cm["total"], "locked": (entry["unlocked"] and lock["unlocked"])})
            out["careers"].append({"career_id": career, "code": meta3["code"], "name": meta3["name"], "name_en": meta3["name_en"],
                                   "color": meta3["color"], "courses": cmods})
        return out
    seq = meta["seq"]
    out["sequence"] = seq
    for cid in seq:
        co = meta["data"][cid]
        cm = _course_modules_score(cid)
        lock = _course_gate(level, cid)
        out.setdefault("courses", []).append({"id": cid, "code": co["code"], "name": co["name"], "name_en": co["name_en"],
            "desc": co["desc"], "credits": co["credits"], "color": co["color"], "required": co["required"],
            "prereq": co.get("prereq"), "mastery": cm["score"], "done": cm["done"], "total": cm["total"], "locked": lock["unlocked"],
            "mode": "modules"})
    return out

@app.get("/api/level/{level}/course/{cid}")
def level_course(level: int, cid: str):
    if level not in LEVELS:
        raise HTTPException(404, "nivel no existe")
    if level == 3:
        co = None
        for career, meta3 in LEVEL3.items():
            if cid in meta3["courses"]:
                co = meta3["courses"][cid]
                career_id = career
                break
        if not co:
            raise HTTPException(404, "curso no existe")
    else:
        if cid not in LEVELS[level]["data"]:
            raise HTTPException(404, "curso no existe")
        co = LEVELS[level]["data"][cid]
        career_id = None
    t = LEVELS[level]["t"]
    mods = q(f"SELECT id,name,order_no FROM l{t}_modules WHERE course_id=? ORDER BY order_no", (cid,))
    mod_items = []
    for mo in mods:
        mas = q("SELECT score,mastered,level FROM masteries WHERE module_id=?", (mo["id"],), one=True) or {"score": None, "mastered": False, "level": None}
        lessons = q(f"SELECT id,title,order_no FROM l{t}_lessons WHERE module_id=? ORDER BY order_no", (mo["id"],))
        prog = q("SELECT lessons_done FROM progress WHERE module_id=?", (mo["id"],), one=True)
        mod_items.append({"id": mo["id"], "name": mo["name"], "order": mo["order_no"],
                          "score": mas["score"], "mastered": mas["mastered"],
                          "lessons": [{"id": le["id"], "title": le["title"], "order": le["order_no"]} for le in lessons],
                          "lessons_done": (prog["lessons_done"] if prog else 0)})
    lock = _course_gate(level, cid)
    ent = _level_entry_unlocked(level)
    return {"id": cid, "code": co["code"], "name": co["name"], "name_en": co["name_en"], "desc": co["desc"],
            "credits": co["credits"], "color": co["color"], "required": co["required"], "prereq": co.get("prereq"),
            "career_id": career_id, "unlocked": (ent["unlocked"] and lock["unlocked"]),
            "gate": lock, "entry": ent, "modules": mod_items}

@app.get("/api/level/{level}/module/{mid}")
def level_module(level: int, mid: str):
    if level not in LEVELS:
        raise HTTPException(404, "nivel no existe")
    t = LEVELS[level]["t"]
    row = q(f"SELECT * FROM l{t}_modules WHERE id=?", (mid,), one=True)
    if not row:
        raise HTTPException(404, "módulo no existe")
    lessons = q(f"SELECT * FROM l{t}_lessons WHERE module_id=? ORDER BY order_no", (mid,))
    mas = q("SELECT score,mastered,level FROM masteries WHERE module_id=?", (mid,), one=True) or {"score": None, "mastered": False, "level": None}
    prog = q("SELECT lessons_done FROM progress WHERE module_id=?", (mid,), one=True)
    return {"id": mid, "name": row["name"], "course_id": row["course_id"],
            "mastery": mas, "progress": prog or {"lessons_done": 0}, "lessons": lessons}

@app.post("/api/level/{level}/module/{mid}/read")
def level_module_read(level: int, mid: str, body: Optional[LessonReadIn] = None):
    if level not in LEVELS:
        raise HTTPException(404, "nivel no existe")
    t = LEVELS[level]["t"]
    body = body or LessonReadIn()
    row = q(f"SELECT COUNT(*) AS c FROM l{t}_lessons WHERE module_id=?", (mid,), one=True)
    total = row["c"]
    p = q("SELECT lessons_done FROM progress WHERE module_id=?", (mid,), one=True)
    done = (p["lessons_done"] if p else 0)
    if body.lesson_id is not None:
        done = min(done + 1, total)
    else:
        done = total
    status = "completed" if done >= total else "in_progress"
    x("""INSERT INTO progress(module_id,status,lessons_done,lessons_total,updated)
        VALUES(?,?,?,?,?)
        ON CONFLICT(module_id) DO UPDATE SET status=?, lessons_done=?, lessons_total=?, updated=?""",
      (mid, status, done, total, int(time.time()), status, done, total, int(time.time())))
    return {"ok": True, "done": done, "total": total}

@app.get("/api/mastery")
def get_mastery():
    m = q("SELECT module_id,score,level,attempts,mastered,error_model,updated FROM masteries ORDER BY score DESC")
    return m

@app.get("/api/progress")
def get_progress():
    tot = q("SELECT COUNT(*) AS c FROM modules")[0]["c"]
    done = q("SELECT COUNT(*) AS c FROM masteries WHERE score>=70")[0]["c"]
    return {"modules_total": tot, "modules_done": done, "percent": round(done/max(tot,1)*100,1)}

@app.get("/api/credits")
def get_credits():
    rows = q("SELECT c.credits, m.score FROM modules mo JOIN courses c ON mo.course_id=c.id LEFT JOIN masteries m ON m.module_id=mo.id")
    base = sum(r["credits"] for r in rows if r["score"] is not None and r["score"]>=80)
    return {"total_credits_academic": 240, "earned": base, "progress": round(base/240*100,1)}

@app.get("/api/recommendations")
def get_recommendations():
    low = q("SELECT module_id,score FROM masteries WHERE score<70 ORDER BY score LIMIT 3")
    return {
      "reinforce": [{"module": r["module_id"], "score": r["score"],
                     "suggested": "Reinforcement: revisa teoría y re-evalúa con variantes nuevas."} for r in low],
      "advisory": "Concentra sesiones de 50 min con pausas de 10 min (Break Manager)."
    }

def _lv_tables(module_id):
    s = str(module_id or "")
    if s.startswith("l") and len(s) > 2 and s[1].isdigit() and s[2] == "_":
        lvl = int(s[1])
        return lvl if lvl in LEVELS else None
    return None

def _qtable(module_id):
    t = _lv_tables(module_id)
    return f"l{t}_questions" if t is not None else "questions"

def _get_questions(module_id):
    return q(f"SELECT * FROM {_qtable(module_id)} WHERE module_id=? ORDER BY id", (module_id,))

@app.post("/api/university/evaluation/start")
def eval_start(body: AnswerIn):
    qs = _get_questions(body.module_id)
    if not qs:
        raise HTTPException(404, "module no encontrado o sin preguntas")
    return {"started": True, "quiz_id": uuid.uuid4().hex[:12], "module_id": body.module_id,
            "questions": [{"id": r["id"], "q": r["q"], "options": json.loads(r["options"]) if r["options"] else None,
                           "type": r["type"], "difficulty": r["difficulty"],
                           "explanation": r.get("explanation") if "explanation" in r else None} for r in qs]}

@app.post("/api/university/evaluation/answer")
def eval_answer(body: AnswerIn):
    if not body.answers:
        return {"ok": True, "accepted": 0}
    n = 0
    for a in body.answers:
        qid = a.get("question_id")
        given = (a.get("answer") or "").strip()
        table = _qtable(body.module_id)
        row = q(f"SELECT answer,q,explanation FROM {table} WHERE id=?", (qid,), one=True)
        if not row: continue
        ok = given.upper() == row["answer"].upper()
        if not ok:
            cls = _classify_error(given)
            m = q("SELECT error_model FROM masteries WHERE module_id=?", (body.module_id,), one=True)
            em = json.loads(m["error_model"]) if m and m["error_model"] else {}
            em[cls] = em.get(cls,0)+1
            x("INSERT INTO masteries(module_id,score,level,attempts,mastered,error_model,updated) VALUES(?,0,?,1,0,?,?) "
              "ON CONFLICT(module_id) DO UPDATE SET attempts=attempts+1, error_model=?, updated=?",
              (body.module_id,"Inicial",json.dumps(em),int(time.time()),json.dumps(em),int(time.time())))
        n += 1
    return {"ok": True, "accepted": n, "feedback": "Evaluación registrada. Continúa con las siguientes preguntas."}

@app.post("/api/university/evaluation/submit")
def eval_submit(body: AnswerIn):
    table = _qtable(body.module_id)
    qs = q(f"SELECT id,answer,q,type,difficulty,explanation FROM {table} WHERE module_id=? ORDER BY id", (body.module_id,))
    total = len(qs)
    right = 0
    wrong = []
    for a in body.answers:
        qid = a.get("question_id")
        given = (a.get("answer") or "").strip()
        for rb in qs:
            if rb["id"] == qid:
                if given.upper() == rb["answer"].upper(): right += 1
                else: wrong.append({"question": rb["q"], "given": given, "key": rb["answer"], "explanation": rb.get("explanation") or ""})
    pct = round(right/max(total,1)*100,1)
    level = _score_to_mastery(pct)
    errors = {}
    for w in wrong:
        errors.setdefault(_classify_error(w["given"]),0)
        errors[_classify_error(w["given"])] += 1
    m = q("SELECT error_model FROM masteries WHERE module_id=?", (body.module_id,), one=True)
    em = json.loads(m["error_model"]) if m and m["error_model"] else {}
    for k,v in errors.items(): em[k]=em.get(k,0)+v
    attempts_p = q("SELECT attempts FROM masteries WHERE module_id=?", (body.module_id,), one=True)
    att = (attempts_p["attempts"] if attempts_p else 0) + 1
    x("""INSERT INTO masteries(module_id,score,level,attempts,mastered,error_model,updated)
        VALUES(?,?,?,?,?,?,?)
        ON CONFLICT(module_id) DO UPDATE SET score=?, level=?, attempts=?, mastered=?, error_model=?, updated=?""",
      (body.module_id,pct,level,att,1 if pct>=70 else 0,json.dumps(em),int(time.time()),
       pct,level,att,1 if pct>=70 else 0,json.dumps(em),int(time.time())))
    x("INSERT INTO attempts(module_id,kind,score,answers,errors,ts) VALUES(?,?,?,?,?,?)",
      (body.module_id,"quiz",pct,json.dumps({"right":right,"total":total}),json.dumps(errors),int(time.time())))
    return {"module_id": body.module_id, "score": pct, "level": level, "mastered": pct>=70,
            "right": right, "total": total, "errors": errors, "error_analysis": em,
            "wrong": wrong,
            "recommendation": "Reinforcement: revisa teoría y re-evalúa" if pct<70 else "Dominio logrado. Continúa al siguiente módulo."}

@app.get("/api/university/evaluation/result")
def eval_result(module_id: str):
    rows = q("SELECT kind,score,answers,errors,ts FROM attempts WHERE module_id=? ORDER BY ts DESC LIMIT 1", (module_id,))
    if not rows: raise HTTPException(404,"sin intentos")
    r = rows[0]
    return {"module_id": module_id, "score": r["score"], "answers": json.loads(r["answers"]),
            "errors": json.loads(r["errors"] or "{}"), "ts": r["ts"]}

@app.post("/api/university/exercise/generate")
def exercise_generate(body: AnswerIn):
    qs = q("SELECT * FROM questions WHERE module_id=?", (body.module_id,))
    if not qs: raise HTTPException(404,"sin preguntas")
    r = random.choice(qs)
    return {"question": r["q"], "options": json.loads(r["options"]) if r["options"] else None,
            "type": r["type"], "difficulty": r["difficulty"], "hint": "Revisa la lección del módulo."}

@app.post("/api/university/exam/generate")
def exam_generate(body: AnswerIn):
    qs = q("SELECT * FROM questions WHERE module_id=?", (body.module_id,))
    if len(qs)<2: raise HTTPException(404,"preguntas insuficientes")
    picked = random.sample(qs, min(4,len(qs)))
    return {"module_id": body.module_id, "exam_id": uuid.uuid4().hex[:10],
            "questions": [{"id": r["id"], "q": r["q"], "type": r["type"], "difficulty": r["difficulty"]} for r in picked]}

@app.get("/api/university/portfolio")
def get_portfolio():
    return {"projects": q("SELECT * FROM projects ORDER BY ts DESC"), "masteries": get_mastery()}

# ---------------- Health Manager ----------------
@app.get("/api/health-manager/dashboard")
def health_dash():
    today = date.today().isoformat()
    h = q("SELECT * FROM health WHERE d=?", (today,), one=True)
    if not h: return {"today": {"mood":"Normal"},"load":"NORMAL","recovery":"Normal","study_h":6,"sleep_h":7.5}
    study = h["study_h"] or 0
    sleep = h["sleep_h"] or 7
    load = "RECOVERY RECOMMENDED" if (study>=10 and sleep<6) else ("HIGH LOAD" if study>=8 else ("LOW LOAD" if study<4 else "NORMAL"))
    return {"today": dict(h), "load": load, "recovery": "Baja" if sleep<5 else ("Normal" if sleep>=7 else "Media")}

@app.post("/api/health-manager/checkin")
def health_checkin(b: CheckinIn):
    today = date.today().isoformat()
    x("""INSERT INTO health(d,mood,sleep_h,activity,energy,study_h,breaks,checkins,updated)
        VALUES(?,?,?,?,?,?,?,1,?)
        ON CONFLICT(d) DO UPDATE SET mood=excluded.mood, sleep_h=excluded.sleep_h,
        activity=excluded.activity, energy=excluded.energy, study_h=excluded.study_h,
        breaks=excluded.breaks, checkins=checkins+1, updated=excluded.updated""",
      (today,b.mood,b.sleep_h,b.activity,b.energy,b.study_h,b.breaks,int(time.time())))
    return {"ok": True, "note": "Registrado. Zi Health Manager es un sistema de bienestar, no diagnóstico médico."}

@app.post("/api/health-manager/sleep")
def health_sleep(b: WellnessIn):
    today = date.today().isoformat()
    try: v=float(b.val)
    except: v=None
    if v is not None:
        x("UPDATE health SET sleep_h=? WHERE d=?", (v,today))
    return {"ok": True}

@app.post("/api/health-manager/activity")
def health_activity(b: WellnessIn):
    today = date.today().isoformat()
    x("UPDATE health SET activity=? WHERE d=?", (b.val,today))
    return {"ok": True}

@app.post("/api/health-manager/break")
def health_break(b: WellnessIn):
    today = date.today().isoformat()
    x("UPDATE health SET breaks=COALESCE(breaks,0)+1 WHERE d=?", (today,))
    x("INSERT INTO wellness(kind,ts,val) VALUES(?,?,?)", ("break", int(time.time()), b.val))
    return {"ok": True, "tip": "Levántate, camina, descansa la vista e hidrátate."}

@app.get("/api/health-manager/recommendations")
def health_rec():
    h = q("SELECT * FROM health WHERE d=?", (date.today().isoformat(),), one=True)
    out = ["Plan 50 min de estudio y 10 de pausa (Break Manager)."]
    if h and (h["sleep_h"] or 7)<6: out.append("Trata de completar al menos 7 h de sueño esta noche.")
    if h and (h["breaks"] or 0)<2: out.append("Programa al menos 2 pausas activas hoy.")
    return {"recommendations": out}

@app.get("/api/health-manager/recovery")
def health_recovery():
    h = q("SELECT * FROM health WHERE d=?", (date.today().isoformat(),), one=True)
    sleep = h["sleep_h"] if h else 7
    study = h["study_h"] if h else 6
    return {"recovery": "Baja" if sleep<5 else ("Media" if sleep<7 else "Buena"),
            "load": "HIGH" if study>=8 else ("NORMAL" if study>=4 else "LOW")}

# ---------------- demo student dashboard ----------------
@app.get("/api/student/dashboard")
def student_dash():
    prog = get_progress()
    gpa_v = q("SELECT AVG(score) AS a FROM masteries")[0]["a"] or 0
    return {
      "program": "Aerospace & Space Systems Engineering",
      "level": "Advanced Engineering",
      "progress": prog["percent"],
      "gpa": round(gpa_v/10,2),
      "mastery": round(gpa_v,1),
      "credits": get_credits()["progress"],
      "professional": 76,
      "health": "Normal",
    }

# ---------------- static SPA ----------------
@app.get("/university/{rest:path}")
def spa(rest: str):
    p = STATIC / rest
    if rest and p.is_file():
        return FileResponse(p)
    return FileResponse(STATIC / "index.html")

@app.get("/")
def root():
    return FileResponse(STATIC / "index.html")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("UNI_PORT","4010"))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")