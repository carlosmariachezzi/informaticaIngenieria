import numpy as np

# Cargamos los vectores en memoria
u = np.array([1, 2, 1])
v = np.array([2, 4, 6])
w = np.array([3, 6, 2])

# Formamos una matriz colocando los vectores como columnas
M = np.column_stack((u, v, w))

print("Vector u:")
print(u)

print("Vector v:")
print(v)

print("Vector w:")
print(w)

print("Matriz formada por los vectores:")
print(M)


# 1. Calcular el rango de la matriz
rango = np.linalg.matrix_rank(M)

print("1. Rango de la matriz:")
print(rango)


# 2. Calcular el determinante
determinante = np.linalg.det(M)

print("2. Determinante:")
print(determinante)


# 3. Determinar si los vectores son independientes o dependientes
if rango == 3:
    print("3. Los vectores son LINEALMENTE INDEPENDIENTES.")
else:
    print("3. Los vectores son LINEALMENTE DEPENDIENTES.")


# 4. Justificación

print("4. Justificación:")

if determinante == 0:
    print("El determinante es igual a 0.")
    print("Por lo tanto, los vectores son linealmente dependientes.")
else:
    print("El determinante es diferente de 0.")
    print("Por lo tanto, los vectores son linealmente independientes.")


if rango < 3:
    print("El rango es", rango, "y es menor que 3.")
    print("Por lo tanto, los tres vectores no son linealmente independientes.")
else:
    print("El rango es", rango, "y es igual a 3.")
    print("Por lo tanto, los tres vectores son linealmente independientes.")