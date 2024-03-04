# Escriba un programa que entregue todos los divisores del número entero ingresado:
numero = int(input("Ingrese un número entero: "))
print("Los divisores de", numero, "son:")

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
