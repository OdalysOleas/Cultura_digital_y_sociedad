# Optimización de código y medición de tiempos

## Introducción

En esta actividad se trabajó con un programa en Python que calcula los números primos entre 1 y 100 000.  
El código original usa una función es_primo(n) que revisa si un número es primo probando todos los divisores desde 2 hasta n-1.  
Después recorre todo el rango y va guardando los primos en una lista.

El programa funciona, pero tarda bastante.  
En las primeras pruebas el tiempo de ejecución fue de unos **15.1 segundos**, lo cual es alto para un rango que no es tan grande.  
Por eso se decidió buscar formas de optimizar el código y medir de forma más precisa los tiempos que se obtienen antes y después de los cambios.

## Optimización realizada

Los cambios principales que se aplicaron al código fueron:

1. **Revisión de divisores solo hasta la raíz cuadrada de n**

   En la función es_primo(n) ya no se revisan divisores hasta n-1, sino solo hasta int(sqrt(n)).  
   Si un número no tiene divisores menores o iguales a su raíz cuadrada, se puede considerar primo.  
   Esto reduce bastante el número de divisiones que se hacen en cada llamada.

2. **Uso de NumPy para las comprobaciones**

   Se usó la librería **NumPy** para crear arreglos de posibles divisores y hacer las operaciones de forma vectorizada.  
   NumPy está optimizado en C, por lo que estas operaciones son más rápidas que un bucle for puro en Python.

3. **Pequeñas mejoras de estilo**

   - Se organizaron mejor las funciones.  
   - Se limpiaron algunas partes del código para que sea más fácil de leer.  
   - Se siguieron algunas recomendaciones básicas de PEP 8 (nombres de variables, sangrías, etc.).

Con estos ajustes se buscó que el programa sea más rápido, pero manteniendo el mismo resultado (lista de números primos en el mismo rango).

## Resultados

### 1. Tiempos de ejecución

Las mediciones se hicieron con el módulo time:

- **Código original:** tiempo de ejecución = **15.1 segundos**.  
- **Código optimizado:** tiempo de ejecución entre **0.6 y 0.8 segundos** (según la corrida).

Con esto, el código optimizado es mucho más rápido.  
La mejora es de alrededor de un **95 % del tiempo**, es decir, el programa corre unas **20 veces más rápido** que la versión inicial.
En el **gráfico de barras** generado con Matplotlib se ve claramente esta diferencia: la barra del código original es muy alta y la del código optimizado es casi mínima en comparación.

### 2. Análisis con cProfile

También se usó **cProfile** para ver en qué funciones se estaba gastando más tiempo.

En el código original se observó que:

- La función es_primo() ocupa alrededor del **92 % del tiempo total** del programa.  
- La operación append() sobre la lista de primos usa cerca de un **5 %**.  
- El resto del tiempo se reparte entre las llamadas a time() y otras funciones internas (alrededor de un 3 %).
Con el gráfico de pastel se ve que casi todo el círculo corresponde a es_primo().  
Esto confirma que esa función era el principal cuello de botella y que ahí tenía sentido aplicar la optimización.
Después de hacer los cambios, la función es_primo() sigue siendo la que más tiempo usa, pero como el algoritmo interno es más eficiente, el tiempo total del programa baja bastante.

### 3. Gráficos generados

Se crearon dos figuras con Matplotlib:

1. **Gráfico de pastel** con la distribución del tiempo de ejecución por función (datos de `cProfile`).
   <img width="886" height="631" alt="image" src="https://github.com/user-attachments/assets/04cbc7e1-195e-46ae-9daa-8c699395052c" />

2. **Gráfico de barras** comparando el tiempo del código original y el código optimizado.
   <img width="886" height="629" alt="image" src="https://github.com/user-attachments/assets/e8f84b93-d8cf-4611-ba8c-68ca51946749" />

Estos gráficos ayudan a entender mejor dónde se está gastando el tiempo y a mostrar de forma visual el impacto de la optimización.

## Conclusiones

- El código original era correcto, pero no estaba pensado para rendimiento en rangos grandes.  
- El cambio más importante fue limitar las pruebas de divisores hasta la raíz cuadrada de cada número, lo que redujo mucho el número de operaciones.  
- El uso de NumPy y algunas mejoras de estilo también aportaron a que el código sea más rápido y ordenado.  
- Gracias a estas modificaciones, el tiempo de ejecución pasó de unos 15 segundos a menos de 1 segundo, lo cual es una mejora muy grande.  
- Herramientas como cProfile y Matplotlib fueron útiles para comprobar de manera objetiva dónde se estaba perdiendo tiempo y cómo cambió el rendimiento después de optimizar.  
- Finalmente, todo el trabajo se versionó con **Git y GitHub**, creando una rama de trabajo para la optimización, haciendo los *commits* correspondientes y luego un *pull request* para integrar los cambios a la rama principal.

---

## Anexos  
<img width="886" height="588" alt="image" src="https://github.com/user-attachments/assets/b3e97bc3-f0ed-4948-8ee5-2c1cfdca722f" />

<img width="886" height="423" alt="image" src="https://github.com/user-attachments/assets/bf507536-ed37-41a8-96ac-81f1f2b5fb1b" />

<img width="1891" height="923" alt="b8f20c13-014c-4cae-83cb-2c3c6df9a814" src="https://github.com/user-attachments/assets/b5852d83-7405-4749-b357-f5e1fd80f28b" />

<img width="1095" height="579" alt="image" src="https://github.com/user-attachments/assets/f1e5075e-5da3-4dc9-95c2-e4380f8a47bd" />

<img width="1919" height="833" alt="6cf5dfa5-8948-4dce-9f35-50998fefda9a" src="https://github.com/user-attachments/assets/89883757-4d22-4b5e-9a48-d44bf893229f" />

<img width="1919" height="930" alt="3cfe666b-1037-4512-a897-e060ad91ddfb" src="https://github.com/user-attachments/assets/9180fc75-5ae0-4077-a2a9-d843d22d261e" />

<img width="1088" height="547" alt="image" src="https://github.com/user-attachments/assets/26d41351-03ca-4659-8fba-5b2066466c2d" />


**Enlace al repositorio en GitHub:**  

https://github.com/OdalysOleas/Cultura_digital_y_sociedad
