import numpy as np

# Ejemplo en Vector
datos = np.array([10, 20, 30, 20])
buscar = 20

indices = np.where(datos == buscar)
print(indices)

indices = np.where(datos == buscar)[0]
print(indices)


# Creamos una matriz 3x3
matriz = np.array([
    [5, 10, 15],
    [20, 25, 10],
    [30, 10, 35]
])

# Valor que queremos buscar
buscar = 10

# Usamos np.where para encontrar las posiciones
indices = np.where(matriz == buscar)

# Mostramos las coordenadas
print("Filas:", indices[0])
print("Columnas:", indices[1])

# Mostramos las coordenadas como pares (fila, columna)
coordenadas = list(zip(indices[0], indices[1]))
print("Coordenadas (fila, columna):", coordenadas)