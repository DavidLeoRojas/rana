import matplotlib.pyplot as plt
import random
from matplotlib.ticker import MaxNLocator

# Parámetros de la simulación
num_pasos = 1000  # Número total de pasos a simular
probabilidad_adelante = 0.5  # Probabilidad de avanzar hacia adelante

# Inicializar las posiciones
x_coords = [0]  # Eje x (número de pasos)
posicion = [0]  # Posición en la recta numérica (inicia en el origen)

# Simulación de los pasos
for i in range(1, num_pasos + 1):
    paso = random.random()  # Generar un número aleatorio entre 0 y 1
    
    # Decidir si avanza o retrocede
    if paso < probabilidad_adelante:
        nueva_posicion = posicion[-1] + 1  # Avanza
    else:
        nueva_posicion = posicion[-1] - 1  # Retrocede
    
    # Registrar los datos de la simulación
    x_coords.append(i)
    posicion.append(nueva_posicion)

# Crear el gráfico 1D
plt.plot(x_coords, posicion, marker='o')

# Etiquetas de ejes
plt.xlabel('Número de pasos')
plt.ylabel('Posición en la recta numérica')

# Alinear los marcadores de los ejes y asegurarse de que sean números enteros
ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

# Mostrar el gráfico
plt.title('Simulación del movimiento de la rana en 1D')
plt.grid(True)
plt.show()