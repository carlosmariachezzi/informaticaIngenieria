# Ejercicio 1.5
# Conjunto A=(0,3) 

print("Valores pertenecientes al conjunto:")

# Estructural de control for que permite evaluar los valores de -1 a 4
for x in range(-1, 5):
    if 0 < x < 3:
        print(x, "pertenece al conjunto")
    else:
        print(x, "NO pertenece al conjunto")

