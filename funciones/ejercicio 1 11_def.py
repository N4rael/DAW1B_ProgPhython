def suma(num):
    suma = (((num + 1) * num )/2)
    str(suma)
    return suma

num = int(input("Introduce un número para la suma: "))

# la división siempre va a devolver un valor float
print("El resultado de la suma es " + str(suma(num)))