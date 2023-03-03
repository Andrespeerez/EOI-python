"""
Mostrar tabla de multiplicar del número indicado por el usuario
Resolver con un **for** y también con un **while**
"""

print("Dame un número entero:")
entrada = input()

try:
    numero = int(entrada)
except:
    print("Introduce un número")
    exit()

print("\nTabla de multiplicar con for:")
for ii in range(1, 11, 1):
    print(ii*numero)

print("\nTabla de multiplicar con while:")
ii = 1
while(ii < 11):
    print(ii*numero)
    ii += 1
