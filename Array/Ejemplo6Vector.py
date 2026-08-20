# Cargar un vector de float con validación de entrada (Uso de try/except para capturar errores)

import numpy as np

# Validar que el usuario ingrese un número entero positivo
while True:
    try:
        n = int(input("¿Cuántos números reales (float) desea ingresar? "))
        if n <= 0:
            print("Por favor, ingrese un número mayor a cero.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

# Inicializar vector con ceros de tipo float
vector = np.zeros(n, dtype=float)

# Cargar los datos con validación
for i in range(n):
    while True:
        try:
            valor = float(input(f"Ingrese el valor decimal para la posición {i}: "))
            vector[i] = valor
            break  # Salir del bucle si fue exitoso
        except ValueError:
            print("Entrada inválida. Ingrese un número decimal (ej: 3.14).")

# Mostrar el vector cargado
print("Vector ingresado correctamente:")
print(vector)
