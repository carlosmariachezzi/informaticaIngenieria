# Definición de la función que obtienne el promedio entre dos valores
# sin incluir los extremos
def funcprom(x1,x2):
    i=int()
    suma=float(0)
    cont=int(0)
    prom=float()
    for i in range(x1+1,x2):
        suma += i
        cont += 1
    prom = suma/cont
    return prom

# Comienzo del programa
n1=int(input('Ingrese el valor del primer número '))
n2=int(input('Ingrese el valor del segundo número '))

# Se verifican que los datos ingresados seancorrectos
# n2 debe ser mayor que n1 y además debe existir por lo menos 
# un número entre n1 y n2
if n2 > n1+1:
    print('El promedio entre x1 y x2 es ', funcprom(n1,n2))
else:
    print('Error en los valores ingresados ')        