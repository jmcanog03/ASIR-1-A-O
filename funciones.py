# # Funcion def
# def saludar():
#     print("Hola a todos")
#     print("Estamos en clase de ISO")
#     print("Hoy solo tenemos una hora")


# saludar()
# print("*******************************************")

# # Función def con argumento

# def saludarconargumento(nombre):
#     print(f"Hola {nombre}")
# nombre=input("Introduce tu nombre: ")
# saludarconargumento(nombre)

# print("\n**************************************")
# # Ejercio 1

# def saludanombreApellidos(nombre,apellido1,apellido2):
#     print(f"\nHola {nombre} , tu 1º apellido es '{apellido1} y tu 2º apellido es {apellido2}'")

# nom=input("Introduzca su nombre: ")
# ape1=input("Introduce tu 1º apellido: ")
# ape2=input("Introduce tu 2º apellido: ")

# saludanombreApellidos(nom,ape1,ape2)

# print("\n***********************************************")

# Ejercicios con funciones 


# def imprimir20numeros():
#         for i in range(0,20):
#             print(i,end=",")

# imprimir20numeros()

# 2. Pide al usuario su nombre y apellidos y muestralo letra a letra

# def nombreApellidos():
#     nombre=input("Introduce tu nombre y apellidos: ")   
#     i=0
#     while i<len(nombre):
#         print(nombre[i],end=",")
#         i+=1


# nombreApellidos()



# 3. Crea una lista con los 20 primeros números. (Del 1 al 19). Recorre la lista con un for y con un while.

def listaNumero():
     lista=[]
     for i in range(0,21):
        lista.append(i)
     print(lista)

listaNumero()


# 4. Pide al usuario un Número y comprueba si el número está en la lista anterior.

def listanumero4():
    lista=[]
    numero=int(input("Introduce un numero: "))
    for i in range(0,20):
        lista.append(i)
    if numero in lista:
        print("El numero esta en la lista")
    else:
        print("El numero no esta en la lista")
listanumero4()

# lista=[]
# def anadirElemento(i):
#     lista.append(i)
# a=6
# anadirElemento(6)
# print(lista)
# a=8
# anadirElemento(a)
# print(lista)