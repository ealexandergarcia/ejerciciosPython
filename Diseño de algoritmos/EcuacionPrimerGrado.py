# Solicitar coeficientes al usuario
try:
    coeficiente_a = float(input("Ingrese el coeficiente 'a': "))
    coeficiente_b = float(input("Ingrese el coeficiente 'b': "))

    if coeficiente_a == 0:
        if coeficiente_b == 0:
            print("No hay solucion unica.")
        else:
            print("Sin solucion")
    else:
        x = -coeficiente_b / coeficiente_a
        print(f"Solucion unica: {x:.2f}")
except ValueError:
    print("Por favor, ingrese coeficientes válidos (números).")
