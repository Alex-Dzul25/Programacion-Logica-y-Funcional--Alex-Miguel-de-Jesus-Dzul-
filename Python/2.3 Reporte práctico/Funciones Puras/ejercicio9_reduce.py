#ejemplo:

from functools import reduce

jugadores = [
    {"nombre":"armando", "edad":22},
    {"nombre":"alex", "edad":22},
    {"nombre":"angel", "edad":22},
    {"nombre":"rodri", "edad":22},

]

suma_edades= reduce(lambda acumulador, jugador: acumulador+jugador ["edad"], jugadores, 0)

print(suma_edades)