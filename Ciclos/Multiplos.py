# Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:
num1 =int(input("Ingrese el numero del que desea ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar de {num1}".center(40,"="))
for i in range (11):
    print(f"{i} x {num1} = {i*num1}")