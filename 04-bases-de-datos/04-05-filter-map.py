numeros = [1, 85, 200, 15, 152, 450, 5, 3601, 63, 77, 8]

print(f"Valores mayores de 100: ", list(filter(lambda x : x > 100, numeros)))

print("\n(========================)\n")

def Procesar(lista):
    resultado = []
    for numero in lista:
        resultado.append(numero * 10)

    return resultado

print(numeros)
print(Procesar(numeros))

# la funcion map() puede hacer lo mismo
print(list(map(lambda x : x * 10, numeros)))

# combinacion map() y filter()
print(list(map(lambda x : x * 10, filter(lambda x : x > 100, numeros))))