# Programa para ingresar un número y calcular su raiz cuadrada.

# Importar el módulo math para poder utilizar la función raiz cuadrada
import math

# 2 Definir variables
raizc=float

# 3. Leer el número y definirlo como real
numero = float(input("Ingrese un número: "))

# 4. Evaluar si el número ingresado es positivo
if numero >= 0:
    # 5. Calcular la raíz cuadrada
    raizc = math.sqrt(numero)
    # 6. Mostrar el resultado
    print("La raiz de ", numero, " es ", raizc)
else:
    # 7. Mostrar mensaje de error
    print("No se puede calcular la raíz cuadrada de un número negativo.")