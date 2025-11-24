import matplotlib.pyplot as plt

tiempos = [15.1, 0.82]
labels = ['Código original', 'Código optimizado']

plt.figure(figsize=(8,5))
plt.bar(labels, tiempos)
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación de tiempo de ejecución")
plt.grid(axis='y')
plt.show()
