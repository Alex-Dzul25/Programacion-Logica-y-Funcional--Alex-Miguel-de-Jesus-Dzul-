
jugadores = [
    {"nombre":"armando", "edad":22},
    {"nombre":"alex", "edad":22},
    {"nombre":"angel", "edad":22},
    {"nombre":"rodri", "edad":22},

]

nombres_jugadores = list(map(lambda jugador: jugador["nombre"], jugadores))

print(nombres_jugadores)