#funcion da la vuelta al numero
#
def funcion():
    numOp = abs(num1)
    string = f"{num1} -> {num1} + "
    cont = 1
    while (cont <= numOp):
        string = string + str(numOp - cont) + " + "
        string = string + str(numOp - cont)  
        cont += 1
    string = string + " = " + str(numOp)
    return string


num1 = int(input("Num1: "))


while (num1 > 100 or num1 < -100):
        print("El número debe de ser menor que 100 y mayor que -100: ")
        num1 = int(input())

print(funcion())