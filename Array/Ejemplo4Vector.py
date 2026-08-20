# Carga de un vector de números reales sin usar listas con n datos usando np.zeros()
import numpy as np

# Tamaño del vector
n = int(input("¿Cuántos números reales (float) desea ingresar? "))

# Inicializar vector con ceros y tipo float
vector_float = np.zeros(n, dtype=float)

# Cargar valores reales
for i in range(n):
    valor = float(input(f"Ingrese el valor decimal para la posición {i}: "))
    vector_float[i] = valor

# Mostrar vector
print("Vector de números reales ingresado:")
print(vector_float)