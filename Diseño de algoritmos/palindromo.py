num = input("Ingrese el numero deseado: ")
numR = num[::-1]

if num == numR:
    print(f"{num} es palindromo")
else:
    print(f"{num} no es palindromo")
