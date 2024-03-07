import re
from os import system

puntaje1 = 0
puntaje2 = 0

while puntaje1 < 3 and puntaje2 < 3:
    system("clear")
    print("Piedra, Papel o Tijera".center(50, "="))
    print("Puntaje Actual".center(50, "="))
    print("")
    print(f"Usuario 1: {puntaje1} | Usuario 2: {puntaje2}".center(50))

    user1 = input("Ingrese su jugada: ").lower()
    user2 = input("Ingrese su jugada: ").lower()

    if re.match(r"(tijera|papel|piedra)$", user1) and re.match(r"(tijera|papel|piedra)$", user2):
        if user1 == "tijera":
            if user2 == "papel":
                puntaje1 += 1
            elif user2 == "piedra":
                puntaje2 += 1
        elif user1 == "papel":
            if user2 == "piedra":
                puntaje1 += 1
            elif user2 == "tijera":
                puntaje2 += 1
        elif user1 == "piedra":
            if user2 == "tijera":
                puntaje1 += 1
            elif user2 == "papel":
                puntaje2 += 1
    else:
        print("Jugada no válida. Intente de nuevo.")

if puntaje1 > puntaje2:
    print("¡El Usuario 1 ha ganado!")
elif puntaje1 < puntaje2:
    print("¡El Usuario 2 ha ganado!")
else:
    print("¡Hubo un empate!")
