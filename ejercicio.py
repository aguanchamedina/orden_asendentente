# Organizar tres números en orden ascendente.

# INPUT
a = int(input("ingrese el primer número: "))
b = int(input("ingrese el segundo número: "))
c = int(input("ingrese el tercer número: "))

# PROCESS
if a > b:
    if a > c:
        if b > c:
            print("Orden:", c, b, a) 
        else:
            print("Orden:", b, c, a) 
    else: 
        print("Orden:", b, a, c) 
else:
    if a > c:
        print("Orden:", c, a, b) 
    else:
        if b > c:
            print("Orden:", a, c, b) 
        else:
            print("Orden:", a, b, c) 

# OUTPUT