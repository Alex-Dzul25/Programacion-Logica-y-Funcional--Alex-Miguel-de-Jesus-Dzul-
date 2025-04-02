from functools import reduce


ventasMX = [1500, 2500, 3200, 4500, 6000, 1200, 8000]

tipo_cambio = 20.45 


promedio_ventas_mx = reduce(lambda x, y: x + y, ventasMX) / len(ventasMX)

ventasUSD = list(map(lambda x: x / tipo_cambio, ventasMX))

ventas_mayores_150 = list(filter(lambda x: x > 150, ventasUSD))

suma_ventas_mayores_150 = reduce(lambda x, y: x + y, ventas_mayores_150)


print("Promedio de ventas en pesos mexicanos:", promedio_ventas_mx)
print("Ventas en dólares:", ventasUSD)
print("Ventas mayores a 150 dólares:", ventas_mayores_150)
print("Suma total de ventas mayores a 150 dólares:", suma_ventas_mayores_150)
