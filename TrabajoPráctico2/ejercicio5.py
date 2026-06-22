# Ingresar el valor de x
x = float(input("Ingrese el valor de x: "))

# Inicializar variables
E = 0
factorial = 1  # Usaremos esto para ir calculando el factorial

# Calcular los 10 primeros términos
for n in range(1, 11):
    factorial *= n  # Calcular n!
    signo = (-1) ** (n + 1)  # Alternar signos
    termino = signo * n * x / factorial  # Término de la sucesión
    E += termino  # Acumular
    print(f"Término {n}: {termino}")

# Mostrar el resultado total
print(f"\nEl valor de la sucesión (suma de 10 términos) es: {E}")
