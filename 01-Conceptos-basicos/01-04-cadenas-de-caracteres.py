#!/usr/bin/python3
"""
CADENAS DE CARACTERES
"""

cadena = "    hoLa muNDo !!!"

print(cadena)
print(cadena[2])
print(cadena[2:])
print(cadena[:6])
print(cadena[2:6])
print(cadena[-2])
print(len(cadena))

print()
# Funciones de la clase String
print(cadena.lower())
print(cadena.upper())
print(cadena.capitalize())
print(cadena.strip())
print(cadena.replace('o', '0'))
print(cadena.isdigit())
print("57".isdigit())
print(cadena.count('o'))

print()

# Dandole formato a una cadena de caracteres
mensaje = "Mundo"

print("Hola "+mensaje+" !!!") # forma mala
print("Hola {} !!!".format(mensaje)) # más adecuado
print("Hola {s} !!!".format(s=mensaje))
print("Hola {mensaje} !!!")  # no funcionaría
print(f"Hola {mensaje} !!!") # la mejor, como en javascript

resultado = "Hola {s} !!!".format(s=mensaje)

print()
# Dandole formato a números
numero = 10 / 3
print("Numero : {n}".format(n=numero))
print("Numero : {n:1.2f}".format(n=numero)) # dos digitos para la parte decimal
