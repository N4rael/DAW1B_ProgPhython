print("Introduce dos números: ")
n1 = float(input())
n2 = float(input())

opcion = 0
while opcion < 1 or opcion > 4:
    print("Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): ")
    opcion = int(input())
    if opcion < 1 or opcion > 4:
        print("Error - No es una opción correcta (1-4)")

if opcion == 1:
    resultado = n1 + n2
    print(f"{n1} + {n2} = {resultado}")
elif opcion == 2:
    resultado = n1 - n2
    print(f"{n1} - {n2} = {resultado}")
elif opcion == 3:
    resultado = n1 * n2
    print(f"{n1} * {n2} = {resultado}")
elif opcion == 4:
    if n2 == 0:
        print("La división por cero no es posible")
    else:
        resultado = n1 / n2
        print(f"{n1} / {n2} = {resultado}")
