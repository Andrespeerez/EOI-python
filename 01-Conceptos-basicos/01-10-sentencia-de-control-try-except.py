#!/usr/bin/python3

num1 = 0
num2 = 100

print("Inicio")

try:
    num3 = num2 / num1
    print(f"Resultado : {num3}")
except:
    print("Algo salio mal")
else:
    print("Bloque ELSE")
finally:
    print("Bloque finally")

print("Fin\n")

#######################
# Errores ZeroDivisionError

try:
    num3 = num2 / num1 # error ZeroDivisionError
    print(f"Resultado : {num3}")
except ZeroDivisionError as err:
    print("Has intentado dividir por cero")
    print(err.args)
except:
    print("Algo salio mal")
else:
    print("Bloque ELSE")
finally:
    print("Bloque finally")

#################
# Error FileNotFoundError

print()

try:
    f = open('noexiste.txt') # error FileNotFoundError
except FileNotFoundError as err:
    print("Has intentado abrir un archivo que no existe")
    print(err)
except:
    print("Algo salio mal")
else:
    print("Bloque ELSE")
finally:
    print("Bloque finally")

#################
# Error propio

print()

try:
    raise Exception("Error fantabuloso")
except Exception as err:
    print(err)
else:
    print("Bloque ELSE")
finally:
    print("Bloque finally")