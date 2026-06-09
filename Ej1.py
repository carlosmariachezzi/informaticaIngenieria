# Ejercicio 1.1
# A=(0,1) ∪ (2,3) 

# Se lee el valor de x verificacndo que no se ingrese un dato incorrecto
controlIngreso = True
while controlIngreso:
    try:
        x = float(input("Ingrese un número real: "))
        controlIngreso = False
    except ValueError: 
        print("Debes ingresar un número real")

if (0 < x < 1) or (2 < x < 3):
    print("El valor pertenece al conjunto A")
else:
    print("El valor NO pertenece al conjunto A")

