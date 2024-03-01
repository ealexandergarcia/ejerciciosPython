"""Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
del triangulo, dado por el teorema de Pitágoras: c2=a2+b2"""
import math #Importamos la libreria Math para usar la raiz cuadrada
catA = float(input("Ingrese cateto a: "))
catB = float(input("Ingrese cateto b: "))

hipotenusa = math.sqrt(catA**2 + catB**2)

print(hipotenusa)