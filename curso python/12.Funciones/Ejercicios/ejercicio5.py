'''Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio'''

from math import pi

def areaCuadrado(base , altura):
    area = base * altura
    return area

print("El area del cuadrado es:" , areaCuadrado(10 , 5))

def areaCirculo(radio):
    area = pi * pow(radio, 2)
    return area

print("El area del circulo es: " , areaCirculo(5) , "m2")