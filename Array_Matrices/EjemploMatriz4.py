# Cargar matriz de str (caracteres) usando NumPy (dtype=str)
import numpy as np

# Dimensiones
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Inicializar matriz con cadenas vacías
matriz = np.full((filas, columnas), '', dtype=str)

# Cargar datos
for i in range(filas):
    for j in range(columnas):
        valor = input(f"Ingrese una palabra para [{i}, {j}]: ")
        matriz[i, j] = valor

# Mostrar la matriz
print("Matriz ingresada:")
print(matriz)