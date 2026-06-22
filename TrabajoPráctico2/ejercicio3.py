# Ingreso de la cantidad de pares
n = int(input("Ingrese el número de pares (n): "))
E=float(0)

# Repetir para cada par
for i in range(1, n + 1):
    print(f"\nPar {i}:")
    x = float(input("Ingrese el valor de x: "))
    z = float(input("Ingrese el valor de z (z > 0): "))
    # Asegurarse de que z > 0
    while z ==0:
        z = float(input("Ingrese el valor de z (z > 0): "))
 
    # Sumar el término a E
    E += x / z

# Mostrar el resultado
print(f"\nEl valor de la expresión E es: {E}")
