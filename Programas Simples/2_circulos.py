#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área
import math

radio = int(input("Ingrese el radio: "))
perimetro = 2 * math.pi * radio
print(f"Perimetro: {perimetro:.1f}")

area = math.pi * radio**2
print(f"Area: {area:.1f}")
