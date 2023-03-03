""""
Requerimientos funcionales

    Visualizar la media de opinion 
    Visualizar el numero total de encuestas
    El resultado se muestra al escribir FIN
    El valor de opinión es entre 0 y 10

"""

# Declaracion de variables
encuestas = []

print("\n~~~ Encuestas de Opinion ~~~")

# Toma de datos
while True:
    try:
        opinion = input("Opinion (0 a 10 ó FIN):  ")

        # fin de la toma de datos
        if (opinion == "FIN"):
            break

        opinion = int(opinion) # Error -> ValueError 
        if(opinion > 10 or opinion < 0):
            raise Exception("Numero fuera de rangos! (0 a 10)")
        
    except ValueError:
        print("Introduce un numero\n(Entre 0 y 10, o FIN para terminar)")

    except Exception as err:
        print(f"{err} : ")

    else: # solo si es correcto
        encuestas.append(opinion)

print(f"\n{encuestas}")

# Calculos
numOpiniones = len(encuestas)
try:
    meanValOpiniones = sum(encuestas)/numOpiniones
except Exception as err:
    print(err)
    exit()

# mostrar los resultados de la encuesta
print("\nResultados de las encuestas:")
print(f"Numero total de encuestas registradas   : {numOpiniones}")
print(f"Valor promedio de las encuestas:        : {meanValOpiniones:1.2f}")

print("\n~~~ Fin del programa ~~~")

