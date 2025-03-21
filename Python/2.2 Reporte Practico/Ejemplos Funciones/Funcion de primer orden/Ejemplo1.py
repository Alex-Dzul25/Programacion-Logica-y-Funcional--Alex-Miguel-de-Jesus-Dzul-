def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

notas = [85, 90, 78]
promedio = calcular_promedio(*notas)
print(f"Tu promedio es: {promedio}")