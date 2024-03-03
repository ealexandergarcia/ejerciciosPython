# Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
print("Ingrese los numeros para la operacion".center(50,"="))
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print("Seleccione una operación:".center(50,"="))
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion = input("Ingrese el número correspondiente a la operación deseada (1/2/3/4): ")

if opcion == '1':
    resultado = num1 + num2
    print(f"Resultado de la suma {num1} + {num2}: {resultado}")
elif opcion == '2':
    resultado = num1 - num2
    print(f"Resultado de la resta {num1} - {num2}: {resultado}")
elif opcion == '3':
    resultado = num1 * num2
    print(f"Resultado de la multiplicación {num1} * {num2}: {resultado}")
elif opcion == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado de la división {num1} / {num2}: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción inválida. Por favor, seleccione una operación válida.")
