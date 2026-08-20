import numpy as np
import matplotlib.pyplot as plt

# Función para generar vectores aleatorios

def generar_vectores(n_vectores, dimension, minimo=-10, maximo=10):
    vectores = [np.random.randint(minimo, maximo + 1, dimension) for _ in range(n_vectores)]
    return vectores

# Función para calcular norma euclidiana

def calcular_norma(vector):
    return np.linalg.norm(vector)

# Función para sumar varios vectores
def suma_vectores(vectores):
    return np.sum(vectores, axis=0)


# Función para producto escalar

def producto_escalar(v1, v2):
    """
    Calcula el producto escalar entre dos vectores.
    """
    return np.dot(v1, v2)


# Función para graficar
def graficar_vectores(vectores, dimension, tipo="scatter"):
    """
    for i, v in enumerate(vectores, start=1):
        plt.scatter(range(len(v)), v, label=f"Vector {i}")
    
    plt.axhline(0, color="black", linewidth=0.8)  # Línea horizontal en y=0
    plt.title("Vectores ")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.legend()
    plt.show()
    """
    plt.scatter((range(1, dimension+1)), vectores[0], label=f"Vector {1}")
    plt.scatter((range(1, dimension+1)), vectores[1], label=f"Vector {2}")
    plt.scatter((range(1, dimension+1)), vectores[2], label=f"Vector {3}")
    plt.axhline(0, color="black", linewidth=0.8)  # Línea horizontal en y=0
    plt.title("Vectores ")
    plt.xlabel("Índice")
    plt.ylabel("Valor")
    plt.legend()
    plt.show()

cant=int(input("ingrese cantidad de vectores") )
dimension=int(input("ingrese dimension de los vectores") )
# 1. Generar vectores
vectores = generar_vectores(cant, dimension)
print("Vectores generados:")
for i, v in enumerate(vectores, start=1):
    print(f"Vector {i}: {v}")

# 2. Calcular norma de cada vector
for i, v in enumerate(vectores, start=1):
    print(f"Norma Vector {i}: {calcular_norma(v):.4f}")

# 3. Calcular suma de los vectores
suma = suma_vectores(vectores)
print(f"Suma de los 3 vectores: {suma}")

# 3b. Producto escalar entre los dos primeros
prod = producto_escalar(vectores[0], vectores[1])
print(f"Producto escalar entre Vector 1 y Vector 2: {prod}")

# 4. Graficar los vectores (puede ser scatter o line)
graficar_vectores(vectores,dimension)  # Cambiar "line" por "scatter" si se quiere dispersión


