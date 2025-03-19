def preparar_cafe_a():
    return "cafe amerricano"

def preparar_cafe_o():
    return "cafe de olla"

def ordenar_cafe (funcion, numeros_tazas):
    tazas_cafe=[funcion() for _ in range(numeros_tazas)]
    return tazas_cafe

cafe_grupo_a = ordenar_cafe(preparar_cafe_a, 10)
cafe_grupo_b = ordenar_cafe(preparar_cafe_o, 12)

print (cafe_grupo_a, cafe_grupo_b)