playerA = int(input("Ingrese los juegos del jugador A: "))
playerB = int(input("Ingrese los juegos del jugador B: "))

if playerA < 0 or playerB < 0 or abs(playerA - playerB) > 2:
    print("Invalido")
elif playerA == playerB == 6:
    print("El set se define en un último juego.")
elif playerA >= 6 and playerA - playerB >= 2:
    print("Gano A")
elif playerB >= 6 and playerB - playerA >= 2:
    print("Gano B")
else:
    print("Aun no termina")