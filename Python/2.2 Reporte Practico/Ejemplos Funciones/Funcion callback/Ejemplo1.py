def verificar_acceso(usuario, funcion):
    return funcion(usuario)

def es_admin(usuario):
    return usuario == "admin"

print(verificar_acceso("admin", es_admin))  
