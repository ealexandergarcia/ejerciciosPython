# Desarolle un programa para estimar el valor de π
num1 = int(input("Ingrese el valor deseado: "))
suma = 0
signo = 1
for i in range(1, 2*num1, 2):
    suma += signo * 4 / i
    signo *= -1
print(suma)