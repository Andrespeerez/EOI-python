numeros = [40, 38, -35, 8, 98, 102]

def demo1(lista):
    for ii in lista:
        yield ii * 5

generador = demo1(numeros)

print(next(generador))
print(next(generador))

print("\nRecorrer con for:")
generador = demo1(numeros)
for i in generador:
    print(f"Generador1 >> {i}")

print()
# La forma alternativa de crear el generador
generador2 = ( ii * 5 for ii in numeros)
for ii in generador2:
    print(f"Generador2 >> {ii}")