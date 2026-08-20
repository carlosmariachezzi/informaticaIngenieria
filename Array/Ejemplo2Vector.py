# # Carga de un vector a partir de una lista con n datos

import numpy as np

# Leer N elementos definidos por el usuario
N = int(input("¿Cuántos elementos desea ingresar? "))
datos = []

for i in range(N):
    valor = int(input(f"Ingrese el valor {i+1}: "))
    datos.append(valor)

# Convertir a array
datos = np.array(datos)

print("Datos ingresados:", datos)

# Buscar un número dentro del vector
buscar = int(input("Ingrese un número a buscar: "))
indices = np.where(datos == buscar)[0]  # Devuelve array con índices

if indices.size > 0:
    print(f"El número {buscar} se encuentra en la(s) posición(es): {indices}")
else:
    print("Número no encontrado.")

# Contar ocurrencias de un valor
valor = int(input("¿Qué número desea contar? "))
veces = np.count_nonzero(datos == valor)

print(f"El número {valor} aparece {veces} veces.")

# Ordenar el vector
ordenado_asc = np.sort(datos)
ordenado_desc = np.sort(datos)[::-1]

print("Vector ordenado de menor a mayor:", ordenado_asc)
print("Vector ordenado de mayor a menor:", ordenado_desc)