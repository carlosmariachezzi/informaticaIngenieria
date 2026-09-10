import numpy as np

# Dimensiones
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Inicializar matriz
matriz = np.zeros((filas, columnas), dtype=int)

# Cargar matriz
for i in range(filas):
    for j in range(columnas):
        matriz[i, j] = int(input(f"Ingrese un entero para [{i}][{j}]: "))

# Mostrar matriz
print("Matriz ingresada:")
print(matriz)

# Recorrido por filas
print("Recorrido por filas:")

for i in range(filas):
    print(f"Fila {i}: ", end="") # end para saltar línea
    for j in range(columnas):
        print(matriz[i, j], end=" ") # end para saltar línea
    print()