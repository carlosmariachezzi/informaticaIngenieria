# Cargar un vector de float con validación de entrada
# Uso de try/except para capturar errores

import numpy as np

# Validar que el usuario ingrese un número entero positivo
valido = False
while not valido:
    try:
        n = int(input("¿Cuántos números reales (float) desea ingresar? "))
        if n > 0:
            valido = True
        else:
            print("Por favor, ingrese un número mayor que cero.")
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

# Inicializar el vector con ceros de tipo float
vector = np.zeros(n, dtype=float)

# Cargar los datos con validación
for i in range(n):
    valido = False
    while not valido:
        try:
            valor = float(input(f"Ingrese el valor decimal para la posición {i}: "))
            vector[i] = valor
            valido = True
        except ValueError:
            print("Entrada inválida. Ingrese un número decimal (ej: 3.14).")

# Mostrar el vector cargado
print("Vector ingresado correctamente:")
print(vector)
