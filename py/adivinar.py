#la máquina elige un número
from random import randint
num=int(randint(1,100))
#el usuario elige un numero
print(num)
print("Elige un numero:")
num2=int(input())
#el número de intentos
trynum= 1

while(num != num2):
    print("Intentalo de nuevo")
    trynum = (trynum + 1)
    diferencia = abs((num) - (num2))
    if diferencia <= 30:
        print("Caliente caliente")
    else:
        print("Frio frio")
    num2=int(input())



print("Acertaste!")
if (trynum == 1):
    print("Acertaste en tu primer intento")
else:
    print("Acertaste en " + str(trynum) + " intentos")