fila = int(input("Ingrese la fila actual del caballo (1-8): "))
columna = int(input("Ingrese la columna actual del caballo (1-8): "))

movimientos = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
               (1, -2), (1, 2), (2, -1), (2, 1)]

posiciones_validas = []
for movimiento in movimientos:
    nueva_fila = fila + movimiento[0]
    nueva_columna = columna + movimiento[1]
    if 1 <= nueva_fila <= 8 and 1 <= nueva_columna <= 8:
        posiciones_validas.append((nueva_fila, nueva_columna))

print("Posiciones hacia las cuales el caballo puede moverse:")
for posicion in posiciones_validas:
    print(f"Fila: {posicion[0]}, Columna: {posicion[1]}")
