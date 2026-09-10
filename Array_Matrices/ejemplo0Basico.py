import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Suma por colummas los datos de la matriz")
print(A.sum(axis=0))  # [12 15 18]

print("Suma por filas los datos de la matriz")
print(A.sum(axis=1))  # [ 6 15 24]

print("Promedio por colummas los datos de la matriz")
print(A.mean(axis=0))  # [4. 5. 6.]

print("Promedio por filas los datos de la matriz")
print(A.mean(axis=1))  # [2. 5. 8.]

print("Máximo por colummas los datos de la matriz")
print(A.max(axis=0))  # [7 8 9]

print("Máximo por filas los datos de la matriz")
print(A.max(axis=1))  # [3 6 9]

print("Mínimo por colummas los datos de la matriz")
print(A.min(axis=0))  # [1 2 3]

print("Mínimo por filas los datos de la matriz")
print(A.min(axis=1))  # [1 4 7]