nombre_producto = input("Introduce el nombre del producto: ")
precio_unitario = float(input("Introduce el precio unitario del producto: "))
unidades = int(input("Introduce el número de unidades: "))

coste_total = precio_unitario * unidades

print(f"Nombre del producto: {nombre_producto}")
print(f"Precio unitario: {precio_unitario:.2f}")
print(f"Número de unidades: {unidades:03d}")
print(f"Coste total: {coste_total:.2f}")
