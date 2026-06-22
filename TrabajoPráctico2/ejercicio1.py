suma = 1
print(suma)
for n in range(39):
    termino = (-1)**n / ( 2*n)
    suma += termino
    print(suma)
# Suma de los primeros 40 términos

print(f"Suma de los 40 primeros términos: {suma}")
