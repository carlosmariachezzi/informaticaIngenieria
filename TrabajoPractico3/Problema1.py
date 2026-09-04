import numpy as np

# Creamos las matrices en base a listas
A = np.array([
    [2, 1, -1],
    [4, 2,  0],
    [2, 3,  1]
])

B = np.array([
    [1, 2, 1],
    [2, 4, 3],
    [1, 1, 2]
])

# 1. Calcular A - B y B + A
resta = A - B
suma_matrices = B + A

print("1. A - B:")
print(resta)

print("1. B + A:")
print(suma_matrices)


# 2. Calcular el producto A · B
producto = A @ B

print("2. Producto A · B:")
print(producto)


# 3. Calcular la transpuesta de A y B
transpuesta_A = A.T
transpuesta_B = B.T

print("3. Transpuesta de A:")
print(transpuesta_A)

print("Transpuesta de B:")
print(transpuesta_B)


# 4. Calcular la suma de todos los elementos
suma_A = np.sum(A)
suma_B = np.sum(B)

print("4. Suma de todos los elementos:")
print("Suma de A:", suma_A)
print("Suma de B:", suma_B)


# 5. Obtener el máximo y mínimo de cada matriz
max_A = np.max(A)
min_A = np.min(A)

max_B = np.max(B)
min_B = np.min(B)

print("5. Máximo y mínimo:")
print("A -> Máximo:", max_A, "Mínimo:", min_A)
print("B -> Máximo:", max_B, "Mínimo:", min_B)