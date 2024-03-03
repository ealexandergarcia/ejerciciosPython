# Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
# si acaso el triángulo es inválido; y
# si no lo es, qué tipo de triángulo es.

print("Ingrese los lados del trinagulo".center(50,"="))
ladoA = float(input("Ingrese A: "))
ladoB = float(input("Ingrese B: "))
ladoC = float(input("Ingrese C: "))


if ladoA + ladoB > ladoC and  ladoA + ladoC > ladoB and ladoC + ladoB > ladoA:
    if ladoA == ladoB == ladoC:
        print("".center(50,"="))
        print("Es un tringulo equilatero")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("".center(50,"="))
        print("Es un tringulo isosceles")
    else:
        print("".center(50,"="))
        print("Es un tringulo escaleno")
else:
    print("No es un triangulo valido.")