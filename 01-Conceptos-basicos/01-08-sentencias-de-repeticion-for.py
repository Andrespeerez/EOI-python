#!/usr/bin/python

for i in range(0, 100, 1):
    print(f"Número {i}")

citricos = ["limon", "naranja", "pomelo", "lima" ]
print()
print(citricos)
print(citricos[0]) # primer valor en la lista
print(f"Numero de valores en la coleccion citricos {len(citricos)}")
print()

print("\nRecorriendo la coleccion usando in: \n")
for fruta in citricos:
    print(f"{fruta}")

print("\nUsando range: \n")
for i in range(0, len(citricos), 1):
    print(f"{i} : {citricos[i]}")