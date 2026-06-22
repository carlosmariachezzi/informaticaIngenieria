# Ingreso de n y x
n = int(input("Ingrese el valor de n: "))
x = float(input("Ingrese el valor de x: "))

# Inicializar E
E = 0

# Calcular la expresión
for i in range(n + 1):
    termino = ((-1) ** i) * (x ** i)
    E += termino

# Mostrar el resultado
print(f"\nEl valor de la expresión E es: {E}")
