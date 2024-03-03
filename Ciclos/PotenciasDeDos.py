# Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:
num1 =int(input("Ingrese el rengo de la potencia: "))
for i in range(num1+1):
    num2 = 2 ** i
    print(num2)