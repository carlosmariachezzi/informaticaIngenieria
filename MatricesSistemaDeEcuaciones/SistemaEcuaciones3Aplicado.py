# Simulación de un sistema de masas y resortes (sistema lineal)
# Resolver un sistema tipo  𝐾 𝑥 = 𝐹
# K: matriz de rigidez (simétrica)
# x: desplazamientos
# F: fuerzas aplicadas

import numpy as np

# Matriz de rigidez (sistema de 3 masas)
K = np.array([[10, -5, 0],
              [-5, 10, -5],
              [0, -5, 5]])

# Fuerzas aplicadas
F = np.array([100, 50, 0])

# Resolviendo el sistema
x = np.linalg.solve(K, F)

print("Desplazamientos:", x)