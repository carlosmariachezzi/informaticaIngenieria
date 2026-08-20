# Ejemplo 1
# Carga de un vector de caracteres con n datos usando np.full() y dtype=str en su definición
import numpy as np

# Tamaño del vector
n = int(input("¿Cuántas palabras desea ingresar? "))

# Inicializar vector con cadenas vacías de una letra en cada palabra
vector_str = np.full(n, '', dtype=str)

# Cargar letras
for i in range(n):
    palabra = input(f"Ingrese una letra para la posición {i}: ")
    vector_str[i] = palabra

# Mostrar vector
print("Vector de letras ingresado:")
print(vector_str)

# Ejemplo 2
# Carga de un vector que permita cargar palabras de hasta 5 caracteres dtype='U5'

# Tamaño del vector
n = int(input("¿Cuántas palabras desea ingresar? "))

# Inicializar vector c
vector_str = np.full(n, '', dtype='U5')

# Cargar palabras
for i in range(n):
    palabra = input(f"Ingrese una lakabra de cinco caracteres máximo para la posición {i}: ")
    vector_str[i] = palabra

# Mostrar vector
print("Vector de palabras ingresado:")
print(vector_str)