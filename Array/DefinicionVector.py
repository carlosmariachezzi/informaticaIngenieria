# Definición del tamaño y tipo de dato de un vector
import numpy as np

# 1.- Vector de tamaño 5 con tipo real
print( "Vector de tamaño 5 con tipo real")
vector = np.zeros(5, dtype=float)
print(vector)

# 2.- Vector de tamaño 7 con tipo entero
print("Vector de tamaño 7 con tipo entero")
vector = np.zeros(7, dtype=int)
print(vector)

# 3.- Vector de tamaño 7 con tipo complejo
print("Vector de tamaño 7 con tipo complejo")
vector = np.zeros(7, dtype=complex)
print(vector)

# 4.- Vector de tamaño 7 con tipo boolean inicializado con verdadero
print("Vector de tamaño 7 con tipo boolean inicializado con verdadero")
vector = np.full(7, True, dtype=bool)
print(vector)

# 5.- Vector de tamaño 7 con tipo boolean no inicializado
print(" Vector de tamaño 7 con tipo boolean no inicializado")
vector = np.zeros(7, dtype=bool)
print(vector)

# 6.- Vector de tamaño 7 con tipo boolean inicializado con verdadero
print("Vector de tamaño 7 con tipo boolean inicializado con verdadero")
vector = np.full(7, True, dtype=bool)
print(vector)

# 7.- Vector de tamaño 7 con tipo string (caracter)
print("Vector de tamaño 7 con tipo string (caracter)")
vector = np.zeros(7, dtype=str)
print(vector)

# 8.- Vector de tamaño 7 con tipo de dato fecha
print("Vector de tamaño 7 con tipo de dato fecha")
vector = np.zeros(7, dtype='datetime64[D]')
print(vector)