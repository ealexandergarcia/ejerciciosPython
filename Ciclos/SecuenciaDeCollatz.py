# Desarrolle un programa que entregue la secuencia de Collatz de un número entero:
numero = int(input("Ingrese un número entero: "))
secuencia = [numero]

while numero != 1:
    if numero % 2 == 0:
        numero //= 2
    else:
        numero = 3 * numero + 1
    secuencia.append(numero)

print("Secuencia de Collatz:")
print(secuencia)

# Desarrolle un programa que grafique los largos de las secuencias de Collatz de los números enteros positivos menores que el ingresado por el usuario:
for i in reversed(secuencia):
    print(f"{i}".ljust(i+1,"*"))