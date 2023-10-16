while True:
    num = int(input("Introduce un número: "))

    if 1 <= num <= 10:
        print("Correcto!")
        break
    else:
        print("Inténtalo otra vez! (1-10)")
