import numpy as np

import numpy as np

M = np.array([
    [1, 2, 1],
    [2, 4, 6],
    [3, 6, 2]
])

# 1. Calcular el rango de la matriz
rango = np.linalg.matrix_rank(M)
print("1. Rango de la matriz:")
print(rango)


# 2. Calcular el determinante
determinante = np.linalg.det(M)
print("2. Determinante:")
print(determinante)


# 3. Determinar si los vectores son independientes o dependientes
if rango == M.shape[0]:
    print("Los vectores son linealmente independientes.")
else:
    print("Los vectores son linealmente dependientes.")


# 4. Justificación

print("4. Justificación:")

if rango == M.shape[0]:
    print("El rango es igual a la cantidad de vectores.")
    print("Rango:", rango)
    print("Cantidad de vectores:", M.shape[0])
    print("Por lo tanto, los vectores son linealmente independientes.")
else:
    print("El rango es menor que la cantidad de vectores.")
    print("Rango:", rango)
    print("Cantidad de vectores:", M.shape[0])
    print("Por lo tanto, los vectores son linealmente dependientes.")