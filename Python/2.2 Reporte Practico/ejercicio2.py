def prepara_HotCakes ():
    return "🥞"


def ordenar_hotcakes(num_piezas):
    piezas_hotcakes =[prepara_HotCakes() for _ in range(num_piezas)]
    return piezas_hotcakes

mi_familia = ordenar_hotcakes(int(input("Cuanto son en tu familia: ")))

print(mi_familia)