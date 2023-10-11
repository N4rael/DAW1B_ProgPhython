"""
    num1 = entero(lee(''Escriba el primer número: ''))
    num2 = entero(lee(''Escriba el segundo número: ''))

    si num1 = num2:
        escribe(''los números no pueden ser iguales'')

    si num1 >= num2
        numMayor = num1
        numMenor = num2
    sino si num2 >= num1:
        numMayor = num2
        numMenor = num1

    dif = numMayor - numMenor
    escribe(f''El número menor es el {numMenor} y entre ellos hay {dif} números enteros.'')
"""

num1 = int(input("Escribe el primer número: " ))
num2 = int(input("Escribe el segundo número: "))

if num1 == num2:
    print("Los números no pueden ser iguales")

if num1 >= num2:
    numMayor = num1
    numMenor = num2
elif num2 >= num1:
    numMayor = num2
    numMenor = num1

dif = numMayor - numMenor
print(f"El número menor es el {numMenor} y entre ellos existen {dif} números enteros.")