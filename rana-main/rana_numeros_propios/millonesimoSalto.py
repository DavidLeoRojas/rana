import random
import matplotlib.pyplot as plt

# Inicializar la posición
position = 0
positions = [position]

# Simulación del movimiento de la rana
n_saltos = 1000000
for _ in range(n_saltos):
    salto = random.choice([-1, 1])  # La rana puede saltar hacia adelante (+1) o hacia atrás (-1)
    position += salto
    positions.append(position)

# Graficar el movimiento de la rana
plt.plot(positions)
plt.xlabel('Número de saltos')
plt.ylabel('Posición en la recta')
plt.title('Simulación del movimiento de la rana hasta 1,000,000 saltos')
plt.grid(True)
plt.show()
