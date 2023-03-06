#!/usr/bin/python3

import json

frutas = ["limón", "pomelo", "pera", "naranjas", "ciruelas"]

frutasJSON = json.dumps(frutas)

# Esto es un objeto lista
print(frutas)
print(type(frutas))

# Esto es un string
print()
print(frutasJSON)
print(type(frutasJSON))

frutas2 = json.loads(frutasJSON)

# comprobamos que podemos recuperar el objeto a partir del JSON
print()
print(frutas2)
print(type(frutas2))

