import sympy as sp
import numpy as np

# RESOLUCIÓN SIMBÓLICA (Ítems 1 y 2)
x1, x2 = sp.symbols('x1 x2', real=True)

# Definición de vectores simbólicos
a_sym = sp.Matrix([1, -1, 0])
b_sym = sp.Matrix([0, 0, 4])
x_sym = sp.Matrix([x1, x2, 0])

# 1. Producto escalar a · x
prod_escalar = a_sym.dot(x_sym)

# 2. Relación para a · x = 3
ecuacion = sp.Eq(prod_escalar, 3)
relacion_x2 = sp.solve(ecuacion, x2)[0]  # Expresa x2 en función de x1

print("1. EXPRESIÓN SIMBÓLICA DEL PRODUCTO ESCALAR ")
print(f"a · x = {prod_escalar}")

print("2. RELACIÓN ENTRE x1 Y x2 (a · x = 3)")
print(f"Ecuación: {ecuacion}")
print(f"x2 en función de x1: x2 = {relacion_x2}")

# --- RESOLUCIÓN NUMÉRICA Y VERIFICACIÓN (Ítems 3 y 4) ---
a = np.array([1, -1, 0])
b = np.array([0, 0, 4])

# 3. Probar distintas parejas (x1, x2)
parejas_prueba = [
    (5, 2),   # Cumple: 5 - 2 = 3
    (3, 0),   # Cumple: 3 - 0 = 3
    (0, -3),  # Cumple: 0 - (-3) = 3
    (4, 2)    # No cumple: 4 - 2 = 2
]

print("3. VERIFICACIÓN DE PAREJAS (x1, x2)")
for x1_val, x2_val in parejas_prueba:
    x_vec = np.array([x1_val, x2_val, 0])
    dot_val = np.dot(a, x_vec)
    cumple = dot_val == 3
    print(f"Pareja ({x1_val:2d}, {x2_val:2d}) -> a · x = {dot_val:2d} | ¿Cumple?: {cumple}")

# 4. Producto vectorial a x b
prod_vectorial = np.cross(a, b)

print("4. PRODUCTO VECTORIAL (a x b) ---")
print(f"a x b = {prod_vectorial}")