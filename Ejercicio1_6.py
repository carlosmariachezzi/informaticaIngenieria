# Se piden los extremos del intervalo (conjunto)
a = float(input("Ingrese el extremo inferior: "))   # límite inferior del conjunto
b = float(input("Ingrese el extremo superior: "))   # límite superior del conjunto

# Se piden los valores inicial y final para recorrer
inicio = int(input("Ingrese el valor inicial: "))   # inicio del rango de números a evaluar
fin = int(input("Ingrese el valor final: "))        # fin del rango de números a evaluar

print("\nValores pertenecientes al conjunto:")

# Estrcutura de control repetitiva for que recorre todos los números enteros desde 'inicio' hasta 'fin'
for x in range(inicio, fin + 1):
    # Condición: verificamos si el número x está dentro del intervalo (a, b)
    if a < x < b:
        print(x, "Pertenece al conjunto")   # si cumple, se muestra como perteneciente
    else:
        print(x, "No pertenece al conjunto") # si no cumple, se muestra como NO perteneciente
