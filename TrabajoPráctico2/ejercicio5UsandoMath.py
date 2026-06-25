from math import factorial

x = float(input("Ingrese el valor de X: "))

suma = 0

for n in range(1, 11):
    termino = ((-1) ** (n + 1)) * (n * x) / factorial(n)
    suma += termino
    print(f"Término {n}: {termino}")

print("\nSuma total =", suma)
