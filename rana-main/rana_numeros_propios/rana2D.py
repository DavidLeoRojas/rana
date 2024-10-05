import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os

# Ruta del archivo que contiene los pasos
file_path = 'C:/Universidad/Simulacion/Taller#1/rana-main/rana-main/rana_numeros_propios/numeros_generados.txt'
# Verificar si el archivo existe
if os.path.exists(file_path):
    print("El archivo existe")

    # Leer los pasos del archivo
    with open(file_path, 'r') as file:
        # Leer la línea y dividirla por comas
        line = file.readline().strip()  # Leer la primera línea
        steps = [float(num) for num in line.split(',')]  # Convertir cada número a float

    # Inicializar contadores para las coordenadas
    horizontalCounter = 0
    verticalCounter = 0

    # Listas para almacenar las coordenadas
    x_coords = [horizontalCounter]
    y_coords = [verticalCounter]

    n = 1 / 4  # Probabilidad por cada dirección

    # Realizar el recorrido de la rana en 2D
    for step in steps:
        if 0 < step <= n:
            verticalCounter += 1  # Subir
        elif n < step <= 2 * n:
            verticalCounter -= 1  # Bajar
        elif 2 * n < step <= 3 * n:
            horizontalCounter += 1  # Derecha
        elif 3 * n < step <= 1:
            horizontalCounter -= 1  # Izquierda

        # Registrar las coordenadas en la serie
        x_coords.append(horizontalCounter)
        y_coords.append(verticalCounter)

    # Crear el gráfico en 2D
    plt.plot(x_coords[:-1], y_coords[:-1], marker='o', color='red')  # Trazo de la rana en rojo
    plt.plot(x_coords[-1], y_coords[-1], marker='o', color='red')    # Última posición en rojo

    # Etiquetas de ejes
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')

    # Título del gráfico
    plt.title('Recorrido de la rana en 2D')

    # Mostrar el gráfico
    plt.grid(True)  # Agregar una cuadrícula para mejor visualización
    plt.show()

else:
    print("Archivo no encontrado en la ruta especificada")
