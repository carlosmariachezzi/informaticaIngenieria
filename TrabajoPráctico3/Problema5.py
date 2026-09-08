import numpy as np

# Cargamos las matrices complejas

A = np.array([
    [1 + 2j, 3 - 1j],
    [2j, -1 + 4j]
], dtype=complex)


B = np.array([
    [2 - 1j, 1 + 3j],
    [-2, 4j]
], dtype=complex)


print("Matriz A:")
print(A)

print("Matriz B:")
print(B)


# 1. Suma de matrices A + B

suma = A + B

print("1. Suma de matrices A + B:")
print(suma)


# 2. Producto matricial A · B

producto = A @ B

print("2. Producto matricial A · B:")
print(producto)


# 3. Transpuesta de A

transpuesta_A = A.T

print("3. Transpuesta de A:")
print(transpuesta_A)