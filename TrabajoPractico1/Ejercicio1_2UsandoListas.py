# Modificación del ejercicio 1.2 con el uso listas para matener los valores que
# pertenecen y los que no pertenecen

# Inicializamos contadores y acumuladores
cant_pertenecen = 0
cant_no = 0

suma_pertenecen = 0
suma_no = 0
suma_total = 0

# Listas para almacenar los valores
lista_pertenecen = []
lista_no = []

# Bucle para ingresar 7 valores
for i in range(7):
    x = float(input(f"Ingrese el valor {i+1}: "))
    suma_total += x
    
    if (0 < x < 1) or (2 < x < 3):
        print("Pertenece al conjunto A")
        cant_pertenecen += 1
        suma_pertenecen += x
        lista_pertenecen.append(x)  # se agrega un dato en la lista pertenecen
    else:
        print("NO pertenece al conjunto A")
        cant_no += 1
        suma_no += x
        lista_no.append(x)  # se agrega un dato en la lista no pertenecen

# Cálculo de promedios

# Cálculo de promedios de los que pertenecen y no pertenecen
if cant_pertenecen > 0:
    promedio_pertenecen = suma_pertenecen / cant_pertenecen
else:
    promedio_pertenecen = 0  # evitamos división por cero

if cant_no > 0:
    promedio_no = suma_no / cant_no
else:
    promedio_no = 0  # evitamos división por cero

# Cálculo de promedio general
promedio_total = suma_total / 7

# Resultados
print("\nCantidad que pertenecen:", cant_pertenecen)
print("Cantidad que NO pertenecen:", cant_no)

print("Promedio pertenecientes:", promedio_pertenecen)
print("Promedio NO pertenecientes:", promedio_no)
print("Promedio total:", promedio_total)

# Mostrar listas completas
print("\nLista de valores que pertenecen:", lista_pertenecen)
print("Lista de valores que NO pertenecen:", lista_no)

# Ejemplos de extracción de datos de las listas
if lista_pertenecen:  # si no está vacía
    print("Primer valor que pertenece:", lista_pertenecen[0])  # acceso por índice
    print("Último valor que pertenece:", lista_pertenecen[-1])   # acceso al último
    print("Máximo de los que pertenecen:", max(lista_pertenecen)) # función max
    print("Mínimo de los que pertenecen:", min(lista_pertenecen)) # función min

if lista_no:  # si no está vacía
    print("Primer valor que NO pertenece:", lista_no[0])
    print("Último valor que NO pertenece:", lista_no[-1])
    print("Máximo de los que NO pertenecen:", max(lista_no))
    print("Mínimo de los que NO pertenecen:", min(lista_no))

# Eliminamos un valor específico de la lista si existe
# Ejemplo de uso de remove()
valor_a_eliminar = float(input("Ingrese un valor a eliminar de la lista de pertenecientes: "))
if valor_a_eliminar in lista_pertenecen:
    lista_pertenecen.remove(valor_a_eliminar)
    print("Se eliminó", valor_a_eliminar, "de la lista de pertenecientes.")
else:
    print("El valor no está en la lista de pertenecientes.")

print("Lista actualizada de pertenecientes:", lista_pertenecen)
