def aplicar_operacion(funcion, valores):
    return [funcion(valor) for valor in valores]

def elevar_cuadrado(x):
    return x ** 2

numeros = [2, 3, 4, 5]
print(aplicar_operacion(elevar_cuadrado, numeros))  # Salida: [4, 9, 16, 25]
