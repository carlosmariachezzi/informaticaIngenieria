import numpy as np

# 1. Expresar el sistema en forma matricial: A * X = b
# 2. Crear la matriz de coeficientes A
A = np.array([
    [1,  2, 1],
    [2, -1, 3],
    [1,  1, 2]
], dtype=float)

# 3. Crear el vector de términos independientes b

b = np.array([8, 9, 7], dtype=float)

# 4. Resolver el sistema (A * X = b)
X = np.linalg.solve(A, b)

# Impresión de Resultados
print("MATRIZ DE COEFICIENTES A")
print(A)

print("VECTOR DE TÉRMINOS INDEPENDIENTES b")
print(b)

print("SOLUCIÓN DEL SISTEMA X")
print(X)

# 5. Verificar el resultado (comprobar que A * X se aproxima a b)
b_verificacion = np.dot(A, X)
es_correcto = np.allclose(b_verificacion, b)
print("VERIFICACIÓN")
print(f"A * X ={b_verificacion}")
print(f"¿La solución es correcta?: {es_correcto}")