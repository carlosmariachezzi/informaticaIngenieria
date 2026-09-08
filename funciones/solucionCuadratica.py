import math

def resolvente(a,b,c):
    r=float()
    r = b**2-4*a*c
    return r

x1=float()
x2=float()
c1=complex()
c2=complex()

a=int(input('Ingrese el valor de a--> '))
b=int(input('Ingrese el valor de b--> '))
c=int(input('Ingrese el valor de c--> '))

if a!= 0:
    if resolvente(a,b,c)>0:
        x1=(-b+math.sqrt(resolvente(a,b,c)))/(2*a)
        x2=(-b-math.sqrt(resolvente(a,b,c)))/(2*a)
        print(x1)
        print(x2)
    else:
        if resolvente(a,b,c)==0:
            print('La solución única  es ', -b/(2*a))
        else:
            c1=complex(-b/(2*a) , math.sqrt(abs(resolvente(a,b,c)))/(2*a))
            c2=complex(-b/(2*a) , -math.sqrt(abs(resolvente(a,b,c)))/(2*a))
            print(c1)
            print(c2)
else:
    print('El valor de a ingresado es cero')