# 1. Crea una función que calcule el área de un cuadrado.

from ast import main
import math
# def areacuadrado():
#     lado=int(input("ingrese el lado del cuadrado: "))
#     area=a*a
#     print(f"\nEl área del cuadrado es: {area}")
# areacuadrado()

# def areaCuadrado(lado):
#     return lado*lado

# ladoUsuario = int(input("Introduce el lado del cuadrado: "))
# print("El aŕea es: ",areaCuadrado(ladoUsuario))


# 2. Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro. 

#include <stdio.h>
#define PI 3.1416 /* definición de constante */
# int main () {
# float perim, radio; int dos=2;
# printf(" Calcula el perímetro de una circunferencia");
# printf(" Indique el tamaño de radio de la circunferencia");
# scanf("%f", &radio);
# perim= dos*PI*radio;
# printf(" El perímetro de la circunferencia es %f", perim);
# printf("Valores utilizados para calcular el perímetro:");
# printf(" Constante PI=%f, valor de dos = %d, radio=%f ",
# PI, dos,radio);
# return 0;
# }


# 3. Desarrolla una función que pida al usuario si quiere calcular el área de un cuadrado o el de un círculo. Dependiendo de lo que introduzca se hará una cosa o la otra.

# def circulo():
#     lado=int(input("ingrese el lado del cuadrado: "))
#     area=lado*lado
#     radio=int(f"El radio es: "+str(math.sqrt(area / math.pi/2)))
#     circulo=int(f"El circulo es:"+str(math.pi*radio))
#     escoger=input("Que quieres calcular el área o el circulo")
#     if area != radio():
#         print(f"Has elegido calcular el área: {area}")
#     else:
#         print(f"Has elegido calcular el circulo: {circulo}")

# circulo()



# 3


def edades():
    edad_como_cadena = input("Dime tu edad: ")
    edad = int(edad_como_cadena)
    if edad >= 0 and edad <= 2:
        print("Bebé")
    elif edad >= 3 and edad <= 11:
        print("Niño")
    elif edad >= 12 and edad <= 17:
        print("Adolescente")
    elif edad >= 18 and edad <= 64:
        print("Adulto")
    elif edad >= 65:
        print("Anciano")
    else:
        print("Edad inválida")
edades()