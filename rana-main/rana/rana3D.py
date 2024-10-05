import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importar para gráficos en 3D
import random

# Generar 1000 pasos aleatorios
steps = [random.random() for _ in range(1000)]  # 1000 pasos aleatorios entre 0 y 1

# Inicializar contadores para las coordenadas
x_counter = 0
y_counter = 0
z_counter = 0  # Nueva coordenada Z para 3D

# Listas para almacenar las coordenadas
x_coords = [x_counter]
y_coords = [y_counter]
z_coords = [z_counter]  # Coordenadas Z

n = 1 / 6  # Probabilidad por cada dirección (ahora hay 6 direcciones posibles en 3D)

# Realizar el recorrido de la rana en 3D
for step in steps:
    if 0 < step <= n:
        y_counter += 1  # Subir (en el eje Y)
    elif n < step <= 2 * n:
        y_counter -= 1  # Bajar (en el eje Y)
    elif 2 * n < step <= 3 * n:
        x_counter += 1  # Derecha (en el eje X)
    elif 3 * n < step <= 4 * n:
        x_counter -= 1  # Izquierda (en el eje X)
    elif 4 * n < step <= 5 * n:
        z_counter += 1  # Adelante (en el eje Z)
    elif 5 * n < step <= 1:
        z_counter -= 1  # Atrás (en el eje Z)

    # Registrar las coordenadas en la serie
    x_coords.append(x_counter)
    y_coords.append(y_counter)
    z_coords.append(z_counter)

# Crear la figura y el gráfico en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # Gráfico 3D

# Trazar el recorrido de la rana en 3D
ax.plot(x_coords[:-1], y_coords[:-1], z_coords[:-1], marker='o', color='purple')  # Línea en rojo
ax.scatter(x_coords[-1], y_coords[-1], z_coords[-1], color='purple', s=100)  # Última posición en rojo

# Etiquetas de ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Título del gráfico
ax.set_title('Recorrido de la rana en 3D')

# Mostrar el gráfico
plt.show()
