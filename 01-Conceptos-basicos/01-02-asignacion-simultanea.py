#!/usr/bin/python3

"""
ASIGNACION SIMULTANEA DE VARIABLES

    SINTAXIS : <Var1>, <Var2>, <Var3> = <valor1>, <valor2>, <valor3>

    Las referencias y valores están separados por comas

    Ejemplo:

"""

a = 5
b = 10

# intercambiar los valores de las variables
a, b = b, a 

print("Asignación simultanea de a y b:")
print(a)
print(b)

"""
La asignación se realiza simultaneamente.
Sin necesidad de volcar la información en una variable temporal.
"""