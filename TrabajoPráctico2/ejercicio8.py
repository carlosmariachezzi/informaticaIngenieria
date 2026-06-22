# Solicitar entrada del usuario
n = input("Ingresa un número natural y positivo: ")

# Verificar si es un número entero
if not n.isdigit():
    print("Error: el número no es natural (debe ser un entero positivo).")
else:
    n = int(n)
    if n <= 0:
        print("Error: el número no es positivo (debe ser mayor que 0).")
    else:
        pasos = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 2 + 2
            pasos += 1
        print(f"Se llegó al valor 1 en {pasos} paso(s).")
