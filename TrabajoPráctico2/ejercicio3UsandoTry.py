n = int(input("Ingrese la cantidad de pares (x,z): "))
E = 0

for i in range(1, n + 1):
    x = float(input(f"Ingrese x{i}: "))

    z_valido = False # varable tipo bandera o flag
    while not z_valido:
        try:
            z = float(input(f"Ingrese z{i}: "))
            if z == 0:
                raise ZeroDivisionError # (lanza una excepción)
            z_valido = True
        except ZeroDivisionError:
            print("Error: z debe ser distinto de 0")

    E = E + (x / z)
print("\nResultado final:")
print("E =", E)

