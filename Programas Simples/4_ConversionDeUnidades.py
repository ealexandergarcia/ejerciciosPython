#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.
longitud = int(input("Ingrese longitud: "))

pulgada = longitud / 2.54
print(f"{longitud} cm = {pulgada:.4f} in")