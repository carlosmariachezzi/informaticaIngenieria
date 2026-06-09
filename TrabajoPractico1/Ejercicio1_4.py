# Ejercicio 1.4
# Conjunto A=(0,4)∪{7} 


# Se lee el valor de x verificacndo que no se ingrese un dato incorrecto
controlIngreso = True
while controlIngreso:
    try:
        x = float(input("Ingrese un número real: "))
        controlIngreso = False
    except ValueError: 
        print("Debes ingresar un número real")

# Pertenencia
if (0 < x < 4) or (x == 7):
    print("El valor pertenece al conjunto A")
else:
    print("El valor NO pertenece al conjunto A")

# Punto de acumulación
if 0 <= x <= 4:
    print("El valor es punto de acumulación")
else:
    print("El valor NO es punto de acumulación")
