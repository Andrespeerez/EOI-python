""""
Requerimientos funcionales

    Visualizar la media de opinion 
    Visualizar el numero total de encuestas
    El resultado se muestra al escribir FIN
    El valor de opinion es entre 0 y 10
    Se registra la edad
    Visualizaremos promedio por grupos de edad
        Menor 18, 18-55, Mayor 55

"""

# declaracion de variables
encT = []

encMenor18 = []
enc18y55 = []
encMay55 = []

print("\n~~~ Encuestas de Opinion ~~~")

# lectura de encuestas
while True:
    try:
        opinion = input("Opinion (0 a 10 ó FIN):  ")

        # Fin de toma de datos
        if (opinion == "FIN"):
            break
         
        opinion = int(opinion) # conversion
        if(opinion > 10 or opinion < 0):
            raise Exception("Numero fuera de rangos! (0 a 10)")
        
        edad = input("¿Cuantos años tienes?  : ")
        if(not edad.isdigit()):
            raise Exception("No has introducido una edad valida")
        else:
            edad = int(edad)

    except ValueError:
        print("Introduce un numero\n(Entre 0 y 10, o FIN para terminar)") 

    except Exception as err:
        print(f"{err} : ")

    else: 
        encT.append(opinion)

        # Añadir encuesta en su grupo de edad
        if(edad < 18 ):
            encMenor18.append(opinion)
        elif(edad > 55):
            encMay55.append(opinion)
        else:
            enc18y55.append(opinion)

# Mostrar listas de encuestas registradas
print(f"\n{encT}")
print(f"\n{encMenor18}")
print(f"\n{encMay55}")
print(f"\n{enc18y55}")

# Calculos de numero de encuestas y media
numOpT = len(encT)
numOpMen18 = len(encMenor18)
numOpMay55 = len(encMay55)
numOp18y55 = len(enc18y55)

# media de edad
try:
    meanValT = sum(encT)/numOpT
    if(numOpMen18 != 0):
        meanValMen18 = sum(encMenor18) / numOpMen18
    if(numOpMay55 != 0):
        meanValMay55 = sum(encMay55) / numOpMay55
    if(numOp18y55 != 0):
        meanVal18y55 = sum(enc18y55) / numOp18y55
except Exception as err:
    print(err)
    exit()

# Resultados totales de las encuestas:
print("\nResultados de las encuestas:")
print(f"Numero total de encuestas registradas   : {numOpT}")
print(f"Valor promedio de las encuestas:        : {meanValT:1.2f}")

# Opiniones por edades:
# Comprobar que haya valores y mostrar la informacion
if(numOpMen18 != 0):
    print("\nMenores de 18 :")
    print(f"Numero encuestas registradas   : {numOpMen18}")
    print(f"Valor promedio de las encuestas: {meanValMen18:1.2f}")

if(numOp18y55 != 0):
    print("\nEntre 18 a 55 años :")
    print(f"Numero encuestas registradas   : {numOp18y55}")
    print(f"Valor promedio de las encuestas: {meanVal18y55:1.2f}")

if(numOpMay55 != 0):
    print("\nMayores de 55 :")
    print(f"Numero encuestas registradas   : {numOpMay55}")
    print(f"Valor promedio de las encuestas: {meanValMay55:1.2f}")

print("\n~~~ Fin del programa ~~~")