import math

try:
    n = int(input("Ingrese n (entero positivo o cero): "))

    if n < 0:
        print("El valor debe ser mayor o igual a 0.")
    else:
        catalan = math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))

        print("Número de Catalán C(n):", catalan)
        print("Triangulaciones de un polígono de", n + 2, "lados:", catalan)

except ValueError:
    print("Debe ingresar un número entero.")
