# -*- coding: utf-8 -*-
"""Level 3 · Career Cores — Enrichment layer (ZiCore University).

Adds a second lesson ("Aplicación en ZICORE") plus one applied question to every
Career Core module. Each lesson connects the theory of the module to the real
subsystem of the ZICORE digital aerospace operating system that implements it.

Consumed by level3.py at import time (see merge block at the bottom of level3.py).
Keyed by module id (l3_<career><course>_m<n>).
"""

EXTRA_LESSONS = {
    # ---------------- COMPUTATIONAL SCIENCES & SIMULATION (CSE) ----------------
    "l3_cs01_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Buffers y colas de telemetría",
            "body": "En el Telemetry Engine de ZICORE los datos se encolan (FIFO) por canal y se consumen en orden de llegada; los buffers LIFO reaparecen en la pila de llamadas del intérprete del motor.\n\nPráctica: en el panel de Telemetría, identifica una cola de muestras por canal y explica por qué su orden no debe alterarse al graficar la serie temporal."},
        "question": {"q": "La cola de mensajes del Telemetry Engine de ZICORE debe procesarse en orden:", "options": {"A": "FIFO (primero en entrar, primero en salir)", "B": "LIFO", "C": "aleatorio", "D": "por prioridad inversa"}, "answer": "A", "difficulty": "basic",
            "explanation": "Las series temporales de telemetría pierden sentido si se reordena la llegada de muestras."},
    },
    "l3_cs01_m2": {
        "lesson": {"title": "Aplicación en ZICORE · El Knowledge Graph",
            "body": "La Knowledge Base de ZICORE organiza documentos y conceptos como un grafo: nodos (temas) y aristas (relaciones), y el buscador recorre ese árbol para responder.\n\nPráctica: en ZIPLASH pide una explicación de dos niveles y observa cómo el sistema navega del concepto general a sus relaciones (grafos de conocimiento)."},
        "question": {"q": "La Knowledge Base de ZICORE representa conceptos y sus relaciones como:", "options": {"A": "un grafo", "B": "una lista lineal", "C": "una pila", "D": "una matriz anónima"}, "answer": "A", "difficulty": "basic",
            "explanation": "Nodos (temas) + aristas (relaciones) forman el grafo de conocimiento."},
    },
    "l3_cs01_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Optimización de trayectorias",
            "body": "El Trajectory Optimizer usa programación dinámica para elegir la secuencia de maniobras de mínimo Δv, reutilizando subproblemas (mismo estado orbital) en lugar de recalcularlos.\n\nPráctica: compara una transferencia de Hohmann (analítica) con una búsqueda por etapas y discute cuándo conviene la tabla de subproblemas."},
        "question": {"q": "El Trajectory Optimizer reduce cómputo reutilizando soluciones de subproblemas (mismo estado orbital) mediante:", "options": {"A": "programación dinámica", "B": "fuerza bruta", "C": "recursión infinita", "D": "eliminación gaussiana"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Subestructura óptima + subproblemas repetidos = tabla de DP."},
    },
    "l3_cs02_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Resolver la anomalía excéntrica",
            "body": "El núcleo de Mecánica Orbital resuelve la ecuación de Kepler M = E − e·sen E por iteración de Newton-Raphson para obtener la posición del satélite en cada instante.\n\nPráctica: con e = 0.7, parte de E₀ = M y reporta cuántas iteraciones bastan para |ΔE| < 1e-6."},
        "question": {"q": "En ZICORE, la ecuación de Kepler (M = E − e·senE) se resuelve típicamente con:", "options": {"A": "el método de Newton-Raphson iterativo", "B": "una solución algebraica exacta", "C": "suma de matrices", "D": "transformada de Fourier"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Es trascendente: se resuelve numéricamente por iteración."},
    },
    "l3_cs02_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Análisis estructural",
            "body": "El módulo de Structural Analysis ensambla la matriz de rigidez K y resuelve K·u = f para obtener desplazamientos; la factorización de Cholesky (matriz simétrica) acelera el cálculo.\n\nPráctica: explica por qué una matriz de rigidez es simétrica y definida positiva, y qué implica para el método de solución."},
        "question": {"q": "Para resolver K·u = f con K simétrica y definida positiva, ZICORE usa preferentemente:", "options": {"A": "factorización de Cholesky", "B": "inversión explícita de K", "C": "regla de Cramer", "D": "eliminación por fuerza bruta"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Cholesky es estable y dos veces más rápido que LU para esos casos."},
    },
    "l3_cs02_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Terreno e interpolación",
            "body": "El Terrain Generator y el Real Star Map interpolan mallas y catálogos: la interpolación bilineal/trilineal reconstruye elevación o brillo entre muestras conocidas.\n\nPráctica: interpola la altitud de un punto entre dos nodos de la malla del terreno y comenta el error frente a una superficie real."},
        "question": {"q": "Para estimar la elevación entre nodos de la malla del Terrain Generator, ZICORE aplica:", "options": {"A": "interpolación (bilineal/trilineal)", "B": "extrapolación constante", "C": "derivación", "D": "integración de Monte Carlo"}, "answer": "A", "difficulty": "basic",
            "explanation": "La interpolación reconstruye valores continuos a partir de muestras discretas."},
    },
    "l3_cs03_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Cálculo numérico vectorizado",
            "body": "El Physics Engine y la simulación orbital operan con arreglos (numpy) para calcular posiciones/velocidades de muchos cuerpos a la vez, evitando bucles en Python.\n\nPráctica: reescribe un bucle que suma fuerzas gravitatorias N-body como operaciones vectorizadas y mide la mejora de tiempo."},
        "question": {"q": "Vectorizar un bucle de fuerzas N-body en ZICORE sirve para:", "options": {"A": "aprovechar operaciones de arreglo sin bucles en Python", "B": "aumentar el tamaño del disquete", "C": "evitar la física", "D": "reducir la masa del satélite"}, "answer": "A", "difficulty": "basic",
            "explanation": "numpy ejecuta el cálculo a nivel de arreglo, muy superior a un bucle interpretado."},
    },
    "l3_cs03_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Integración del Flight Sim",
            "body": "El Flight Sim integra las ecuaciones de movimiento con un método Runge-Kutta de orden 4 (RK4), logrando gran precisión por paso para la dinámica de vuelo.\n\nPráctica: compara Euler explícito y RK4 en un paso grande y observa cómo RK4 conserva mejor la energía de la órbita."},
        "question": {"q": "El Flight Sim integra la dinámica de vuelo con RK4 porque:", "options": {"A": "ofrece más precisión por paso que Euler", "B": "es el método más barato", "C": "no usa derivadas", "D": "solo sirve para ecuaciones lineales"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "RK4 evalúa la pendiente 4 veces y reduce el error de truncamiento."},
    },
    "l3_cs03_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Riesgo de misión",
            "body": "El análisis de riesgo de misión usa Monte Carlo: se muestrean incertidumbres (masa, Isp, dispersión de inyección) y se propagan miles de trayectorias para estimar probabilidades de éxito.\n\nPráctica: con una dispersión del 2% en Δv, corre 1000 muestras y reporta la probabilidad de alcanzar la órbita objetivo."},
        "question": {"q": "La simulación Monte Carlo de una misión ZICORE sirve para:", "options": {"A": "estimar distribuciones de resultados bajo incertidumbre", "B": "eliminar la gravedad", "C": "diseñar el logo", "D": "medir temperatura"}, "answer": "A", "difficulty": "basic",
            "explanation": "Muestrea entradas aleatorias y propaga para obtener probabilidades."},
    },
    "l3_cs04_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Dashboards de Mission Control",
            "body": "Los paneles de Mission Control resumen estadísticas de telemetría (media, desviación, percentiles) y las grafican en tiempo real con estilo glass HUD.\n\nPráctica: sobre una serie de altitud, calcula media y rango intercuartílico y explica qué te dice de la estabilidad del vehículo."},
        "question": {"q": "Para resumir la dispersión de una telemetría en Mission Control, ZICORE reporta:", "options": {"A": "estadísticas como media y desviación estándar", "B": "solo el primer valor", "C": "el color del panel", "D": "el nombre del operador"}, "answer": "A", "difficulty": "basic",
            "explanation": "Media y desviación resumen tendencia central y dispersión."},
    },
    "l3_cs04_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Predicción con ZIO",
            "body": "ZIO y los módulos de análisis ajustan modelos de regresión para predecir consumo, empuje o demanda de potencia a partir de datos históricos.\n\nPráctica: ajusta una regresión lineal de consumo de combustible vs tiempo de encendido y evalúa el coeficiente de determinación R²."},
        "question": {"q": "La regresión en ZICORE se usa para:", "options": {"A": "predecir una variable continua a partir de datos", "B": "clasificar imágenes", "C": "comprimir audio", "D": "enrutar subdominios"}, "answer": "A", "difficulty": "basic",
            "explanation": "La regresión estima una salida numérica continua."},
    },
    "l3_cs04_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Visión por computadora",
            "body": "El módulo de Computer Vision clasifica imágenes (detección de rasgos, OCR) con modelos de clasificación; el umbral de decisión convierte probabilidades en etiquetas.\n\nPráctica: sobre una imagen de un panel, identifica cómo un clasificador binario (alerta/no alerta) cambiaría al variar el umbral."},
        "question": {"q": "El módulo de Computer Vision de ZICORE resuelve principalmente tareas de:", "options": {"A": "clasificación y detección", "B": "termodinámica", "C": "orbitales", "D": "finanzas"}, "answer": "A", "difficulty": "basic",
            "explanation": "Clasificación/detección sobre imágenes y video."},
    },

    # ---------------- AEROSPACE & SPACE SYSTEMS (ASE) ----------------
    "l3_as01_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Pestaña Mecánica Orbital",
            "body": "La pestaña Orbital de ZICORE calcula periodo, velocidad y energía a partir de GM y del radio, mostrando la órbita resultante.\n\nPráctica: obtén v_orb = √(GM/r) para LEO (r ≈ 6771 km) y verifica el periodo con T = 2π√(a³/GM)."},
        "question": {"q": "La velocidad de una órbita circular baja (LEO) ronda:", "options": {"A": "7.8 km/s", "B": "1.1 km/s", "C": "30 km/s", "D": "0.3 km/s"}, "answer": "A", "difficulty": "basic",
            "explanation": "v = √(GM/r) ≈ 7.8 km/s para r ≈ 6771 km."},
    },
    "l3_as01_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Seguimiento de satélites",
            "body": "Con los elementos orbitales (TLE) el módulo de Satellite Control propaga la posición y el Real Star Map la proyecta sobre el cielo.\n\nPráctica: identifica la inclinación de la ISS (≈51.6°) y explica por qué su sub-satélite cubre latitudes hasta ±51.6°."},
        "question": {"q": "Con los elementos orbitales, ZICORE puede:", "options": {"A": "predecir la posición futura del satélite", "B": "cambiar su masa", "C": "anular la gravedad", "D": "eliminar el arrastre"}, "answer": "A", "difficulty": "basic",
            "explanation": "La propagación orbital proyecta el estado en el tiempo."},
    },
    "l3_as01_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Trajectory Optimizer",
            "body": "El Trajectory Optimizer compara Hohmann, bi-elíptica y asistencias gravitatorias para minimizar Δv entre dos órbitas.\n\nPráctica: calcula el Δv total de un Hohmann LEO→GEO y compáralo con la opción bi-elíptica."},
        "question": {"q": "Para un cambio de LEO a GEO coplanar, la maniobra de menor Δv es generalmente:", "options": {"A": "transferencia de Hohmann", "B": "cambio de plano directo", "C": "ascenso en espiral químico", "D": "sin maniobra"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Hohmann es óptima para órbitas circulares coplanares con razón moderada."},
    },
    "l3_as02_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Aerodynamics y CFD",
            "body": "El módulo de Aerodynamics estima coeficientes y condiciones de flujo (Mach, Reynolds) y ofrece placeholders de CFD para perfiles y vehículos.\n\nPráctica: para V = 240 m/s a nivel del mar (a ≈ 340 m/s), calcula el número de Mach y clasifica el régimen."},
        "question": {"q": "Módulo de ZICORE que estima sustentación, arrastre y Mach:", "options": {"A": "Aerodynamics", "B": "Power Management", "C": "Ground Station", "D": "ISRU"}, "answer": "A", "difficulty": "basic",
            "explanation": "Aerodynamics cubre los coeficientes y números adimensionales."},
    },
    "l3_as02_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Vehicle Designer",
            "body": "El Vehicle Designer dimensiona el ala y estima L = ½ρV²SC_L; al aumentar el ángulo de ataque, C_L sube hasta el stall.\n\nPráctica: para un ala de S = 16 m², ρ = 1.225, V = 60 m/s y C_L = 1.2, calcula la sustentación."},
        "question": {"q": "El Vehicle Designer usa qué relación para estimar la sustentación:", "options": {"A": "L = ½ρV²SC_L", "B": "F = ma", "C": "E = mc²", "D": "Q = mcΔT"}, "answer": "A", "difficulty": "basic",
            "explanation": "Es la ecuación clásica de sustentación."},
    },
    "l3_as02_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Vehículos hipersónicos",
            "body": "El diseño VTOL/hipersónico de ZICORE considera el arrastre de onda y el calentamiento a M > 1, con toberas convergente-divergente para propulsión.\n\nPráctica: explica por qué a M > 1 la sección necesaria para acelerar el gas pasa de convergente a convergente-divergente."},
        "question": {"q": "A M = 1 la sección de paso en una tobera es:", "options": {"A": "la garganta (área mínima)", "B": "máxima", "C": "nula", "D": "irrelevante"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "En la garganta el flujo alcanza M = 1; después se expande."},
    },
    "l3_as03_m1": {
        "lesson": {"title": "Aplicación en ZICORE · CG y margen estático",
            "body": "El Vehicle Designer calcula el centro de gravedad y lo compara con el foco aerodinámico para reportar el margen estático SM.\n\nPráctica: con h_foco = 0.42 y h_cg = 0.30 (en cuerdas), calcula SM y decide si el vehículo es estable."},
        "question": {"q": "Con h_foco = 0.42 y h_cg = 0.30, el margen estático es:", "options": {"A": "0.12 (estable)", "B": "−0.12 (inestable)", "C": "0.72", "D": "no se puede saber"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "SM = h_foco − h_cg = 0.12 > 0 ⟹ estable."},
    },
    "l3_as03_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Flight Sim",
            "body": "El Flight Sim reproduce los modos de cabeceo (phugoid y short-period) y responde a las superficies de control del vehículo.\n\nPráctica: en el simulador, aplica una perturbación de cabeceo y observa si la oscilación se atenúa (estable) o crece (inestable)."},
        "question": {"q": "El Flight Sim de ZICORE modela los modos:", "options": {"A": "phugoid y short-period", "B": "solo térmicos", "C": "químicos", "D": "financieros"}, "answer": "A", "difficulty": "basic",
            "explanation": "Son los modos longitudinales básicos del avión."},
    },
    "l3_as03_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Rendezvous & Docking",
            "body": "El simulador de Rendezvous usa control en lazo cerrado con actuadores de RCS para guiar la maniobra de acoplamiento, igual que el control de actitud de una nave.\n\nPráctica: en /rendezvous, ejecuta el modo automático y observa cómo el perfil de tasas corrige la alineación en cada fase."},
        "question": {"q": "El autopiloto de Rendezvous de ZICORE guía la nave mediante:", "options": {"A": "control en lazo cerrado con RCS", "B": "empuje continuo máximo", "C": "sin sensores", "D": "velocidad constante"}, "answer": "A", "difficulty": "basic",
            "explanation": "Realimenta rango y tasas para corregir la aproximación."},
    },
    "l3_as04_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Digital Twin y subsistemas",
            "body": "El Digital Twin mantiene sincronizados los subsistemas de la nave (estructura, AOCS, potencia, térmico, coms) con su modelo virtual para monitoreo y FDIR.\n\nPráctica: abre el Digital Twin y lista qué subsistema protegería primero ante una caída de potencia y por qué."},
        "question": {"q": "El Digital Twin de ZICORE sirve para:", "options": {"A": "sincronizar el modelo virtual con el estado real del sistema", "B": "imprimir en 3D", "C": "cifrar enlaces", "D": "medir radiación"}, "answer": "A", "difficulty": "basic",
            "explanation": "Réplica sincronizada para monitoreo, predicción y FDIR."},
    },
    "l3_as04_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Rocket Designer",
            "body": "El Rocket Designer y el generador de Engine Nozzle aplican la ecuación del cohete para dimensionar el vehículo y exportar la tobera como malla 3D.\n\nPráctica: con Isp = 350 s, m₀ = 500 t y m_f = 50 t, calcula el Δv disponible."},
        "question": {"q": "El Rocket Designer exporta componentes como:", "options": {"A": "mallas 3D (STL/GLB)", "B": "solo texto", "C": "audio", "D": "hojas de cálculo"}, "answer": "A", "difficulty": "basic",
            "explanation": "Se integra con el Materializer para generar geometría."},
    },
    "l3_as04_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Power Management y Ground Station",
            "body": "Power Management dimensiona paneles y baterías para el ciclo luz/eclipse, y Ground Station gestiona la antena y el enlace de datos.\n\nPráctica: estima la energía de un eclipse de 35 min para una carga de 500 W y decide la capacidad mínima de batería (con 80% de profundidad de descarga)."},
        "question": {"q": "Durante el eclipse, la energía de la nave proviene de:", "options": {"A": "las baterías", "B": "los paneles solares", "C": "el RTG únicamente", "D": "la antena"}, "answer": "A", "difficulty": "basic",
            "explanation": "Sin sol, las baterías cubren la carga."},
    },

    # ---------------- PROPULSION & ROCKET TECHNOLOGY (PRE) ----------------
    "l3_pr01_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Propulsion Lab",
            "body": "El Propulsion Lab aplica la primera y segunda ley a cada tipo de motor, reportando temperatura de cámara, expansión y eficiencia.\n\nPráctica: con T_c = 3500 K y T_f = 1000 K, calcula la eficiencia máxima de Carnot y comenta cuánto se acerca un motor real."},
        "question": {"q": "El rendimiento máximo teórico entre dos focos es:", "options": {"A": "η = 1 − T_f/T_c", "B": "η = T_c/T_f", "C": "η = T_f·T_c", "D": "η = 100% siempre"}, "answer": "A", "difficulty": "basic",
            "explanation": "Es el límite de Carnot."},
    },
    "l3_pr01_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Ciclos de potencia",
            "body": "El Propulsion Lab modela ciclos (Brayton, Rankine) para turbinas y sistemas de alimentación de motores cohete.\n\nPráctica: identifica en qué etapa del ciclo de un motor de ciclo cerrado entra la turbina de accionamiento."},
        "question": {"q": "En un motor cohete de ciclo cerrado, la turbina se acciona con:", "options": {"A": "gas caliente del prequemador", "B": "electricidad", "C": "imanes permanentes", "D": "luz solar"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Un prequemador genera gas que mueve la turbobomba."},
    },
    "l3_pr01_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Engine Test Stand",
            "body": "El banco de pruebas estima empuje y eficiencia (Isp, c*) y valida el diseño del motor antes de fabricarlo.\n\nPráctica: con F = 800 kN y ṁ = 250 kg/s, calcula el impulso específico efectivo (Isp = F/(ṁ·g₀))."},
        "question": {"q": "El impulso específico se mide en:", "options": {"A": "segundos", "B": "newton", "C": "kg/m³", "D": "julios"}, "answer": "A", "difficulty": "basic",
            "explanation": "Isp = F/(ṁ·g₀); las unidades de g₀ lo dejan en segundos."},
    },
    "l3_pr02_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Misión y presupuesto de Δv",
            "body": "El Mission Planner usa la ecuación del cohete para traducir el Δv de la misión en masa de propulsor necesaria.\n\nPráctica: para Δv = 9500 m/s e Isp = 340 s, calcula la fracción de masa de propulsor requerida."},
        "question": {"q": "La ecuación del cohete relaciona Δv con:", "options": {"A": "Isp, g₀ y la relación de masas", "B": "solo la altura", "C": "la temperatura ambiente", "D": "la latitud"}, "answer": "A", "difficulty": "basic",
            "explanation": "Δv = Isp·g₀·ln(m₀/m_f)."},
    },
    "l3_pr02_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Generador de toberas",
            "body": "El Materializer genera la geometría de la tobera (Engine Nozzle) a partir de la relación de expansión ε y la garganta, lista para imprimir.\n\nPráctica: explica cómo ε = A_e/A_t controla el empuje y qué ocurre si la presión de salida no se adapta a la ambiente."},
        "question": {"q": "Una tobera sobreexpandida puede causar:", "options": {"A": "separación del flujo", "B": "mayor Isp siempre", "C": "cero empuje", "D": "vacío"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Si p_e < p_amb el flujo puede desprenderse de la pared."},
    },
    "l3_pr02_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Cámara de combustión",
            "body": "El Engine Test Stand modela la cámara (presión, L*, velocidad característica c*) y detecta inestabilidades de combustión.\n\nPráctica: comenta por qué se enfría regenerativamente la pared de la cámara en motores de alta presión."},
        "question": {"q": "El enfriamiento regenerativo usa:", "options": {"A": "el propio propelente antes de inyectarse", "B": "solo radiadores", "C": "aire exterior", "D": "termopares"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "El combustible/oxidante enfría la pared y luego se quema."},
    },
    "l3_pr03_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Mezcla de propelentes",
            "body": "El Propulsion Lab calcula la relación oxidante/combustible (O/F) óptima y su impacto en c* e Isp; ISRU produce esos propelentes in situ.\n\nPráctica: para metano/LOX, comenta por qué el Isp máximo en vacío aparece cerca de O/F ≈ 3.4."},
        "question": {"q": "La relación O/F afecta principalmente a:", "options": {"A": "el impulso específico y la temperatura de cámara", "B": "la forma de la tobera", "C": "el color de la llama", "D": "la masa del tanque"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Determina energía disponible y temperatura."},
    },
    "l3_pr03_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Catálogo de motores",
            "body": "El Space Database de ZICORE almacena motores reales (RS-25, Raptor, Merlin) con sus propelentes, Isp y empuje para compararlos.\n\nPráctica: compara el Isp de un motor de hidrógeno (RS-25) con uno metálico (Merlin) y explica la diferencia."},
        "question": {"q": "El propelente con mayor Isp químico típico es:", "options": {"A": "LOX/LH2", "B": "sólido", "C": "hipergólico", "D": "aire/queroseno"}, "answer": "A", "difficulty": "basic",
            "explanation": "El hidrógeno ofrece la mayor velocidad de escape."},
    },
    "l3_pr03_m3": {
        "lesson": {"title": "Aplicación en ZICORE · FDIR e inestabilidades",
            "body": "El sistema FDIR detecta inestabilidades de combustión o fallos de encendido y ejecuta respuestas de aislamiento y recuperación.\n\nPráctica: describe una respuesta FDIR ante un aumento anómalo de la vibración de la cámara."},
        "question": {"q": "Ante una inestabilidad de combustión, ZICORE (FDIR) debería:", "options": {"A": "aislar/throttle y registrar el evento", "B": "ignorarla", "C": "apagar todos los sensores", "D": "aumentar el empuje"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Detectar, aislar y recuperar con registro para análisis."},
    },
    "l3_pr04_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Turbobombas",
            "body": "El Rocket Designer dimensiona turbobombas para entregar alto caudal a alta presión en motores de ciclo cerrado.\n\nPráctica: con potencia de bombeo P = ṁ·Δp/ρ, estima la potencia para ṁ = 300 kg/s y Δp = 20 MPa (LOX)."},
        "question": {"q": "Las bombas de alta presión en un motor cohete existen para:", "options": {"A": "vencer la presión de cámara sin tanques ultrapesados", "B": "enfriar la tobera", "C": "guiar el vehículo", "D": "medir el empuje"}, "answer": "A", "difficulty": "basic",
            "explanation": "Permiten tanques ligeros presurizados solo lo mínimo."},
    },
    "l3_pr04_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Turbinas",
            "body": "La turbina extrae energía del gas del prequemador para accionar la bomba; su eficiencia y temperatura límite condicionan el ciclo.\n\nPráctica: explica por qué el margen de temperatura en los álabes de turbina es crítico en el ciclo cerrado."},
        "question": {"q": "La turbina de un motor cohete sirve para:", "options": {"A": "accionar la turbobomba con el gas de prequemador", "B": "generar sustentación", "C": "enfriar el motor", "D": "medir altitud"}, "answer": "A", "difficulty": "basic",
            "explanation": "Convierte energía del gas en trabajo de bombeo."},
    },
    "l3_pr04_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Ciclos de alimentación",
            "body": "ZICORE compara ciclos (generador de gas, expander, staged combustion, full-flow) según Isp, presión y reutilización.\n\nPráctica: explica una ventaja del ciclo full-flow staged combustion (como Raptor) frente al generador de gas."},
        "question": {"q": "El ciclo full-flow staged combustion se caracteriza por:", "options": {"A": "todos los propelentes pasan por prequemadores/turbinas", "B": "no usa bomba", "C": "solo usa sólidos", "D": "cero recalentamiento"}, "answer": "A", "difficulty": "advanced",
            "explanation": "Mejora eficiencia y permite alta presión de cámara."},
    },

    # ---------------- NUCLEAR ENGINEERING & ADVANCED ENERGY (NEE) ----------------
    "l3_nu01_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Reactores y Power Management",
            "body": "Power Management de ZICORE integra fuentes nucleares (fisión) para misiones de alta potencia; el núcleo se modela con su enriquecimiento y criticidad.\n\nPráctica: explica por qué un reactor de fisión supera a los paneles solares más allá de Marte."},
        "question": {"q": "Para misiones de gran potencia más allá de Marte, ZICORE considera:", "options": {"A": "reactores de fisión", "B": "solo baterías de litio", "C": "velas solares", "D": "imanes"}, "answer": "A", "difficulty": "basic",
            "explanation": "La fisión da alta potencia independiente del Sol."},
    },
    "l3_nu01_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Space Weather Center",
            "body": "El Space Weather Center monitorea radiación (partículas, GCR, SPE) que degrada electrónica y afecta a la tripulación.\n\nPráctica: si una SPE eleva la dosis, decide cómo cambia la planificación de EVA y el refugio de la tripulación."},
        "question": {"q": "El Space Weather Center alerta principalmente sobre:", "options": {"A": "eventos de partículas solares y radiación", "B": "mareas", "C": "viento en superficie", "D": "presión de neumáticos"}, "answer": "A", "difficulty": "basic",
            "explanation": "GCR/SPE y tormentas geomagnéticas."},
    },
    "l3_nu01_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Propulsión nuclear térmica",
            "body": "La propulsión nuclear térmica (NTP) calienta hidrógeno en un reactor para lograr Isp ≈ 800–900 s, muy superior al químico.\n\nPráctica: compara el Δv disponible con Isp = 850 s frente a Isp = 340 s para la misma fracción de masa."},
        "question": {"q": "La energía de ligadura por nucleón es máxima en:", "options": {"A": "el hierro-56", "B": "el hidrógeno", "C": "el uranio", "D": "el helio-3"}, "answer": "A", "difficulty": "basic",
            "explanation": "Fe-56 tiene la mayor energía de ligadura por nucleón."},
    },
    "l3_nu02_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Criticidad y control",
            "body": "El modelo de reactor de ZICORE usa el factor de multiplicación k: k = 1 crítico, k > 1 supercrítico, k < 1 subcrítico.\n\nPráctica: explica qué acción (insertar/retirar barras) lleva el reactor de supercrítico a crítico."},
        "question": {"q": "Un reactor con k = 1 se encuentra en estado:", "options": {"A": "crítico (potencia estable)", "B": "subcrítico", "C": "apagado", "D": "fundido"}, "answer": "A", "difficulty": "basic",
            "explanation": "k = 1 mantiene la reacción en cadena estable."},
    },
    "l3_nu02_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Moderación y FDIR",
            "body": "El moderador frena neutrones para aumentar la probabilidad de fisión; las barras de control absorben neutrones. FDIR ejecuta el scram ante anomalías.\n\nPráctica: describe la secuencia de un scram automático disparado por alta temperatura del refrigerante."},
        "question": {"q": "El moderador cumple la función de:", "options": {"A": "lentificar neutrones para sostener la reacción", "B": "absorberlos", "C": "generar electricidad", "D": "enfriar la turbina"}, "answer": "A", "difficulty": "basic",
            "explanation": "Neutrones térmicos tienen mayor sección eficaz de fisión."},
    },
    "l3_nu02_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Ciclo del combustible e ISRU",
            "body": "El ciclo del combustible cubre minería, enriquecimiento, uso y gestión de residuos; ISRU adapta ideas similares para producir recursos lunares/marcianos.\n\nPráctica: compara la extracción de uranio con la producción de oxígeno ISRU desde regolito y comparte criterios de seguridad."},
        "question": {"q": "En el ciclo del combustible, el enriquecimiento busca aumentar:", "options": {"A": "la proporción del isótopo fisible (U-235)", "B": "la masa total", "C": "la temperatura", "D": "el volumen"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Más U-235 facilita la criticidad."},
    },
    "l3_nu03_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Crew Health Monitor",
            "body": "El Crew Health Monitor acumula dosis de radiación (Sv) y alerta al superar umbrales de misión, integrando datos del Space Weather Center.\n\nPráctica: con una tasa de 0.5 mSv/día y un límite de 500 mSv de carrera, estima cuántos días puedes operar antes de alcanzar el límite."},
        "question": {"q": "La dosimetría en ZICORE se usa para:", "options": {"A": "acumular y vigilar la dosis de radiación de la tripulación", "B": "medir el empuje", "C": "calcular la órbita", "D": "cifrar datos"}, "answer": "A", "difficulty": "basic",
            "explanation": "La dosis es el principal riesgo de salud en el espacio."},
    },
    "l3_nu03_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Blindaje",
            "body": "El blindaje reduce la dosis: capas de polietileno (rico en H) o regolito atenúan GCR y SPE.\n\nPráctica: explica por qué la radiación secundaria (neutrones, gammas) puede volver inefectivo un blindaje mal diseñado."},
        "question": {"q": "Para radiación de protones GCR se prefieren materiales ricos en:", "options": {"A": "hidrógeno (polietileno, agua)", "B": "plomo puro", "C": "hierro", "D": "vacío"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "El hidrógeno fragmenta eficazmente los núcleos incidentes."},
    },
    "l3_nu03_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Seguridad y FDIR",
            "body": "Los criterios ALARA (tan bajo como razonablemente posible) y el diseño a prueba de fallos guían la seguridad nuclear; FDIR implementa detección e interlock.\n\nPráctica: propón tres interlocks de seguridad para una fuente radiactiva a bordo."},
        "question": {"q": "El principio ALARA significa:", "options": {"A": "dosis tan baja como razonablemente posible", "B": "máxima dosis permitida", "C": "cero radiación siempre", "D": "radiación solo de noche"}, "answer": "A", "difficulty": "basic",
            "explanation": "Principio de optimización de protección radiológica."},
    },
    "l3_nu04_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Control térmico",
            "body": "El módulo térmico resuelve conducción (q = −kA·dT/dx) para dimensionar el circuito que evacúa el calor del núcleo o de la electrónica.\n\nPráctica: con k = 200 W/m·K, A = 0.01 m², ΔT = 50 K y L = 0.05 m, calcula el flujo de calor por conducción."},
        "question": {"q": "La ley que rige la conducción de calor es:", "options": {"A": "la ley de Fourier", "B": "la ley de Faraday", "C": "la ley de Hooke", "D": "la ley de Ohm"}, "answer": "A", "difficulty": "basic",
            "explanation": "q = −kA·dT/dx (Fourier)."},
    },
    "l3_nu04_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Radiadores",
            "body": "En el vacío solo hay radiación: el calor se evacúa con radiadores según Stefan-Boltzmann (q = εσAT⁴).\n\nPráctica: con ε = 0.9, T = 300 K y A = 5 m², calcula la potencia radiada (σ = 5.67e-8)."},
        "question": {"q": "En el vacío, el calor se disipa principalmente por:", "options": {"A": "radiación", "B": "convección", "C": "conducción al aire", "D": "evaporación"}, "answer": "A", "difficulty": "basic",
            "explanation": "Sin medio material, solo radiación térmica."},
    },
    "l3_nu04_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Nuclear Electric Propulsion",
            "body": "La propulsión nuclear eléctrica convierte el calor del reactor en electricidad para motores iónicos (alto Isp, empuje bajo y continuo).\n\nPráctica: diseña un presupuesto de potencia: reactor 100 kW → 30 kW a propulsión, 70 kW a carga útil y radiadores."},
        "question": {"q": "La propulsión nuclear eléctrica usa el reactor para:", "options": {"A": "generar electricidad para motores iónicos", "B": "calentar directamente el hidrógeno como única opción", "C": "generar sustentación", "D": "iluminar"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Combina energía nuclear con propulsión eléctrica de alto Isp."},
    },

    # ---------------- ADVANCED SPACE SYSTEMS (SSE) ----------------
    "l3_ss01_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Mission Planner",
            "body": "El Mission Planner traduce requisitos (órbita objetivo, masa, presupuesto de Δv) en una secuencia de eventos y recursos.\n\nPráctica: escribe tres requisitos medibles para una misión de observación de la Tierra y asígnalos a subsistemas."},
        "question": {"q": "Un requisito bien formulado debe ser:", "options": {"A": "medible y verificable", "B": "vago y abierto", "C": "secreto", "D": "opcional"}, "answer": "A", "difficulty": "basic",
            "explanation": "Verificabilidad es central en ingeniería de sistemas."},
    },
    "l3_ss01_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Integración y Digital Twin",
            "body": "La arquitectura espacial integra módulos con interfaces definidas; el Digital Twin verifica que las interfaces y presupuestos cierren.\n\nPráctica: identifica una interfaz crítica (potencia, datos o térmica) entre dos módulos de la estación y define su contrato."},
        "question": {"q": "La integración de sistemas se basa en:", "options": {"A": "interfaces y presupuestos bien definidos", "B": "improvisación", "C": "solo software", "D": "el azar"}, "answer": "A", "difficulty": "basic",
            "explanation": "Interfaces claras permiten verificar y ensamblar."},
    },
    "l3_ss01_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Payload Bay Manager",
            "body": "El Payload Bay Manager cierra presupuestos de masa y volumen, distribuyendo margen entre subsistemas.\n\nPráctica: con masa asignada 1000 kg y 30% de margen, calcula la masa con margen y el margen remanente si dos componentes sobrepasan 40 kg."},
        "question": {"q": "El presupuesto de masa de una misión:", "options": {"A": "asigna y controla el margen de cada subsistema", "B": "solo suma", "C": "se ignora", "D": "depende del clima"}, "answer": "A", "difficulty": "basic",
            "explanation": "El margen protege contra sobrepesos imprevistos."},
    },
    "l3_ss02_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Power Management solar",
            "body": "Propagación orbital determina el ciclo luz/eclipse que fija la generación y el tamaño del arreglo solar.\n\nPráctica: para una carga de 600 W con 65% de tiempo iluminado, estima la potencia que deben generar los paneles durante el sol."},
        "question": {"q": "El tamaño del arreglo solar depende principalmente de:", "options": {"A": "la carga y el ciclo luz/eclipse", "B": "el color de la nave", "C": "la antena", "D": "el software"}, "answer": "A", "difficulty": "basic",
            "explanation": "Generación debe cubrir carga y recarga de baterías."},
    },
    "l3_ss02_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Baterías",
            "body": "Las baterías cubren el eclipse; su capacidad se dimensiona con energía, profundidad de descarga (DoD) y eficiencia.\n\nPráctica: para 500 W durante 35 min de eclipse y DoD = 80%, calcula la capacidad mínima en Wh."},
        "question": {"q": "La profundidad de descarga (DoD) afecta:", "options": {"A": "la vida y capacidad útil de la batería", "B": "la órbita", "C": "la antena", "D": "el empuje"}, "answer": "A", "difficulty": "basic",
            "explanation": "DoD bajo alarga la vida de ciclado."},
    },
    "l3_ss02_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Regulación y RTG",
            "body": "Los reguladores convierten y limitan la potencia; en misiones lejanas el RTG (efecto Seebeck) genera electricidad del calor radiactivo.\n\nPráctica: explica por qué el RTG es preferible a paneles en la órbita de Júpiter."},
        "question": {"q": "Un sistema de regulación de potencia se encarga de:", "options": {"A": "estabilizar el bus eléctrico y proteger cargas", "B": "cambiar la órbita", "C": "generar empuje", "D": "enfriar"}, "answer": "A", "difficulty": "basic",
            "explanation": "Mantiene voltaje/nivel seguros para la carga."},
    },
    "l3_ss03_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Ground Station",
            "body": "Ground Station controla la antena y el enlace; la ecuación de Friis y la relación Eb/N0 fijan la tasa de datos alcanzable.\n\nPráctica: si aumentas la potencia transmitida x2, en cuánto mejora (en dB) el enlace; ¿cuánto mejora la tasa?"},
        "question": {"q": "Duplicar la potencia transmitida mejora la señal en aproximadamente:", "options": {"A": "3 dB", "B": "10 dB", "C": "100 dB", "D": "0 dB"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Cada factor 2 de potencia = +3 dB."},
    },
    "l3_ss03_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Antenas espaciales",
            "body": "La antena de alta ganancia enfoca el haz; el apuntado fino y el seguimiento mantienen el enlace durante los pases de LEO.\n\nPráctica: explica cómo cambia el requisito de apuntado al pasar de una antena de baja a una de alta ganancia con haz estrecho."},
        "question": {"q": "Un haz más estrecho (alta ganancia) exige:", "options": {"A": "mayor precisión de apuntado y seguimiento", "B": "menos precisión", "C": "ningún apuntado", "D": "más masa siempre nula"}, "answer": "A", "difficulty": "basic",
            "explanation": "El lóbulo es más directivo y sensible a errores de puntería."},
    },
    "l3_ss03_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Celestial Navigation",
            "body": "El módulo de Celestial Navigation usa rastreadores de estrellas y el Real Star Map para determinar actitud y posición; GNSS ayuda en LEO.\n\nPráctica: explica por qué un star tracker no funciona bien durante el eclipse (sin referencia estelar)."},
        "question": {"q": "En el espacio, la navegación de actitud puede usar:", "options": {"A": "rastreadores de estrellas (star trackers)", "B": "brújula magnética únicamente", "C": "GPS siempre", "D": "barómetro"}, "answer": "A", "difficulty": "basic",
            "explanation": "Las estrellas dan una referencia inercial estable."},
    },
    "l3_ss04_m1": {
        "lesson": {"title": "Aplicación en ZICORE · Robot Designer y Rover Control",
            "body": "El Robot Designer define cinemática y grados de libertad de brazos y rovers; Rover Control planifica rutas con percepción.\n\nPráctica: para un brazo de 3 GDL, explica cómo obtendrías la posición del efector final con cinemática directa."},
        "question": {"q": "La cinemática directa de un robot obtiene:", "options": {"A": "la posición del efector a partir de los ángulos", "B": "los ángulos a partir de la fuerza", "C": "el empuje", "D": "la temperatura"}, "answer": "A", "difficulty": "basic",
            "explanation": "De articulaciones → pose del extremo."},
    },
    "l3_ss04_m2": {
        "lesson": {"title": "Aplicación en ZICORE · Autonomía y estimación",
            "body": "El filtro de Kalman fusiona sensores (IMU, cámara) para estimar estado, y el controlador guía la maniobra sin esperar el mando de Tierra.\n\nPráctica: explica por qué un rover marciano necesita autonomía dado el retardo de comunicación (hasta ~24 min de ida y vuelta)."},
        "question": {"q": "La fusión de sensores con filtro de Kalman mejora:", "options": {"A": "la estimación del estado con mediciones ruidosas", "B": "la potencia del motor", "C": "la masa", "D": "el cifrado"}, "answer": "A", "difficulty": "intermediate",
            "explanation": "Combina modelo dinámico y mediciones para estimar mejor."},
    },
    "l3_ss04_m3": {
        "lesson": {"title": "Aplicación en ZICORE · Simulador de Rendezvous",
            "body": "El simulador Rendezvous de ZICORE reproduce la fase final de aproximación (RPO) y el docking sobre la ISS, con control manual y automático.\n\nPráctica: en /rendezvous, acopla con éxito en V-bar y luego intenta un contacto con velocidad alta para observar el fallo de docking."},
        "question": {"q": "El fracaso del docking en el simulador puede deberse a:", "options": {"A": "velocidad relativa o desalineación excesivas", "B": "exceso de combustible", "C": "falta de luz solar", "D": "poco volumen de datos"}, "answer": "A", "difficulty": "basic",
            "explanation": "Rates altas o mala alineación provocan un contacto duro/fallido."},
    },
}
