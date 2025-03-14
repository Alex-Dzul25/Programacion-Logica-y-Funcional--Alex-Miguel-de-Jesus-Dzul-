# Definir las ramas y sus puntajes
redes = 0
bases_de_datos = 0
desarrollo_software = 0
programacion_hardware = 0
modelado_3d = 0
gestion_proyectos = 0

# Preguntas
print("¡Hola! Vamos a descubrir qué rama de Sistemas Computacionales es para ti.")
print("Responde las siguientes preguntas con el número de la opción que más te guste.\n")

# Pregunta 1
print("1. ¿Qué te gusta más?")
print("1. Configurar redes y servidores.")
print("2. Diseñar y manejar bases de datos.")
print("3. Programar aplicaciones y software.")
print("4. Trabajar con hardware y circuitos.")
print("5. Crear modelos 3D y gráficos.")
print("6. Organizar y liderar equipos de trabajo.")
respuesta = input("Elige una opción (1-6): ")
if respuesta == "1":
    redes += 1
elif respuesta == "2":
    bases_de_datos += 1
elif respuesta == "3":
    desarrollo_software += 1
elif respuesta == "4":
    programacion_hardware += 1
elif respuesta == "5":
    modelado_3d += 1
elif respuesta == "6":
    gestion_proyectos += 1

# Pregunta 2
print("\n2. ¿Qué tipo de proyectos te emociona más?")
print("1. Optimizar la red de una empresa.")
print("2. Crear una base de datos para un hospital.")
print("3. Desarrollar una app móvil.")
print("4. Construir un robot.")
print("5. Diseñar un videojuego.")
print("6. Liderar un equipo para crear un software.")
respuesta = input("Elige una opción (1-6): ")
if respuesta == "1":
    redes += 1
elif respuesta == "2":
    bases_de_datos += 1
elif respuesta == "3":
    desarrollo_software += 1
elif respuesta == "4":
    programacion_hardware += 1
elif respuesta == "5":
    modelado_3d += 1
elif respuesta == "6":
    gestion_proyectos += 1

# Pregunta 3
print("\n3. ¿Qué habilidades te gustaría aprender?")
print("1. Configurar routers y firewalls.")
print("2. Usar SQL para consultar datos.")
print("3. Programar en Python o Java.")
print("4. Diseñar circuitos electrónicos.")
print("5. Usar Blender o Maya para modelar.")
print("6. Aprender metodologías ágiles.")
respuesta = input("Elige una opción (1-6): ")
if respuesta == "1":
    redes += 1
elif respuesta == "2":
    bases_de_datos += 1
elif respuesta == "3":
    desarrollo_software += 1
elif respuesta == "4":
    programacion_hardware += 1
elif respuesta == "5":
    modelado_3d += 1
elif respuesta == "6":
    gestion_proyectos += 1

# Pregunta 4
print("\n4. ¿Qué te parece más interesante?")
print("1. Resolver problemas de conectividad.")
print("2. Diseñar bases de datos seguras.")
print("3. Crear software innovador.")
print("4. Integrar hardware y software.")
print("5. Crear gráficos en 3D.")
print("6. Gestionar proyectos tecnológicos.")
respuesta = input("Elige una opción (1-6): ")
if respuesta == "1":
    redes += 1
elif respuesta == "2":
    bases_de_datos += 1
elif respuesta == "3":
    desarrollo_software += 1
elif respuesta == "4":
    programacion_hardware += 1
elif respuesta == "5":
    modelado_3d += 1
elif respuesta == "6":
    gestion_proyectos += 1

# Pregunta 5
print("\n5. ¿En qué te gustaría trabajar?")
print("1. En una empresa de telecomunicaciones.")
print("2. En una empresa que maneje grandes datos.")
print("3. En una startup de tecnología.")
print("4. En una empresa de hardware.")
print("5. En una empresa de videojuegos.")
print("6. En una consultoría de software.")
respuesta = input("Elige una opción (1-6): ")
if respuesta == "1":
    redes += 1
elif respuesta == "2":
    bases_de_datos += 1
elif respuesta == "3":
    desarrollo_software += 1
elif respuesta == "4":
    programacion_hardware += 1
elif respuesta == "5":
    modelado_3d += 1
elif respuesta == "6":
    gestion_proyectos += 1

# Calcular la rama con más puntos
puntajes = {
    "Redes": redes,
    "Bases de Datos": bases_de_datos,
    "Desarrollo de Software": desarrollo_software,
    "Programación Hardware": programacion_hardware,
    "Modelado 3D": modelado_3d,
    "Gestión de Proyectos": gestion_proyectos
}

rama_recomendada = max(puntajes, key=puntajes.get)

# Mostrar resultado
print("\n¡Gracias por responder!")
print(f"Tu rama recomendada es: {rama_recomendada}")