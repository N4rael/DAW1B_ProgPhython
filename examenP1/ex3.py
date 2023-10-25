"""
Escribe un programa en Python que lea una palabra y la encripte:

    1. Pedir la palabra hasta que cumpla que tiene un mínimo de 8 letras.
    
    2. Después, transformar o encriptar la palabra de la siguiente manera:
        - Sin bucles, pero escribiendo varias instrucciones si lo necesitáis.
        - Eliminar espacios.
        - Consonantes a mayúsculas
        - La vocal a pasa a ser una @.
        - La vocal e pasa a ser un 3.
        - La vocal i pasa a ser un 1.
        - El resto de vocales serán minúsculas.
        - Si tiene solo 8 letras, añade un * al principio y un # al final.

    3. Ejemplos:

    > Introduzca una palabra: Pedro PAblO    1984
    > Su palabra encriptada es P3DRoP@BLo1984

    > Introduzca una palabra: ArIADNa2
    > Su palabra encriptada es *@R1@DN@2#

    > Introduzca una palabra: USER       89
    > Introduzca una palabra *mínimo 8 letras*: USER  893465
    > Su palabra encriptada es uS3R893465

"""

def encriptar_palabra(palabra):
    palabra = palabra.replace(" ", "").upper()
    
    palabra = palabra.replace("A", "@" "E", "3").replace("I", "1").replace("O", "o").replace("U", "u")
    
    if len(palabra) == 8:
        palabra = "*" + palabra + "#"
    
    return palabra

while True:
    palabra = input("Introduzca una palabra: ")
    
    if len(palabra) >= 8:
        palabra_encriptada = encriptar_palabra(palabra)
        print(f"Su palabra encriptada es {palabra_encriptada}")
        break
    else:
        print("Introduzca una palabra *mínimo 8 letras*.")



