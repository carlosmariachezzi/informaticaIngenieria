# Resolver el sistema de ecuaciones
#  2x1​+x2​=5
#  x1​+3x2​=10​
# resuelve un sistema de ecuaciones lineales de la forma:
# 𝐾 ⋅ 𝑥 = 𝐹
# K: es una matriz cuadrada de coeficientes (por ejemplo, matriz de rigidez en problemas mecánicos).
# F: es un vector columna (o array unidimensional en NumPy), que representa los términos independientes (como fuerzas aplicadas).
# x: es el vector solución, que contiene las incógnitas (como desplazamientos, corrientes, temperaturas, etc.).

import numpy as np

K = np.array([[2, 1],
              [1, 3]])

F = np.array([5, 10])

x = np.linalg.solve(K, F)

print("Solución del sistema:")
print("x1 =", x[0])
print("x2 =", x[1])