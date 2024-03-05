num1 = int(input("Ingrese su numero: "))
prueba = []
for i in range(num1):
    pruebita =int(input("Ingrese el numero: "))
    prueba.append(pruebita)

numeros_ordenados = sorted(prueba, reverse=True)
print(f"EL mayor es {numeros_ordenados[0]}")