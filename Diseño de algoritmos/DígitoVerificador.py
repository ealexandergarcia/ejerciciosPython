rol = input("Ingrese el rol (201012341): ")
num1 = int(rol[::-1])
resultado = 0
secuencia = [2, 3, 4, 5, 6, 7]
for i, digito in enumerate(str(num1)):
    resultado += int(digito) * secuencia[i % len(secuencia)]

modulo = resultado % 11
codigo = 11 - modulo 

print(f"El digito verificador es {rol}-{codigo}")