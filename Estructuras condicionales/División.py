# Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.
dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))

cociente = dividendo // divisor
resto = dividendo % divisor

# Verificar si la división es exacta
if resto == 0:
    print("La división es exacta.")
    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")
else:
    print("La división no es exacta.")
    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")
