
def total(horas: int , coste: float):
    frase = "El total de las horas es " + str(horas * coste) + " euros."
    return frase

horas = int(input("Cuantas horas: "))
coste= int(input("A cuanto la hora: "))

print(total(horas, coste))