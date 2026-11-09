# ZiCore University — Sesiones por niveles (piloto: ARIT, tronco común)
# Modelo: CURSO -> NIVELES -> SESIONES (cada sesión = contenido + examen)
#   + examen final por nivel (aprobarlo otorga créditos del nivel)

SESSIONS0 = {
    "aritmetica": {
        "course_id": "aritmetica",
        "levels": [
            {
                "no": 1,
                "name": "Números y operaciones con enteros",
                "credits": 0.5,
                "sessions": [
                    {
                        "id": "l0_arit_s1", "title": "Los números enteros y la recta",
                        "body": "Los números naturales son 0, 1, 2, 3, … y surgen de contar. Los enteros agregan los negativos: …, −2, −1, 0, 1, 2, … Se representan sobre una recta numérica donde el cero divide el lado negativo (izquierda) del positivo (derecha).\n\nRegla clave: restar un número equivale a sumar su opuesto. Ejemplo: 7 − (−3) = 7 + 3 = 10. Al multiplicar o dividir: signos iguales producen positivo (5 × 6 = 30; −5 × −6 = 30); signos distintos producen negativo (−5 × 6 = −30).\n\nEl valor absoluto |x| es la distancia desde cero: |−8| = 8.",
                        "exam": [
                            {"q": "¿Cuál es el resultado de −3 − (−7)?", "options": {"A": "−10", "B": "4", "C": "−4", "D": "10"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "Restar un negativo equivale a sumar: −3 + 7 = 4."},
                            {"q": "¿Cuál es el valor de |−12| + |5|?", "options": {"A": "17", "B": "−7", "C": "7", "D": "−17"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "|−12| = 12 y |5| = 5; 12 + 5 = 17."},
                        ],
                    },
                    {
                        "id": "l0_arit_s2", "title": "Jerarquía de operaciones y reglas de signos",
                        "body": "La jerarquía de operaciones (paréntesis, exponentes, multiplicación y división, suma y resta) determina el orden:\n\n1. Paréntesis y otros agrupadores (de adentro hacia afuera).\n2. Exponentes y raíces.\n3. Multiplicación y división, de izquierda a derecha.\n4. Suma y resta, de izquierda a derecha.\n\nEjemplo: 2 + 3 × 4 = 2 + 12 = 14 (la multiplicación va primero). Con paréntesis: (2 + 3) × 4 = 5 × 4 = 20. El resultado cambia, por eso el orden importa.\n\nCombinando signos: 6 − (−2) × 3 = 6 + 6 = 12. Evalúa primero la potencia o multiplicación y luego la suma o resta.",
                        "exam": [
                            {"q": "Calcula: 6 + 2 × 5", "options": {"A": "40", "B": "16", "C": "13", "D": "30"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "Primero la multiplicación: 2 × 5 = 10; luego 6 + 10 = 16."},
                            {"q": "Calcula: (6 + 2) × 5", "options": {"A": "40", "B": "16", "C": "13", "D": "30"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "El paréntesis manda: 6 + 2 = 8; luego 8 × 5 = 40."},
                        ],
                    },
                ],
                "final": [
                    {"q": "Si a = −5 y b = −6, ¿cuánto vale a × b?", "options": {"A": "−30", "B": "30", "C": "−11", "D": "11"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "Signo negativo × signo negativo = positivo: 5 × 6 = 30."},
                    {"q": "Calcula: (−4 + 6) × 3", "options": {"A": "6", "B": "2", "C": "18", "D": "−6"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "Dentro del paréntesis: −4 + 6 = 2; luego 2 × 3 = 6."},
                    {"q": "¿Cuál es el valor de |−9| − |4|?", "options": {"A": "5", "B": "−5", "C": "13", "D": "−13"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "|−9| = 9 y |4| = 4; 9 − 4 = 5."},
                ],
            },
            {
                "no": 2,
                "name": "Fracciones",
                "credits": 1.0,
                "sessions": [
                    {
                        "id": "l0_arit_s3", "title": "Significado de fracción y equivalencia",
                        "body": "Una fracción a/b representa a partes de b partes iguales. El numerador (a) cuenta las partes; el denominador (b) indica en cuántas partes se dividió el entero. El denominador nunca puede ser cero.\n\nFracciones equivalentes: al multiplicar numerador y denominador por el mismo número distinto de cero, la fracción no cambia. Ejemplo: 1/2 = 2/4 = 3/6. Simplificar es lo inverso: dividir ambos por su máximo común divisor (MCD). Ejemplo: 8/12 = 8÷4 / 12÷4 = 2/3.",
                        "exam": [
                            {"q": "¿Cuál de estas fracciones es equivalente a 2/5?", "options": {"A": "4/10", "B": "2/10", "C": "5/2", "D": "4/5"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Multiplicando numerador y denominador por 2: 2/5 = 4/10."},
                            {"q": "Simplifica la fracción 12/18", "options": {"A": "2/3", "B": "3/4", "C": "6/9", "D": "4/6"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "MCD(12,18)=6: 12÷6 / 18÷6 = 2/3."},
                        ],
                    },
                    {
                        "id": "l0_arit_s4", "title": "Suma y resta de fracciones",
                        "body": "Suma y resta con igual denominador: se suman o restan los numeradores y se conserva el denominador. Ejemplo: 3/7 + 2/7 = 5/7.\n\nCon distinto denominador: se halla el mínimo común múltiplo (mcm) de los denominadores y se convierten las fracciones a ese denominador. Ejemplo: 1/4 + 1/6 → mcm(4,6) = 12 → 3/12 + 2/12 = 5/12.\n\nResta: 5/8 − 1/4 → mcm(8,4) = 8 → 5/8 − 2/8 = 3/8.",
                        "exam": [
                            {"q": "Calcula: 1/3 + 1/6", "options": {"A": "2/9", "B": "1/2", "C": "2/6", "D": "1/4"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "mcm(3,6)=6: 2/6 + 1/6 = 3/6 = 1/2."},
                            {"q": "Calcula: 5/8 − 1/4", "options": {"A": "3/8", "B": "4/4", "C": "5/8", "D": "1/2"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "mcm(8,4)=8: 5/8 − 2/8 = 3/8."},
                        ],
                    },
                    {
                        "id": "l0_arit_s5", "title": "Multiplicación, división y simplificación",
                        "body": "Multiplicación: numerador × numerador y denominador × denominador. Ejemplo: 2/3 × 3/4 = 6/12 = 1/2.\n\nDivisión: se multiplica la primera fracción por el recíproco de la segunda (invertir numerador y denominador). Ejemplo: 3/4 ÷ 1/2 = 3/4 × 2/1 = 6/4 = 3/2.\n\nSiempre que sea posible simplifica el resultado (divide numerador y denominador por su MCD). Ejemplo: 4/6 = 2/3.",
                        "exam": [
                            {"q": "Calcula: 2/3 × 3/4", "options": {"A": "1/2", "B": "2/3", "C": "3/4", "D": "1"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "2/3 × 3/4 = 6/12; simplificando por 6 → 1/2."},
                            {"q": "Calcula: 2/3 ÷ 4/9", "options": {"A": "3/2", "B": "8/27", "C": "4/9", "D": "6/9"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Multiplica por el recíproco: 2/3 × 9/4 = 18/12 = 3/2."},
                        ],
                    },
                ],
                "final": [
                    {"q": "Calcula: 2/5 + 3/10", "options": {"A": "7/10", "B": "1/2", "C": "3/5", "D": "5/10"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "mcm(5,10)=10: 4/10 + 3/10 = 7/10."},
                    {"q": "Calcula: 3/4 × 2/3", "options": {"A": "1/2", "B": "3/4", "C": "2/3", "D": "1"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "6/12, simplificando por 6 → 1/2."},
                    {"q": "Calcula: 3/4 ÷ 9/8", "options": {"A": "2/3", "B": "27/32", "C": "3/4", "D": "4/3"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Multiplica por el recíproco: 3/4 × 8/9 = 24/36 = 2/3."},
                ],
            },
            {
                "no": 3,
                "name": "Decimales y porcentajes",
                "credits": 1.0,
                "sessions": [
                    {
                        "id": "l0_arit_s6", "title": "Decimales y su conversión",
                        "body": "Un decimal es una fracción con denominador 10, 100, 1000…, escrita con coma. 0.75 = 75/100 = 3/4. Para convertir fracción→decimal se divide el numerador entre el denominador: 1/4 = 0.25; 3/8 = 0.375.\n\nPara convertir decimal→fracción: se escribe como fracción con potencia de 10 y se simplifica. 0.6 = 6/10 = 3/5.\n\nOperaciones con decimales: alinear comas para suma y resta; multiplicar como enteros y colocar la coma según el total de cifras decimales.",
                        "exam": [
                            {"q": "¿Cuál es el decimal equivalente a 3/8?", "options": {"A": "0.375", "B": "0.30", "C": "0.38", "D": "0.35"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "3 ÷ 8 = 0.375."},
                            {"q": "0.6 como fracción simplificada es:", "options": {"A": "3/5", "B": "2/3", "C": "1/6", "D": "5/6"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "0.6 = 6/10; simplificando por 2 → 3/5."},
                        ],
                    },
                    {
                        "id": "l0_arit_s7", "title": "Porcentajes: cálculo directo",
                        "body": "El porcentaje es una razón con denominador 100: 25% = 25/100 = 0.25. Para calcular el n% de una cantidad: cantidad × n/100. Ejemplo: 30% de 200 = 200 × 30/100 = 60.\n\nTambién se puede multiplicar la cantidad por el decimal equivalente: 30% de 200 = 200 × 0.30 = 60. El 8% de 300 = 300 × 0.08 = 24.",
                        "exam": [
                            {"q": "Calcula el 25% de 240", "options": {"A": "120", "B": "60", "C": "48", "D": "96"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "240 × 0.25 = 60."},
                            {"q": "Calcula el 8% de 300", "options": {"A": "24", "B": "30", "C": "18", "D": "240"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "300 × 0.08 = 24."},
                        ],
                    },
                    {
                        "id": "l0_arit_s8", "title": "Aplicaciones: descuentos, aumentos y cambio porcentual",
                        "body": "Descuento: se multiplica la cantidad por (1 − p/100). Si un precio de 120 tiene 20% de descuento: 120 × 0.80 = 96.\n\nAumento: se multiplica por (1 + p/100). Un precio de 80 que sube 15%: 80 × 1.15 = 92.\n\nCambio porcentual: (nuevo − original) / original × 100. Si un número pasa de 40 a 50: (10/40) × 100 = 25% de aumento.",
                        "exam": [
                            {"q": "Un producto cuesta 120 y tiene un descuento de 20%. ¿Cuánto se paga?", "options": {"A": "96", "B": "100", "C": "90", "D": "80"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "120 × (1 − 0.20) = 120 × 0.80 = 96."},
                            {"q": "Si un número aumenta de 40 a 50, ¿qué porcentaje aumentó?", "options": {"A": "25%", "B": "20%", "C": "10%", "D": "22.5%"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Cambio = 10; 10/40 × 100 = 25%."},
                        ],
                    },
                ],
                "final": [
                    {"q": "Calcula el 15% de 200", "options": {"A": "30", "B": "3", "C": "300", "D": "15"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "200 × 0.15 = 30."},
                    {"q": "Un precio de 60 tiene 10% de descuento. ¿Cuánto se paga?", "options": {"A": "54", "B": "6", "C": "50", "D": "60"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "60 × 0.90 = 54."},
                    {"q": "0.45 como porcentaje es:", "options": {"A": "45%", "B": "4.5%", "C": "0.45%", "D": "450%"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "Multiplica por 100: 0.45 × 100 = 45%."},
                ],
            },
            {
                "no": 4,
                "name": "Potencias y raíces",
                "credits": 0.5,
                "sessions": [
                    {
                        "id": "l0_arit_s9", "title": "Potencias con exponente entero",
                        "body": "aⁿ (a elevado a n) significa multiplicar a por sí misma n veces. Propiedades:\n\n• aᵐ × aⁿ = aᵐ⁺ⁿ\n• aᵐ ÷ aⁿ = aᵐ⁻ⁿ\n• (aᵐ)ⁿ = aᵐⁿ\n• (a·b)ⁿ = aⁿ·bⁿ\n• a⁰ = 1 (para a ≠ 0)\n• a⁻ⁿ = 1/aⁿ\n\nEjemplo: 2³ × 2⁴ = 2⁷ = 128. División: x⁵ ÷ x² = x³.",
                        "exam": [
                            {"q": "Calcula 2³ × 2²", "options": {"A": "64", "B": "32", "C": "16", "D": "12"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "2³ × 2² = 2⁵ = 32."},
                            {"q": "Expresa x⁵ ÷ x² como potencia", "options": {"A": "x³", "B": "x⁷", "C": "x²", "D": "x⁵"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Los exponentes se restan: x⁵⁻² = x³."},
                        ],
                    },
                    {
                        "id": "l0_arit_s10", "title": "Raíces cuadradas y potencias fraccionarias",
                        "body": "La raíz cuadrada de x es el número no negativo que elevado al cuadrado da x: √9 = 3 porque 3² = 9. √(a·b) = √a·√b cuando ambos son no negativos. Para simplificar: √50 = √(25·2) = √25·√2 = 5√2.\n\nLa raíz enésima: ⁿ√a es el número que elevado a n da a. Se relaciona con potencias fraccionarias: ⁿ√a = a^(1/n). Ejemplos: ³√8 = 2 porque 2³ = 8; ⁴√81 = 3 porque 3⁴ = 81.\n\nExponentes negativos: 3⁻² = 1/3² = 1/9.",
                        "exam": [
                            {"q": "¿Cuál es el valor de √144?", "options": {"A": "14", "B": "12", "C": "11", "D": "13"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "12² = 144."},
                            {"q": "¿Cuál es el valor de 3⁻²?", "options": {"A": "−9", "B": "1/9", "C": "1/6", "D": "−6"}, "answer": "B", "type": "multiple", "difficulty": "intermediate", "explanation": "a⁻ⁿ = 1/aⁿ: 3⁻² = 1/9."},
                        ],
                    },
                ],
                "final": [
                    {"q": "Calcula (2²)³", "options": {"A": "64", "B": "32", "C": "12", "D": "8"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "(2²)³ = 2⁶ = 64."},
                    {"q": "¿Cuánto vale ⁴√81?", "options": {"A": "3", "B": "9", "C": "27", "D": "81"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "3⁴ = 81, por lo que la raíz cuarta de 81 es 3."},
                    {"q": "Simplifica √50", "options": {"A": "5√2", "B": "25√2", "C": "2√5", "D": "10"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "√50 = √(25·2) = √25·√2 = 5√2."},
                ],
            },
        ],
    },
}