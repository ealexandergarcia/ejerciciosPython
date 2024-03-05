num1 = int(input("Ingrese su numero: "))
s1=0
for i in range(num1+1):
    s1 += i
    s2 = (i*(i+1))/2
print(s1)
print(int(s2))
if s1 == s2:
    print("Son iguales")
