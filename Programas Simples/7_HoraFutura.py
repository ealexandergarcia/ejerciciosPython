# Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
horaAct= int(input("Hora actual: "))
cantHora = int(input("Cantidad de horas: "))
print(f"En {cantHora} horas, el reloj marcara las {(horaAct+cantHora)%24}")