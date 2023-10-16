
def far():
    fahrenheit = float(input("Introduce la temperatura en Fº: "))
    celsius = (fahrenheit - 32) * 5/9
    celsius = round(celsius, 2)
    tempFinal = "La temperatura en grados celsius es " + str(celsius) + "º"
    return tempFinal

print(far())
