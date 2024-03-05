num1 = int(input("Ingrese su puntaje: "))
comb= []
for i in range(1, 7):
    for j in range(1, 7):
        if i + j == num1:
            prueba = f"{i} + {j}"
            comb.append(prueba)
print(f"Hay {len(comb)} para obtener {num1}")