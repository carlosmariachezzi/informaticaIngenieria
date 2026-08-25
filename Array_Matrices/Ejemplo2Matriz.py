# Cargar una matriz con numpy.zeros() y sin listas
import numpy as np

# Dimensiones
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Crear matriz de ceros
matriz = np.zeros((filas, columnas), dtype=int)

# Cargar valores
for i in range(filas):
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor en posición [{i}, {j}]: "))
        matriz[i, j] = valor

# Mostrar matriz
print("Matriz ingresada:")
print(matriz)