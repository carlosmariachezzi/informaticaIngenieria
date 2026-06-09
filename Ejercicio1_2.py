# Inicializamos contadores y acumuladores
cant_pertenecen = 0   # cantidad de valores que pertenecen al conjunto A
cant_no = 0           # cantidad de valores que NO pertenecen al conjunto A

suma_pertenecen = 0   # suma de los valores que pertenecen al conjunto A
suma_no = 0           # suma de los valores que NO pertenecen al conjunto A
suma_total = 0        # suma de todos los valores ingresados

# Bucle para ingresar 7 valores
for i in range(7):
    x = float(input(f"Ingrese el valor {i+1}: "))  # se pide un número decimal
    suma_total += x  # acumulamos el valor en la suma total
    
    # Verificamos si el número pertenece al conjunto A
    # Conjunto A: (0,1) U (2,3)
    if (x > 0 and x < 1) or (x > 2 and x < 3):
        print("Pertenece al conjunto A")
        cant_pertenecen += 1      # aumentamos el contador de pertenecientes
        suma_pertenecen += x      # sumamos el valor en el acumulador correspondiente
    else:
        print("NO pertenece al conjunto A")
        cant_no += 1              # aumentamos el contador de NO pertenecientes
        suma_no += x              # sumamos el valor en el acumulador correspondiente

# Cálculo de promedios
if cant_pertenecen > 0:
    promedio_pertenecen = suma_pertenecen / cant_pertenecen
else:
    promedio_pertenecen = 0  # evitamos división por cero

if cant_no > 0:
    promedio_no = suma_no / cant_no
else:
    promedio_no = 0  # evitamos división por cero

promedio_total = suma_total / 7  # promedio general de los 7 valores

# Mostrar resultados finales
print("\nCantidad que pertenecen:", cant_pertenecen)
print("Cantidad que NO pertenecen:", cant_no)

print("Promedio pertenecientes:", promedio_pertenecen)
print("Promedio NO pertenecientes:", promedio_no)

print("Promedio total:", promedio_total)
