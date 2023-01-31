""" def imprimir20Numeros(): 
    for i in range(0,20):
       print(i, end=", ")

imprimir20Numeros() """

""" def imprimirNNumeros(n): 
    for i in range(0,n):
       print(i, end=", ")
 """

""" def imprimirRango(n,m): 
    for i in range(n,m):
       print(i, end=", ")

a = int(input("Introduzca el principio: "))
b = int(input("Introduzca el fin: "))
imprimirRango(a,b+1) """

def mostrarMensajeFin():
    print("Hemos acabado")

def imprimirYSumarRango(n,m):
    suma=0 
    for i in range(n,m):
       print(i, end=", ")
       suma+=i
    mostrarMensajeFin()
    return suma
print(imprimirYSumarRango(3,8))
print(imprimirYSumarRango(2,9))
print(imprimirYSumarRango(1,5))



