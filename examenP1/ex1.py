"""
Escribe un algoritmo en pseudocódigo que lea un número y te diga si es par o impar.
El número no puede ser negativo ni mayor de 10, en tal caso solo mostrará un mensaje de error.
"""

"""
Inicio

escribe "Escribe un número: "
lee num1

si (num1 < 0 or num1 > 10):
    escribe "El número no puede ser negativo o mayor de 10"

# Saca el resto al dividir el número entre 2, si es 0 será par, si es 1 será impar, 
# ya que no puede superar el 10, o ser negativo, ese patrón siempre se repite.
    
resto = (num1 % 2)

si (resto = 0)
    escribe "El número es par"

sino
    escribe "El número es impar"

Fin
"""
