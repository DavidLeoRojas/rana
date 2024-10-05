import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os

# Ruta del archivo
file_path = 'C:/Universidad/Simulacion/Taller#1/rana-main/rana-main/rana_numeros_propios/numeros_generados.txt'

# Verificar si el archivo existe
if os.path.exists(file_path):
    print("El archivo existe")

    # Leer los datos del archivo
    with open(file_path, 'r') as file:
        # Leer la línea y dividirla por comas
        line = file.readline().strip()  # Leer la primera línea
        datos = [float(num) for num in line.split(',')]  # Convertir cada número a float

    # Parámetros de la simulación
    num_pasos = len(datos)  # Usamos la cantidad de números generados como total de pasos
    probabilidad_adelante = 0.5  # Probabilidad de avanzar hacia adelante

    # Inicializar las posiciones
    x_coords = [0]  # Eje x (número de pasos)
    posicion = [0]  # Posición en la recta numérica (inicia en el origen)

    # Simulación de los pasos usando los datos del archivo
    for i, paso in enumerate(datos, start=1):
        # Decidir si avanza o retrocede según el valor del archivo
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
    plt.title('Simulación del movimiento de la rana en 1D (datos de archivo)')
    plt.grid(True)
    plt.show()

else:
    print("Archivo no encontrado en la ruta especificada")
