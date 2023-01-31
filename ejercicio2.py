# 2. Pide al usuario su nombre y apellidos y muestralo letra a letra

def nombreApellidos():
    nombre=input("Introduce tu nombre y apellidos: ")   
    i=0
    while i<len(nombre):
        print(nombre[i],end=",")
        i+=1

nombreApellidos()



