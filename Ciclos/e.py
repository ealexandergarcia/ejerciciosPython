# Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.
from math import factorial
e = 1
i = 0
while True:
    i += 1
    anterior_e = e
    e += 1 / factorial(i)
    if abs(e - anterior_e) < 0.0001:
        break

print(f"Constante de Euler (e): {e}")
