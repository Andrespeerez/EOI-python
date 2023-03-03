""""
Requerimientos funcionales:

    Calcular la letra del DNI
    Formula : int(dni % 23)   

"""

letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E', 'T']

print("\n~~~ Calculo de la letra del DNI ~~~\n")
while True:
    try:
        entrada = input("DNI (sin letra): ")
        if(len(entrada) != 8):
            raise Exception("El DNI debe tener 8 digitos")
        
        entrada = int(entrada)
        pos = entrada % 23

    except ValueError as err:
        print("Introduce solo numeros")

    except Exception as err:
        print(err)

    else:
        print(f"\nLa letra del DNI es    :    {letras[pos]}\nTu DNI es {entrada}-{letras[pos]}")
        break

print("\n~~~ Fin del programa ~~~")