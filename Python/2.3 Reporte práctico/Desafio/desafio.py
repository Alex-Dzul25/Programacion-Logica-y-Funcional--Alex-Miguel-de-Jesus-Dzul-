def cuadradosLista(arreglo):
    # Filtrar primero los números que son enteros (isinstance(x, int) o x.is_integer()) y positivos
    # Luego mapear cada número a su cuadrado
    return list(map(lambda x: x * x, 
                   filter(lambda x: isinstance(x, int) and x > 0, arreglo)))

# Ejemplo de uso
cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)  # Output: [25, 9]