## Optimización de código y medición de tiempos

## Introducción

El objetivo de esta actividad fue aplicar técnicas de optimización y buenas prácticas de programación para mejorar la eficiencia de un código en Python que calcula los números primos en el rango de 1 a 100 000.  

El código original implementa una función `es_primo(n)` que verifica si un número es primo utilizando un bucle que recorre todos los enteros desde 2 hasta `n - 1`. Después, se recorre el rango completo y se van agregando a una lista todos los números que resultan primos.  

Aunque el algoritmo es correcto, presenta dos problemas principales:

- **Alta complejidad temporal**: para cada número `n` se realizan hasta `n` operaciones de división, lo cual es muy costoso cuando el rango llega hasta 100 000.
- **Uso poco eficiente de estructuras y librerías**: se utiliza únicamente una lista y bucles simples, sin aprovechar herramientas como comprensiones de listas o librerías optimizadas (por ejemplo, NumPy).

Por estos motivos, el tiempo de ejecución del código original fue de aproximadamente **15.1 segundos**, lo que evidencia la necesidad de optimizarlo.

---

## Optimización realizada

Para mejorar el rendimiento se aplicaron varias técnicas de optimización:

1. **Reducción del rango del bucle en `es_primo(n)`**

   En lugar de comprobar divisores desde 2 hasta `n - 1`, se modificó la función para iterar solo hasta la **raíz cuadrada de `n`**.  
   Matemáticamente, si un número `n` no tiene divisores menores o iguales a `√n`, entonces es primo.  

   Esto reduce drásticamente el número de operaciones necesarias y disminuye la complejidad del algoritmo.

2. **Uso de comprensiones de listas**

   Se utilizaron comprensiones de listas para hacer más compacta y eficiente la creación de listas de divisores y/o de números primos, en lugar de bucles `for` tradicionales con `append()`.  
   Esto sigue las buenas prácticas de Python (PEP 8) y suele ofrecer un mejor rendimiento.

3. **Uso de NumPy**

   Se introdujo la librería **NumPy** para trabajar con **arrays** y operaciones vectorizadas.  
   NumPy está implementado en C y permite realizar cálculos numéricos de forma mucho más rápida que los bucles puros en Python.  
   En este caso, se utilizaron arrays de posibles divisores y operaciones vectorizadas para comprobar si un número tiene divisores.

Gracias a estas optimizaciones, el tiempo de ejecución se redujo de manera significativa.

---

## Resultados

### 1. Comparación de tiempos de ejecución

Se midieron los tiempos con la biblioteca `time` antes y después de la optimización:

- **Código original**:  
  Tiempo de ejecución ≈ **15.1 segundos**.

- **Código optimizado**:  
  Tiempo de ejecución ≈ **0.6–0.8 segundos**.

En el gráfico de barras generado con Matplotlib se observa que la barra del código original es mucho mayor que la del código optimizado. Esto muestra de forma visual que el tiempo se redujo aproximadamente en un **95 %**, es decir, el código optimizado es alrededor de **20 veces más rápido**.
<img width="886" height="631" alt="image" src="https://github.com/user-attachments/assets/5e4e0864-9883-4bde-b00e-8eb09dea469d" />

### 2. Análisis de `cProfile`

Se utilizó `cProfile` para identificar las funciones que más tiempo consumen.

En el **código original**:

- La función **`es_primo()`** concentra alrededor del **92 % del tiempo total**.
- La operación **`append()`** sobre la lista de primos representa aproximadamente un **5 %**.
- El resto del tiempo se reparte entre las llamadas a `time()` y otras funciones internas del intérprete (≈3 %).

En el gráfico de pastel se aprecia claramente que `es_primo()` ocupa la mayor parte del círculo, confirmando que es el principal cuello de botella del programa.
<img width="886" height="629" alt="image" src="https://github.com/user-attachments/assets/0e100842-7e74-4593-aeea-be3526719ba1" />

Después de la optimización, aunque `es_primo()` sigue siendo la función más relevante, el tiempo total disminuye de forma notable, lo que demuestra que las mejoras implementadas fueron efectivas.

---

## Conclusiones

- La versión original del código, aunque correcta, no era eficiente para rangos grandes debido al uso de un algoritmo con demasiadas operaciones por número.
- Al aplicar técnicas de optimización como:
  - limitar el recorrido de los divisores hasta la **raíz cuadrada de `n`**,
  - utilizar **comprensiones de listas**, y
  - aprovechar las **operaciones vectorizadas de NumPy**,  
  se consiguió una reducción aproximada del **95 % en el tiempo de ejecución**.

- El uso de **`cProfile`** permitió identificar objetivamente la función `es_primo()` como el principal cuello de botella y guiar el proceso de optimización.
- La generación de gráficos con **Matplotlib** facilitó la comparación visual de tiempos y la distribución del uso de CPU por función, haciendo más claro el impacto de las mejoras.
- Finalmente, el uso de **Git y GitHub** (creación de rama, commits y *pull request* de `optimizacion-codigo`) permitió llevar un control de versiones ordenado y profesional del proyecto.

Como recomendación para futuros desarrollos en Ciencia de Datos:

- Siempre medir tiempos y usar herramientas de profiling antes de optimizar.
- Aprovechar librerías numéricas como NumPy y Pandas.
- Mantener buenas prácticas de programación (PEP 8) y uso de control de versiones con Git.
