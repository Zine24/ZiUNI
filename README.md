# ZiUNI — ZiCore University

Plataforma educativa de **ZiCore University**: niveles académicos (Zi Foundation,
Engineering Core y Career Cores), evaluaciones adaptativas, progreso, créditos,
portafolio y un gestor de bienestar (Zi Health Manager).

Backend en **FastAPI + SQLite** que además sirve el frontend estático.

| | |
|---|---|
| **Backend** | FastAPI + Uvicorn + SQLite (`server.py`) |
| **Frontend** | `static/index.html`, `static/app.js`, `static/style.css` |
| **Puerto por defecto** | `4010` (`UNI_PORT`) |
| **Base de datos** | `data/uni.db` |

## Estructura

```
.
├── server.py            # FastAPI app: rutas, evaluaciones, progreso, bienestar
├── level0.py            # Nivel 0 — Zi Foundation (matemáticas fundamentales)
├── level2.py            # Nivel 2 — Engineering Core
├── level3.py            # Nivel 3 — Career Cores
├── level3_extra.py      # Cursos y evaluaciones adicionales de Career Cores
├── sessions_l0.py       # Sesiones del Nivel 0
├── static/
│   ├── index.html       # Shell de la aplicación (SPA)
│   ├── app.js           # Router y vistas del frontend
│   └── style.css        # Estilos
├── data/                # SQLite (uni.db) — no versionado
└── deploy/
    └── deploy_uni.sh    # Publica server/level3/app.js en /opt/zicore-uni
```

## Arranque

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Opcional: cambiar el directorio base (por defecto, el del repo)
export UNI_BASE="$PWD"
export UNI_PORT=4010

python server.py
# o: uvicorn server:app --host 0.0.0.0 --port 4010
```

Abre <http://localhost:4010/>. La base de datos SQLite se crea/migra
automáticamente en `$UNI_BASE/data/uni.db`.

> En producción el servicio usa `UNI_BASE=/opt/zicore-uni`.

## API principal

| Método | Endpoint | Descripción |
|---|---|---|
| `GET` | `/api/health` | Estado del servicio |
| `GET` | `/api/levels` | Niveles disponibles (0, 2, 3) |
| `GET` | `/api/level/{level}` | Detalle de un nivel |
| `GET` | `/api/level/{level}/course/{cid}` | Curso y módulos |
| `GET` | `/api/level/{level}/module/{mid}` | Módulo |
| `GET` | `/api/careers` | Carreras |
| `GET` | `/api/structure` | Estructura completa |
| `GET` | `/api/progress` | Progreso del estudiante |
| `GET` | `/api/credits` | Créditos acumulados |
| `GET` | `/api/mastery` | Dominio por materia |
| `GET` | `/api/recommendations` | Recomendaciones de estudio |
| `GET` | `/api/student/dashboard` | Dashboard del estudiante |
| `POST` | `/api/level/{level}/session/{sid}/read` | Marcar sesión como leída |
| `POST` | `/api/level/{level}/session/{sid}/exam` | Generar examen de sesión |
| `POST` | `/api/level/{level}/session/{sid}/submit` | Enviar respuestas |
| `POST` | `/api/level/{level}/course/{cid}/final/{n}/exam` | Examen final |
| `POST` | `/api/level/{level}/course/{cid}/final/{n}/submit` | Enviar examen final |
| `POST` | `/api/university/evaluation/start` | Iniciar evaluación |
| `POST` | `/api/university/evaluation/answer` | Responder pregunta |
| `POST` | `/api/university/evaluation/submit` | Enviar evaluación |
| `GET` | `/api/university/evaluation/result` | Resultado |
| `POST` | `/api/university/exercise/generate` | Generar ejercicio |
| `POST` | `/api/university/exam/generate` | Generar examen |
| `GET` | `/api/university/portfolio` | Portafolio |
| `GET` | `/api/health-manager/dashboard` | Dashboard de bienestar |
| `POST` | `/api/health-manager/checkin` | Check-in diario |
| `POST` | `/api/health-manager/sleep` | Registrar sueño |
| `POST` | `/api/health-manager/activity` | Registrar actividad |
| `POST` | `/api/health-manager/break` | Registrar pausa |
| `GET` | `/api/health-manager/recommendations` | Recomendaciones de bienestar |
| `GET` | `/api/health-manager/recovery` | Recuperación |

## Despliegue

`deploy/deploy_uni.sh` copia `server.py`, `level3.py`, `level3_extra.py` y
`static/app.js` a `/opt/zicore-uni` creando respaldos con marca de tiempo.

```bash
sudo ./deploy/deploy_uni.sh
```

## Licencia

Sin archivo de licencia; todos los derechos reservados por el autor salvo que se indique lo contrario.
