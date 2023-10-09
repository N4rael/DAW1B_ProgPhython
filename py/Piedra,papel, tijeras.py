from random import randint
num=str(randint(1,3))
if num == "1":
    cpu= "Tijeras"
elif num == "2":
    cpu= "Papel"
elif num == "3":
    cpu= "Piedra" 
else:
    print("error 3")
    exit()

print("Elija uno de los siguientes valores" 
" 1) Piedra "
" 2) Papel"
" 3) Tijeras")

jugador= str(input())

if jugador == "3":
    print("La máquina eligió: " +cpu)
    if cpu == "Tijeras":
        print("Ganaste!")
    elif cpu== "Papel":
        print("Perdiste...")
    elif cpu== "Piedra":
        print("Empate")
    else:
        print("Error 2")
elif jugador == "2":
    print("La máquina eligió: " +cpu)
    if cpu == "Tijeras":
        print("Perdiste...")
    elif cpu== "Papel":
        print("Empate")
    elif cpu== "Piedra":
        print("Ganaste!")
    else:
        print("Error 2")
elif jugador == "1":
    print("La máquina eligió: " +cpu)
    if cpu == "Tijeras":
        print("empate")
    elif cpu== "Papel":
        print("Ganaste!")
    elif cpu== "Piedra":
        print("Perdiste...")
    else:
        print("Error 2")
else:
    print("Error 1")

