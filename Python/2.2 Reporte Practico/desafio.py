def prepara_pizza ():
    return "🍕"

def prepara_hamburgesa ():
    return "🍔"

def prepara_hotdog ():
    return "🌭"

def bonus (numero_porciones):
    if(numero_porciones >2):
        return "coca gratis"
    else:
        return ""

def ordenar_alimento(funcion, numero_porciones):
    porciones_alimentos = [funcion() for _ in range (numero_porciones)]
    alimentos = bonus(numero_porciones)
    return porciones_alimentos, alimentos

porciones_pizza = ordenar_alimento(prepara_pizza, 10)
porciones_hamburgesa = ordenar_alimento(prepara_hamburgesa, 10)
porciones_hotdog = ordenar_alimento(prepara_hotdog, 10)

print(porciones_hamburgesa, porciones_hotdog, porciones_pizza )