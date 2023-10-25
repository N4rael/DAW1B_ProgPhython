def iva(importe_sin_iva, tipo_iva):
    precio_final = importe_sin_iva + (importe_sin_iva * (tipo_iva / 100))
    return precio_final

importe_sin_iva = float(input("Importe sin IVA: "))
tipo_iva = float(input("Tipo de IVA (%): "))

print(f"Precio final del artículo: " + str(iva(importe_sin_iva, tipo_iva)))