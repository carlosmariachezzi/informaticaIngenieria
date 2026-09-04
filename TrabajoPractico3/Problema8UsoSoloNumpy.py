import numpy as np

# Definición de vectores conocidos
a = np.array([1, -1, 0])
b = np.array([0, 0, 4])

# 1. Expresar el producto escalar a · x
# Como a = [a0, a1, a2], el producto a · x es: a[0]*x1 + a[1]*x2 + a[2]*0
prod_escalar_str = f"{a[0]}*x1 + ({a[1]})*x2 + {a[2]}*0 = {a[0]}*x1 - {abs(a[1])}*x2"

# 2. Relación entre x1 y x2 tal que a · x = 3
# x1 - x2 = 3  =>  x2 = x1 - 3

# 3. Probar distintas parejas (x1, x2) y verificar cuáles cumplen a · x = 3
# Definimos una matriz de parejas de prueba [x1, x2]
parejas_prueba = np.array([
    [5, 2],
    [3, 0],
    [0, -3],
    [4, 2],
    [1, -2]
])

# Evaluamos cada pareja construyendo el vector x = [x1, x2, 0]
resultados = []
for pareja in parejas_prueba:
    x = np.array([pareja[0], pareja[1], 0])
    resultado_dot = np.dot(a, x)
    cumple = (resultado_dot == 3)
    resultados.append((pareja, resultado_dot, cumple))

# 4. Calcular el producto vectorial a x b
prod_vectorial = np.cross(a, b)

# --- Impresión de Resultados ---
print("1. PRODUCTO ESCALAR ---")
print(f"a · x = {prod_escalar_str}")

print("2. RELACIÓN ALGEBRAICA ---")
print(f"a · x = 3  =>  x1 - x2 = 3  =>  x2 = x1 - 3")

print("3. VERIFICACIÓN DE PAREJAS (x1, x2) ---")
for par, dot, cumple in resultados:
    print(f"Pareja {par} -> a · x = {dot:2d} | ¿Cumple?: {cumple}")

print("4. PRODUCTO VECTORIAL ---")
print(f"a x b = {prod_vectorial}")