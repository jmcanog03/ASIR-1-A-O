# Funcion def
def saludar():
    print("Hola a todos")
    print("Estamos en clase de ISO")
    print("Hoy solo tenemos una hora")


saludar()
print("*******************************************")

# Función def con argumento

def saludarconargumento(nombre):
    print(f"Hola {nombre}")
nombre=input("Introduce tu nombre: ")
saludarconargumento(nombre)

print("\n**************************************")
# Ejercio 1

def saludanombreApellidos(nombre,apellido1,apellido2):
    print(f"\nHola {nombre} , tu 1º apellido es '{apellido1} y tu 2º apellido es {apellido2}'")

nom=input("Introduzca su nombre: ")
ape1=input("Introduce tu 1º apellido: ")
ape2=input("Introduce tu 2º apellido: ")

saludanombreApellidos(nom,ape1,ape2)

print("\n***********************************************")

# 2º Ejercicio con funcion return 

