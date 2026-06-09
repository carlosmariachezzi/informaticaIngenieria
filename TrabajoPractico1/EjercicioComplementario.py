# Ejercico complementario del 1.3

cant_ceros = 0
suma_total = 9
contador_total = 0
cant_positivos = 0
cant_negativos = 0
cant_ceros = 0
cant_pertenecen = 0
suma_pertenecen = 0 
cant_no = 0
suma_no = 0

mayor = None
menor = None

x = float(input("Ingrese un valor (-1 para finalizar): "))

while x != -1:
    # Acumuladores generales
    suma_total += x
    contador_total += 1
    # Mayor y menor
    if mayor is None or x > mayor:
        mayor = x

    if menor is None or x < menor:
        menor = x
    # Positivos, negativos y ceros
    if x > 0:
        cant_positivos += 1
    elif x < 0:
        cant_negativos += 1
    else:
        cant_ceros += 1
    # Pertenencia al conjunto A
    if (0 < x < 1) or (2 < x < 3):
        print("Pertenece al conjunto A")
        cant_pertenecen += 1
        suma_pertenecen += x
    else:
        print("No pertenece al conjunto A")
        cant_no += 1
        suma_no += x
    x = float(input("Ingrese otro valor (-1 para finalizar): "))

# Promedio pertenecientes
if cant_pertenecen > 0:
    promedio_pertenecen = suma_pertenecen / cant_pertenecen
else:
    promedio_pertenecen = 0

# Promedio no pertenecientes
if cant_no > 0:
    promedio_no = suma_no / cant_no
else:
    promedio_no = 0

# Promedio general
if contador_total > 0:
    promedio_total = suma_total / contador_total
else:
    promedio_total = 0

# Porcentaje pertenecientes
if contador_total > 0:
    porcentaje_pertenecen = (cant_pertenecen * 100) / contador_total
else:
    porcentaje_pertenecen = 0

# Comparación de promedios
if promedio_pertenecen > promedio_no:
    mensaje = "El grupo perteneciente tiene mayor promedio."
elif promedio_no > promedio_pertenecen:
    mensaje = "El grupo NO perteneciente tiene mayor promedio."
else:
    mensaje = "Ambos grupos tienen el mismo promedio."

# Resultados
print("\n========== RESULTADOS ==========")

print("Cantidad que pertenecen:", cant_pertenecen)
print("Cantidad que NO pertenecen:", cant_no)

print("Suma pertenecientes:", suma_pertenecen)
print("Suma NO pertenecientes:", suma_no)

print("Promedio pertenecientes:", promedio_pertenecen)
print("Promedio NO pertenecientes:", promedio_no)
print("Promedio total:", promedio_total)

print("Mayor valor ingresado:", mayor)
print("Menor valor ingresado:", menor)

print("Cantidad de positivos:", cant_positivos)
print("Cantidad de negativos:", cant_negativos)
print("Cantidad de ceros:", cant_ceros)

print("Porcentaje de pertenecientes:", porcentaje_pertenecen, "%")

print(mensaje)

