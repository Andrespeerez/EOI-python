#!/usr/bin/python3

# usamos los [] para crear listas
vacia = []
frutas = ["naranja", "limón", "pomelo", "lima", "mandarina"]

print("Mostrar cosas en listas")
# mostrar el contenido de una lista
print(frutas)

# mostrar el valor contenido en una posición
print(frutas[2])

# mostrar el numero de elementos que contiene la lista
print(len(frutas))

# mostrar el numero de veces que tenemos un valor
print(frutas.count("sandia"))

print("\nModificar listas")
# modificar el valor en una posicion
frutas[2] = "fresa"
print(f"Donde teníamos pomelo ahora tenemos : {frutas[2]}")

# añadir nuevos valores a lista utilizando .append()
frutas.append("manzana")
frutas.append("melón")
print(frutas)

# añadir si el valor no existe
if("platano" not in frutas):
    frutas.append("platano")
    print(frutas)

# añadir varios valores procedentes de otra lista
nuevasFrutas = ["maracuya", "kiwi", "frambuesa"]
frutas.extend(nuevasFrutas)
print(frutas)

# insertar una fruta en una posición concreta
frutas.insert(1, "sandia")
print(frutas)

print()
print("Eliminar elementos en la lista")
# eliminar un valor en base a la posición en base a .pop(index)
frutas.pop(5)
print(frutas)

# eliminas un valor en base a .remove(valor)
frutas.remove("naranja")
print(frutas)

# eliminar un valor si existe
if("sandia" in frutas):
    frutas.remove("sandia")
    print(frutas)

print()
print("Invertir el orden de la lista")
# invertir el orden de los valores
frutas.reverse()
print(frutas)

print()
print("Ordenar los valores de la lista")
# ordenar los valores con sort
frutas.sort()
frutas.sort(reverse = True) # ordenar y invertirlo

# recorrer la lista 
for fruta in frutas:
    print(fruta)

# copiar todos los valores de la lista 
vacia = frutas.copy()

# eliminar todos los valores de la lista
frutas.clear()
print(f"Todos los valores eliminados : {frutas}")