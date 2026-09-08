import numpy as np

# Definimos el vector a.
# Tiene tres componentes: [1, -1, 0]
a = np.array([1, -1, 0])

# Creamos una lista de pares de valores (x1, x2).
# Cada par representa los valores que vamos a utilizar
# para construir un nuevo vector x.
pares = [
    (3, 0),
    (4, 1),
    (2, -1),
    (5, 2),
    (1, 1)
]

# Recorremos cada par de valores de la lista.
# x1 y x2 toman los valores de cada par.
for x1, x2 in pares:

    # Construimos el vector x utilizando x1, x2 y 0.
    # Por ejemplo, si x1=3 y x2=0:
    # x = [3, 0, 0]
    x = np.array([x1, x2, 0])

    # Calculamos el producto escalar entre los vectores a y x.
    # np.dot() multiplica los elementos que ocupan
    # la misma posición y luego los suma.
    producto = np.dot(a, x)

    # Mostramos el vector x y el resultado del producto escalar.
    print(x, "->", producto)

    # Comprobamos si el producto escalar es igual a 3.
    # Si es igual, el vector cumple la condición.
    if producto == 3:
        print("Cumple")
    else:
        # Si el producto no es igual a 3,
        # el vector no cumple la condición.
        print("No cumple")