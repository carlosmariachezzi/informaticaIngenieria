# Ejemplo de uso:
n = int(input("Introduce el valor de n: "))
fac=1
for i in range(1, 2*n+1):
    fac *=i  
fac1=1
for i in range(1, n+2):
    fac1 *=i  
fac2=1
for i in range(1, n+1):
    fac2 *=i         
        
cat= fac//(fac1*fac2)
print(f"El número de Catalán C_{n} es: {cat}")