n = input("Ingrese cuántas palabras ingresará: ")
plural = "dígitos" if len(n) != 1 else "dígito"
print(f"{n} tiene {len(n)} {plural}")