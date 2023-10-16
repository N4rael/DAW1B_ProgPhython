print("¿Cuántas notas vas a introducir? ")
total = int(input())

while total < 1 or total > 100:
    print("Error - el número de notas debe ser un número entero entre 1 y 100")
    print("¿Cuántas notas vas a introducir? ")
    total = int(input())

print(f"Dame las {total} notas del curso: ")

media = 0.0
cont = 1
while cont <= total:
    nota = float(input())
    media += nota
    cont += 1

media = media / total
print(f"La media es {media:.2f}")
