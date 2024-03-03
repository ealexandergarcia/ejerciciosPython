# Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.
pal1 = input("Palabra 1:")
totPal1 = len(pal1)
pal2 = input("Palabra 2:")
totPal2 = len(pal2)

if totPal1 > totPal2:
    print(f"la palabra {pal1} tiene {totPal1-totPal2} letras mas que {pal2}")
elif totPal1 < totPal2:
    print(f"la palabra {pal2} tiene {totPal2-totPal1} letras mas que {pal1}")
else:
    print(f"Las dos palabras tienen el mismo largo")
