import random
euromillon = set(random.sample(range(1, 51), 5)) 
estrellas = set(random.sample(range(1, 13), 2))
nombre = input("Introduzca su nombre para sacar un boleto del euromillón: ")

boleto = set ()
boleto_estrella = set()
i = 1
seguir="s"
while seguir=="s":

    while i < 6:
        numeros = int(input(f"Introduzca el {i} número: "))
    if numeros < 51 and numeros >= 0 and boleto.count(numeros) == 0:
        boleto.append(numeros)
    i += 1

else:
    print("\nEl máximo es 51 y mínimo 0 y no se pueden repetir números")

i = 1
while i < 3:
    numeros_estrellas = int(input(f"Introduzca la {i} estrella: "))
    if numeros_estrellas < 12 and numeros_estrellas >= 0 and boleto_estrella.count(numeros_estrellas) == 0:
        boleto_estrella.append(numeros_estrellas)
        i += 1
    else:
        print("\nEl máximo es 12 y mínimo 0 y no se pueden repetir")


print(boleto)
print(boleto_estrella)
print (euromillon)
print (estrellas)
print(f"\nEste sería su BOLETO '{nombre}': {boleto}")
print(f"\nY aquí las ESTRELLAS de su boleto: {boleto_estrella}")
print(f"\nEste sería el número del GANADOR del EUROMILLÓN: {euromillon}")
print(f"\nY aquí las ESTRELLAS GANADORAS: {estrellas}")
contador_numero = len(euromillon.intersection(numeros))



