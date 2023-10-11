importe_sin_iva = float(input("Importe sin IVA: "))
tipo_iva = float(input("Tipo de IVA (%): "))
precio_final = importe_sin_iva + (importe_sin_iva * (tipo_iva / 100))
print(f"Precio final del artículo: " + precio_final)
