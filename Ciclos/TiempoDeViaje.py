# El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
hora = 0
while True:
    minutos = int(input("duracion tramo: "))
    hora += (minutos)
    if minutos == 0:
        break

horas = hora // 60
minutos = hora % 60
print(f"El tiempo total de viaje es: {horas}:{minutos} horas")

