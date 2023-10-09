payaso = 112
muneca = 75

numPaya = int(input("Cúantos payasos tiene el paquete? : "))

numMune = int(input("Cuántas muñecas tiene el paquete? : "))

pesoPaya = (payaso * numPaya)

pesoMune = (muneca * numMune)

pesoPaquete = round(((pesoPaya + pesoMune)/ 1000), 2)

print("El peso total del paquete es de " + str(pesoPaquete) + 
                                               " Kg")
