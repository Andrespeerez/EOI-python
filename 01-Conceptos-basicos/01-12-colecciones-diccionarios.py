#!/usr/bin/python3

vacio = {}
frutas = {
          "NA": "naranja",
          "LI": "limón", 
          "PO": "pomelo", 
          "LM": "lima", 
          "MA": "mandarina",
          }

# mostrar el diccionario
print(frutas)

# mostrar un valor utilizando la clave
# Si la clave no existe se produce una Exception
print(frutas["NA"])


# mostrar un valor utilizando la funcion .get()
# si el valor no existe, la función retorna None
print(frutas.get("NA"))
print(frutas.get("NI")) # None

# modificar el valor de un elemento
frutas["NA"] = "sandia"
frutas.update({"NA": "ciruela"})
print(frutas["NA"])

# insertar un nuevo elemento en el diccionario
frutas["ME"] = "melón"
frutas.update({"KW": "kiwi"})
print(frutas)

# pintar el numero de valores del diccionario
print(len(frutas))

# eliminar un elemento del diccionario
frutas.pop("NA")
print(frutas)

# recorremos y mostramos todos los valores del diccionario
for clave in frutas:
    print(f"{clave} : {frutas[clave]}")