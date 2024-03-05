print("Ingrese varios valores, termine con cero: ")
pos= 0
neg=0
while True:
    num1 = int(input())
    if num1 == 0:
        break
    if num1 > 0:
        pos +=1
    else:
        neg +=1

print(f"Positivo: {'*' * pos}")
print(f"Negativo: {'*' * neg}")