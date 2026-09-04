import numpy as np

# Carga  de vectores en R^2
a = np.array([-3, 2])
b = np.array([3, 2])
c = np.array([4, 0])

# 1. Calcular 2c + a - b
res1 = 2 * c + a - b

# 2. Calcular 2c + a
res2 = 2 * c + a

# 3. Calcular el módulo del vector h = c - b
h = c - b
modulo_h = np.linalg.norm(h)

# 4. Calcular el módulo del vector e = a - b
e = a - b
modulo_e = np.linalg.norm(e)

# 5. Calcular: ||c - b|| + ||a - b||
res5 = modulo_h + modulo_e

# --- Impresión de Resultados ---
print(f"1. 2c + a - b = {res1}")
print(f"2. 2c + a     = {res2}")
print(f"3. Vector h = c - b = {h} | Módulo ||h|| = {modulo_h:.4f}")
print(f"4. Vector e = a - b = {e} | Módulo ||e|| = {modulo_e:.4f}")
print(f"5. ||c - b|| + ||a - b|| = {res5:.4f}")