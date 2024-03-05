#El factorial n!de un número entero
num1 = int(input("Ingrese su numero: "))
n = 1

for i in range(1, num1+1):
    n *= i
print(f"{num1}! = {n}")

