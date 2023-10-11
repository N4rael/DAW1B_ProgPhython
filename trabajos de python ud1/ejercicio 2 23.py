correo = input("Introduce tu correo electrónico: ")
nombre, dominio = correo.split('@')
nuevo_correo = nombre + "@ceu.es"
print("Nuevo correo electrónico:", nuevo_correo)
