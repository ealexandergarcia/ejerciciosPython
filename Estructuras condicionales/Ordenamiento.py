# Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:
print("Primera version".center(50,"="))
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
if numero1 < numero2:
    print(f"Los números ordenados de menor a mayor son: {numero1}, {numero2}")
else:
    print(f"Los números ordenados de menor a mayor son: {numero2}, {numero1}")

# A continuación, escriba otro programa que haga lo mismo con tres números:
print("Segunda version".center(50,"="))
# Solicitar al usuario tres números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Ordenar los números
if numero1 <= numero2 <= numero3:
    print(f"Los números ordenados de menor a mayor son: {numero1}, {numero2}, {numero3}")
elif numero1 <= numero3 <= numero2:
    print(f"Los números ordenados de menor a mayor son: {numero1}, {numero3}, {numero2}")
elif numero2 <= numero1 <= numero3:
    print(f"Los números ordenados de menor a mayor son: {numero2}, {numero1}, {numero3}")
elif numero2 <= numero3 <= numero1:
    print(f"Los números ordenados de menor a mayor son: {numero2}, {numero3}, {numero1}")
elif numero3 <= numero1 <= numero2:
    print(f"Los números ordenados de menor a mayor son: {numero3}, {numero1}, {numero2}")
else:
    print(f"Los números ordenados de menor a mayor son: {numero3}, {numero2}, {numero1}")

# Finalmente, escriba un tercer programa que ordene cuatro números:
print("Tercera version".center(50,"="))
cantidad = int(input("Cuanto numeros desea ordenar: "))
mi_lista = []
for i in range(cantidad):
    num= int(input("ingrese el numero: "))
    mi_lista.append(num)
mi_lista.sort()
print(f"Los números ordenados de menor a mayor son: {mi_lista}")