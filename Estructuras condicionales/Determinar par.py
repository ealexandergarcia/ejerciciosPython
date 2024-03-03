# Escriba un programa que determine si el número entero ingresado por el usuario es par o no.
num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print (f"El numero {num} es par")
else:
    print (f"El numero {num} no es par")