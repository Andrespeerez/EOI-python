#!/usr/bin/python

valor = 0

while ( valor < 5 ) :
    print(f"El valor es {valor}")
    if(valor  == 3):
        break
    valor += 1

print("Fin del WHILE\n")

###############

citricos = ["limon", "naranja", "pomelo", "lima", "mandarina"]

ii = 0

while(ii < len(citricos)):
    print(f"{ii}: {citricos[ii]}")
    ii +=1
else:
    print("Else del WHILE")

print("Fin del WHILE\n")

###############
# DO WHILE emulado

citricos = ["limon", "naranja", "pomelo", "lima", "mandarina"]

ii = 0

while True:
    print(f"{ii}: {citricos[ii]}")
    ii +=1
    if (not ii < len(citricos)):
        break

print("Fin del DOWHILE\n")
