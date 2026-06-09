# Solicitar extremos del intervalo y validarlos
z = True
while z:
    try:
        a = int(input("Ingrese extremo inferior a: "))
        b = int(input("Ingrese extremo superior b: "))
        if a > b:
           print("Error: se debe cumplir a < b. Intente nuevamente.")
        else:
            z = False

    except ValueError:
        print("Error: debe ingresar números reales")


# Solicitar límites de evaluación y validarlos
z = True
while z:
    try:
        inicio = int(input("Ingrese el valor inicial: "))
        fin = int(input("Ingrese el valor final: "))
        
        if inicio > fin:
            print("Error: se debe cumplir inicio sea menor que fin. Intente nuevamente.")
        else:
            z = False
    except ValueError:
        print("Error: debe ingresar números enteros. Intente nuevamente.")

print("Valores pertenecientes al conjunto:")

# Evaluar cada valor en el rango [inicio, fin]
for x in range(inicio, fin + 1):
    if a < x < b:   # condición de pertenencia al intervalo abierto (a,b)
        print(x, "pertenece al conjunto")
    else:
        print(x, "NO pertenece al conjunto")
