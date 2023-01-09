import random
euromillon = random.sample(range(1, 51), 5)
estrellas = random.sample(range(1, 13), 2)
nombre = input("Introduzca su nombre para sacar un boleto del euromillón: ")

boleto = []
boleto_estrella = []
i = 1

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


boleto.sort()
boleto_estrella.sort()
euromillon.sort()
estrellas.sort()
print(f"\nEste sería su BOLETO '{nombre}': {boleto}")
print(f"\nY aquí las ESTRELLAS de su boleto: {boleto_estrella}")
print(f"\nEste sería el número del GANADOR del EUROMILLÓN: {euromillon}")
print(f"\nY aquí las ESTRELLAS GANADORAS: {estrellas}")
contador_numero = euromillon.count(boleto[i])
contador_estrella1 = estrellas.count(boleto_estrella[0])
contador_estrella2 = estrellas.count(boleto_estrella[1])
i = 0

while i<1:
    if contador_numero!=euromillon:
        print(f"\nHa acertado {contador_numero} números del euromillón")
        i+=1
    elif contador_numero==euromillon:
        print(f"\n¡ENHORABUENA! {nombre} HA GANADO EL EUROMILLÓN.")
        i+=1

veces=1
i=0

while i<1:
    if contador_estrella1!=1 and contador_estrella2!=1:
        print(f"\nHa acertado 0 estrellas")
        i+=1
    elif contador_estrella1==1 and contador_estrella2==1:
        print(f"ºn¡ENHORABUENA! HA ACERTADO {veces+2} ESTRELLAS.")
        i+=1
    
    else:
        print(f"\nHa acertado {veces} estrella.")

