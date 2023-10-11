importe_final = float(input("Importe final del artículo: "))
tipo_iva = 10  # Suponiendo un IVA del 10%
iva_pagado = importe_final / (1 + (tipo_iva / 100))
importe_sin_iva = importe_final - iva_pagado
print(f"IVA pagado: {iva_pagado:.2f}")
print(f"Importe sin IVA: {importe_sin_iva:.2f}")
