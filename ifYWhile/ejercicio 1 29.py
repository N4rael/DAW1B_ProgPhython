"""
nombre = lee(''Escribe un nombre: '')
edad = lee(''Escribe una edad entre 0 y 125 años'')

si nombre = vacio:
    nombre = 'desconocido'

mientras que edad = vacio:
    edad = lee(''Escribe una edad entre 0 y 125 años'')

edad = entero(edad)

mientras que 0 > edad:
    escribe('La edad debe ser entre 0 y 125 años')
    edad = entero(lee(''Escribe una edad entre 0 y 125 años''))

mientras que edad > 125:
    escribe('La edad debe ser entre 0 y 125 años')
    edad = entero(lee(''Escribe una edad entre 0 y 125 años''))

teQueda = 125 - edad

si teQueda == 1:
    escribe('Te llamas nombre y tienes años, te queda 1 año por cumplir')
sino teQueda == 0:
    escribe('Te llamas nombre y tienes años, este es tu ultimo año de vida')
sino:
    escribe('Te llamas nombre y tienes años, te quedan teQueda años por cumplir')
"""
nombre = input("Escribe un nombre: ")
edad = (input("Escribe una edad entre 0 y 125 años: "))

if nombre == "":
    nombre = "Desconocido"

while edad == "":
    edad = (input("Escribe una edad entre 0 y 125 años: "))


edad = int(edad)

while 0 > edad:
    print("La edad no puede ser menor de 0 o mayor de 125")
    edad = int(input("Escribe una edad entre 0 y 125 años: "))

while edad > 125:
    print("La edad no puede ser menor de 0 o mayor de 125")
    edad = int(input("Escribe una edad entre 0 y 125 años: "))

teQueda = 125 - edad

if teQueda == 1:
    print(f"Te llamas {nombre} y tienes {edad} años, te queda 1 año por cumplir")
elif teQueda == 0:
    print(f"Te llamas {nombre} y tienes {edad} años, este es tu último año de vida")
else:
    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {teQueda} años por cumplir")