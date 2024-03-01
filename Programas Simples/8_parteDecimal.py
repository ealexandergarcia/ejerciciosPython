# Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
numero = float(input("Ingrese un número real: "))
parte_decimal = abs(numero) - abs(int(numero))
print(f"La parte decimal de {numero} es: {parte_decimal:.2f}")
