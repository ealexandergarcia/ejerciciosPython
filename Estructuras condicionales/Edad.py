# Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:
from time import localtime
t = localtime()
dateYear = int(input("Ingresa tu Año de nacimiento: "))
dateMonth = int(input("Ingresa tu Mes de nacimiento (1 hasta 12): "))
if dateMonth > 12:
    print("Seleccione una fecha valida")
    dateMonth = int(input("Ingresa tu Mes de nacimiento (1 hasta 12): "))
dateDay = int(input("Ingresa tu Dia de nacimiento: "))
edad_anios = t.tm_year - dateYear

if (t.tm_mon, t.tm_mday) < (dateMonth, dateDay):
    edad_anios -= 1
    print("".center(50,"="))
    print(f"Hoy es {t.tm_year}/{t.tm_mon}/{t.tm_mday}")
    print(f"Tu cumpleaños es {dateYear}/{dateMonth}/{dateDay}")
    print(f"Aun no cumples años, tu edad acual es {edad_anios} años")
else:
    print("".center(50,"="))
    print(f"Hoy es {t.tm_year}/{t.tm_mon}/{t.tm_mday}")
    print(f"Ya cumpliste años {dateYear}/{dateMonth}/{dateDay}")
    print(f"Tu edad actual es: {edad_anios} años")