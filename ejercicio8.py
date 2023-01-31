# Muestra la media de los 20 primeros números. Redondeada a dos decimales. (Función round).

def media():
    sumar=0
    for i in range(0,20):
        sumar+=i
    print(f"La suma de los 20 primeros numeros de la lista es: {sumar}")
    media=sumar/20
    print(f"La media de {sumar} es: {round(media,2)}")
media()




