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
# shape devuelve la cantidad de filas y columnas de una matriz
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
    # 2. Calcular A · B
    AB = A @ B
    print("2. Resultado de A · B:")
    print(AB)
    print("Dimensiones de la matriz resultante:")
    print(AB.shape)
else:
    print("No es posible realizar A · B.")
    print("La cantidad de columnas de A no coincide")
    print("con la cantidad de filas de B.")

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
# Se evalua si es posible hacer el producto de matrices. Si esto es posible evalua si A.B = B.A
print("4. Comparación:")

if columnas_A == filas_B and columnas_B == filas_A:
    if np.array_equal(AB, BA):
        print("A · B es igual a B · A.")
    else:
        print("A · B es diferente de B · A.")
else:
    print("No se pueden comparar los resultados porque")
    print("alguna de las multiplicaciones no fue posible.")