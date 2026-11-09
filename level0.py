# -*- coding: utf-8 -*-
"""ZiCore University — LEVEL 0: Zi Foundation.
Matemáticas fundamentales con progresión estricta y gates de dominio:
Aritmética → Álgebra → Geometría → Trigonometría → Pre-Cálculo.
"""

LEVEL0 = {
  "aritmetica": {
    "code": "ARIT",
    "name": "Aritmética",
    "name_en": "Arithmetic",
    "desc": "Fundamentos: números, operaciones, fracciones, decimales, porcentajes, potencias y raíces.",
    "credits": 3,
    "prereq": None,
    "required": 70,
    "color": "#38bdf8",
    "modules": [
      {
        "id": "l0_arit_m1",
        "name": "Los números enteros y la recta",
        "lessons": [
          {
            "title": "Los números enteros y la recta",
            "body": "Los números naturales son 0, 1, 2, 3, … y surgen de contar. Los enteros agregan los negativos: …, −2, −1, 0, 1, 2, … Se representan sobre una recta numérica donde el cero divide el lado negativo (izquierda) del positivo (derecha).\n\nRegla clave: restar un número equivale a sumar su opuesto. Ejemplo: 7 − (−3) = 7 + 3 = 10. Al multiplicar o dividir: signos iguales producen positivo (5 × 6 = 30; −5 × −6 = 30); signos distintos producen negativo (−5 × 6 = −30).\n\nEl valor absoluto |x| es la distancia desde cero: |−8| = 8."
          },
          {
            "title": "Ejercicios resueltos con enteros",
            "body": "Ejemplo 1: −3 − (−7). Restar un negativo equivale a sumar: −3 + 7 = 4.\n\nEjemplo 2: |−12| + |5|. El valor absoluto es la distancia desde cero: |−12| = 12 y |5| = 5; 12 + 5 = 17.\n\nEjemplo 3: a × b con a = −5 y b = −6. Signos iguales dan positivo: 5 × 6 = 30.\n\nEjemplo 4: |−9| − |4| = 9 − 4 = 5. Calcula siempre el valor absoluto antes de operar."
          },
        ],
        "questions": [
          {"q": "¿Cuál es el resultado de −3 − (−7)?", "options": {"A": "−10", "B": "4", "C": "−4", "D": "10"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "Restar un negativo equivale a sumar: −3 + 7 = 4."},
          {"q": "¿Cuál es el valor de |−12| + |5|?", "options": {"A": "17", "B": "−7", "C": "7", "D": "−17"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "|−12| = 12 y |5| = 5; 12 + 5 = 17."},
          {"q": "Si a = −5 y b = −6, ¿cuánto vale a × b?", "options": {"A": "−30", "B": "30", "C": "−11", "D": "11"}, "answer": "B", "type": "multiple", "difficulty": "intermediate", "explanation": "Signo negativo × signo negativo = positivo: 5 × 6 = 30."},
          {"q": "¿Cuál es el valor de |−9| − |4|?", "options": {"A": "5", "B": "−5", "C": "13", "D": "−13"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "|−9| = 9 y |4| = 4; 9 − 4 = 5."},
        ],
      },
      {
        "id": "l0_arit_m2",
        "name": "Jerarquía de operaciones y reglas de signos",
        "lessons": [
          {
            "title": "Jerarquía de operaciones",
            "body": "La jerarquía de operaciones (paréntesis, exponentes, multiplicación y división, suma y resta) determina el orden:\n\n1. Paréntesis y otros agrupadores (de adentro hacia afuera).\n2. Exponentes y raíces.\n3. Multiplicación y división, de izquierda a derecha.\n4. Suma y resta, de izquierda a derecha.\n\nEjemplo: 2 + 3 × 4 = 2 + 12 = 14 (la multiplicación va primero). Con paréntesis: (2 + 3) × 4 = 5 × 4 = 20. El resultado cambia, por eso el orden importa."
          },
          {
            "title": "Ejercicios resueltos con jerarquía",
            "body": "Ejemplo 1: 6 + 2 × 5. Primero la multiplicación: 2 × 5 = 10; luego 6 + 10 = 16.\n\nEjemplo 2: (6 + 2) × 5. El paréntesis manda: 6 + 2 = 8; luego 8 × 5 = 40.\n\nEjemplo 3: (−4 + 6) × 3. Dentro del paréntesis: −4 + 6 = 2; luego 2 × 3 = 6.\n\nEjemplo 4: 3 + 4 × 2 = 3 + 8 = 11. Sin paréntesis, la multiplicación siempre va primero."
          },
        ],
        "questions": [
          {"q": "Calcula: 6 + 2 × 5", "options": {"A": "40", "B": "16", "C": "13", "D": "30"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "Primero la multiplicación: 2 × 5 = 10; luego 6 + 10 = 16."},
          {"q": "Calcula: (6 + 2) × 5", "options": {"A": "40", "B": "16", "C": "13", "D": "30"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "El paréntesis manda: 6 + 2 = 8; luego 8 × 5 = 40."},
          {"q": "Calcula: (−4 + 6) × 3", "options": {"A": "6", "B": "2", "C": "18", "D": "−6"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "Dentro del paréntesis: −4 + 6 = 2; luego 2 × 3 = 6."},
          {"q": "Calcula: 3 + 4 × 2", "options": {"A": "11", "B": "14", "C": "20", "D": "10"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "4 × 2 = 8; luego 3 + 8 = 11."},
        ],
      },
      {
        "id": "l0_arit_m3",
        "name": "Significado de fracción y equivalencia",
        "lessons": [
          {
            "title": "Significado de fracción y equivalencia",
            "body": "Una fracción a/b representa a partes de b partes iguales. El numerador (a) cuenta las partes; el denominador (b) indica en cuántas partes se dividió el entero. El denominador nunca puede ser cero.\n\nFracciones equivalentes: al multiplicar numerador y denominador por el mismo número distinto de cero, la fracción no cambia. Ejemplo: 1/2 = 2/4 = 3/6. Simplificar es lo inverso: dividir ambos por su máximo común divisor (MCD). Ejemplo: 8/12 = 8÷4 / 12÷4 = 2/3."
          },
          {
            "title": "Ejercicios resueltos con equivalencia",
            "body": "Ejemplo 1: ¿equivalente a 2/5? Multiplica numerador y denominador por 2: 2/5 = 4/10.\n\nEjemplo 2: simplifica 12/18. MCD(12, 18) = 6: 12÷6 / 18÷6 = 2/3.\n\nEjemplo 3: ¿equivalente a 3/4? 3/4 = 6/8 (multiplicada por 2).\n\nEjemplo 4: 1/3 con denominador 12: multiplica por 4 → 4/12."
          },
        ],
        "questions": [
          {"q": "¿Cuál de estas fracciones es equivalente a 2/5?", "options": {"A": "4/10", "B": "2/10", "C": "5/2", "D": "4/5"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Multiplicando numerador y denominador por 2: 2/5 = 4/10."},
          {"q": "Simplifica la fracción 12/18", "options": {"A": "2/3", "B": "3/4", "C": "6/9", "D": "4/6"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "MCD(12,18) = 6: 12÷6 / 18÷6 = 2/3."},
          {"q": "¿Cuál fracción es equivalente a 3/4?", "options": {"A": "6/8", "B": "9/4", "C": "4/3", "D": "3/3"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Multiplicando numerador y denominador por 2: 3/4 = 6/8."},
          {"q": "¿Qué fracción con denominador 12 es equivalente a 1/3?", "options": {"A": "4/12", "B": "3/12", "C": "1/12", "D": "12/12"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Multiplicando por 4: 1/3 = 4/12."},
        ],
      },
      {
        "id": "l0_arit_m4",
        "name": "Suma y resta de fracciones",
        "lessons": [
          {
            "title": "Suma y resta de fracciones",
            "body": "Suma y resta con igual denominador: se suman o restan los numeradores y se conserva el denominador. Ejemplo: 3/7 + 2/7 = 5/7.\n\nCon distinto denominador: se halla el mínimo común múltiplo (mcm) de los denominadores y se convierten las fracciones a ese denominador. Ejemplo: 1/4 + 1/6 → mcm(4, 6) = 12 → 3/12 + 2/12 = 5/12.\n\nResta: 5/8 − 1/4 → mcm(8, 4) = 8 → 5/8 − 2/8 = 3/8."
          },
          {
            "title": "Ejercicios resueltos de suma y resta",
            "body": "Ejemplo 1: 1/3 + 1/6. mcm(3, 6) = 6: 2/6 + 1/6 = 3/6 = 1/2.\n\nEjemplo 2: 5/8 − 1/4. mcm(8, 4) = 8: 5/8 − 2/8 = 3/8.\n\nEjemplo 3: 2/5 + 3/10. mcm(5, 10) = 10: 4/10 + 3/10 = 7/10.\n\nEjemplo 4: 3/4 − 1/2. mcm(4, 2) = 4: 3/4 − 2/4 = 1/4. Siempre simplifica el resultado."
          },
        ],
        "questions": [
          {"q": "Calcula: 1/3 + 1/6", "options": {"A": "2/9", "B": "1/2", "C": "2/6", "D": "1/4"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "mcm(3,6)=6: 2/6 + 1/6 = 3/6 = 1/2."},
          {"q": "Calcula: 5/8 − 1/4", "options": {"A": "3/8", "B": "4/4", "C": "5/8", "D": "1/2"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "mcm(8,4)=8: 5/8 − 2/8 = 3/8."},
          {"q": "Calcula: 2/5 + 3/10", "options": {"A": "7/10", "B": "1/2", "C": "3/5", "D": "5/10"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "mcm(5,10)=10: 4/10 + 3/10 = 7/10."},
          {"q": "Calcula: 3/4 − 1/2", "options": {"A": "1/4", "B": "2/4", "C": "1/2", "D": "3/1"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "mcm(4,2)=4: 3/4 − 2/4 = 1/4."},
        ],
      },
      {
        "id": "l0_arit_m5",
        "name": "Multiplicación, división y simplificación",
        "lessons": [
          {
            "title": "Multiplicación, división y simplificación",
            "body": "Multiplicación: numerador × numerador y denominador × denominador. Ejemplo: 2/3 × 3/4 = 6/12 = 1/2.\n\nDivisión: se multiplica la primera fracción por el recíproco de la segunda (invertir numerador y denominador). Ejemplo: 3/4 ÷ 1/2 = 3/4 × 2/1 = 6/4 = 3/2.\n\nSiempre que sea posible simplifica el resultado (divide numerador y denominador por su MCD). Ejemplo: 4/6 = 2/3."
          },
          {
            "title": "Ejercicios resueltos de producto y división",
            "body": "Ejemplo 1: 2/3 × 3/4 = 6/12; simplificando por 6 → 1/2.\n\nEjemplo 2: 2/3 ÷ 4/9 = 2/3 × 9/4 = 18/12; simplificando por 6 → 3/2.\n\nEjemplo 3: 3/4 × 2/3 = 6/12 = 1/2.\n\nEjemplo 4: 3/4 ÷ 9/8 = 3/4 × 8/9 = 24/36 = 2/3."
          },
        ],
        "questions": [
          {"q": "Calcula: 2/3 × 3/4", "options": {"A": "1/2", "B": "2/3", "C": "3/4", "D": "1"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "2/3 × 3/4 = 6/12; simplificando por 6 → 1/2."},
          {"q": "Calcula: 2/3 ÷ 4/9", "options": {"A": "3/2", "B": "8/27", "C": "4/9", "D": "6/9"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Multiplica por el recíproco: 2/3 × 9/4 = 18/12 = 3/2."},
          {"q": "Calcula: 3/4 × 2/3", "options": {"A": "1/2", "B": "3/4", "C": "2/3", "D": "1"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "6/12, simplificando por 6 → 1/2."},
          {"q": "Calcula: 3/4 ÷ 9/8", "options": {"A": "2/3", "B": "27/32", "C": "3/4", "D": "4/3"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Multiplica por el recíproco: 3/4 × 8/9 = 24/36 = 2/3."},
        ],
      },
      {
        "id": "l0_arit_m6",
        "name": "Decimales y su conversión",
        "lessons": [
          {
            "title": "Decimales y su conversión",
            "body": "Un decimal es una fracción con denominador 10, 100, 1000…, escrita con coma. 0.75 = 75/100 = 3/4. Para convertir fracción→decimal se divide el numerador entre el denominador: 1/4 = 0.25; 3/8 = 0.375.\n\nPara convertir decimal→fracción: se escribe como fracción con potencia de 10 y se simplifica. 0.6 = 6/10 = 3/5.\n\nOperaciones con decimales: alinear comas para suma y resta; multiplicar como enteros y colocar la coma según el total de cifras decimales."
          },
          {
            "title": "Ejercicios resueltos con decimales",
            "body": "Ejemplo 1: 3/8 como decimal. Divide 3 ÷ 8 = 0.375.\n\nEjemplo 2: 0.6 como fracción simplificada. 0.6 = 6/10; simplificando por 2 → 3/5.\n\nEjemplo 3: 0.25 como fracción = 25/100 = 1/4 (simplifica por 25).\n\nEjemplo 4: 7/8 como decimal = 7 ÷ 8 = 0.875."
          },
        ],
        "questions": [
          {"q": "¿Cuál es el decimal equivalente a 3/8?", "options": {"A": "0.375", "B": "0.30", "C": "0.38", "D": "0.35"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "3 ÷ 8 = 0.375."},
          {"q": "0.6 como fracción simplificada es:", "options": {"A": "3/5", "B": "2/3", "C": "1/6", "D": "5/6"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "0.6 = 6/10; simplificando por 2 → 3/5."},
          {"q": "0.25 como fracción simplificada es:", "options": {"A": "1/4", "B": "2/5", "C": "25/100", "D": "1/5"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "0.25 = 25/100 = 1/4 (simplifica por 25)."},
          {"q": "Convierte 7/8 a decimal:", "options": {"A": "0.875", "B": "0.78", "C": "0.7", "D": "0.85"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "7 ÷ 8 = 0.875."},
        ],
      },
      {
        "id": "l0_arit_m7",
        "name": "Porcentajes: cálculo directo",
        "lessons": [
          {
            "title": "Porcentajes: cálculo directo",
            "body": "El porcentaje es una razón con denominador 100: 25% = 25/100 = 0.25. Para calcular el n% de una cantidad: cantidad × n/100. Ejemplo: 30% de 200 = 200 × 30/100 = 60.\n\nTambién se puede multiplicar la cantidad por el decimal equivalente: 30% de 200 = 200 × 0.30 = 60. El 8% de 300 = 300 × 0.08 = 24."
          },
          {
            "title": "Ejercicios resueltos de porcentaje",
            "body": "Ejemplo 1: 25% de 240 = 240 × 0.25 = 60.\n\nEjemplo 2: 8% de 300 = 300 × 0.08 = 24.\n\nEjemplo 3: 15% de 200 = 200 × 0.15 = 30.\n\nEjemplo 4: ¿qué porcentaje es 50 de 200? (50/200) × 100 = 25%."
          },
        ],
        "questions": [
          {"q": "Calcula el 25% de 240", "options": {"A": "120", "B": "60", "C": "48", "D": "96"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "240 × 0.25 = 60."},
          {"q": "Calcula el 8% de 300", "options": {"A": "24", "B": "30", "C": "18", "D": "240"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "300 × 0.08 = 24."},
          {"q": "Calcula el 15% de 200", "options": {"A": "30", "B": "3", "C": "300", "D": "15"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "200 × 0.15 = 30."},
          {"q": "¿Qué porcentaje de 200 es 50?", "options": {"A": "25%", "B": "50%", "C": "10%", "D": "4%"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "(50/200) × 100 = 25%."},
        ],
      },
      {
        "id": "l0_arit_m8",
        "name": "Aplicaciones: descuentos, aumentos y cambio porcentual",
        "lessons": [
          {
            "title": "Aplicaciones: descuentos, aumentos y cambio porcentual",
            "body": "Descuento: se multiplica la cantidad por (1 − p/100). Si un precio de 120 tiene 20% de descuento: 120 × 0.80 = 96.\n\nAumento: se multiplica por (1 + p/100). Un precio de 80 que sube 15%: 80 × 1.15 = 92.\n\nCambio porcentual: (nuevo − original) / original × 100. Si un número pasa de 40 a 50: (10/40) × 100 = 25% de aumento."
          },
          {
            "title": "Ejercicios resueltos de aplicación",
            "body": "Ejemplo 1: un producto cuesta 120 con 20% de descuento → 120 × (1 − 0.20) = 120 × 0.80 = 96.\n\nEjemplo 2: si un número pasa de 40 a 50, el cambio es 10; (10/40) × 100 = 25%.\n\nEjemplo 3: un precio de 60 con 10% de descuento → 60 × 0.90 = 54.\n\nEjemplo 4: un precio de 80 sube 15% → 80 × 1.15 = 92."
          },
        ],
        "questions": [
          {"q": "Un producto cuesta 120 y tiene un descuento de 20%. ¿Cuánto se paga?", "options": {"A": "96", "B": "100", "C": "90", "D": "80"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "120 × (1 − 0.20) = 120 × 0.80 = 96."},
          {"q": "Si un número aumenta de 40 a 50, ¿qué porcentaje aumentó?", "options": {"A": "25%", "B": "20%", "C": "10%", "D": "22.5%"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Cambio = 10; 10/40 × 100 = 25%."},
          {"q": "Un precio de 60 tiene 10% de descuento. ¿Cuánto se paga?", "options": {"A": "54", "B": "6", "C": "50", "D": "60"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "60 × (1 − 0.10) = 60 × 0.90 = 54."},
          {"q": "Un precio de 80 sube un 15%. ¿Cuánto cuesta ahora?", "options": {"A": "92", "B": "95", "C": "90", "D": "65"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "80 × (1 + 0.15) = 80 × 1.15 = 92."},
        ],
      },
      {
        "id": "l0_arit_m9",
        "name": "Potencias con exponente entero",
        "lessons": [
          {
            "title": "Potencias con exponente entero",
            "body": "aⁿ (a elevado a n) significa multiplicar a por sí misma n veces. Propiedades:\n\n• aᵐ × aⁿ = aᵐ⁺ⁿ\n• aᵐ ÷ aⁿ = aᵐ⁻ⁿ\n• (aᵐ)ⁿ = aᵐⁿ\n• (a·b)ⁿ = aⁿ·bⁿ\n• a⁰ = 1 (para a ≠ 0)\n• a⁻ⁿ = 1/aⁿ\n\nEjemplo: 2³ × 2⁴ = 2⁷ = 128. División: x⁵ ÷ x² = x³."
          },
          {
            "title": "Ejercicios resueltos con potencias",
            "body": "Ejemplo 1: 2³ × 2² = 2³⁺² = 2⁵ = 32.\n\nEjemplo 2: x⁵ ÷ x² = x⁵⁻² = x³.\n\nEjemplo 3: (2²)³ = 2⁶ = 64.\n\nEjemplo 4: cualquier número distinto de cero elevado a 0 es 1: 5⁰ = 1."
          },
        ],
        "questions": [
          {"q": "Calcula 2³ × 2²", "options": {"A": "64", "B": "32", "C": "16", "D": "12"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "2³ × 2² = 2⁵ = 32."},
          {"q": "Expresa x⁵ ÷ x² como potencia", "options": {"A": "x³", "B": "x⁷", "C": "x²", "D": "x⁵"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Los exponentes se restan: x⁵⁻² = x³."},
          {"q": "Calcula (2²)³", "options": {"A": "64", "B": "32", "C": "12", "D": "8"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "(2²)³ = 2⁶ = 64."},
          {"q": "¿Cuánto vale 5⁰?", "options": {"A": "1", "B": "0", "C": "5", "D": "25"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Cualquier número distinto de cero elevado a 0 es 1."},
        ],
      },
      {
        "id": "l0_arit_m10",
        "name": "Raíces cuadradas y potencias fraccionarias",
        "lessons": [
          {
            "title": "Raíces cuadradas y potencias fraccionarias",
            "body": "La raíz cuadrada de x es el número no negativo que elevado al cuadrado da x: √9 = 3 porque 3² = 9. √(a·b) = √a·√b cuando ambos son no negativos. Para simplificar: √50 = √(25·2) = √25·√2 = 5√2.\n\nLa raíz enésima: ⁿ√a es el número que elevado a n da a. Se relaciona con potencias fraccionarias: ⁿ√a = a^(1/n). Ejemplos: ³√8 = 2 porque 2³ = 8; ⁴√81 = 3 porque 3⁴ = 81.\n\nExponentes negativos: 3⁻² = 1/3² = 1/9."
          },
          {
            "title": "Ejercicios resueltos con raíces",
            "body": "Ejemplo 1: √144 = 12 porque 12² = 144.\n\nEjemplo 2: 3⁻² = 1/3² = 1/9.\n\nEjemplo 3: ⁴√81 = 3 porque 3⁴ = 81.\n\nEjemplo 4: √50 = √(25·2) = √25·√2 = 5√2. Simplifica extrayendo cuadrados perfectos."
          },
        ],
        "questions": [
          {"q": "¿Cuál es el valor de √144?", "options": {"A": "14", "B": "12", "C": "11", "D": "13"}, "answer": "B", "type": "multiple", "difficulty": "basic", "explanation": "12² = 144."},
          {"q": "¿Cuál es el valor de 3⁻²?", "options": {"A": "−9", "B": "1/9", "C": "1/6", "D": "−6"}, "answer": "B", "type": "multiple", "difficulty": "intermediate", "explanation": "a⁻ⁿ = 1/aⁿ: 3⁻² = 1/9."},
          {"q": "¿Cuánto vale ⁴√81?", "options": {"A": "3", "B": "9", "C": "27", "D": "81"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "3⁴ = 81, por lo que la raíz cuarta de 81 es 3."},
          {"q": "Simplifica √50", "options": {"A": "5√2", "B": "25√2", "C": "2√5", "D": "10"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "√50 = √(25·2) = √25·√2 = 5√2."},
        ],
      },
    ],
  },
  "algebra": {
    "code": "ALG",
    "name": "Álgebra",
    "name_en": "Algebra",
    "desc": "Variables, expresiones, ecuaciones lineales, sistemas y factorización.",
    "credits": 4,
    "prereq": "aritmetica",
    "required": 70,
    "color": "#a5b4fc",
    "modules": [
      {
        "id": "l0_alg_m1",
        "name": "Expresiones algebraicas",
        "lessons": [
          {
            "title": "Variables y términos",
            "body": "Una variable es un símbolo que representa un valor desconocido (x, y, t). Un término es el producto de un coeficiente, variables y exponentes: en 5x², el coeficiente es 5 y la variable x con exponente 2.\n\nExpresión algebraica: combinación de términos con operaciones. 3x + 2y − 7. El valor de la expresión se obtiene sustituyendo las variables. Si x = 4: 3(4) + 2y − 7 = 12 + 2y − 7 = 5 + 2y."
          },
          {
            "title": "Términos semejantes",
            "body": "Los términos semejantes tienen las mismas variables con los mismos exponentes. Solo ellos pueden sumarse o restarse. Ejemplo: 3x + 5x = 8x, pero 3x + 5x² no se pueden combinar.\n\nSimplificar una expresión es combinar los semejantes. 4x + 3 − 2x + 7 = (4x − 2x) + (3 + 7) = 2x + 10."
          },
        ],
        "questions": [
          {"q": "¿Cuál es el valor de 3x + 5 cuando x = 7?", "options": {"A": "26", "B": "21", "C": "16", "D": "35"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "3(7) + 5 = 21 + 5 = 26."},
          {"q": "Simplifica: 5x + 3 − 2x + 8", "options": {"A": "3x + 11", "B": "7x + 11", "C": "3x − 5", "D": "7x + 5"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Agrupa semejantes: (5x − 2x) + (3 + 8) = 3x + 11."},
          {"q": "¿Cuánto vale la expresión 2a² − 3a + 1 si a = −1?", "options": {"A": "6", "B": "0", "C": "−6", "D": "4"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "2(1) − 3(−1) + 1 = 2 + 3 + 1 = 6."},
          {"q": "¿Cuál de las siguientes es una propiedad distributiva correcta?", "options": {"A": "a(b + c) = ab + ac", "B": "a(b + c) = ab + c", "C": "a + (b × c) = (a + b)(a + c)", "D": "a(bc) = ab + c"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "La distributividad: multiplicar afuera por cada término dentro."},
        ],
      },
      {
        "id": "l0_alg_m2",
        "name": "Ecuaciones de primer grado",
        "lessons": [
          {
            "title": "Concepto y soluciones",
            "body": "Una ecuación es una igualdad entre dos expresiones con una incógnita. Resolver es encontrar el valor de la incógnita que hace verdadera la igualdad.\n\nReglas de transformación: puedes sumar/restar el mismo número a ambos lados, y multiplicar/dividir ambos lados por el mismo número distinto de cero.\n\nEjemplo: 2x + 3 = 11. Resta 3: 2x = 8. Divide entre 2: x = 4. Comprobación: 2(4) + 3 = 11 ✓."
          },
          {
            "title": "Ecuaciones con variables en ambos lados",
            "body": "Cuando la incógnita aparece en ambos lados, agrupa los términos con la variable en un lado y las constantes en el otro.\n\nEjemplo: 5x + 4 = 2x + 16. Resta 2x: 3x + 4 = 16. Resta 4: 3x = 12. Divide: x = 4. Comprobación: 5(4)+4 = 24 y 2(4)+16 = 24 ✓."
          },
        ],
        "questions": [
          {"q": "Resuelve: x + 7 = 15", "options": {"A": "8", "B": "22", "C": "−8", "D": "7"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "x = 15 − 7 = 8."},
          {"q": "Resuelve: 3x = 27", "options": {"A": "9", "B": "24", "C": "81", "D": "6"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "x = 27 ÷ 3 = 9."},
          {"q": "Resuelve: 2x − 5 = 13", "options": {"A": "9", "B": "4", "C": "18", "D": "8"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "2x = 18, x = 9."},
          {"q": "Resuelve: 4x + 3 = 2x + 11", "options": {"A": "4", "B": "7", "C": "3.5", "D": "2"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "4x − 2x = 11 − 3 → 2x = 8 → x = 4."},
        ],
      },
      {
        "id": "l0_alg_m3",
        "name": "Sistemas de ecuaciones",
        "lessons": [
          {
            "title": "Sustitución",
            "body": "Un sistema de ecuaciones es un conjunto de dos o más ecuaciones con las mismas incógnitas. Resolverlo es hallar los valores que satisfacen todas a la vez.\n\nMétodo de sustitución: despeja una variable en una ecuación y sustitúyela en la otra.\n\nEjemplo:\ny = 2x\nx + y = 9\nSustituyendo: x + 2x = 9 → 3x = 9 → x = 3, y = 6."
          },
          {
            "title": "Reducción (suma y resta)",
            "body": "Método de reducción: suma o resta las ecuaciones para eliminar una variable.\n\nEjemplo:\nx + y = 10\nx − y = 4\nSumando: 2x = 14 → x = 7. Sustituyendo en la primera: 7 + y = 10 → y = 3."
          },
        ],
        "questions": [
          {"q": "Resuelve el sistema: y = 3x; x + y = 16", "options": {"A": "x=4, y=12", "B": "x=3, y=9", "C": "x=5, y=15", "D": "x=4, y=4"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "x + 3x = 16 → x = 4, y = 12."},
          {"q": "Resuelve: x + y = 12; x − y = 2", "options": {"A": "x=7, y=5", "B": "x=5, y=7", "C": "x=6, y=6", "D": "x=8, y=4"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "Suma: 2x = 14 → x = 7, y = 5."},
          {"q": "¿Cuál es la solución del sistema 2x + y = 7 y x − y = 2?", "options": {"A": "x=3, y=1", "B": "x=2, y=3", "C": "x=1, y=3", "D": "x=4, y=−1"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Suma: 3x = 9 → x = 3; 2(3)+y=7 → y = 1."},
          {"q": "En el sistema x + y = 8 y 2x − y = 4, ¿cuánto vale y?", "options": {"A": "4", "B": "2", "C": "6", "D": "3"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Suma: 3x = 12 → x = 4; y = 8 − 4 = 4."},
        ],
      },
      {
        "id": "l0_alg_m4",
        "name": "Productos notables y factorización",
        "lessons": [
          {
            "title": "Productos notables",
            "body": "Identidades que se deben reconocer de inmediato:\n\n• (a + b)² = a² + 2ab + b²\n• (a − b)² = a² − 2ab + b²\n• (a + b)(a − b) = a² − b²\n\nEjemplo: (x + 5)² = x² + 10x + 25."
          },
          {
            "title": "Factorización",
            "body": "Factorizar es escribir una expresión como producto de factores.\n\nFactor común: 6x + 9 = 3(2x + 3).\n\nDiferencia de cuadrados: a² − b² = (a + b)(a − b). Ejemplo: x² − 25 = (x + 5)(x − 5).\n\nTrinomio de la forma x² + bx + c: busca dos números que sumen b y multipliquen c. x² + 7x + 12 = (x + 3)(x + 4)."
          },
        ],
        "questions": [
          {"q": "Desarrolla (x + 3)²", "options": {"A": "x² + 9", "B": "x² + 6x + 9", "C": "x² + 3x + 9", "D": "x² + 6x"}, "answer": "B", "type": "multiple", "difficulty": "intermediate", "explanation": "(a+b)² = a² + 2ab + b²: x² + 6x + 9."},
          {"q": "Factoriza x² − 49", "options": {"A": "(x+7)(x−7)", "B": "(x−7)²", "C": "(x+7)²", "D": "x(x−49)"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Diferencia de cuadrados: (x+7)(x−7)."},
          {"q": "Extrae el factor común de 15x + 25", "options": {"A": "5(3x + 5)", "B": "3(5x + 25)", "C": "5(3x − 5)", "D": "25(x + 1)"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "MCD(15,25) = 5 → 5(3x + 5)."},
          {"q": "Factoriza x² + 9x + 20", "options": {"A": "(x+4)(x+5)", "B": "(x+10)(x+2)", "C": "(x+5)(x+4) y también", "D": "(x−4)(x−5)"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Dos números que sumen 9 y multipliquen 20: 4 y 5."},
        ],
      },
    ],
  },
  "geometria": {
    "code": "GEO",
    "name": "Geometría",
    "name_en": "Geometry",
    "desc": "Ángulos, triángulos, Pitágoras, áreas, perímetros y volúmenes.",
    "credits": 4,
    "prereq": "algebra",
    "required": 75,
    "color": "#fbbf24",
    "modules": [
      {
        "id": "l0_geo_m1",
        "name": "Puntos, rectas y ángulos",
        "lessons": [
          {
            "title": "Elementos fundamentales",
            "body": "En geometría plana los objetos básicos son el punto, la recta y el plano. Dos rectas pueden ser paralelas (no se cruzan), secantes (se cruzan) o perpendiculares (se cruzan formando 90°).\n\nUn ángulo se forma por dos rayos con un vértice común. Se mide en grados: un ángulo recto mide 90°, uno llano 180° y uno completo 360°."
          },
          {
            "title": "Relaciones entre ángulos",
            "body": "Ángulos complementarios suman 90°. Ángulos suplementarios suman 180°.\n\nDos rectas que se cruzan forman ángulos opuestos por el vértice que son iguales. Cuando una recta transversal corta dos paralelas, los ángulos correspondientes son iguales y los alternos internos también.\n\nLos ángulos interiores de un triángulo suman 180°, y los de un cuadrilátero 360°."
          },
        ],
        "questions": [
          {"q": "Dos ángulos son complementarios; uno mide 35°. ¿Cuánto mide el otro?", "options": {"A": "55°", "B": "65°", "C": "145°", "D": "25°"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "90 − 35 = 55°."},
          {"q": "Dos ángulos son suplementarios; uno mide 110°. ¿Cuál es el otro?", "options": {"A": "70°", "B": "80°", "C": "90°", "D": "60°"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "180 − 110 = 70°."},
          {"q": "En un triángulo dos ángulos miden 45° y 60°. ¿Cuánto mide el tercero?", "options": {"A": "75°", "B": "85°", "C": "95°", "D": "65°"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "180 − 45 − 60 = 75°."},
          {"q": "Un ángulo congruente a uno de 68° es:", "options": {"A": "68°", "B": "22°", "C": "112°", "D": "92°"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Congruente significa igual medida."},
        ],
      },
      {
        "id": "l0_geo_m2",
        "name": "Triángulos y teorema de Pitágoras",
        "lessons": [
          {
            "title": "Clasificación y propiedades",
            "body": "Según sus lados, un triángulo es equilátero (3 lados iguales), isósceles (2 iguales) o escaleno (todos distintos). Según sus ángulos: acutángulo (todos < 90°), rectángulo (tiene un ángulo de 90°) u obtusángulo (uno > 90°).\n\nLa desigualdad triangular: la suma de dos lados siempre es mayor que el tercero."
          },
          {
            "title": "Teorema de Pitágoras",
            "body": "En un triángulo rectángulo, el cuadrado de la hipotenusa (lado opuesto al ángulo recto, c) es igual a la suma de los cuadrados de los catetos (a y b):\n\nc² = a² + b²\n\nEjemplo: si a = 3 y b = 4, entonces c² = 9 + 16 = 25 → c = 5. La terna (3, 4, 5) es una terna pitagórica."
          },
        ],
        "questions": [
          {"q": "Un triángulo tiene catetos de 6 y 8. ¿Cuánto mide la hipotenusa?", "options": {"A": "10", "B": "12", "C": "14", "D": "9"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "√(36+64) = √100 = 10."},
          {"q": "El área de un triángulo con base 10 y altura 6 es:", "options": {"A": "30", "B": "60", "C": "16", "D": "45"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "A = b·h/2 = 10·6/2 = 30."},
          {"q": "¿Un triángulo con lados 5, 12, 13 es rectángulo?", "options": {"A": "Sí, porque 5²+12²=13²", "B": "No", "C": "Solo si es equilátero", "D": "Depende de los ángulos"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "25 + 144 = 169 = 13². Terna pitagórica."},
          {"q": "En un triángulo isósceles los lados iguales miden 5 y la base 8. ¿Cuál es su altura?", "options": {"A": "3", "B": "4", "C": "5", "D": "6"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "La altura divide la base: h² = 5² − 4² = 25 − 16 = 9 → h = 3."},
        ],
      },
      {
        "id": "l0_geo_m3",
        "name": "Áreas y perímetros",
        "lessons": [
          {
            "title": "Perímetro y área de figuras planas",
            "body": "El perímetro es la suma de todos los lados. El área mide la superficie.\n\n• Rectángulo: P = 2(b + h), A = b·h\n• Cuadrado: P = 4l, A = l²\n• Triángulo: A = b·h/2\n• Círculo: perímetro (circunferencia) C = 2πr, área A = πr². π ≈ 3.1416.\n\nEjemplo: rectángulo de 8×3 → A = 24, P = 22."
          },
          {
            "title": "Áreas compuestas",
            "body": "Para figuras irregulares, divide en figuras conocidas y suma sus áreas. Por ejemplo, una figura con un rectángulo y un semicírculo encima: A = área del rectángulo + (πr²)/2."
          },
        ],
        "questions": [
          {"q": "El área de un rectángulo de 9 × 4 es:", "options": {"A": "36", "B": "26", "C": "13", "D": "40"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "A = b·h = 9·4 = 36."},
          {"q": "El perímetro de un cuadrado de lado 7 es:", "options": {"A": "28", "B": "49", "C": "14", "D": "21"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "P = 4·7 = 28."},
          {"q": "El área de un círculo de radio 3 (π=3.14) es:", "options": {"A": "28.26", "B": "18.84", "C": "9.42", "D": "31.4"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "A = πr² = 3.14·9 = 28.26."},
          {"q": "Un triángulo tiene área 24 y base 8. ¿Cuál es su altura?", "options": {"A": "6", "B": "3", "C": "12", "D": "4"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "h = 2A/b = 48/8 = 6."},
        ],
      },
      {
        "id": "l0_geo_m4",
        "name": "Volúmenes",
        "lessons": [
          {
            "title": "Cuerpos geométricos",
            "body": "El volumen mide el espacio que ocupa un cuerpo.\n\n• Cubo: V = l³\n• Prisma rectangular: V = b·h·p (largo × ancho × alto)\n• Cilindro: V = πr²·h\n• Esfera: V = (4/3)πr³\n• Cono: V = (1/3)πr²·h\n\nEjemplo: cilindro de radio 2 y altura 5 → V = 3.14·4·5 = 62.8."
          },
          {
            "title": "Unidades de volumen",
            "body": "El volumen se mide en unidades cúbicas (cm³, m³) o en litros: 1 dm³ = 1 L. Para convertir entre unidades cúbicas se multiplica por 1000 por cada nivel (1 m³ = 1000 L).\n\nPrisma con base triangular: V = Área de la base × altura del prisma."
          },
        ],
        "questions": [
          {"q": "El volumen de un cubo de lado 4 es:", "options": {"A": "64", "B": "16", "C": "12", "D": "48"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "V = 4³ = 64."},
          {"q": "El volumen de un cilindro de radio 2 y altura 10 (π=3.14) es:", "options": {"A": "125.6", "B": "62.8", "C": "40", "D": "31.4"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "V = πr²h = 3.14·4·10 = 125.6."},
          {"q": "Una prisma rectangular mide 5 × 3 × 2. Su volumen es:", "options": {"A": "30", "B": "10", "C": "60", "D": "15"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "V = 5·3·2 = 30."},
          {"q": "El volumen de una esfera de radio 3 (π=3) es:", "options": {"A": "108", "B": "36", "C": "27", "D": "84"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "V = (4/3)πr³ = (4/3)·3·27 = 108."},
        ],
      },
    ],
  },
  "trigonometria": {
    "code": "TRIG",
    "name": "Trigonometría",
    "name_en": "Trigonometry",
    "desc": "Razones trigonométricas, identidades, leyes de senos y cosenos, funciones y ecuaciones.",
    "credits": 4,
    "prereq": "geometria",
    "required": 75,
    "color": "#f87171",
    "modules": [
      {
        "id": "l0_trig_m1",
        "name": "Razones trigonométricas",
        "lessons": [
          {
            "title": "Razones en el triángulo rectángulo",
            "body": "Para un ángulo agudo θ en un triángulo rectángulo:\n\n• sen(θ) = cateto opuesto / hipotenusa\n• cos(θ) = cateto adyacente / hipotenusa\n• tan(θ) = cateto opuesto / adyacente = sen/cos\n\nOtra identidad: sen²(θ) + cos²(θ) = 1.\n\nValores notables: sen(30°)=1/2, cos(60°)=1/2, sen(45°)=cos(45°)=√2/2 ≈ 0.707, tan(45°)=1."
          },
          {
            "title": "Cálculo de lados y ángulos",
            "body": "Con una razón trigonométrica y un dato puedes hallar lo demás. Ejemplo: en un triángulo rectángulo con hipotenusa 10 y ángulo 30°, el cateto opuesto es 10·sen(30°) = 10·0.5 = 5.\n\nPara hallar el ángulo se usa la función inversa: θ = sen⁻¹(opuesto/hipotenusa)."
          },
        ],
        "questions": [
          {"q": "sen(30°) vale:", "options": {"A": "1/2", "B": "√3/2", "C": "1/√2", "D": "1"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "sen(30°) = 1/2."},
          {"q": "cos(60°) vale:", "options": {"A": "1/2", "B": "√2/2", "C": "√3", "D": "0"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "cos(60°) = 1/2."},
          {"q": "Si tan(θ) = 1, θ vale (en grados):", "options": {"A": "45°", "B": "30°", "C": "60°", "D": "90°"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "tan(45°) = 1."},
          {"q": "En un triángulo rectángulo, hipotenusa = 13 y cateto opuesto = 5. ¿Cuánto vale sen(θ)?", "options": {"A": "5/13", "B": "12/13", "C": "13/5", "D": "5/12"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "sen(θ) = opuesto/hipotenusa = 5/13."},
        ],
      },
      {
        "id": "l0_trig_m2",
        "name": "Identidades fundamentales",
        "lessons": [
          {
            "title": "Identidades pitagóricas",
            "body": "Las tres identidades pitagóricas:\n\n• sen²(x) + cos²(x) = 1\n• 1 + tan²(x) = sec²(x)\n• 1 + cot²(x) = csc²(x)\n\nDesde la primera, si conoces sen(x) puedes hallar cos(x): cos(x) = √(1 − sen²(x))."
          },
          {
            "title": "Identidades recíprocas",
            "body": "Las razones recíprocas:\n\n• csc(x) = 1/sen(x)\n• sec(x) = 1/cos(x)\n• cot(x) = 1/tan(x) = cos(x)/sen(x)\n\nEstas identidades permiten simplificar expresiones trigonométricas complejas sustituyendo cada función por su forma equivalente."
          },
        ],
        "questions": [
          {"q": "Si sen(x) = 3/5, ¿cuánto vale cos(x) (ángulo agudo)?", "options": {"A": "4/5", "B": "2/5", "C": "5/4", "D": "3/4"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "cos² = 1 − sen² = 1 − 9/25 = 16/25 → cos = 4/5."},
          {"q": "sec(x) es igual a:", "options": {"A": "1/cos(x)", "B": "1/sen(x)", "C": "1/tan(x)", "D": "cos(x)"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "La secante es el recíproco del coseno."},
          {"q": "La identidad sen²(x) + cos²(x) es igual a:", "options": {"A": "1", "B": "0", "C": "tan(x)", "D": "2"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Es la identidad pitagórica fundamental."},
          {"q": "cot(x) equivale a:", "options": {"A": "cos(x)/sen(x)", "B": "sen(x)/cos(x)", "C": "1/sen(x)", "D": "1/cos(x)"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "La cotangente es el recíproco de la tangente."},
        ],
      },
      {
        "id": "l0_trig_m3",
        "name": "Ley de senos y de cosenos",
        "lessons": [
          {
            "title": "Ley de senos",
            "body": "En cualquier triángulo, la razón entre un lado y el seno de su ángulo opuesto es constante:\n\na/sen(A) = b/sen(B) = c/sen(C)\n\nÚtil cuando conoces dos ángulos y un lado (AAL)."
          },
          {
            "title": "Ley de cosenos",
            "body": "Para resolver triángulos cuando conoces dos lados y el ángulo entre ellos (LAL) o los tres lados (LLL):\n\nc² = a² + b² − 2ab·cos(C)\n\nEs una generalización del teorema de Pitágoras: si C = 90°, cos(C) = 0 y queda c² = a² + b²."
          },
        ],
        "questions": [
          {"q": "Ley de senos: a/sen(A) = ?", "options": {"A": "b/sen(B)", "B": "a·sen(B)", "C": "cos(B)", "D": "2ab"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "Todas las razones lado/seno(ángulo opuesto) son iguales."},
          {"q": "La ley de cosenos c² = a² + b² − 2ab·cos(C) se deduce del teorema de Pitágoras cuando:", "options": {"A": "C = 90°", "B": "C = 0°", "C": "C = 180°", "D": "A = 90°"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "cos(90°) = 0, por lo que queda c² = a² + b²."},
          {"q": "Para usar la ley de cosenos necesitas:", "options": {"A": "Dos lados y el ángulo entre ellos", "B": "Dos ángulos y un lado", "C": "Solo los tres ángulos", "D": "Un lado y un ángulo"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "La ley de cosenos usa tres lados o dos lados + ángulo incluido."},
          {"q": "La ley de senos es más directa cuando conoces:", "options": {"A": "Dos ángulos y un lado", "B": "Dos lados y el ángulo entre ellos", "C": "Tres lados", "D": "El perímetro"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Con dos ángulos y un lado aplicas directamente las proporciones."},
        ],
      },
      {
        "id": "l0_trig_m4",
        "name": "Funciones trigonométricas",
        "lessons": [
          {
            "title": "Funciones y sus propiedades",
            "body": "Las funciones trigonométricas son periódicas. El seno y el coseno tienen período 360° (2π rad): sen(x + 360°) = sen(x).\n\n• Dominio de sen y cos: todos los reales; rango [−1, 1].\n• La tangente tiene asíntotas donde cos(x) = 0 (90°, 270°…).\n• sen es impar (sen(−x) = −sen(x)), cos es par (cos(−x) = cos(x))."
          },
          {
            "title": "Gráficas",
            "body": "La gráfica de sen(x) es una onda que parte de 0, sube a 1 en 90°, baja a 0 en 180°, llega a −1 en 270° y vuelve a 0 en 360°. La de cos(x) parte de 1 (es la de seno desplazada 90°).\n\nAmplitud A en y = A·sen(x) estira verticalmente; el período se modifica en y = sen(k·x), siendo 360°/k."
          },
        ],
        "questions": [
          {"q": "El rango de sen(x) es:", "options": {"A": "[−1, 1]", "B": "(0, 1)", "C": "Todos los reales", "D": "[0, ∞)"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "El seno solo toma valores entre −1 y 1."},
          {"q": "sen(360°) es igual a:", "options": {"A": "0", "B": "1", "C": "−1", "D": "0.5"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Un ciclo completo vuelve a 0."},
          {"q": "El período de sen(2x) es (en grados):", "options": {"A": "180°", "B": "360°", "C": "90°", "D": "720°"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Período = 360°/k = 360°/2 = 180°."},
          {"q": "cos(0°) vale:", "options": {"A": "1", "B": "0", "C": "−1", "D": "0.5"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "La función coseno parte de 1 en 0°."},
        ],
      },
    ],
  },
  "precalculo": {
    "code": "PREC",
    "name": "Pre-Cálculo",
    "name_en": "Pre-Calculus",
    "desc": "Funciones, línea recta, cuadráticas, exponenciales, logaritmos y puente hacia el límite.",
    "credits": 4,
    "prereq": "trigonometria",
    "required": 80,
    "color": "#34d399",
    "modules": [
      {
        "id": "l0_prec_m1",
        "name": "Funciones",
        "lessons": [
          {
            "title": "Concepto de función",
            "body": "Una función f asigna a cada entrada x exactamente una salida f(x). Se escribe f: x ↦ f(x). El dominio es el conjunto de entradas permitidas; el rango, el de salidas.\n\nUna función debe pasar el test de la recta vertical: ninguna recta vertical corta su gráfica más de una vez.\n\nLa composición: (f ∘ g)(x) = f(g(x)). Ejemplo: f(x) = x², g(x) = x + 1 → f(g(x)) = (x+1)²."
          },
          {
            "title": "Evaluar y graficar",
            "body": "Ejemplo: f(x) = 2x − 3. f(4) = 2(4) − 3 = 5. La gráfica es una recta con pendiente 2 e intersección en y = −3.\n\nFunción par: f(−x) = f(x) (simétrica respecto al eje y). Función impar: f(−x) = −f(x) (simétrica respecto al origen)."
          },
        ],
        "questions": [
          {"q": "Si f(x) = 3x − 2, calcula f(5)", "options": {"A": "13", "B": "17", "C": "10", "D": "15"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "f(5) = 3(5) − 2 = 15 − 2 = 13."},
          {"q": "El dominio de f(x) = 1/(x − 2) excluye:", "options": {"A": "x = 2", "B": "x = 0", "C": "x = −2", "D": "x = 1"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "El denominador no puede ser cero: x − 2 = 0 → x = 2."},
          {"q": "Si f(x) = x² y g(x) = 2x, ¿cuánto vale f(g(3))?", "options": {"A": "36", "B": "18", "C": "12", "D": "6"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "g(3) = 6; f(6) = 36."},
          {"q": "El valor de f(0) cuando f(x) = 4 − x² es:", "options": {"A": "4", "B": "0", "C": "−4", "D": "16"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "4 − 0 = 4."},
        ],
      },
      {
        "id": "l0_prec_m2",
        "name": "Función lineal y cuadrática",
        "lessons": [
          {
            "title": "Función lineal",
            "body": "La función lineal es f(x) = mx + b. m es la pendiente (razón de cambio) y b la ordenada al origen (valor en x = 0).\n\nPendiente entre dos puntos: m = (y₂ − y₁)/(x₂ − x₁). Si m > 0 crece; si m < 0 decrece; si m = 0 es constante.\n\nEjemplo: f(x) = 2x + 1 pasa por (0,1) y crece 2 unidades por cada unidad horizontal."
          },
          {
            "title": "Función cuadrática",
            "body": "La función cuadrática es f(x) = ax² + bx + c, con a ≠ 0. Su gráfica es una parábola. Si a > 0 abre hacia arriba; si a < 0 hacia abajo.\n\nEl vértice (máximo o mínimo) está en x = −b/(2a). Sus raíces (si existen) se hallan con la fórmula cuadrática: x = [−b ± √(b² − 4ac)]/(2a). El discriminante b² − 4ac indica si hay 2, 1 o 0 raíces reales."
          },
        ],
        "questions": [
          {"q": "La pendiente de la recta que pasa por (1, 3) y (4, 9) es:", "options": {"A": "2", "B": "3", "C": "1", "D": "6"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "m = (9−3)/(4−1) = 6/3 = 2."},
          {"q": "El vértice de f(x) = x² − 4x + 1 está en x =", "options": {"A": "2", "B": "−2", "C": "4", "D": "1"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "x = −b/(2a) = 4/2 = 2."},
          {"q": "Las raíces de x² − 5x + 6 = 0 son:", "options": {"A": "2 y 3", "B": "1 y 6", "C": "−2 y −3", "D": "2 y −3"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "(x−2)(x−3)=0."},
          {"q": "La parábola f(x) = 3x² + 2x + 1 abre hacia:", "options": {"A": "Arriba", "B": "Abajo", "C": "No abre", "D": "Lateral"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "a = 3 > 0 → abre hacia arriba."},
        ],
      },
      {
        "id": "l0_prec_m3",
        "name": "Exponenciales y logaritmos",
        "lessons": [
          {
            "title": "Función exponencial",
            "body": "f(x) = a·bˣ con b > 0, b ≠ 1. Si b > 1 crece (crecimiento exponencial); si 0 < b < 1 decrece (decaimiento). El caso b = e ≈ 2.71828 es la base natural usada en ciencia e ingeniería.\n\nPropiedades: b⁰ = 1, b¹ = b, bˣ·bʸ = bˣ⁺ʸ.\n\nEjemplo: f(x) = 2ˣ: f(0)=1, f(1)=2, f(3)=8."
          },
          {
            "title": "Logaritmos",
            "body": "El logaritmo es la función inversa del exponente: log_b(x) = y si y solo si bʸ = x.\n\nPropiedades:\n• log(xy) = log(x) + log(y)\n• log(x/y) = log(x) − log(y)\n• log(xⁿ) = n·log(x)\n• log(1) = 0, log(b) = 1\n\nEl logaritmo natural ln(x) usa base e. Ejemplo: log₁₀(1000) = 3 porque 10³ = 1000."
          },
        ],
        "questions": [
          {"q": "log₁₀(100) es igual a:", "options": {"A": "2", "B": "10", "C": "100", "D": "1"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "10² = 100."},
          {"q": "El valor de 2⁴ es:", "options": {"A": "16", "B": "8", "C": "12", "D": "6"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "2·2·2·2 = 16."},
          {"q": "log₂(32) vale:", "options": {"A": "5", "B": "4", "C": "6", "D": "16"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "2⁵ = 32."},
          {"q": "¿Cuál es el dominio de f(x) = ln(x)?", "options": {"A": "x > 0", "B": "x ≥ 0", "C": "Todos los reales", "D": "x ≠ 0"}, "answer": "A", "type": "multiple", "difficulty": "intermediate", "explanation": "El logaritmo solo existe para argumentos positivos."},
        ],
      },
      {
        "id": "l0_prec_m4",
        "name": "Introducción a límites",
        "lessons": [
          {
            "title": "Idea de límite",
            "body": "El límite de f(x) cuando x tiende a a, escrito lim[x→a] f(x), es el valor al que se acerca f(x) conforme x se acerca a a (sin necesidad de que f(a) exista).\n\nEjemplo: lim[x→2] (x² − 4)/(x − 2). Aunque en x = 2 hay indeterminación 0/0, al factorizar: (x−2)(x+2)/(x−2) = x + 2, y lim = 4.\n\nLímites notables: lim[x→0] sen(x)/x = 1; lim [x→∞] 1/x = 0."
          },
          {
            "title": "Propiedades y continuidad",
            "body": "Propiedades: lim(f + g) = lim f + lim g; lim(f·g) = lim f · lim g; lim(k·f) = k·lim f.\n\nUna función es continua en a si lim[x→a] f(x) = f(a). Las funciones polinomiales son continuas en todo R.\n\nEl límite lateral por la izquierda y por la derecha deben coincidir para que exista el límite."
          },
        ],
        "questions": [
          {"q": "lim[x→3] (x + 2) es:", "options": {"A": "5", "B": "3", "C": "6", "D": "4"}, "answer": "A", "type": "multiple", "difficulty": "basic", "explanation": "Sustitución directa: 3 + 2 = 5."},
          {"q": "lim[x→0] sen(x)/x es:", "options": {"A": "1", "B": "0", "C": "∞", "D": "No existe"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Límite trigonométrico fundamental = 1."},
          {"q": "lim[x→2] (x² − 4)/(x − 2) vale:", "options": {"A": "4", "B": "0", "C": "2", "D": "No existe"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Factoriza: (x+2)(x−2)/(x−2) = x+2 → 4."},
          {"q": "Para que exista lim[x→a] f(x) es necesario que:", "options": {"A": "Los límites laterales coincidan", "B": "f(a) exista", "C": "f sea creciente", "D": "f(a) = 0"}, "answer": "A", "type": "multiple", "difficulty": "advanced", "explanation": "Límite por izquierda = límite por derecha."},
        ],
      },
    ],
  },
}

SEQUENCE = ["aritmetica", "algebra", "geometria", "trigonometria", "precalculo"]