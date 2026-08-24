# Resolver el sistema de ecuaciones
#  	​3x+2y−z=1
#   2x−2y+4z=−2 
#   −1x+0.5y−z=0


import numpy as np

# Matriz de coeficientes
A = np.array([[3, 2, -1],
              [2, -2, 4],
              [-1, 0.5, -1]])

# Vector de términos independientes
b = np.array([1, -2, 0])

# Resolviendo el sistema
x = np.linalg.solve(A, b)

print("Solución del sistema:")
print("x =", x[0])
print("y =", x[1])
print("z =", x[2])