nombre = input("Por favor, introduce tu nombre: ")
numero = int(input("Introduce un número entero: "))

for _ in range(numero):
    print(nombre)
    
nombre_minusculas = nombre.lower()
nombre_mayusculas = nombre.upper()
nombre_capitalizado = nombre.title()

print("Nombre en minúsculas:", nombre_minusculas)
print("Nombre en mayúsculas:", nombre_mayusculas)
print("Nombre capitalizado:", nombre_capitalizado)
