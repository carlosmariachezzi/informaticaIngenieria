# Ejercicio 1.3

# Inicializamos contadores y acumuladores
cant_pertenecen = 0   # cantidad de valores que pertenecen al conjunto A
cant_no = 0           # cantidad de valores que NO pertenecen al conjunto A

suma_pertenecen = 0   # suma de los valores que pertenecen al conjunto A
suma_no = 0           # suma de los valores que NO pertenecen al conjunto A
suma_total = 0        # suma de todos los valores ingresados

contador_total = 0    # cantidad total de valores ingresados (excepto el -1)

# Primer ingreso de datos
x = float(input("Ingrese un valor (-1 para finalizar): "))

# Estructura de control while que se repite hasta que el usuario ingrese -1
while x != -1:
    suma_total += x          # acumulamos el valor en la suma total suma_total = suma_total + x 
    contador_total += 1      # aumentamos el contador de valores ingresados  contador_total = contador_total +1  

    # Verificamos si el número pertenece al conjunto A: (0,1) U (2,3)
    if (0 < x < 1) or (2 < x < 3):
        print("Pertenece al conjunto A")
        cant_pertenecen += 1     # aumentamos el contador de pertenecientes
        suma_pertenecen += x     # sumamos el valor en el acumulador correspondiente
    else:
        print("NO pertenece al conjunto A")
        cant_no += 1             # aumentamos el contador de NO pertenecientes
        suma_no += x             # sumamos el valor en el acumulador correspondiente

    # Pedimos otro valor para continuar el ciclo
    x = float(input("Ingrese otro valor (-1 para finalizar): "))

# Cálculo de promedios
if cant_pertenecen > 0:
    promedio_pertenecen = suma_pertenecen / cant_pertenecen
else:
    promedio_pertenecen = 0   # evitamos división por cero

if cant_no > 0:
    promedio_no = suma_no / cant_no
else:
    promedio_no = 0           # evitamos división por cero

if contador_total > 0:
    promedio_total = suma_total / contador_total
else:
    promedio_total = 0        # evitamos división por cero

# Mostrar resultados finales
print("\nCantidad que pertenecen:", cant_pertenecen)
print("Cantidad que NO pertenecen:", cant_no)

print("Promedio pertenecientes:", promedio_pertenecen)
print("Promedio NO pertenecientes:", promedio_no)

print("Promedio total:", promedio_total)
