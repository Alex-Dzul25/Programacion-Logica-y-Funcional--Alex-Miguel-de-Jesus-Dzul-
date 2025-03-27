def agregar_asignaturas (lista):
    asig_nueva = input("Escribe la asignatura nueva o exit para salir: ")
    if asig_nueva == "exit":
        return lista
    return agregar_asignaturas (lista + [asig_nueva])

asignaturas = ["fisica", "programacion","matematicas"]

nueva_lista = agregar_asignaturas(asignaturas)

print(nueva_lista)
