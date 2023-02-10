'''Escribir un programa que, dado un número entero, muestre su valor absoluto.'''

numero = int(input("Por favor digita un numero: "))

if numero >= 0:
    print("El valor absoluto es: ", numero)
else:
    numero2 = numero * -1
    print("El valor absoluto es: ", numero2)