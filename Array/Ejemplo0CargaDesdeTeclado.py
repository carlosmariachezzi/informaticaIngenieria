# Carga de datos al vector desde teclado
import numpy as np

# Solicitar la cantidad de elementos
n = int(input("¿Cuántas temperaturas desea ingresar? "))

# Crear el vector
vector = np.zeros(n, dtype=float)

# Cargar los datos
for i in range(n):
    vector[i] = float(input(f"Ingrese la temperatura {i}: "))

# Mostrar el vector
print("Vector de temperaturas:")
print(vector)