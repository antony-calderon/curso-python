'''Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, el que haya ingresado, es la letra que debe imprimir el programa'''


alfabeto = ("a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "ñ" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z")

numero = int(input("Por favor digita el numero que quieres consultar: "))

if alfabeto[numero-1]:
    print("La letra numero" , numero , "es:" , alfabeto[numero-1])
else:
    print("La letra con dicho numero no existe.")