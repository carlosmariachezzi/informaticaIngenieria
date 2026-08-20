# Cargar una matriz con validación (try/except)
import numpy as np

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
matriz = np.zeros((filas, columnas), dtype=float)

for i in range(filas):
    for j in range(columnas):
        while True:
            try:
                valor = float(input(f"Ingrese un número para [{i}][{j}]: "))
                matriz[i, j] = valor
                break
            except ValueError:
                print("Dato inválido. Ingrese un número decimal.")

print("Matriz resultante:")
print(matriz)