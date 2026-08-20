# Carga de un vector de números enteros sin usar listas con n datos usando np.zeros()

import numpy as np

# Preguntar al usuario cuántos elementos desea
n = int(input("¿Cuántos elementos tendrá el vector? "))

# Crear un vector de ceros del tamaño n
vector = np.zeros(n, dtype=int)  # dtype=int para asegurarnos de que sean enteros

# Cargar los valores en el vector
for i in range(n):
    valor = int(input(f"Ingrese el valor para la posición {i}: "))
    vector[i] = valor  # Asignación directa en el array

# Mostrar el vector cargado
print("Vector ingresado:", vector)

