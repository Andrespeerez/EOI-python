# pos 0 = numero
# pos 1 = numero
# pos 2 = texto con operacion a realizar:
#       sum para +
#       res para -
#       mul para *
#       div para /

def calcular(*args):
    try:
        if (args[2] == "sum" ):
            return args[0] + args[1]
        if (args[2] == "res" ):
            return args[0] - args[1]
        if (args[2] == "mul" ):
            return args[0] * args[1]
        if (args[2] == "div" ):
            return args[0] / args[1]
    except ZeroDivisionError:
        print("División por cero >> return None")


operaciones = ["sum", "res", "mul", "div"]
num1 = 2
num2 = 3
for ii in operaciones:
    print(calcular(num1,num2,ii))

print("\nManejar excepcion:")
print(calcular(num1, 0,"div"))
