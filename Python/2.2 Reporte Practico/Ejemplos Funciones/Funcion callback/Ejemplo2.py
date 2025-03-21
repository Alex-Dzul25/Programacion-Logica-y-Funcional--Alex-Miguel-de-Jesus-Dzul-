def registrar_usuario(nombre, callback):
    print(f"Usuario {nombre} registrado con éxito.")
    callback(nombre)

def enviar_correo(nombre):
    print(f"Correo enviado a {nombre}.")

registrar_usuario("Juan", enviar_correo)
