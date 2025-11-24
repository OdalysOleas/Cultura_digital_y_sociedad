import numpy as np
import time
import math

def es_primo_np(n):
    if n < 2:
        return False

    limite = int(math.sqrt(n))  # raíz cuadrada
    divisores = np.arange(2, limite + 1)  # genera números del 2 al límite pero en NumPy

    return not np.any(n % divisores == 0)

inicio = time.time()

numeros = np.arange(1, 100001)  # vector de 1 a 100000
primos = [n for n in numeros if es_primo_np(n)]

fin = time.time()
print("Tiempo optimizado:", fin - inicio, "segundos")
