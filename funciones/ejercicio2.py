import numpy as np
import matplotlib.pyplot as plt

# Función para generar matriz aleatoria
def generar_matriz(filas, columnas, minimo=1, maximo=10):
    return np.random.randint(minimo, maximo + 1, (filas, columnas))

# Función para calcular sumas
def calcular_sumas(matriz):
    suma_filas = np.sum(matriz, axis=1)
    suma_columnas = np.sum(matriz, axis=0)
    return suma_filas, suma_columnas

# Función para graficar sumas
def graficar_sumas(suma_filas, suma_columnas):
    n_filas = len(suma_filas)
    n_columnas = len(suma_columnas)
    
    # Graficar sumas de filas
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.bar(range(1, n_filas+1), suma_filas, color='skyblue')
    plt.title("Suma de cada fila")
    plt.xlabel("Fila")
    plt.ylabel("Suma")
    
    # Graficar sumas de columnas
    plt.subplot(1,2,2)
    plt.bar(range(1, n_columnas+1), suma_columnas, color='salmon')
    plt.title("Suma de cada columna")
    plt.xlabel("Columna")
    plt.ylabel("Suma")
    
    plt.tight_layout()
    plt.show()


# Definir tamaño de la matriz
n = 4  # número de filas
m = 5  # número de columnas

# 1. Generar matriz
matriz = generar_matriz(n, m)
print("Matriz generada:")
print(matriz)

# 2. Calcular sumas
suma_filas, suma_columnas = calcular_sumas(matriz)
print(f"Suma de filas: {suma_filas}")
print(f"Suma de columnas: {suma_columnas}")

# 3. Graficar resultados
graficar_sumas(suma_filas, suma_columnas)
