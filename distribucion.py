import matplotlib.pyplot as plt

funciones = ['es_primo()', 'append()', 'time()', 'otras']
porcentajes = [92, 5, 1, 2]

plt.figure(figsize=(8,5))
plt.pie(porcentajes, labels=funciones, autopct='%1.1f%%')
plt.title("Distribución del tiempo por función (cProfile)")
plt.show()
