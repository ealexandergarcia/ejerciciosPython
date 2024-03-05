n = int(input("Ingrese cuántas palabras ingresará: "))

palabra_mas_larga = ""
palabra_mas_corta = None

for i in range(n):
    palabra = input(f"Ingrese la palabra {i + 1}: ")
    if not palabra_mas_larga or len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra
    if not palabra_mas_corta or len(palabra) < len(palabra_mas_corta):
        palabra_mas_corta = palabra
print("Palabra más larga:", palabra_mas_larga)
print("Palabra más corta:", palabra_mas_corta)
