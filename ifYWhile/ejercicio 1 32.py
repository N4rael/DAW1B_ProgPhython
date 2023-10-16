x = int(input("Introduce un número: "))
y = int(input("Introduce otro: "))

if x >= y:
    num_ini = y
    num_fin = x
else:
    num_ini = x
    num_fin = y

while num_ini <= num_fin:
    print(num_ini, end="")
    if num_ini != num_fin:
        print("-", end="")
    num_ini += 1

