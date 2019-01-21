def ddg(jugador):
    jugador = int(jugador)
    jugadores = ["Juan", "Maria", "Carlos"]
    for i in range(len(jugadores)):
        if i == jugador:
            return jugadores[i]

jugador = input("Introduce numero: ")
print(ddg(jugador))
print(hola)
