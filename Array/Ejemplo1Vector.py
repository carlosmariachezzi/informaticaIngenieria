# Carga de un vector a partir de una lista con un número constante de datos

# Ingreso manual de datos
import numpy as np

numeros = []

for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Convertir lista a array de NumPy
numeros = np.array(numeros)

print("Los números ingresados son:")
print(numeros)

# Calcular la suma y el promedio
suma = np.sum(numeros)
promedio = np.mean(numeros)

print(f"Suma: {suma}")
print(f"Promedio: {promedio}")

# Encontrar el mayor y el menor valor
mayor = np.max(numeros)
menor = np.min(numeros)

print(f"Mayor número: {mayor}")
print(f"Menor número: {menor}")

# Sumar cuántos números son pares
pares = np.sum(numeros % 2 == 0)
print(f"Cantidad de números pares: {pares}")

# Multiplicar cada valor por 2 y mostrar nuevo vector
dobles = numeros * 2

print("Vector original:", numeros)
print("Vector con valores multiplicados por 2:", dobles)

