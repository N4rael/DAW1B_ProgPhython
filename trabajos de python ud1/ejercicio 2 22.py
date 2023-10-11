frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

if len(vocal) == 1 and vocal in "aeiouAEIOU":
    frase_modificada = frase.replace(vocal.lower(), vocal.upper())
    print("Frase con la vocal en mayúscula:", frase_modificada)
else:
    print("Por favor, introduce una vocal válida.")
