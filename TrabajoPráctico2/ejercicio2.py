# Ingreso del grado del polinomio
n = int(input("Ingrese el grado del polinomio (n): "))

# Ingreso del valor de x
x = float(input("Ingrese el valor de x: "))


resultado=0
# Ingreso de los coeficientes desde a0 hasta an
print("Ingrese los coeficientes desde a0 hasta a" + str(n) + ":")
for i in range(n + 1):
    coef = float(input(f"a{i} = "))
    resultado += coef * (x ** i)

# Mostrar el resultado
print(f"\nEl valor del polinomio en x = {x} es: {resultado}")
