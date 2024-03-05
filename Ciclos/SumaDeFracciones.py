# Desarrolle un programa que permita trabajar con las potencias fraccionales de dos
from tabulate import tabulate
potencia = 0
exp = 1
base = 2
suma=0
tabla = []
while True:
    potencia +=1
    exp *= base
    frac = 1/exp
    suma += frac
    fila = {
                "Potencia": potencia,
                "Fraccion": frac,
                "Suma": suma
            }
    tabla.append(fila)
    if frac <=0.000001:
        break
print(tabulate(tabla, headers="keys", tablefmt="grid"))