# Ingreso del límite
limite = float(input("Ingrese el valor del LIMITE (mayor que 0): "))

# Validación del límite
while limite <= 0:
    print("El valor debe ser mayor que cero.")
    limite = float(input("Ingrese el valor del LIMITE nuevamente: "))

# Inicialización de variables
suma = 0
n = 0

# Calcular la serie hasta superar el límite
while suma <= limite:
    n += 1
    suma += 1 / n

# Mostrar el resultado
print(f"\nSe necesitan {n} términos de la serie armónica para superar el límite {limite}.")
