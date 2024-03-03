# Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula
caracter = input("Ingrese un caracter: ")

if caracter.isalpha():
    if caracter.isupper():
        print(f"{caracter} es una letra mayúscula.")
    else:
        print(f"{caracter} es una letra minúscula.")
elif caracter.isdigit():
    print(f"{caracter} es un número.")
else:
    print(f"{caracter} no es ni letra ni número.")
