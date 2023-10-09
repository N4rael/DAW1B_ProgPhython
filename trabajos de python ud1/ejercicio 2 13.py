n = int(input("Escribe un número entero: "))
m = int(input("Escriba otro número entero: "))

c = round((n / m), 3) 
r = (n % m)

print("La división de " + str(n) + " y de " + str(m) +
      " de un cociente " + str(c) + " y un resto de " + str(r))