notas = [85, 60, 90, 50, 78]
aprobadas = list(filter(lambda nota: nota >= 70, notas))
print(f"Notas aprobadas: {aprobadas}")