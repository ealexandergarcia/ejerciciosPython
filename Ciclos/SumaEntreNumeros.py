# Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos.
num1 =int(input("Ingrese el primer numero: "))
num2 =int(input("Ingrese el segundo numero: "))
suma = 0
for i in range (num1+1 , num2):
    suma += i
print(f"La suma es {suma}")