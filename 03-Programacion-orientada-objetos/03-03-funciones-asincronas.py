import asyncio

##############################
# ejecucion sincrona

def mainsin():
    print("Hola ...")
    print("... mundo!!")

print("Inicio")
mainsin()
print("Final")

##############################
# ejecucion asincrona

async def main():
    print("\nInicio main...")
    await asyncio.gather(func1(), func2())
    print("... fin main!")

async def func1():
    for ii in range(11):
        print(ii)
        await asyncio.sleep(1)

async def func2():
    print("Hola...")
    await asyncio.sleep(5)
    print("... Mundo!")

print("Inicio")
asyncio.run(main())
print("Final")