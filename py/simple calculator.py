
print("Escriba el primer número")
first_number=int(input())

print ("Escriba el segundo número")
second_number=int(input())

print ("Escriba el signo (+, -, *, /)")
sing= str(input())

if sing == "+":
        print(first_number + second_number)
elif sing == "-":
    print(first_number - second_number)
elif sing == "*":
    print(first_number * second_number)
elif sing == "/":
    print(first_number / second_number)
else:
    print("Syntax error")
    exit