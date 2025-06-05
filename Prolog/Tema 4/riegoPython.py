# Datos de entrada
humedad_suelo = 'baja'
temperatura = 35
hora = 20
pronostico_lluvia = False


def hora_adecuada(hora):
    return hora < 10 or hora > 18


def activar_riego(humedad_suelo, pronostico_lluvia, hora):
    return humedad_suelo == 'baja' and not pronostico_lluvia and hora_adecuada(hora)

# Función para determinar el estado del riego
def estado_riego(activar):
    if activar:
        return 'Activado'
    else:
        return 'No Activado'

# Función para verificar alerta de calor 
def alerta_calor(temperatura):
    return temperatura >= 32

# Función para emitir recomendaciones 
def recomendacion(humedad_suelo, pronostico_lluvia, hora, temperatura):
    if activar_riego(humedad_suelo, pronostico_lluvia, hora):
        if alerta_calor(temperatura):
            print('Alerta: riego activado con temperatura alta.')
            print('Considere riego nocturno o por goteo.')
        else:
            print('Riego activado. Sin alertas.')
    else:
        print('Sin recomendaciones.')


activar = activar_riego(humedad_suelo, pronostico_lluvia, hora)
print(estado_riego(activar))
recomendacion(humedad_suelo, pronostico_lluvia, hora, temperatura)