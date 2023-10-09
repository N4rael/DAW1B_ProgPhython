# Inicializar la variable que acumulará la suma de las notas
suma_notas = 0
num_notas = input("numero de notas")
# Solicitar al usuario las 10 notas
print("Dame las 10 notas del curso:")

# Bucle para leer las 10 notas y acumular la suma
for i in range(int(num_notas)):
    nota = float(input())
    suma_notas += nota

# Calcular la media dividiendo la suma de las notas por 10
media = suma_notas / 10

# Mostrar el resultado
print("La media es", media)