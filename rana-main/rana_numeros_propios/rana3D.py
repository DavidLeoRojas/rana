import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importar la herramienta para gráficos 3D
import os

# Ruta del archivo que contiene los pasos
file_path = 'C:/Universidad/Simulacion/Taller#1/rana-main/rana-main/rana_numeros_propios/numeros_generados.txt'

# Verificar si el archivo existe
if os.path.exists(file_path):
    print("El archivo existe")

    # Leer los pasos del archivo
    with open(file_path, 'r') as file:
        line = file.readline().strip()  # Leer la primera línea
        steps = [float(num) for num in line.split(',')]  # Convertir cada número a float

    # Inicializar contadores para las coordenadas
    horizontalCounter = 0
    verticalCounter = 0
    depthCounter = 0  # Nuevo contador para la dimensión Z

    # Listas para almacenar las coordenadas
    x_coords = [horizontalCounter]
    y_coords = [verticalCounter]
    z_coords = [depthCounter]  # Lista para la dimensión Z

    n = 1 / 6  # Probabilidad por cada dirección (ajustado para 6 direcciones)

    # Realizar el recorrido de la rana en 3D
    for step in steps:
        if 0 < step <= n:
            verticalCounter += 1  # Subir en Y
        elif n < step <= 2 * n:
            verticalCounter -= 1  # Bajar en Y
        elif 2 * n < step <= 3 * n:
            horizontalCounter += 1  # Derecha en X
        elif 3 * n < step <= 4 * n:
            horizontalCounter -= 1  # Izquierda en X
        elif 4 * n < step <= 5 * n:
            depthCounter += 1  # Adelante en Z
        elif 5 * n < step <= 1:
            depthCounter -= 1  # Atrás en Z

        # Registrar las coordenadas en la serie
        x_coords.append(horizontalCounter)
        y_coords.append(verticalCounter)
        z_coords.append(depthCounter)

    # Crear el gráfico en 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # Crear un subplot 3D

    # Trazo de la rana en morado
    ax.plot(x_coords, y_coords, z_coords, marker='o', color='purple')

    # Etiquetas de ejes
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    # Título del gráfico
    ax.set_title('Recorrido de la rana en 3D')

    # Mostrar el gráfico
    plt.grid(True)  # Agregar una cuadrícula para mejor visualización
    plt.show()

else:
    print("Archivo no encontrado en la ruta especificada")
