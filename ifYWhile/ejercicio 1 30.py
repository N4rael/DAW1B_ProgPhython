"""
Leer inicio

Si inicio <= 0, entonces
    Mostrar "El número de inicio debe ser mayor que cero"
Sino

    Leer incremento

    Si incremento <= 0, entonces
        Mostrar "El incremento debe ser mayor que cero"
    Sino
        Leer total

        Si total <= 0, entonces
            Mostrar "El total de la serie debe ser mayor que cero"
        Sino
            serie = ""

            numero_actual = inicio

            i = 0
            Mientras i < total hacer
                serie = serie + numero_actual
                serie = serie + "-"
                numero_actual = numero_actual + incremento
                i = i + 1
            Fin Mientras

            Mostrar "SERIE => " + serie[0:len(serie)-1]
        Fin Si
    Fin Si
Fin Si
"""

inicio = int(input("Introduce el número de inicio: "))

while inicio <= 0:
    print("El número de inicio debe ser mayor que cero")
    inicio = int(input("Introduce el número de inicio: "))

incremento = int(input("Introduce el incremento: "))

while incremento <= 0:
        print("El incremento debe ser mayor que cero")
        incremento = int(input("Introduce el incremento: "))

total = int(input("Introduce el total de la serie: "))

while total <= 0:
    print("El total de la serie debe ser mayor que cero")
    total = int(input("Introduce el total de la serie: "))

serie = ""

cont = 0
while cont < total:
    serie += str(inicio)
    serie += "-"
    inicio += incremento
    cont += 1

print("SERIE => " + serie[:-1])

