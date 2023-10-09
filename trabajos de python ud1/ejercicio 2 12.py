estatura = float(input("Escriba su estatura en metros: "))
peso = float(input("Escriba su peso en Kg: "))

estatura2= (estatura**2)
imc = round((peso / estatura2), 2)

print("Su IMC es: " + str(imc))