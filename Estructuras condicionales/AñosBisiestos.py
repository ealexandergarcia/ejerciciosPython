# Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:
# Si el año no es divisible por 4, no es bisiesto.
# Si el año es divisible por 4 pero no por 100, es bisiesto.
# Si el año es divisible por 100 pero no por 400, no es bisiesto.
# Si el año es divisible por 400, es bisiesto.
try:
    year = int(input("Ingrese un año: "))
    if year % 4 != 0:
        print(f"El año {year} no es bisiesto.")
    elif year % 100 != 0:
        print(f"El año {year} es bisiesto.")
    elif year % 400 != 0:
        print(f"El año {year} no es bisiesto.")
    else:
        print(f"El año {year} es bisiesto.")
except ValueError:
    print("Por favor, ingrese un año válido.")

