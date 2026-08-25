# 3 ¿Cómo definir una matriz en tamaño y tipo de dato?
# Se presentan distintos ejemplos y el resultado de ejecución del script

import numpy as np

# 1.- Definir una matriz de 3 filas y 4 columnas
matriz = np.zeros((3, 4))  # 3 filas, 4 columnas
print(matriz)

# 2.- Definir una matriz y asignale a cada celda el valor 7
matriz = np.full((2, 3), 7, dtype=int)  # 2x3 con todos los valores = 7
print(matriz)

# 3.- Definir una matriz identidad de 4 filas y 4 columnas
matriz = np.eye(4, dtype=int)  # Matriz identidad 4x4
print(matriz)

# 4.- Definir una matriz de datos lógicos de  3 filas y 3 columnas
matriz_bool = np.ones((3, 3), dtype=bool)  # Matriz 3x3 con True
print(matriz_bool)

# 5.- Definir una matriz de datos tipo fecha de  2 filas y 2 columnas
matriz_fechas = np.full((2, 2), '2025-09-05', dtype='datetime64[D]')
print(matriz_fechas)

# 6.- Definir una matriz de datos tipo string de 2x3 de cadenas vacías ('') con espacio para hasta 20 caracteres 
matriz_str = np.full((2, 3), '', dtype='U20') # U20 = Unicode string de hasta 20 caracteres
print(matriz_str)
