#!/usr/bin/python3
"""
CONVERSION DE DATOS USANDO CONVERSORES 

    str()   : transforma el dato en string
    int()   : intenta transformarlo en número entero
    float() : intenta transformarlo en decimal

"""

a = 5
b = "25"
c = "25.7"

print("Numero : "+str(a))
print(type(b))
print(type(int(b)))
print(type(float(c)))
print(str(int(float(c))))