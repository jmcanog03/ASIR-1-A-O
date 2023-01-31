# 4. Pide al usuario un Número y comprueba si el número está en la lista anterior.


lista=[]
def imprimir20numeros():
        for i in range(0,20):
            lista.append(i)
           
        print(lista)
imprimir20numeros()

numero=int(input("Introduce un numero: "))
def listanumero4():
    if numero in lista:
        print("El numero esta en la lista")
    else:
        print("El numero no esta en la lista")

listanumero4()