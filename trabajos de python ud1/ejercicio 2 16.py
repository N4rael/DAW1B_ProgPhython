precio_por_barra = 3.49

descuento = 0.60

barras_no_frescas = int(input("Ingrese el número de barras no frescas vendidas: "))

costo_total = barras_no_frescas * precio_por_barra * (1 - descuento)

print("Precio habitual de una barra de pan: {:.2f}€".format(precio_por_barra))
print("Descuento por no ser fresca: {:.0%}".format(descuento))
print("Costo total de todas las barras no frescas: {:.2f}€".format(costo_total))
