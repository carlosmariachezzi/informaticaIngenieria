import numpy as np

# Definimos las matrices

A = np.array([
    [2, 6],
    [1, 3]
])

B = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])

C = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [0, 1, 5]
])


print("Matriz A:")
print(A)

print("Matriz B:")
print(B)

print("Matriz C:")
print(C)


# 1. Calcular su determinante

det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
det_C = np.linalg.det(C)

print("1. Determinantes:")

print("Determinante de A:", det_A)
print("Determinante de B:", det_B)
print("Determinante de C:", det_C)


# 2. Determinar si posee inversa
# Una matriz tiene inversa si su determinante es distinto de 0.

print("2. Determinar si poseen inversa:")

if det_A != 0:
    print("A posee inversa.")
    
    inversa_A = np.linalg.inv(A)
    print("La inversa de A es:")
    print(inversa_A)
else:
    print("A no posee inversa porque su determinante es 0.")


if det_B != 0:
    print("B posee inversa.")
    
    inversa_B = np.linalg.inv(B)
    print("La inversa de B es:")
    print(inversa_B)
else:
    print("B no posee inversa porque su determinante es 0.")


if det_C != 0:
    print("C posee inversa.")
    
    inversa_C = np.linalg.inv(C)
    print("La inversa de C es:")
    print(inversa_C)
else:
    print("C no posee inversa porque su determinante es 0.")


# 3. Verificar el resultado calculando A · A^-1

if det_A != 0:

    identidad = A @ inversa_A

    print("3. Verificación A · A^-1:")
    print(identidad)

    print("La matriz obtenida debería ser la matriz identidad.")