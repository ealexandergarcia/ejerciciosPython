# Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:
print("Rectangulo".center(50,"="))
altura = int(input("Altura: "))
ancho = int(input("Ancho: "))
for i in range(altura):
    print("".center(ancho,"*"))

# Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario:
print("Triangulo".center(50,"="))
altura = int(input("Altura: "))
for i in range(altura+1):
    print("".center(i,"*"))

# Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:
print("Hexágono ".center(50,"="))
lado = int(input("Lado del hexágono: "))



