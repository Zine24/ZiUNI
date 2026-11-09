# -*- coding: utf-8 -*-
"""Level 3 · Career Cores (per-career) - ZiCore University.
Each of the 5 careers has its own core sequence. Entry requires Engineering Core complete.
"""

import json as _json  # noqa

# career_id -> career metadata + its core course sequence
LEVEL3 = {
    "computational": {
        "name": "Ciencias Computacionales y Simulación", "name_en": "Computational Sciences & Simulation Engineering",
        "color": "#22d3ee", "code": "CSE", "career_id": "computational",
        "courses": {
            "cs01": {
                "code": "CS01", "name": "Algoritmos y Estructuras de Datos", "name_en": "Algorithms & Data Structures",
                "desc": "Estructuras fundamentales, análisis de complejidad y técnicas de diseño de algoritmos para cómputo científico.",
                "credits": 5, "prereq": None, "required": 70, "color": "#22d3ee",
                "modules": [
                    {"id": "l3_cs01_m1", "name": "Estructuras de datos lineales",
                     "lessons": [
                         {"title": "Listas, pilas y colas",
                          "body": "Las listas enlazadas almacenan datos en nodos con apuntadores. Las pilas operan LIFO (último en entrar, primero en salir) y las colas FIFO (primero en entrar, primero en salir).\n\nEn cómputo científico, las pilas modelan llamadas recursivas y las colas gestionan planificación y buffers de procesamiento de datos."}],
                     "questions": [
                         {"q": "Una pila opera bajo el principio:", "options": {"A": "FIFO", "B": "LIFO", "C": "aleatorio", "D": "ordenado"}, "answer": "B", "difficulty": "basic",
                          "explanation": "LIFO: el último que entra es el primero que sale."},
                         {"q": "La operación de agregar a una pila se llama:", "options": {"A": "push", "B": "pop", "C": "enqueue", "D": "peek devuelve el tope"}, "answer": "A", "difficulty": "basic",
                          "explanation": "push agrega al tope; pop retira del tope."},
                         {"q": "Una cola procesa elementos en orden:", "options": {"A": "LIFO", "B": "FIFO", "C": "por prioridad inversa", "D": "aleatorio"}, "answer": "B", "difficulty": "basic",
                          "explanation": "FIFO: el primero que entra es el primero que sale."},
                     ]},
                    {"id": "l3_cs01_m2", "name": "Árboles y grafos",
                     "lessons": [
                         {"title": "Árboles binarios y recorridos",
                          "body": "Un árbol binario de búsqueda mantiene la propiedad: los menores van a la izquierda y los mayores a la derecha, permitiendo búsqueda en O(log n) si está balanceado.\n\nLos recorridos preorden, inorden y postorden son la base de evaluar expresiones y ordenar. Un árbol balanceado (AVL o rojo-negro) garantiza altura logarítmica."}],
                     "questions": [
                         {"q": "En un BST, los elementos menores al nodo van:", "options": {"A": "a la izquierda", "B": "a la derecha", "C": "en la raíz", "D": "en hojas"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Menores a la izquierda, mayores a la derecha."},
                         {"q": "El recorrido inorden de un BST produce:", "options": {"A": "orden aleatorio", "B": "los elementos en orden ascendente", "C": "solo hojas", "D": "el nivel máximo"}, "answer": "B", "difficulty": "intermediate",
                          "explanation": "izquierda–nodo–derecha da la secuencia ordenada."},
                         {"q": "Un árbol balanceado busca mantener la altura en:", "options": {"A": "O(n)", "B": "O(log n)", "C": "O(n²)", "D": "O(1)"}, "answer": "B", "difficulty": "intermediate",
                          "explanation": "Balanceado ⟹ altura logarítmica ⟹ búsqueda rápida."},
                     ]},
                    {"id": "l3_cs01_m3", "name": "Técnicas de diseño",
                     "lessons": [
                         {"title": "Divide y vencerás y programación dinámica",
                          "body": "Divide y vencerás parte el problema en subproblemas independientes y combina (merge sort, quicksort, multiplicación de matrices).\n\nLa programación dinámica guarda soluciones de subproblemas repetidos en una tabla para evitar recomputar — el método de memoria y 'optimal substructure'. Esencial en optimización y procesamiento de secuencias."}],
                     "questions": [
                         {"q": "La programación dinámica se apoya en:", "options": {"A": "fuerza bruta", "B": "memorización de subproblemas", "C": "aleatorización", "D": "recursión infinita"}, "answer": "B", "difficulty": "basic",
                          "explanation": "Almacena resultados de subproblemas superpuestos."},
                         {"q": "El problema de la serie de Fibonacci con programación dinámica tiene complejidad:", "options": {"A": "O(2ⁿ)", "B": "O(n)", "C": "O(n²)", "D": "O(log n)"}, "answer": "B", "difficulty": "intermediate",
                          "explanation": "Cada término se calcula una vez: O(n)."},
                         {"q": "Un ejemplo clásico de divide y vencerás es:", "options": {"A": "búsqueda lineal", "B": "merge sort", "C": "inserción directa", "D": "recorrido de lista"}, "answer": "B", "difficulty": "basic",
                          "explanation": "Merge sort parte, ordena y combina."},
                     ]},
                ],
            },
            "cs02": {
                "code": "CS02", "name": "Análisis Numérico", "name_en": "Numerical Analysis",
                "desc": "Métodos numéricos para raíces, sistemas lineales, interpolación e integración con análisis de error.",
                "credits": 5, "prereq": "cs01", "required": 70, "color": "#2dd4bf",
                "modules": [
                    {"id": "l3_cs02_m1", "name": "Raíces de ecuaciones",
                     "lessons": [
                         {"title": "Bisección y Newton-Raphson",
                          "body": "La bisección parte el intervalo donde la función cambia de signo; converge siempre pero lento. Newton-Raphson usa la tangente: x_(n+1) = x_n − f(x_n)/f'(x_n), convergencia cuadrática si hay buena aproximación inicial.\n\nEl análisis de error distingue error absoluto, relativo y de redondeo; la tolerancia define cuándo detenerse."}],
                     "questions": [
                         {"q": "El método de bisección requiere:", "options": {"A": "que f cambie de signo en el intervalo", "B": "la derivada de f", "C": "una matriz", "D": "datos ordenados"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Necesita f(a)·f(b) < 0 para asegurar una raíz en [a, b]."},
                         {"q": "Newton-Raphson requiere evaluar:", "options": {"A": "solo f", "B": "f y f'", "C": "solo f'", "D": "la integral de f"}, "answer": "B", "difficulty": "basic",
                          "explanation": "Usa la tangente, requiere derivada."},
                         {"q": "La convergencia de Newton-Raphson cerca de la raíz es típicamente:", "options": {"A": "lineal", "B": "cuadrática", "C": "divergente", "D": "nula"}, "answer": "B", "difficulty": "intermediate",
                          "explanation": "Dobla cifras correctas por iteración con buena semilla."},
                     ]},
                    {"id": "l3_cs02_m2", "name": "Sistemas lineales numéricos",
                     "lessons": [
                         {"title": "Eliminación de Gauss y factorización LU",
                          "body": "La eliminación de Gauss con pivoteo resuelve Ax = b convirtiendo A en triangular. La factorización LU separa A = LU para resolver múltiples b eficientemente.\n\nEl condicionamiento de la matriz (número de condición) mide sensibilidad a errores de redondeo: matrices mal condicionadas amplifican el error."}],
                     "questions": [
                         {"q": "La factorización LU descompone A como:", "options": {"A": "L×U", "B": "U×L solo", "C": "A⁻¹", "D": "L+U"}, "answer": "A", "difficulty": "basic",
                          "explanation": "A = L·U con L triangular inferior y U superior."},
                         {"q": "El número de condición alto indica:", "options": {"A": "matriz eficiente", "B": "sensibilidad a errores", "C": "solución exacta", "D": "matriz identidad"}, "answer": "B", "difficulty": "basic",
                          "explanation": "Amplifica errores de redondeo en la solución."},
                         {"q": "El pivoteo en Gauss se usa para:", "options": {"A": "acelerar la suma", "B": "evitar división por ceros y mejorar estabilidad", "C": "ordenar los datos", "D": "calcular determinantes siempre"}, "answer": "B", "difficulty": "intermediate",
                          "explanation": "Reordena filas buscando pivotes grandes y estables."},
                     ]},
                    {"id": "l3_cs02_m3", "name": "Interpolación e integración numérica",
                     "lessons": [
                         {"title": "Interpolación e integración compuesta",
                          "body": "El polinomio interpolador de Lagrange pasa por n+1 puntos dados; para muchos puntos conviene splines cúbicos que evitan las oscilaciones.\n\nLa integración numérica usa cuadraturas: la regla del trapecio y las de Simpson (1/3 y 3/8), compuestas dividiendo el intervalo en subintervalos para mejorar precisión con error del orden de h⁴."}],
                     "questions": [
                         {"q": "La interpolación de Lagrange construye:", "options": {"A": "una recta promedio", "B": "un polinomio que pasa por los puntos dados", "C": "una matriz", "D": "la derivada"}, "answer": "B", "difficulty": "basic",
                          "explanation": "Garantiza p(xᵢ) = yᵢ en los datos dados."},
                         {"q": "La regla de Simpson 1/3 aproxima la integral con:", "options": {"A": "parábolas", "B": "rectas", "C": "exponenciales", "D": "logaritmos"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Interpola tres puntos con una parábola."},
                         {"q": "Dividir el intervalo en más subintervalos en una regla compuesta:", "options": {"A": "empeora el error", "B": "reduce el error", "C": "no cambia nada", "D": "duplica el dominio"}, "answer": "B", "difficulty": "basic",
                          "explanation": "El error de Simpson decrece como h⁴."},
                     ]},
                ],
            },
            "cs03": {
                "code": "CS03", "name": "Cómputo Científico y Simulación", "name_en": "Scientific Computing & Simulation",
                "desc": "NumPy, ODEs, simulación Monte Carlo y la cadena para resolver problemas físicos por computadora.",
                "credits": 5, "prereq": "cs02", "required": 70, "color": "#38bdf8",
                "modules": [
                    {"id": "l3_cs03_m1", "name": "Computación vectorizada",
                     "lessons": [
                         {"title": "NumPy y operaciones vectorizadas",
                          "body": "NumPy ofrece arreglos n-dimensionales con operaciones vectorizadas que ejecutan en C, decenas de veces más rápido que ciclos Python.\n\nLa 'data parallelism' y el broadcasting permiten operar sobre arreglos completos sin loops explícitos; el uso de operaciones sobre matrices es el artículo central del cómputo científico."}],
                     "questions": [
                         {"q": "Las operaciones de NumPy sobre arreglos son:", "options": {"A": "lentas", "B": "vectorizadas", "C": "imposibles", "D": "solo enteras"}, "answer": "B", "difficulty": "basic",
                          "explanation": "Operan sobre todo el arreglo a la vez, en código nativo."},
                         {"q": "np.dot(A, B) calcula:", "options": {"A": "el producto punto de A y B", "B": "suma de A y B", "C": "transpuesta", "D": "inversa"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Es el producto matricial / producto punto de NumPy."},
                         {"q": "El broadcasting permite:", "options": {"A": "operar arreglos de dimensiones compatibles", "B": "borrar arreglos", "C": "solo leer datos", "D": "imprimir resultados"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Expande dimensiones para operar arreglos de formas compatibles."},
                     ]},
                    {"id": "l3_cs03_m2", "name": "Ecuaciones diferenciales",
                     "lessons": [
                         {"title": "Método de Euler y Runge-Kutta",
                          "body": "Simular dinámicas requiere resolver ODEs: el método de Euler avanza con x'(t) = f(t, x) usando pendiente constante por paso.\n\nLos métodos de Runge-Kutta (RK4) mejoran la precisión muestreando la pendiente en varios puntos del intervalo; el error por paso es O(h⁴). La estabilidad numérica y la elección del paso son críticas."}],
                     "questions": [
                         {"q": "El método de Euler aproxima la solución de una ODE avanzando con:", "options": {"A": "la pendiente del punto actual", "B": "la integral exacta", "C": "valores aleatorios", "D": "la segunda derivada"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Usa x' en el punto para extrapolar linealmente."},
                         {"q": "RK4 tiene error local por paso del orden de:", "options": {"A": "O(h)", "B": "O(h⁴)", "C": "O(4h)", "D": "O(1)"}, "answer": "B", "difficulty": "intermediate",
                          "explanation": "Runge-Kutta de 4 etapas: error O(h⁴)."},
                         {"q": "Un paso de integración demasiado grande en Euler puede:", "options": {"A": "mejorar exactitud", "B": "producir inestabilidad numérica", "C": "no tener efecto", "D": "acelerar convergencia"}, "answer": "B", "difficulty": "intermediate",
                          "explanation": "La solución numérica puede oscilar o explotar."},
                     ]},
                    {"id": "l3_cs03_m3", "name": "Simulación Monte Carlo",
                     "lessons": [
                         {"title": "Muestreo aleatorio y estimación",
                          "body": "Monte Carlo usa muestras aleatorias para estimar cantidades deterministas: el valor de π con puntos en un cuadrado, integrales de alta dimensión y propagación de incertidumbre.\n\nLa precisión mejora como 1/√N (independiente de la dimensión), lo que la hace ideal donde otras cuadraturas fallan. El generador de números pseudoaleatorios y el error estadístico definen la calidad."}],
                     "questions": [
                         {"q": "El error de Monte Carlo decrece como:", "options": {"A": "1/N", "B": "1/√N", "C": "1/N²", "D": "log N"}, "answer": "B", "difficulty": "basic",
                          "explanation": "El error estándar del estimador es σ/√N."},
                         {"q": "Monte Carlo es especialmente útil cuando:", "options": {"A": "la integral es 1D exacta", "B": "la dimensión es alta", "C": "hay datos ordenados", "D": "el problema es lineal"}, "answer": "B", "difficulty": "basic",
                          "explanation": "No sufre la maldición de la dimensión como las cuadraturas."},
                         {"q": "Para estimar π con Monte Carlo se usa:", "options": {"A": "puntos aleatorios en un cuadrado inscrito en un círculo", "B": "la serie de Taylor", "C": "la raíz cuadrada exacta", "D": "interpolación"}, "answer": "A", "difficulty": "basic",
                          "explanation": "La proporción dentro del círculo estima π/4."},
                     ]},
                ],
            },
            "cs04": {
                "code": "CS04", "name": "Análisis de Datos y Fundamentos de IA", "name_en": "Data Analysis & AI Fundamentals",
                "desc": "Estadística aplicada, regresión, clasificación y los primeros modelos de aprendizaje automático.",
                "credits": 5, "prereq": "cs03", "required": 70, "color": "#818cf8",
                "modules": [
                    {"id": "l3_cs04_m1", "name": "Estadística y visualización",
                     "lessons": [
                         {"title": "Descripción y exploración de datos",
                          "body": "Las medidas de tendencia central (media, mediana) y dispersión (desviación estándar) resumen datos. El histograma muestra la distribución; el boxplot revela outliers.\n\nEl análisis exploratorio (EDA) precede a cualquier modelo: detecta valores faltantes, sesgos y correlaciones antes de construir hipótesis."}],
                     "questions": [
                         {"q": "Una medida robusta al outlier es:", "options": {"A": "la media", "B": "la mediana", "C": "la moda única", "D": "el rango"}, "answer": "B", "difficulty": "basic",
                          "explanation": "La mediana depende solo del valor central."},
                         {"q": "La desviación estándar mide:", "options": {"A": "la dispersión de los datos", "B": "el número de datos", "C": "la moda", "D": "la simetría"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Raíz cuadrada de la varianza: esparcimiento típico."},
                         {"q": "Un boxplot es útil para:", "options": {"A": "detectar outliers", "B": "calcular derivadas", "C": "entrenar redes", "D": "ordenar matrices"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Muestra cuartiles y señala valores atípicos."},
                     ]},
                    {"id": "l3_cs04_m2", "name": "Regresión",
                     "lessons": [
                         {"title": "Regresión lineal",
                          "body": "La regresión lineal modela y = β₀ + β₁x ajustando por mínimos cuadrados: minimiza la suma de errores al cuadrado.\n\nLa calidad se mide con R² (fracción de varianza explicada) y el error RMSE. La regresión multivariable extiende $\\mathbf{y} = \\mathbf{X}\\beta $ y se resuelve con la ecuación normal o descenso de gradiente."}],
                     "questions": [
                         {"q": "El método de mínimos cuadrados minimiza:", "options": {"A": "la suma de errores al cuadrado", "B": "la suma de errores absolutos", "C": "el máximo error", "D": "la varianza de x"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Minimiza Σ(yᵢ − ŷᵢ)²."},
                         {"q": "El coeficiente R² indica:", "options": {"A": "la fracción de varianza explicada", "B": "el número de variables", "C": "la pendiente", "D": "el tamaño de muestra"}, "answer": "A", "difficulty": "basic",
                          "explanation": "R² ∈ [0,1]: proporción de variación explicada por el modelo."},
                         {"q": "La ecuación normal para regresión es:", "options": {"A": "β = (XᵀX)⁻¹Xᵀy", "B": "β = Xᵀy", "C": "β = y/X", "D": "β = XXᵀ"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "Soluciona mínimos cuadrados directamente."},
                     ]},
                    {"id": "l3_cs04_m3", "name": "Clasificación y primeros modelos",
                     "lessons": [
                         {"title": "Regresión logística y validación",
                          "body": "La regresión logística clasifica estimando P(y=1|x) mediante la función sigmoide y una frontera de decisión lineal.\n\nLa validación divide datos en entrenamiento y prueba; se evalúa con exactitud, precisión y recall. Un modelo que memoriza el entrenamiento pero falla en prueba sufre overfitting; la regularización lo mitiga."}],
                     "questions": [
                         {"q": "La regresión logística produce:", "options": {"A": "probabilidades entre 0 y 1", "B": "valores sin cota", "C": "solo enteros", "D": "la media"}, "answer": "A", "difficulty": "basic",
                          "explanation": "La sigmoide comprime la salida al intervalo (0,1)."},
                         {"q": "El overfitting ocurre cuando:", "options": {"A": "el modelo generaliza perfecto", "B": "memoriza el entrenamiento y falla en prueba", "C": "hay pocas variables", "D": "el entrenamiento es insuficiente"}, "answer": "B", "difficulty": "basic",
                          "explanation": "Alta exactitud en train, baja en test."},
                         {"q": "La precisión del modelo en datos nuevos se estima con:", "options": {"A": "el conjunto de prueba", "B": "el conjunto de entrenamiento", "C": "la ecuación normal", "D": "el gradiente"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Se evalúa sobre datos no vistos."},
                     ]},
                ],
            },
        },
    },
    "aerospace": {
        "name": "Aeroespacial y Sistemas Espaciales", "name_en": "Aerospace & Space Systems Engineering",
        "color": "#60a5fa", "code": "ASE", "career_id": "aerospace",
        "courses": {
            "as01": {
                "code": "AS01", "name": "Mecánica Orbital", "name_en": "Orbital Mechanics",
                "desc": "Órbitas keplerianas, leyes de movimiento orbital y maniobras en el espacio.",
                "credits": 5, "prereq": None, "required": 70, "color": "#60a5fa",
                "modules": [
                    {"id": "l3_as01_m1", "name": "Leyes de Kepler y Newton",
                     "lessons": [
                         {"title": "Movimiento orbital",
                          "body": "La primera ley de Kepler: las órbitas son secciones cónicas (círculo, elipse, parábola, hipérbola) con el cuerpo central en un foco. La segunda: el radio vector barre áreas iguales en tiempos iguales (conservación del momentum angular).\n\nLa tercera ley conecta el periodo orbital con el semieje mayor: T² ∝ a³. La gravedad newtoniana F = GMm/r² explica la aceleración orbital a = GM/r²."}],
                     "questions": [
                         {"q": "Las órbitas keplerianas son:", "options": {"A": "circunferencias perfectas", "B": "secciones cónicas", "C": "líneas rectas", "D": "espirales logarítmicas"}, "answer": "B", "difficulty": "basic",
                          "explanation": "Círculo, elipse, parábola e hipérbola."},
                         {"q": "La tercera ley de Kepler establece:", "options": {"A": "T² ∝ a³", "B": "T² ∝ 1/a", "C": "T ∝ a", "D": "a² ∝ T³"}, "answer": "A", "difficulty": "basic",
                          "explanation": "El cuadrado del periodo es proporcional al cubo del semieje mayor."},
                         {"q": "La velocidad necesaria para la órbita circular a radio r es:", "options": {"A": "√(GM/r)", "B": "GM/r", "C": "√(2GM/r)", "D": "GM/r²"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "Igualando fuerza centrípeta y gravitatoria: v_orb = √(GM/r)."},
                     ]},
                    {"id": "l3_as01_m2", "name": "Elementos orbitales",
                     "lessons": [
                         {"title": "Parámetros de la órbita",
                          "body": "Los elementos orbitales clásicos describen la órbita: semieje mayor, excentricidad, inclinación, argumento de perigeo, ascensión recta del nodo y anomalía del movimiento.\n\nEl semi- eje mayor define el tamaño, la excentricidad la elongación, y la inclinación orienta la órbita respecto al ecuador. Conocerlos permite predecir la posición del satélite."}],
                     "questions": [
                         {"q": "La excentricidad de una órbita circular es:", "options": {"A": "0", "B": "1", "C": "infinita", "D": "0.5"}, "answer": "A", "difficulty": "basic",
                          "explanation": "e = 0 corresponde a un círculo perfecto."},
                         {"q": "La inclinación orbital es el ángulo respecto al:", "options": {"A": "plano ecuatorial", "B": "eje galáctico", "C": "plano orbital", "D": "horizonte local"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Inclina la órbita respecto al ecuador terrestre."},
                         {"q": "Una órbita sun-synchronous está diseñada para:", "options": {"A": "mantener constante la iluminación solar sobre el terreno", "B": "seguir la Luna", "C": "evitar la gravedad", "D": "estar siempre sobre el ecuador"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "Su plano rota con ritmo solar: idéntica luz en cada paso."},
                     ]},
                    {"id": "l3_as01_m3", "name": "Maniobras y transferencias",
                     "lessons": [
                         {"title": "Transferencia de Hohmann",
                          "body": "La transferencia de Hohmann es la maniobra de mínimo costo entre órbitas circulares coplanares: usa dos impulsos, uno en perigeo y otro en apogeo, con una elipse intermedia.\n\nEl Δv total es la suma de los cambios de velocidad. Planear el encuentro requiere fases: los tiempos y posiciones deben sincronizarse; el impulso gravitacional (gravedad de asistencia) puede ahorrar Δv enorme."}],
                     "questions": [
                         {"q": "La transferencia de Hohmann conecta dos órbitas circulares con:", "options": {"A": "una elipse tangente", "B": "una parábola", "C": "un único impulso", "D": "una espiral"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Dos impulsos con elipse de transferencia tangente a ambas órbitas."},
                         {"q": "El Δv mide:", "options": {"A": "el cambio de velocidad requerido", "B": "el cambio de masa", "C": "la altura de la órbita", "D": "la duración del vuelo"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Es el incremento de velocidad del propulsor."},
                         {"q": "La gravedad de asistencia (flyby) sirve para:", "options": {"A": "ganar o perder energía sin combustible", "B": "estabilizar actitud", "C": "comunicarse", "D": "enfriar el satélite"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "Aprovecha el movimiento del planeta para cambiar velocidad relativa."},
                     ]},
                ],
            },
            "as02": {
                "code": "AS02", "name": "Aerodinámica I", "name_en": "Aerodynamics I",
                "desc": "Flujo en fluidos, sustentación, arrastre y los conceptos básicos del ala y el perfil.",
                "credits": 5, "prereq": "as01", "required": 70, "color": "#93c5fd",
                "modules": [
                    {"id": "l3_as02_m1", "name": "Fundamentos del flujo",
                     "lessons": [
                         {"title": "Flujo de fluidos y continuidad",
                          "body": "La ecuación de continuidad conserva la masa: ρ₁A₁V₁ = ρ₂A₂V₂. La ecuación de Bernoulli relaciona presión, velocidad y altura en flujo incompresible.\n\nEl número de Reynolds Re = ρVd/μ clasifica flujo laminar (Re bajo) y turbulento (Re alto) y gobierna la transición sobre superficies."}],
                     "questions": [
                         {"q": "En la ecuación de continuidad, si el área aumenta entonces la velocidad:", "options": {"A": "aumenta", "B": "disminuye", "C": "no cambia", "D": "se vuelve cero"}, "answer": "B", "difficulty": "basic",
                          "explanation": "Como el flujo es constante, mayor área ⟹ menor velocidad."},
                         {"q": "Un número de Reynolds alto típicamente indica flujo:", "options": {"A": "laminar", "B": "turbulento", "C": "estancado", "D": "supersónico"}, "answer": "B", "difficulty": "basic",
                          "explanation": "Re alto ⟹ inercia domina ⟹ turbulencia."},
                         {"q": "La ecuación de Bernoulli relaciona:", "options": {"A": "presión y velocidad", "B": "temperatura y masa", "C": "densidad y volumen", "D": "velocidad y densidad"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Suma de presión dinámica y estática constante en flujo incompresible."},
                     ]},
                    {"id": "l3_as02_m2", "name": "Sustentación y arrastre",
                     "lessons": [
                         {"title": "Fuerzas aerodinámicas",
                          "body": "El flujo alrededor de un perfil produce sustentación (perpendicular a la corriente) y arrastre (paralelo). El coeficiente de sustentación C_L y de arrastre C_D se usan en L = ½ρV²SC_L.\n\nLa diferencia de presión entre extradós e intradós, explicada por la circulación y el efecto Coandă, genera la fuerza neta; el ángulo de ataque modula C_L hasta el stall."}],
                     "questions": [
                         {"q": "La sustentación de un ala es proporcional a:", "options": {"A": "½ρV²SC_L", "B": "ρVSC_D", "C": "mg/C_L", "D": "½ ρ S C_D"}, "answer": "A", "difficulty": "basic",
                          "explanation": "L = ½ρV²SC_L, relación clásica de sustentación."},
                         {"q": "El stall ocurre al superar:", "options": {"A": "el ángulo de ataque crítico", "B": "la velocidad del sonido", "C": "la altura de servicio", "D": "la densidad atmosférica"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Más allá del ángulo crítico el flujo se desprende y C_L cae."},
                         {"q": "El arrastre inducido se debe principalmente a:", "options": {"A": "los vórtices de punta de ala", "B": "la fricción viscosa", "C": "la gravedad", "D": "el combustible"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "La sustentación crea circulación en punta que genera vórtices."},
                     ]},
                    {"id": "l3_as02_m3", "name": "Flujo compresible básico",
                     "lessons": [
                         {"title": "Número de Mach y régimen supersónico",
                          "body": "El número de Mach M = V/a clasifica flujo subsónico (M<1) y supersónico (M>1). Al pasar M = 1 aparecen ondas de choque que cambian bruscamente presión y temperatura.\n\nLa relación de área de es la 'tubo convergente-divergente' para acelerar a M>1; en aeronaves, las ondas de choque crean arrastre de onda y limitan el diseño a altas velocidades."}],
                     "questions": [
                         {"q": "El número de Mach es:", "options": {"A": "velocidad sobre velocidad del sonido", "B": "densidad por velocidad", "C": "presión por área", "D": "altura sobre velocidad"}, "answer": "A", "difficulty": "basic",
                          "explanation": "M = V/a."},
                         {"q": "Una onda de choque en flujo supersónico produce:", "options": {"A": "cambio brusco de presión y temperatura", "B": "aumento de velocidad", "C": "flujo laminar", "D": "vacío total"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Compresión abrupta con disipación de energía."},
                         {"q": "Para acelerar un gas de subsónico a supersónico se usa:", "options": {"A": "tubería convergente-divergente", "B": "tubería convergente simple", "C": "tobera divergente simple", "D": "un difusor"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "La garganta alcanza M=1 y la sección divergente acelera a M>1."},
                     ]},
                ],
            },
            "as03": {
                "code": "AS03", "name": "Dinámica de Vuelo y Control", "name_en": "Flight Dynamics & Control",
                "desc": "Estabilidad estática y dinámica, ejes del avión y sistemas de control de vuelo.",
                "credits": 5, "prereq": "as02", "required": 70, "color": "#7dd3fc",
                "modules": [
                    {"id": "l3_as03_m1", "name": "Estabilidad estática",
                     "lessons": [
                         {"title": "Estabilidad longitudinal",
                          "body": "La estabilidad estática indica si el vehículo vuelve a un equilibrio tras una perturbación. En longitudinal, el margen estático requiere el centro de gravedad delante del foco aerodinámico.\n\nEl criterio del margen estático SM = h_foco − h_cg > 0 garantiza estabilidad; un margen pequeño da menos estabilidad pero más maniobrabilidad."}],
                     "questions": [
                         {"q": "Para estabilidad estática longitudinal, el CG debe estar:", "options": {"A": "delante del foco", "B": "detrás del foco", "C": "en el foco", "D": "en el morro"}, "answer": "A", "difficulty": "basic",
                          "explanation": "CG delante del foco ⟹ momento restaurador tras perturbación."},
                         {"q": "Un margen estático negativo indica:", "options": {"A": "inestabilidad estática", "B": "máxima estabilidad", "C": "velocidad supersónica", "D": "exceso de sustentación"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "La perturbación se amplifica en lugar de atenuarse."},
                         {"q": "El morro de un avión apuntando a la subida tras una perturbación es:", "options": {"A": "una perturbación de estabilidad de cabeceo", "B": "el trim", "C": "el control de yaw", "D": "el flaperón"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Pitching: perturbación en el eje de cabeceo que la estabilidad debe amortiguar."},
                     ]},
                    {"id": "l3_as03_m2", "name": "Dinámica del vehículo",
                     "lessons": [
                         {"title": "Ejes y modos de movimiento",
                          "body": "Los tres ejes del vehículo son balanceo (roll), cabeceo (pitch) y guiñada (yaw). Los modos dinámicos del avión: phugoid (oscilación lenta de energía), short period (rápida en actitud) y los modos lateral-direccionales (dutch roll, roll y espiral).\n\nLos modos deben ser estables o al menos débilmente inestables para las aeronaves de combate; en cohetes y satélites el control es activo."}],
                     "questions": [
                         {"q": "El eje de cabeceo es responsable de:", "options": {"A": "mover el morro arriba/abajo", "B": "girar sobre el eje longitudinal", "C": "variar el rumbo", "D": "cambiar la velocidad de sonido"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Pitch: rotación alrededor del eje lateral (cabeceo)."},
                         {"q": "El modo phugoid es:", "options": {"A": "una oscilación lenta de intercambio energía-altura-velocidad", "B": "una rotación rápida lateral", "C": "la respuesta al gas", "D": "un modo estructural"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "El avión sube y baja intercambiando energía cinética y potencial."},
                         {"q": "Los alerones controlan principalmente:", "options": {"A": "el balanceo (roll)", "B": "la guiñada", "C": "el cabeceo", "D": "el empuje"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Alerones diferenciales crean el momento de balanceo."},
                     ]},
                    {"id": "l3_as03_m3", "name": "Sistemas de control",
                     "lessons": [
                         {"title": "Control de actitud y trayectoria",
                          "body": "El control de vuelo mantiene la actitud y trayectoria deseadas. En cohetes y vehículos espaciales, sensores (giróscopos, acelerómetros) y actuadores gobiernan la orientación.\n\nLos sistemas de control de actitud usan lazo cerrado con sensores en el vehículo; en microgravedad los actuadores típicos son toberas de gas frío, ruedas de reacción y magnetorqueros."}],
                     "questions": [
                         {"q": "Una rueda de reacción cambia la actitud mediante:", "options": {"A": "conservación del momentum angular", "B": "consumo de gas", "C": "calor", "D": "magnetismo externo"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Girar la rueda gira el vehículo en sentido opuesto."},
                         {"q": "Un magnetorquer genera torque usando:", "options": {"A": "el campo magnético terrestre", "B": "gas comprimido", "C": "propulsión química", "D": "paneles solares"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Pares magnéticos con el campo terrestre."},
                         {"q": "En un lazo de control cerrado:", "options": {"A": "se mide el estado y se corrige", "B": "se ejecuta a ciegas", "C": "no hay sensores", "D": "se apaga el actuador"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Realimentación: sensor → controlador → actuador."},
                     ]},
                ],
            },
            "as04": {
                "code": "AS04", "name": "Sistemas de Espacio Nave", "name_en": "Spacecraft Systems",
                "desc": "Estructura, propulsión, energía, termal y comunicaciones de una nave espacial.",
                "credits": 5, "prereq": "as03", "required": 70, "color": "#a5b4fc",
                "modules": [
                    {"id": "l3_as04_m1", "name": "Arquitectura de la nave",
                     "lessons": [
                         {"title": "Subsistemas de una nave",
                          "body": "Una nave espacial integra subsistemas: estructura y mecánica, propulsión, determinación de actitud y control, potencia, control térmico, telemetría y comunicaciones, y computadora de a bordo.\n\nCada misión equilibra masa, costo y confiabilidad: la redundancia y el análisis de modo de falla (FMEA) son el estándar de diseño espacial."}],
                     "questions": [
                         {"q": "El subsistema de control térmico mantiene:", "options": {"A": "la temperatura dentro de rangos operativos", "B": "la órbita", "C": "la comunicación", "D": "el poder"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Radiadores y mantas protegen los componentes del vacío."},
                         {"q": "El FMEA se usa para:", "options": {"A": "analizar modos de falla y sus efectos", "B": "diseñar la órbita", "C": "calcular revenida", "D": "entrenar pilotos"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Identificar riesgos en cada subsistema."},
                         {"q": "Un sistema redundante:", "options": {"A": "duplica funciones para aumentar confiabilidad", "B": "reduce masa", "C": "acelera la órbita", "D": "economiza costo"}, "answer": "A", "difficulty": "basic",
                          "explanation": "La copia de respaldo sube la probabilidad de éxito."},
                     ]},
                    {"id": "l3_as04_m2", "name": "Propulsión de la nave",
                     "lessons": [
                         {"title": "Propulsores y control orbital",
                          "body": "Los propulsores para maniobras usan la ecuación del cohete: Δv = Iₛₚ·g₀·ln(m₀/m_f). El impulso específico Iₛₚ cualifica la eficiencia: químicos ~300 s, eléctricos (ion) ~3000 s.\n\nPara maniobras finas se usan monopropelentes (hidracina) o propulsión eléctrica de alto Iₛₚ con empuje bajo pero prolongado."}],
                     "questions": [
                         {"q": "La ecuación del cohete calcula Δv a partir de:", "options": {"A": "Isp, g₀ y relación de masas", "B": "la altitud", "C": "la temperatura", "D": "la presión en la tobera"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Δv = Isp·g₀·ln(m₀/mf)."},
                         {"q": "Un Iₛₚ alto significa:", "options": {"A": "mayor eficiencia de propulsión", "B": "más masa de estructura", "C": "menor velocidad", "D": "mayor g"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Más empuje por unidad de flujo másico."},
                         {"q": "La propulsión iónica se caracteriza por:", "options": {"A": "bajo empuje y alto Iₛₚ", "B": "alto empuje instantáneo", "C": "combustión química", "D": "sin electricidad"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Empuje continuo pequeño con eficiencia altísima."},
                     ]},
                    {"id": "l3_as04_m3", "name": "Energía y comunicaciones",
                     "lessons": [
                         {"title": "Potencia y enlace de datos",
                          "body": "La energía de una nave proviene de paneles solares (para LEO) o RTG (para misiones lejanas). Las celdas solares y baterías gestionan la carga en la sombra.\n\nLas comunicaciones dependen del enlace: la ecuación de Friis cuantifica la potencia recibida; las bandas de radio (S, X, Ka) y la óptica ofrecen tasas distintas. La antena de alta ganancia enfoca el haz."}],
                     "questions": [
                         {"q": "Para misiones lejos del Sol, la energía típica es:", "options": {"A": "RTG (generador radiactivo)", "B": "paneles solares grandes", "C": "baterías de litio solamente", "D": "celdas de combustible"}, "answer": "A", "difficulty": "basic",
                          "explanation": "La luz solar es muy débil; los RTG convierten el calor de la desintegración."},
                         {"q": "La ecuación de Friis se usa para calcular:", "options": {"A": "la potencia recibida de un enlace", "B": "el periodo orbital", "C": "la masa de la nave", "D": "el empuje"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Modela la transmisión entre antenas transmisora y receptora."},
                         {"q": "Una antena de alta ganancia:", "options": {"A": "enfoca la señal en una dirección", "B": "emite en todas direcciones", "C": "aumenta la masa siempre", "D": "solo funciona en órbita baja"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Dirigibilidad ⟹ mayor potencia efectiva hacia la Tierra."},
                     ]},
                ],
            },
        },
    },
    "propulsion": {
        "name": "Propulsión y Tecnología de Cohetes", "name_en": "Propulsion & Rocket Technology Engineering",
        "color": "#fb923c", "code": "PRE", "career_id": "propulsion",
        "courses": {
            "pr01": {
                "code": "PR01", "name": "Termodinámica y Ciclos de Propulsión", "name_en": "Thermodynamics & Propulsion Cycles",
                "desc": "Primera y segunda ley, ciclos termodinámicos y su aplicación a motores y cohetes.",
                "credits": 5, "prereq": None, "required": 70, "color": "#fb923c",
                "modules": [
                    {"id": "l3_pr01_m1", "name": "Leyes de la termodinámica",
                     "lessons": [
                         {"title": "Primera y segunda ley",
                          "body": "La primera ley conserva la energía: ΔU = Q − W. La segunda limita la dirección: la entropía de un sistema aislado nunca decrece; introduce eficiencias de máquina por temperatura entre fuentes.\n\nEl rendimiento de Carnot η = 1 − T_f/T_c es el límite máximo alcanzable; la entropía y la irreversibilidad gobiernan todos los motores térmicos y propulsores."}],
                     "questions": [
                         {"q": "La primera ley de la termodinámica enuncia:", "options": {"A": "conservación de la energía", "B": "aumento indefinido de calor", "C": "conservación de la masa", "D": "el cero absoluto"}, "answer": "A", "difficulty": "basic",
                          "explanation": "ΔU = Q − W: la energía total se conserva."},
                         {"q": "El rendimiento de Carnot depende de:", "options": {"A": "las temperaturas de las fuentes", "B": "la presión", "C": "el volumen", "D": "la masa"}, "answer": "A", "difficulty": "basic",
                          "explanation": "η = 1 − T_f/T_c (temperaturas absolutas)."},
                         {"q": "La entropía de un sistema aislado:", "options": {"A": "nunca decrece", "B": "siempre es cero", "C": "aumenta solo con el calor", "D": "es constante"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Segunda ley: tendencia al aumento de la entropía."},
                     ]},
                    {"id": "l3_pr01_m2", "name": "Ciclos de potencia",
                     "lessons": [
                         {"title": "Ciclos Brayton, Otto y Rankine",
                          "body": "El ciclo Brayton describe turbinas de gas usando compresor, cámara de combustión y turbina. El ciclo Otto modela el motor de gasolina; el Rankine el ciclo de vapor.\n\nEn propulsión aeronaútica, el turborreactor es un Brayton con tobera de escape; su empuje deriva del exceso de momento que sale por la tobera. La eficiencia térmica y de propulsión definen el rendimiento total."}],
                     "questions": [
                         {"q": "Un turborreactor opera fundamentalmente sobre el ciclo:", "options": {"A": "Brayton", "B": "Otto", "C": "Rankine", "D": "Carnot reversible"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Compresión, combustión y expansión en turbina: Brayton."},
                         {"q": "El ciclo Otto corresponde a:", "options": {"A": "motor de encendido por chispa", "B": "turboeje", "C": "planta nuclear", "D": "cohete químico"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Gasolina: compresión, combustión a volumen, escape."},
                         {"q": "La eficiencia térmica aumenta al incrementar:", "options": {"A": "la relación de compresión", "B": "la fricción", "C": "las pérdidas de calor", "D": "la presión de salida"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "Mayor compresión ⟹ mayor temperatura de entrada a turbina ⟹ más eficiencia."},
                     ]},
                    {"id": "l3_pr01_m3", "name": "Empuje y eficiencia",
                     "lessons": [
                         {"title": "Origen del empuje",
                          "body": "El empuje nace de la variación de momento del flujo: F = ṁ(v_exit − v_inlet) más la contribución de presión en la tobera. En un cohete, todo el flujo proviene del propulsor a bordo.\n\nLa eficiencia de propulsión η_p = 2/(1 + v_e/v_f) varía con la velocidad de vuelo; el compromiso entre alta velocidad de escape y eficiencia guía el diseño de toberas y sistemas."}],
                     "questions": [
                         {"q": "El empuje del cohete proviene de:", "options": {"A": "el cambio de momento del flujo expulsado", "B": "el rozamiento con el aire", "C": "la flotación", "D": "los paneles solares"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Tercera ley: expulsar masa acelera el vehículo."},
                         {"q": "En un cohete, la masa del propulsor proviene de:", "options": {"A": "a bordo del vehículo", "B": "la atmósfera", "C": "el oxígeno del aire", "D": "la pista"}, "answer": "A", "difficulty": "basic",
                          "explanation": "A diferencia de turborreactores, el cohete lleva oxidante."},
                         {"q": "Mayor velocidad de escape aumenta:", "options": {"A": "el Iₛₚ pero puede reducir la eficiencia de propulsión", "B": "la masa de estructura", "C": "el arrastre", "D": "la presión de cámara"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "Compromiso habitual entre eficiencia de propulsión y Isp."},
                     ]},
                ],
            },
            "pr02": {
                "code": "PR02", "name": "Propulsión de Cohetes I", "name_en": "Rocket Propulsion I",
                "desc": "Ecuación del cohete, toberas, presión de cámara y el diseño básico de motores químicos.",
                "credits": 5, "prereq": "pr01", "required": 70, "color": "#fdba74",
                "modules": [
                    {"id": "l3_pr02_m1", "name": "Ecuación del cohete",
                     "lessons": [
                         {"title": "Tsiolkovsky y Δv",
                          "body": "La ecuación de Tsiolkovsky: Δv = Iₛₚ·g₀·ln(m₀/m_f). El Iₛₚ es el impulso por unidad de peso de propulsor; m₀/m_f es la relación de masas.\n\nLos 'pasos' multiplican la fracción de masa estructural. Alcanzar LEO requiere Δv ≈ 9.4 km/s; la relación de masas y el Isp determinan cuánto cohete se necesita."}],
                     "questions": [
                         {"q": "La ecuación de Tsiolkovsky involucra:", "options": {"A": "Isp, g₀ y ln(m₀/mf)", "B": "la temperatura", "C": "la altitud", "D": "la presión barométrica"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Δv = Isp·g₀·ln(m₀/mf)."},
                         {"q": "Δv para llegar a LEO es aproximadamente:", "options": {"A": "9.4 km/s", "B": "1 km/s", "C": "300 m/s", "D": "28 km/s"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "La suma de pérdidas por gravedad, arrastre y velocidad orbital."},
                         {"q": "El Iₛₚ de un motor químico típico es del orden de:", "options": {"A": "300 s", "B": "3000 s", "C": "30 s", "D": "0.3 s"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Químicos: ~250–450 s en el vacío."},
                     ]},
                    {"id": "l3_pr02_m2", "name": "Toberas",
                     "lessons": [
                         {"title": "Tobera convergente-divergente",
                          "body": "La tobera convierte entalpía en velocidad cinética del gas. La relación A_e/A* se deriva de las ecuaciones de flujo isentrópico en condiciones supersónicas.\n\nEl ajuste de la relación de expansión a la altitud optimiza la presión de salida; una tobera subexpandida o sobreexpandida pierde eficiencia. El flujo se acelera hasta M>1 pasando la garganta."}],
                     "questions": [
                         {"q": "En una tobera de cohete, la garganta alcanza:", "options": {"A": "M=1", "B": "M=0", "C": "M=2", "D": "presión máxima"}, "answer": "A", "difficulty": "basic",
                          "explanation": "La garganta estrangula el flujo a sónico."},
                         {"q": "Una tobera adecuada expande el gas para igualar:", "options": {"A": "la presión de salida con la ambiente", "B": "la presión de cámara", "C": "la presión de estancamiento", "D": "cero"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Expansión óptima: p_e = p_a."},
                         {"q": "Una tobera sobreexpandida actúa:", "options": {"A": "con presión de salida menor a la ambiente", "B": "con presión de salida mayor", "C": "sin choque", "D": "a M=1 siempre"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "La presión ambiente empuja el flujo y puede formar ondas de choque."},
                     ]},
                    {"id": "l3_pr02_m3", "name": "Cámara de combustión",
                     "lessons": [
                         {"title": "Presión, temperatura y propulsantes",
                          "body": "En la cámara, la combustión eleva temperatura y presión; la velocidad característica c* mide la calidad de la combustión: c* = P_c·A_t/ṁ. La temperatura de llama y la presión definen el comportamiento termodinámico.\n\nPropulsantes comunes: LOX/RP-1 (queroseno), LOX/LH₂ (hidrógeno) y LOX/CH₄ (metano). El hidrógeno da alto Isp pero baja densidad; el metano combina densidad y reutilización."}],
                     "questions": [
                         {"q": "La velocidad característica c* mide:", "options": {"A": "la eficiencia de la combustión", "B": "el arrastre", "C": "la altitud", "D": "el peso"}, "answer": "A", "difficulty": "basic",
                          "explanation": "c* responde a la calidad de la llama en cámara."},
                         {"q": "El propulsante LOX/LH₂ destaca por:", "options": {"A": "alto Isp", "B": "alta densidad", "C": "bajo costo", "D": "fácil almacenamiento"}, "answer": "A", "difficulty": "basic",
                          "explanation": "El hidrógeno proporciona el Isp químico más alto."},
                         {"q": "El metano como combustible es atractivo por:", "options": {"A": "densidad, bajo hollín y reutilización", "B": "alto peso molecular", "C": "alta temperatura", "D": "falta de oxígeno"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "Densidad aceptable y depósitos limpios en reutilizables."},
                     ]},
                ],
            },
            "pr03": {
                "code": "PR03", "name": "Fundamentos de Combustión", "name_en": "Combustion Fundamentals",
                "desc": "Estequiometría, entalpía de reacción, velocidad de llama y la química de la combustión propulsiva.",
                "credits": 5, "prereq": "pr02", "required": 70, "color": "#fcd34d",
                "modules": [
                    {"id": "l3_pr03_m1", "name": "Estequiometría",
                     "lessons": [
                         {"title": "Balances de combustión",
                          "body": "La combustión balancea reactivos y productos: CH₄ + 2O₂ → CO₂ + 2H₂O. La relación equivalente φ = (F/A)/(F/A)_establecida indica mezcla rica (φ>1) o pobre (φ<1).\n\nEn motores de cohete el balance de masa y energía define temperaturas y gastos: el diseño parte del balance estequiométrico para fijar la relación de mezcla O/F."}],
                     "questions": [
                         {"q": "La ecuación balanceada de combustión de metano es:", "options": {"A": "CH₄ + 2O₂ → CO₂ + 2H₂O", "B": "CH₄ + O₂ → CO₂", "C": "2CH₄ + O₂ → CO₂ + H₂O", "D": "CH₄ + 3O₂ → 2CO₂ + 2H₂O"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Un carbono a CO₂ y cuatro hidrógenos a dos aguas."},
                         {"q": "Una mezcla rica tiene relación de equivalencia:", "options": {"A": "φ > 1", "B": "φ < 1", "C": "φ = 1", "D": "φ = 0"}, "answer": "A", "difficulty": "basic",
                          "explanation": "φ>1: combustible en exceso."},
                         {"q": "La cantidad de O₂ para quemar 2 mol de H₂ es:", "options": {"A": "1 mol", "B": "2 mol", "C": "4 mol", "D": "0.5 mol"}, "answer": "A", "difficulty": "basic",
                          "explanation": "2H₂ + O₂ → 2H₂O: 1 mol por cada 2 de H₂."},
                     ]},
                    {"id": "l3_pr03_m2", "name": "Química de la combustión",
                     "lessons": [
                         {"title": "Entalpía de reacción y llama",
                          "body": "La entalpía de combustión ΔH_c mide el calor liberado. La temperatura adiabática de llama se calcula igualando entalpías de productos y reactivos; es el límite teórico de la temperatura en cámara.\n\nLa disociación a alta temperatura reduce la temperatura real; la velocidad de reacción sigue la ley de Arrhenius, dependiendo exponencialmente de la temperatura."}],
                     "questions": [
                         {"q": "La temperatura adiabática de llama es:", "options": {"A": "el límite teórico sin pérdidas", "B": "la temperatura real en cámara", "C": "la temperatura ambiente", "D": "el punto de ebullición"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Línea límite con toda la energía en productos."},
                         {"q": "La ley de Arrhenius modela:", "options": {"A": "la dependencia de la velocidad de reacción con la temperatura", "B": "la densidad del gas", "C": "la presión de saturación", "D": "el Isp"}, "answer": "A", "difficulty": "basic",
                          "explanation": "k = A·e^(−Ea/RT)."},
                         {"q": "La disociación a alta temperatura:", "options": {"A": "reduce la temperatura alcanzada", "B": "aumenta el Isp siempre", "C": "incrementa la densidad", "D": "elimina el CO₂"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "Parte de la energía se invierte en romper moléculas."},
                     ]},
                    {"id": "l3_pr03_m3", "name": "Velocidad de llama y estabilidad",
                     "lessons": [
                         {"title": "Frentes de llama y extinción",
                          "body": "La velocidad de llama laminar es la velocidad a la que avanza el frente de reacción. La velocidad turbulenta es mayor y distorsiona el frente con remolinos.\n\nLa estabilidad de llama depende de mantener anclaje y mezcla; un enfriamiento excesivo o ricardo extremo produce extinción. En cohetes, la estabilidad de la combustión evita inestabilidades de presión destructivas (combustión pulsante)."}],
                     "questions": [
                         {"q": "La velocidad de llama turbulenta es:", "options": {"A": "mayor que la laminar", "B": "menor que la laminar", "C": "igual siempre", "D": "cero"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Los remolinos estiran y aceleran el frente de llama."},
                         {"q": "Una mezcla demasiado rica puede causar:", "options": {"A": "extinción de la llama", "B": "mayor velocidad de llama", "C": "flujo supersónico de salida", "D": "menor presión"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "Fuera del límite de inflamabilidad la llama no sostiene."},
                         {"q": "Las inestabilidades de combustión en cohetes son peligrosas porque:", "options": {"A": "generan oscilaciones de presión destructivas", "B": "aumentan el Isp", "C": "reducen la masa", "D": "alimentan más oxígeno"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Resonancias pueden destruir la cámara."},
                     ]},
                ],
            },
            "pr04": {
                "code": "PR04", "name": "Turbomáquinas", "name_en": "Turbomachinery",
                "desc": "Bombas, turbinas y conejos: cómo se alimentan los motores de cohete a alta presión.",
                "credits": 5, "prereq": "pr03", "required": 70, "color": "#fde68a",
                "modules": [
                    {"id": "l3_pr04_m1", "name": "Bombas de alta presión",
                     "lessons": [
                         {"title": "Turbobombas y ciclo de presión",
                          "body": "Los motores de cohete presurizan los propulsantes con turbobombas, no con helio, para mantener cámaras de alta presión sin tanques masivos.\n\nLa turbobomba combina una bomba centrífuga (flujo a alta presión) movida por una turbina alimentada por gas quemado. Proporcionar la potencia de la turbina es el corazón del feed system."}],
                     "questions": [
                         {"q": "La turbobomba sube la presión de:", "options": {"A": "los propulsantes antes de la cámara", "B": "los tanques", "C": "la atmosfera", "D": "el escape"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Bombea combustible y oxidante a presión de cámara."},
                         {"q": "Usar turbobombas permite:", "options": {"A": "cámaras de alta presión con tanques ligeros", "B": "tanques de helio masivos", "C": "menor empuje", "D": "combustión externa"}, "answer": "A", "difficulty": "basic",
                          "explanation": "El sistema de presión no depende de tanques pesados."},
                         {"q": "En el ciclo abierto (gas-generator), el gas de turbina:", "options": {"A": "se descarta por una tobera secundaria", "B": "retorna a la cámara", "C": "se condensa", "D": "se usa para enfriar"}, "answer": "A", "difficulty": "intermediate",
                          "explanation": "Mezclado con el escape principal o por su propia tobera."},
                     ]},
                    {"id": "l3_pr04_m2", "name": "Turbinas",
                     "lessons": [
                         {"title": "Potencia de la turbina",
                          "body": "La turbina extrae potencia del gas de alta temperatura usando álabes curvados; la ecuación de Euler para turbomáquinas relaciona el torque con el cambio de momento angular del flujo.\n\nLa eficiencia del conducto y la geometría de los álabes definen cuánto de la entalpía se convierte en trabajo; los álabes de turbina en cohetes deben soportar gas caliente abrasivo."}],
                     "questions": [
                         {"q": "La ecuación de Euler de turbomáquina relaciona:", "options": {"A": "torque con cambio de momento angular del flujo", "B": "presión con temperatura", "C": "masa con volumen", "D": "velocidad con watt"}, "answer": "A", "difficulty": "basic",
                          "explanation": "T = ṁ(r₁vu₁ − r₂vu₂)."},
                         {"q": "Los álabes de turbina de cohete enfrentan:", "options": {"A": "gas caliente y abrasivo", "B": "vacio total", "C": "oxígeno líquido puro", "D": "temperatura criogénica"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Alta temperatura y partículas del gas generador."},
                         {"q": "La turbina convierte la energía del gas en:", "options": {"A": "trabajo mecánico de eje", "B": "presión en cámara", "C": "vibración", "D": "calor residual"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Impulsa la bomba vía eje."},
                     ]},
                    {"id": "l3_pr04_m3", "name": "Ciclos de alimentación",
                     "lessons": [
                         {"title": "Ciclos generador de gas, stage-combustion y expander",
                          "body": "El ciclo de generador de gas quema propulsante de forma separada y descarga el escape. El ciclo de encapsulamiento (stage combustion) inyecta todo el gas a la cámara, subiendo la presión con complejidad. El ciclo expansor usa el calor del refrigerante para impulsar la turbina.\n\nLa elección del ciclo equilibra eficiencia, complejidad y reutilización: stage combustion logra mayor Isp pero exige gestión fina de presiones."}],
                     "questions": [
                         {"q": "El ciclo de generador de gas (abierto) descarga el gas de turbina:", "options": {"A": "al exterior", "B": "a la cámara", "C": "a los tanques", "D": "al intercooler"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Es la característica que lo hace 'abierto'."},
                         {"q": "El stage combustion envía todo el gas:", "options": {"A": "a la cámara de combustión", "B": "al escape", "C": "a la tobera secundaria", "D": "al tanque de oxidante"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Máxima eficiencia: nada se desperdicia."},
                         {"q": "El ciclo expansor usa el calor de:", "options": {"A": "la refrigeración de la tobera/cámara", "B": "la combustión externa", "C": "el sol", "D": "la fricción"}, "answer": "A", "difficulty": "basic",
                          "explanation": "El propulsante refrigerante se vaporiza y mueve la turbina."},
                     ]},
                ],
            },
        },
    },
    "nuclear": {
        "name": "Nuclear y Energía Avanzada", "name_en": "Nuclear Engineering & Advanced Energy",
        "color": "#a3e635", "code": "NEE", "career_id": "nuclear",
        "courses": {
            "nu01": {
                "code": "NU01", "name": "Física Nuclear", "name_en": "Nuclear Physics",
                "desc": "Núcleo atómico, fuerzas nucleares, radiactividad y la energía de ligadura.",
                "credits": 5, "prereq": None, "required": 70, "color": "#a3e635",
                "modules": [
                    {"id": "l3_nu01_m1", "name": "El núcleo atómico",
                     "lessons": [
                         {"title": "Composición y estabilidad",
                          "body": "El núcleo contiene protones y neutrones (nucleones). La fuerza nuclear fuerte mantiene unidos nucleones a muy corta distancia venciendo la repulsión eléctrica.\n\nCada elemento tiene isótopos: mismo número de protones, distinto número de neutrones. La carta de nuclidos organiza los núcleos por estabilidad; la mayoría de los núcleos pesados son radiactivos."}],
                     "questions": [
                         {"q": "Los nucleones son:", "options": {"A": "protones y neutrones", "B": "electrones y protones", "C": "quarks libres", "D": "fotones"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Partículas que forman el núcleo."},
                         {"q": "La fuerza nuclear fuerte actúa a:", "options": {"A": "distancias muy cortas", "B": "distancias astronómicas", "C": "todas las escalas", "D": "solo a nivel orbital"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Rango del femtometro, domina la escala nuclear."},
                         {"q": "Los isótopos comparten el mismo número de:", "options": {"A": "protones", "B": "neutrones", "C": "nucleones", "D": "electrones siempre"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Mismo Z, distinto N."},
                     ]},
                    {"id": "l3_nu01_m2", "name": "Radiactividad",
                     "lessons": [
                         {"title": "Tipos de decaimiento",
                          "body": "El decaimiento alfa emite núcleos de helio (reduce Z en 2); el beta transforma neutrones en protones (n → p + e⁻ + ν̄); el gamma libera energía electromagnética.\n\nLa ley de decaimiento es exponencial: N(t) = N₀e^(−λt), con vida media t₁/₂ = ln2/λ. Cada radionúclido tiene su vida media característica que determina su peligro y uso."}],
                     "questions": [
                         {"q": "Una partícula alfa es:", "options": {"A": "un núcleo de helio", "B": "un electrón", "C": "un fotón", "D": "un neutrón libre"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Dos protones y dos neutrones."},
                         {"q": "En el decaimiento beta, un neutrón:", "options": {"A": "se convierte en protón", "B": "desaparece", "C": "se duplica", "D": "permanece igual"}, "answer": "A", "difficulty": "basic",
                          "explanation": "n → p + e⁻ + ν̄, cambiando Z."},
                         {"q": "Si la vida media es de 10 años, tras 20 años queda:", "options": {"A": "1/4 del material", "B": "la mitad", "C": "todo", "D": "nada"}, "answer": "A", "difficulty": "basic",
                          "explanation": "En 2 vidas medias: (1/2)² = 1/4."},
                     ]},
                    {"id": "l3_nu01_m3", "name": "Energía de ligadura",
                     "lessons": [
                         {"title": "Defecto de masa y fisión",
                          "body": "La masa de un núcleo es menor que la suma de sus nucleones; el defecto de masa se convierte en energía de ligadura (E = mc²).\n\nLa curva de energía de ligadura por nucleón muestra un máximo alrededor del hierro: los núcleos muy pesados liberan energía al fisionarse (fisión) y los ligeros al fusionarse (fusión). Los reactores explotan la fisión del uranio."}],
                     "questions": [
                         {"q": "El defecto de masa se transforma en:", "options": {"A": "energía de ligadura", "B": "calor solo", "C": "partículas beta", "D": "vacio"}, "answer": "A", "difficulty": "basic",
                          "explanation": "ΔE = Δm·c²."},
                         {"q": "El elemento con mayor energía de ligadura por nucleón es:", "options": {"A": "hierro", "B": "uranio", "C": "hidrógeno", "D": "helio"}, "answer": "A", "difficulty": "basic",
                          "explanation": "El pico de la curva de estabilidad está en Fe."},
                         {"q": "La fisión libera energía al dividir núcleos:", "options": {"A": "pesados", "B": "ligeros", "C": "estables", "D": "gaseosos"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Uranio y plutonio: núcleos pesados sobre el pico."},
                     ]},
                ],
            },
            "nu02": {
                "code": "NU02", "name": "Teoría de Reactores", "name_en": "Reactor Theory",
                "desc": "Reacción en cadena, moderación, reactividad, criticidad y el ciclo del combustible nuclear.",
                "credits": 5, "prereq": "nu01", "required": 70, "color": "#bef264",
                "modules": [
                    {"id": "l3_nu02_m1", "name": "Reacción en cadena",
                     "lessons": [
                         {"title": "Fisión y neutrones",
                          "body": "La fisión del U-235 con un neutrón libera ~200 MeV, dos o tres neutrones rápidos y fragmentos radiactivos. En un reactor, esos neutrones inducen nuevas fisiones.\n\nEl factor de multiplicación k = P(fisiones en una generación)/P(anterior). k=1 es crítico (reacción sostenida), k<1 subcrítico y k>1 supercrítico. Los reactores se operan cerca de k=1."}],
                     "questions": [
                         {"q": "El reactor crítico tiene k:", "options": {"A": "= 1", "B": "> 1", "C": "< 1", "D": "= 0"}, "answer": "A", "difficulty": "basic",
                          "explanation": "k=1: una fisión genera exactamente la siguiente."},
                         {"q": "Cada fisión de U-235 libera energía del orden de:", "options": {"A": "200 MeV", "B": "2 eV", "C": "1 J", "D": "20 keV"}, "answer": "A", "difficulty": "basic",
                          "explanation": "~200 MeV por fisión."},
                         {"q": "Con k>1 el reactor:", "options": {"A": "aumenta la potencia", "B": "se apaga", "C": "mantiene constante", "D": "se enfría"}, "answer": "A", "difficulty": "basic",
                          "explanation": "La población de neutrones crece generación a generación."},
                     ]},
                    {"id": "l3_nu02_m2", "name": "Moderación y control",
                     "lessons": [
                         {"title": "Moderador y absorbentes",
                          "body": "La U-235 fisiona mejor con neutrones lentos (térmicos). El moderador (agua, agua pesada, grafito) reduce la velocidad de los neutrones rápidos por colisiones.\n\nLas barras de control (boro) y el sistema de seguridad absorben neutrones para controlar la reactividad. La ecuación de la difusión de neutrones rige la distribución espacial del flujo en el núcleo."}],
                     "questions": [
                         {"q": "La función del moderador es:", "options": {"A": "desacelerar neutrones", "B": "absorberlos siempre", "C": "generar calor solo", "D": "eliminar uranio"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Los neutrones térmicos fisionan mejor la U-235."},
                         {"q": "Las barras de control controlan la reactividad al:", "options": {"A": "absorber neutrones", "B": "emitir neutrones", "C": "calentar agua", "D": "enriquecer uranio"}, "answer": "A", "difficulty": "basic",
                          "explanation": "El boro-cadmio captura neutrones:"},
                         {"q": "Un buen moderador de bajo poder absorción es:", "options": {"A": "agua pesada", "B": "plomo", "C": "hierro", "D": "uranio natural"}, "answer": "A", "difficulty": "basic",
                          "explanation": "El deuterio absorbe pocos neutrones comparado con el hidrógeno."},
                     ]},
                    {"id": "l3_nu02_m3", "name": "Ciclo del combustible",
                     "lessons": [
                         {"title": "Del uranio al reprocesado",
                          "body": "El ciclo comienza con la minería y el enriquecimiento (aumentar U-235 del 0.7% al 3–5% en centrales), sigue con la formación de pellets y ensamblajes.\n\nTras la operación, el combustible gastado contiene actínidos y productos de fisión: opciones de gestión son almacenamiento temporal, disposición final geológica o reprocesado para extraer plutonio y uranio."}],
                     "questions": [
                         {"q": "El uranio natural tiene U-235 al:", "options": {"A": "0.7%", "B": "3%", "C": "20%", "D": "90%"}, "answer": "A", "difficulty": "basic",
                          "explanation": "El U-235 es minoritario (~0.7%); el resto U-238."},
                         {"q": "La mayoría de las centrales comerciales usan U-235:", "options": {"A": "3–5% enriquecido", "B": "al 100%", "C": "al 0.7% sin enriquecer", "D": "al 50%"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Enriquecimiento bajo para reactores de agua ligera."},
                         {"q": "El reprocesado extrae del combustible gastado:", "options": {"A": "uranio y plutonio", "B": "solo calor", "C": "hidrógeno", "D": "vidrio"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Recupera material fisionable para nuevos ciclos."},
                     ]},
                ],
            },
            "nu03": {
                "code": "NU03", "name": "Radiación y Seguridad Nuclear", "name_en": "Radiation & Nuclear Safety",
                "desc": "Dosis, blindaje, protección radiológica y los criterios de seguridad de instalaciones nucleares.",
                "credits": 5, "prereq": "nu02", "required": 70, "color": "#d9f99d",
                "modules": [
                    {"id": "l3_nu03_m1", "name": "Dosimetría",
                     "lessons": [
                         {"title": "Magnitudes y unidades",
                          "body": "El gris (Gy) mide la dosis absorbida (energía por unidad de masa); el sievert (Sv) pondera por el tipo de radiación y el daño biológico.\n\nLa dosis efectiva suma contribuciones de diferentes tejidos y radiaciones. La tasa de dosis decrece con la distancia (inverso del cuadrado) y se reduce con blindaje en función del coeficiente de atenuación."}],
                     "questions": [
                         {"q": "El sievert mide:", "options": {"A": "la dosis efectiva ponderada", "B": "la energía absorbida sola", "C": "la actividad", "D": "el flujo"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Ponderación por daño biológico y tipo de radiación."},
                         {"q": "El gris es la unidad de:", "options": {"A": "dosis absorbida", "B": "actividad", "C": "potencia", "D": "blindaje"}, "answer": "A", "difficulty": "basic",
                          "explanation": "J/kg absorbidos."},
                         {"q": "La dosis por una fuente puntual decrece con la distancia como:", "options": {"A": "1/r²", "B": "1/r", "C": "r", "D": "constante"}, "answer": "A", "difficulty": "basic",
                          "explanation": "La ley del inverso del cuadrado domina la geometría."},
                     ]},
                    {"id": "l3_nu03_m2", "name": "Blindaje",
                     "lessons": [
                         {"title": "Atenuación y materiales",
                          "body": "La atenuación exponencial I = I₀e^(−μx) describe cómo el blindaje reduce la intensidad; μ es el coeficiente de atenuación lineal.\n\nCada radiación exige materiales distintos: fotones requieren materiales densos (plomo, hormigón), beta se frena con materiales ligeros (evitando bremsstrahlung) y neutrones con moderadores ricos en hidrógeno y absorbentes de boro. El espesor de décima (TVD) reduce la dosis a la décima."}],
                     "questions": [
                         {"q": "La atenuación de radiación gamática sigue:", "options": {"A": "una exponencial decreciente", "B": "una recta", "C": "una parábola", "D": "una onda"}, "answer": "A", "difficulty": "basic",
                          "explanation": "I = I₀ e^(−μx)."},
                         {"q": "Para blindar neutrones se necesitan:", "options": {"A": "materiales con hidrógeno y boro", "B": "láminas de plomo gruesas", "C": "solo vacío", "D": "vidrio"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Los moderadores frenan neutrones; el boro los captura."},
                         {"q": "El espesor de décima (TVD) es aquel que:", "options": {"A": "reduce la dosis a 1/10", "B": "la reduce a la mitad", "C": "la duplica", "D": "la anula por completo"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Tras TVD, I = I₀/10."},
                     ]},
                    {"id": "l3_nu03_m3", "name": "Criterios de seguridad",
                     "lessons": [
                         {"title": "Defensa en profundidad",
                          "body": "La seguridad nuclear descansa en la defensa en profundidad: múltiples barreras y capas de protección en vez de una sola. Las barreras van del combustible cladding al contenedor y la contención.\n\nLos criterios de diseño consideran la protección en profundidad y la gestión de accidentes; los ACs (analyses de accidentes) evalúan eventos con análisis determinista y probabilista (PSA). Los límites de exposición ocupacional (20 mSv/año) rigen el trabajo radiológico."}],
                     "questions": [
                         {"q": "La defensa en profundidad se basa en:", "options": {"A": "múltiples barreras independientes", "B": "una única barrera gruesa", "C": "solo procedimientos", "D": "distancia infinita"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Redundancia de capas para tolerar fallos."},
                         {"q": "El límite típico de dosis ocupacional anual es:", "options": {"A": "20 mSv/año", "B": "200 mSv/año", "C": "2 Sv/año", "D": "0.1 mSv/año"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Límite estándar para trabajadores expuestos."},
                         {"q": "El PSA (análisis probabilístico de seguridad) evalúa:", "options": {"A": "probabilidades de secuencias de accidente", "B": "el costo del uranio", "C": "el rendimiento energético", "D": "la eficiencia de la turbina"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Estima la frecuencia de trayectorias de fallo."},
                     ]},
                ],
            },
            "nu04": {
                "code": "NU04", "name": "Sistemas Térmicos y Transferencia de Calor", "name_en": "Thermal Systems & Heat Transfer",
                "desc": "Conducción, convección, radiación y el circuito térmico que convierte la fisión en electricidad.",
                "credits": 5, "prereq": "nu03", "required": 70, "color": "#ecfccb",
                "modules": [
                    {"id": "l3_nu04_m1", "name": "Conducción",
                     "lessons": [
                         {"title": "Ley de Fourier",
                          "body": "La conducción transporta calor sin movimiento de masa: q = −k∇T (ley de Fourier). La conductividad k mide la facilidad; metales altos, cerámicas y gases bajos.\n\nLa ecuación de difusión de calor ∂T/∂t = α∇²T combina la ley de Fourier con la conservación de energía; α = k/(ρc_p) es la difusividad térmica que regula la rapidez de respuesta."}],
                     "questions": [
                         {"q": "La ley de Fourier describe el calor por:", "options": {"A": "conducción", "B": "radiación", "C": "convección forzada", "D": "condensación"}, "answer": "A", "difficulty": "basic",
                          "explanation": "q = −k∇T: conducción molecular."},
                         {"q": "La difusividad térmica mide:", "options": {"A": "la rapidez de propagación de la temperatura", "B": "la emisividad", "C": "la presión", "D": "el enfriamiento nuclear"}, "answer": "A", "difficulty": "basic",
                          "explanation": "α = k/(ρcₚ): velocidad de respuesta térmica."},
                         {"q": "Entre metal, gas y cerámica, la mayor conductividad típicamente es:", "options": {"A": "metal", "B": "gas", "C": "cerámica", "D": "vacío"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Los electrones libres del metal conducen muy bien."},
                     ]},
                    {"id": "l3_nu04_m2", "name": "Convección y radiación",
                     "lessons": [
                         {"title": "Coeficientes de transferencia",
                          "body": "La convección transfiere calor entre una superficie y un fluido en movimiento: q = h·A·(T_s − T_∞). El coeficiente h depende de la geometría, el fluido y el régimen (natural o forzado).\n\nLos números adimensionales (Nusselt, Reynolds, Prandtl) agrupan los parámetros y permiten correlaciones generalizadas; el reactor rechaza calor por convección al agua de enfriamiento.\n\nLa radiación sigue la ley de Stefan-Boltzmann: q = εσA(T⁴). Todo objeto emite como ε·σ·T⁴; el vacío del espacio elimina la convección y hace dominante la radiación."}],
                     "questions": [
                         {"q": "La convección de calor con flujo forzado usa:", "options": {"A": "un medio en movimiento por bomba/ventilador", "B": "solo radiación", "C": "conducción pura", "D": "el vacío"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Un fluido en movimiento transporta el calor por convecación."},
                         {"q": "La ley de Stefan-Boltzmann depende de T:", "options": {"A": "elevada a la cuarta potencia", "B": "lineal", "C": "al cuadrado", "D": "al cubo"}, "answer": "A", "difficulty": "basic",
                          "explanation": "q = εσAT⁴."},
                         {"q": "El número de Nusselt mide:", "options": {"A": "la convección frente a la conducción", "B": "la viscosidad", "C": "el empuje", "D": "la presión"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Nu = hL/k: convección normalizada."},
                     ]},
                    {"id": "l3_nu04_m3", "name": "Circuito térmico del reactor",
                     "lessons": [
                         {"title": "Del núcleo a la turbina",
                          "body": "Los PWR (reactores de agua a presión) separan circuitos: el primario (agua a alta presión 15 MPa) extrae el calor del núcleo, el generador de vapor lo transfiere al secundario, y el vapor mueve la turbina que impulsa el generador eléctrico.\n\nLa eficiencia del ciclo Rankine define la conversión (~33%); el sistema de enfriamiento de emergencia y las barras garantizan la remoción de calor residual en paradas. La refrigeración del núcleo es la función crítica de seguridad."}],
                     "questions": [
                         {"q": "En un PWR, el circuito primario está a alta presión para:", "options": {"A": "mantener el agua líquida sin hervir", "B": "generar vapor directo", "C": "enfriar la turbina", "D": "construir la contención"}, "answer": "A", "difficulty": "basic",
                          "explanation": "La presión eleva el punto de ebullición del refrigerante."},
                         {"q": "La conversión de calor a electricidad en un reactor usa el ciclo:", "options": {"A": "Rankine", "B": "Brayton", "C": "Otto", "D": "Carnot ideal"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Vapor de agua mueve la turbina: ciclo Rankine."},
                         {"q": "Tras la parada del reactor, el calor residual:", "options": {"A": "debe removerse con sistemas de emergencia", "B": "desaparece al instante", "C": "se convierte en luz", "D": "no existe"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Decae gradualmente y exige refrigeración continua."},
                     ]},
                ],
            },
        },
    },
    "spacesystems": {
        "name": "Sistemas Espaciales Avanzados", "name_en": "Advanced Space Systems Engineering",
        "color": "#f472b6", "code": "SSE", "career_id": "spacesystems",
        "courses": {
            "ss01": {
                "code": "SS01", "name": "Arquitectura de Sistemas Espaciales", "name_en": "Space Systems Architecture",
                "desc": "Ingeniería de sistemas para misiones espaciales: requisitos, interfaces, trade-offs y arquitectura de misión.",
                "credits": 5, "prereq": None, "required": 70, "color": "#f472b6",
                "modules": [
                    {"id": "l3_ss01_m1", "name": "Ingeniería de requisitos",
                     "lessons": [
                         {"title": "De la misión a los requisitos",
                          "body": "La ingeniería de sistemas espaciales parte de la declaración de misión: objetivo, entorno y restricciones. De ella se derivan requisitos de funcionamiento y desempeño para cada subsistema.\n\nLos requisitos deben ser trazables, verificables y sin ambigüedad. La definición de 'concept of operations' (CONOPS) describe cómo se operará el sistema en su ciclo de vida completo: lanzamiento, operación, mantenimiento y disposición."}],
                     "questions": [
                         {"q": "Un requisito debe ser:", "options": {"A": "verificable y trazable", "B": "vago e implícito", "C": "solo económico", "D": "independiente del entorno"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Sin trazabilidad no hay validación."},
                         {"q": "El CONOPS describe:", "options": {"A": "cómo se operará el sistema en su ciclo de vida", "B": "el costo del cohete", "C": "solo el software", "D": "el color del satélite"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Escenarios de operación de inicio a fin."},
                         {"q": "La trazabilidad de requisitos asegura:", "options": {"A": "que cada requisito se cumpla y verifique", "B": "que no haya requisitos", "C": "menor costo siempre", "D": "menos pruebas"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Conecta objetivo-misión con diseño y prueba."},
                     ]},
                    {"id": "l3_ss01_m2", "name": "Integración y arquitectura",
                     "lessons": [
                         {"title": "Bosque de la arquitectura",
                          "body": "La arquitectura del sistema define subsistemas, sus interfaces e interacciones. Una buena arquitectura minimiza interfaces frágiles y permite evolucionar cada subsistema.\n\nLa documentación de interfaces (ICDs) es el acuerdo entre equipos; un cambio de interface es un cambio de misión. El análisis de modos y efectos de falla (FMEA) y la redundancia dan robustez al sistema."}],
                     "questions": [
                         {"q": "Los ICD documentan:", "options": {"A": "las interfaces entre subsistemas", "B": "el presupuesto total", "C": "los nombres de la tripulación", "D": "solo el hardware"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Interface Control Documents: acuerdos de conexión."},
                         {"q": "Una arquitectura robusta:", "options": {"A": "reduce interfaces frágiles y permite evolución", "B": "evita la redundancia", "C": "funciona solo en vacíos", "D": "no necesita ICD"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Desacopla subsistemas y limita el impacto de cambios."},
                         {"q": "El FMEA identifica:", "options": {"A": "modos de falla y sus efectos", "B": "el costo de lanzamiento", "C": "la órbita final", "D": "el tamaño del panel solar"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Evalúa cómo falla cada componente y con qué consecuencia."},
                     ]},
                    {"id": "l3_ss01_m3", "name": "Presupuestos de misión",
                     "lessons": [
                         {"title": "Masa, potencia y costo",
                          "body": "El presupuesto de masa suma cada subsistema y reserva margen; el presupuesto de potencia balancea generación, almacenamiento y consumo en cada fase. El de costo y el de tiempo cierran el triángulo del proyecto.\n\nLos márgenes (20–30% en fases iniciales) absorben incertidumbres. Superar el presupuesto de masa del lanzador obliga a negociar entre subsistemas, con impacto directo en capacidad y costo de misión."}],
                     "questions": [
                         {"q": "El margen en el presupuesto de masa sirve para:", "options": {"A": "absorber incertidumbres de diseño", "B": "aumentar el costo", "C": "reemplazar estructura", "D": "reducir potencia"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Dan espacio ante crecimientos durante desarrollo."},
                         {"q": "El triángulo del proyecto combina:", "options": {"A": "costo, tiempo y alcance", "B": "masa, potencia y órbita", "C": "energía, calor y señal", "D": "lanzamiento, órbita y reentrada"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Compromisos entre costo, plazo y resultados."},
                         {"q": "El presupuesto de potencia balancea:", "options": {"A": "generación, almacenamiento y consumo", "B": "masa y combustible", "C": "antenas y datos", "D": "solo iluminación"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Cada fase de la misión tiene su balance energético."},
                     ]},
                ],
            },
            "ss02": {
                "code": "SS02", "name": "Potencia y Electrónica Espacial", "name_en": "Spacecraft Power & Electronics",
                "desc": "Paneles solares, baterías, regulación de potencia y electrónica robusta en el entorno espacial.",
                "credits": 5, "prereq": "ss01", "required": 70, "color": "#f9a8d4",
                "modules": [
                    {"id": "l3_ss02_m1", "name": "Generación solar",
                     "lessons": [
                         {"title": "Celdas fotovoltaicas",
                          "body": "Las celdas de silicio o multiunión (GaAs) convierten la luz en electricidad. La potencia de salida depende de la irradiancia solar (1367 W/m²) y el ángulo de incidencia.\n\nLa irradiancia decrece con 1/r²; las misiones lejanas usan paneles concentrados o RTG. La curva I-V de la celda define el punto de máxima potencia (MPPT) que el regulador debe perseguir."}],
                     "questions": [
                         {"q": "La constante solar en la Tierra es del orden de:", "options": {"A": "1367 W/m²", "B": "500 W/m²", "C": "50 W/m²", "D": "0 W/m²"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Flujo solar en la distancia Tierra-Sol."},
                         {"q": "El MPPT busca operar la celda en:", "options": {"A": "el punto de máxima potencia", "B": "el de máxima corriente", "C": "el de máxima temperatura", "D": "el mínimo voltaje"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Maximizar el producto V×I."},
                         {"q": "En misiones a Júpiter, la generación solar es menos viable por:", "options": {"A": "la menor irradiancia (1/r²)", "B": "el exceso de luz", "C": "la alta radiación extra", "D": "la gravedad"}, "answer": "A", "difficulty": "basic",
                          "explanation": "La luz se reduce con el cuadrado de la distancia."},
                     ]},
                    {"id": "l3_ss02_m2", "name": "Baterías",
                     "lessons": [
                         {"title": "Almacenamiento orbital",
                          "body": "En la sombra, la nave depende de baterías. Las de iones de litio dominan por densidad de energía y ciclos. La profundidad de descarga (DOD) y el ciclo limitan la vida.\n\nLa gestión de la batería (BMS) controla carga, voltaje y temperatura por celda. El dimensionado de baterías cubre el peor eclipse con el DOD permitido."}],
                     "questions": [
                         {"q": "La batería de una nave en LEO se usa principalmente durante:", "options": {"A": "la sombra", "B": "el día solar", "C": "el lanzamiento", "D": "el amanecer"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Sin Sol no hay generación instantánea."},
                         {"q": "Un mayor DOD en cada ciclo:", "options": {"A": "reduce la vida útil de la batería", "B": "aumenta la vida", "C": "no influye", "D": "dobla la capacidad"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Descargas profundas acortan los ciclos."},
                         {"q": "El BMS controla principalmente:", "options": {"A": "carga, voltaje y temperatura por celda", "B": "la órbita", "C": "las antenas", "D": "los paneles térmicos"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Seguridad y balance de celdas."},
                     ]},
                    {"id": "l3_ss02_m3", "name": "Regulación y radiación",
                     "lessons": [
                         {"title": "Reguladores y dureza a la radiación",
                          "body": "El bus de potencia (típicamente 28 V) reparte energía regulada a los subsistemas; los reguladores conmutados (buck/boost) mantienen el voltaje estable con alta eficiencia.\n\nLa radiación degrada componentes: dosis total ionizante (TID) y efectos de evento único (SEE). Los dispositivos con endurecimiento (rad-hard), la redundancia y el blindaje protegen la electrónica del entorno espacial."}],
                     "questions": [
                         {"q": "El bus de potencia típico de un satélite es:", "options": {"A": "28 V", "B": "220 V AC", "C": "5 V solo", "D": "1000 V"}, "answer": "A", "difficulty": "basic",
                          "explanation": "El estándar espacial clásico de voltaje DC."},
                         {"q": "El TID mide:", "options": {"A": "la dosis total de radiación ionizante acumulada", "B": "el tiempo de órbita", "C": "la potencia de pico", "D": "el tamaño del panel"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Degrada parámetros eléctricos con el tiempo."},
                         {"q": "Un evento de efecto singular (SEE) puede provocar:", "options": {"A": "errores o daño en lógica", "B": "cambio de órbita", "C": "mayor generación", "D": "sobrecalentamiento solar"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Partículas energéticas alteran la electrónica."},
                     ]},
                ],
            },
            "ss03": {
                "code": "SS03", "name": "Comunicaciones y Navegación", "name_en": "Communications & Navigation",
                "desc": "Enlaces satelitales, antenas, protocolos y sistemas de navegación por satélite.",
                "credits": 5, "prereq": "ss02", "required": 70, "color": "#fbcfe8",
                "modules": [
                    {"id": "l3_ss03_m1", "name": "Enlace de comunicaciones",
                     "lessons": [
                         {"title": "Presupuesto de enlace",
                          "body": "El enlace radio entre el satélite y la Tierra se analiza con el presupuesto de enlace: potencia transmitida, ganancias de antena, pérdidas de espacio libre (variando con 1/r²) y ruido del receptor.\n\nLa ecuación del enlace define la relación señal-ruido (SNR) y la tasa de datos posible. El enlace de bajada (sat-Tierra) y subida (Tierra-sat) son diseños simétricos con frecuencias distintas para evitar interferencia."}],
                     "questions": [
                         {"q": "Las pérdidas de espacio libre crecen como:", "options": {"A": "1/r²", "B": "1/r", "C": "r", "D": "log r"}, "answer": "A", "difficulty": "basic",
                          "explanation": "La potencia se reparte en una esfera de área ∝ r²."},
                         {"q": "Una mayor SNR permite:", "options": {"A": "mayor tasa de datos o menor BER", "B": "menor potencia de antena", "C": "órbitas más bajas", "D": "menos ruido siempre"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Señal clara respecto al ruido habilita tasas superiores."},
                         {"q": "El enlace de subida y el de bajada usan frecuencias distintas para:", "options": {"A": "evitar interferencia mutua", "B": "ahorrar energía", "C": "reducir masa", "D": "facilitar el enfriamiento"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Separación de bandas por duplicidad de sentido."},
                     ]},
                    {"id": "l3_ss03_m2", "name": "Antenas espaciales",
                     "lessons": [
                         {"title": "Ganancia y directividad",
                          "body": "La ganancia de una antena concentra la potencia en una dirección; una parabólica de alta ganancia enfoca el haz hacia la Tierra. La apertura efectiva relaciona ganancia y longitud de onda.\n\nEl diagrama de radiación muestra lóbulos principal y secundarios; la polarización (circular o lineal) y el seguimiento de la antena mejoran el enlace. En órbita baja, las ventanas de paso exigen apuntar y rastrear."}],
                     "questions": [
                         {"q": "Una antena de alta ganancia:", "options": {"A": "concentra la potencia en una dirección", "B": "emite isotrópicamente", "C": "absorbe el haz", "D": "funciona solo en audio"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Directividad ⟹ mayor potencia efectiva hacia la Tierra."},
                         {"q": "Los lóbulos secundarios de una antena son:", "options": {"A": "direcciones no deseadas de radiación", "B": "cables internos", "C": "reflectores", "D": "un tipo de señal"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Parte del patrón que se desea minimizar."},
                         {"q": "Para mantener el enlace durante el paso de LEO, la estación debe:", "options": {"A": "apuntar y rastrear al satélite", "B": "mantener antenas fijas", "C": "apagar transmisores", "D": "usar solo baterías"}, "answer": "A", "difficulty": "basic",
                          "explanation": "El satélite cruza rápido el cielo."},
                     ]},
                    {"id": "l3_ss03_m3", "name": "Navegación",
                     "lessons": [
                         {"title": "GNSS y trilateración",
                          "body": "Los sistemas de navegación por satélite (GPS, Galileo) determinan posición midiendo tiempos de llegada de señales de múltiples satélites.\n\nLa trilateración resuelve posición a partir de distancias conocidas a satélites con cronometría precisa; errores de reloj y de ionosfera se corrigen con multicanal y modelos. En el espacio, la navegación usa además efemérides y rastreadores de estrellas."}],
                     "questions": [
                         {"q": "La posición GNSS se calcula por:", "options": {"A": "trilateración de distancias a satélites", "B": "fuerza de gravedad", "C": "brújula sola", "D": "presión barométrica"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Tiempos de propagación a múltiples satélites."},
                         {"q": "Un reloj preciso en el receptor es crítico porque:", "options": {"A": "el error de tiempo se convierte en error de posición", "B": "las señales son analógicas", "C": "los satélites no se mueven", "D": "se usa para el audio"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Distancia = c·Δt; microsegundos de error = cientos de metros."},
                         {"q": "El sistema de navegación europeo es:", "options": {"A": "Galileo", "B": "GPS", "C": "GLONASS", "D": "BeiDou"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Galileo es el GNSS de la Unión Europea."},
                     ]},
                ],
            },
            "ss04": {
                "code": "SS04", "name": "Robótica y Sistemas Autónomos", "name_en": "Robotics & Autonomous Systems",
                "desc": "Robótica espacial, control autónomo, percepción y maniobras de acoplamiento.",
                "credits": 5, "prereq": "ss03", "required": 70, "color": "#fda4af",
                "modules": [
                    {"id": "l3_ss04_m1", "name": "Robótica espacial",
                     "lessons": [
                         {"title": "Brazos y vehículos",
                          "body": "La robótica espacial opera en ambientes y condiciones extremas: temperatura, radiación y retardo de comunicación. Los brazos manipuladores (como Canadarm) y rovers obedecen a planificadores con teleoperación.\n\nLa cinemática de un brazo usa transformaciones y matrices de cambio de base; la dinámica y el control con torque por articulación permiten manipular carga en microgravedad. La autonomía procesa percepciones y toma decisiones sin esperar la Tierra."}],
                     "questions": [
                         {"q": "El retardo de comunicación en el espacio profundo obliga a:", "options": {"A": "autonomía local", "B": "teleoperación instantánea", "C": "eliminar software", "D": "operar solo por radio AM"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Fuera de la ventana de mando directo decide el sistema."},
                         {"q": "La cinemática de un brazo manipulador describe:", "options": {"A": "posiciones y orientaciones sin fuerzas", "B": "torques necesarios", "C": "el consumo eléctrico", "D": "la masa"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Cinemática geométrica; la dinámica añade fuerzas."},
                         {"q": "Un rover en Marte usa percepción para:", "options": {"A": "navegar evitando obstáculos", "B": "modular la órbita", "C": "cargar baterías solamente", "D": "comunicarse por láser"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Sensores construyen el entorno para el planificador."},
                     ]},
                    {"id": "l3_ss04_m2", "name": "Control autónomo",
                     "lessons": [
                         {"title": "Lazos de control y sensores",
                          "body": "El control autónomo cierra el lazo con sensores (cámaras, LiDAR, inerciales), un estimador del estado y controladores que generan comandos.\n\nEl filtro de Kalman fusiona mediciones ruidosas y modelo dinámico para estimar posición y actitud; los controladores PID o basados en modelo corrigen la trayectoria. La arquitectura de decisión (deliberativa-reactiva) distribuye el comportamiento."}],
                     "questions": [
                         {"q": "El filtro de Kalman sirve para:", "options": {"A": "fusionar mediciones ruidosas y estimar estado", "B": "aumentar la potencia", "C": "comprimir datos", "D": "evitar la radiación"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Estimación óptima combinando modelo y sensores."},
                         {"q": "Un controlador PID combina:", "options": {"A": "proporcional, integral y derivativo", "B": "solo proporcional", "C": "posicional, inercial y direccional", "D": "pins, inputs y delays"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Responde al error, acumulación e inercia."},
                         {"q": "La arquitectura reactiva decide respuestas:", "options": {"A": "rápidas basadas en percepción", "B": "planificadas a largo plazo", "C": "sin sensores", "D": "solo por comunicación"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Comportamiento inmediato frente al entorno."},
                     ]},
                    {"id": "l3_ss04_m3", "name": "Acoplamiento y cercanía",
                     "lessons": [
                         {"title": "Proximidad operativa",
                          "body": "Las maniobras de aproximación final (RPO) requieren sensores de cercanía, algoritmos de guiado y control fino de la actitud y traslación.\n\nEn el delicado entorno, la sequestra relativa se estima con sensores ópticos y de rango; el control robusto mantiene al vehículo en el corredor de aproximación. El acoplamiento (docking) exige alineación, velocidad relativa cero y mecanismos de captura con amortiguación."}],
                     "questions": [
                         {"q": "Durante el docking, la velocidad relativa debe:", "options": {"A": "reducirse a casi cero", "B": "maximizarse", "C": "ser constante alta", "D": "ser nula siempre desde antes"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Un impacto controlado minimiza daños."},
                         {"q": "Los sensores de cercanía en RPO usan:", "options": {"A": "ópticos y de rango láser", "B": "solo magnetómetros", "C": "GPS terrestre", "D": "micrófonos"}, "answer": "A", "difficulty": "basic",
                          "explanation": "Cámaras y LiDAR vigilan el objetivo."},
                         {"q": "La 'proximidad operativa' (proximity ops) se refiere a:", "options": {"A": "maniobras a corta distancia entre vehículos", "B": "todo el lanzamiento", "C": "la reentrada", "D": "el control térmico"}, "answer": "A", "difficulty": "basic",
                          "explanation": "La fase de aproximación final al objetivo."},
                     ]},
                ],
            },
        },
    },
}

# ---- Enrichment layer: attach "Aplicación en ZICORE" lesson + applied question ----
try:
    from level3_extra import EXTRA_LESSONS as _EXTRA
except Exception:  # pragma: no cover - enrichment is optional
    _EXTRA = {}


def _apply_extra():
    n = 0
    for _career in LEVEL3.values():
        for _co in _career["courses"].values():
            for _m in _co["modules"]:
                _e = _EXTRA.get(_m["id"])
                if not _e:
                    continue
                if _e.get("lesson"):
                    _m.setdefault("lessons", []).append(_e["lesson"])
                if _e.get("question"):
                    _m.setdefault("questions", []).append(_e["question"])
                n += 1
    return n


APPLIED_EXTRA = _apply_extra()