# Definición de las funciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

# Comienzo del programa
num1=int(input('Ingrese el valor del primer número '))
num2=int(input('Ingrese el valor del segundo número '))
while num1 != 0 and num2 != 0:
    print('La suma es ', sumar(num1,num2))
    print('La resta es ', restar(num1,num2))
    print('La multiplicación es ', mult(num1,num2))
    print('La división es ', div(num1,num2))
    num1=int(input('Ingrese el valor del primer número '))
    num2=int(input('Ingrese el valor del segundo número '))