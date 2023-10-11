telefono = input("Introduce un número de teléfono con formato +34-XXXXXXXXX-XX: ")

partes = telefono.split('-')
if len(partes) == 3 and partes[0] == '+34' and len(partes[1]) == 9 and len(partes[2]) == 2:
    numero_telefono = partes[1]
    print("Número de teléfono sin prefijo ni extensión:", numero_telefono)
else:
    print("El formato del número de teléfono no es válido.")
