
productos = ["Frijoles Refritos","Coca Cola", "Zumo de Naranja", "Cafe de Olla", "Gorditas de Chicharron", "Huevos Motuleños"]


productos_ordenados = sorted(productos)


cadena_nombres = ", ".join(productos_ordenados)


slugs = list(map(lambda x: x.lower().replace(" ", "-"), productos_ordenados))

print("Lista de slugs:", slugs)
print("Cadena de nombres ordenados:", cadena_nombres)