'''Escribir una función que reciba un número entero positivo y devuelva su factorial.'''


'''def factorial():
    numeroInicial = int(input("Digita el numero: "))
    numero = numeroInicial

    if numero < 0:
        print("No puede haber factorial de numeros negativos")
    elif numero == 0:
        print("El factorial de cero es 1")
    else:
        facto = 1
        while numero > 1:
            facto *= numero
            print(facto)
            numero -= 1
    print("El factorial de" , numeroInicial , "es" , facto)'''





'''def factorial():
    numero = int(input("Digita un numero: "))
    if numero < 0:
        print("No existe factorial de los numeros negativos.")
    elif numero == 0:
        print("El factorial de 0 es 1.")
    else:
        facto = 1
        for i in range(1 , numero + 1):
            facto *= i
        print(facto)'''


def factorial():
    from math import factorial
    numero = int(input("Digita un numero: "))

    if numero < 0:
        print("No existe factorial de numeros negativos.")
    elif numero == 0:
        print("El factorial de 0 es 1.")
    else:
        print(factorial(numero))
            

factorial()