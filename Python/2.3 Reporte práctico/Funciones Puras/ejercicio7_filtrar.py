jugadores = [
    {"nombre":"armando", "edad":24},
    {"nombre":"alex", "edad":21},
    {"nombre":"angel", "edad":22},
    {"nombre":"rodri", "edad":25},

]

jugadores_mayores = list(filter(lambda jugador: jugador["edad"] >23, jugadores ))

print(jugadores_mayores)