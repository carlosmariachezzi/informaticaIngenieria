import numpy as np

# Definimos las matrices
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print("Matriz A:")
print(A)

print("Matriz B:")
print(B)


# 1. Determinar si es posible realizar A · B

# Obtenemos las dimensiones de las matrices
filas_A, columnas_A = A.shape
filas_B, columnas_B = B.shape

print("1. ¿Es posible realizar A · B?")

# Para multiplicar matrices:
# La cantidad de columnas de A debe ser igual
# a la cantidad de filas de B.

if columnas_A == filas_B:
    print("Sí, es posible realizar A · B.")
    print("A tiene dimensiones:", A.shape)
    print("B tiene dimensiones:", B.shape)
else:
    print("No es posible realizar A · B.")
    print("La cantidad de columnas de A no coincide")
    print("con la cantidad de filas de B.")


# 2. Calcular A · B
if columnas_A == filas_B:
    AB = A @ B

    print("2. Resultado de A · B:")
    print(AB)

    print("Dimensiones de la matriz resultante:")
    print(AB.shape)


# 3. Calcular B · A
if columnas_B == filas_A:
    BA = B @ A

    print("3. Resultado de B · A:")
    print(BA)

    print("Dimensiones de la matriz resultante:")
    print(BA.shape)
else:
    print("3. No es posible realizar B · A.")

# 4. Comparar ambos resultados
print("4. Comparación:")
print("A · B tiene dimensiones:", AB.shape)
print("B · A tiene dimensiones:", BA.shape)

print("Los resultados son diferentes porque:")
print("- A · B es una matriz 2x2.")
print("- B · A es una matriz 3x3.")
print("- En general, la multiplicación de matrices NO es conmutativa.")
print("Por lo tanto, A · B es distinto B · A.")