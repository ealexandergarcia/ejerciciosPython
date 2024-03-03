# Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, 
# y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

# Solicita las notas al usuario
c1 = float(input("Ingrese la nota del primer certamen: "))
c2 = float(input("Ingrese la nota del segundo certamen: "))
nl = float(input("Ingrese la nota de laboratorio: "))

# Calcula el promedio de los dos primeros certámenes
nc = (c1 + c2) / 2
# Calcula la nota final
nf = nc * 0.7 + nl * 0.3
# Calcula la nota necesaria para aprobar con nota final 60
nota_necesaria = (60 - nf * 0.7) / 0.3

print(f"Necesita nota {nota_necesaria:.2f} en el certamen 3")


