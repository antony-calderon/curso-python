'''Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''

edad = int(input("Por favor digita tu edad: "))
i = 0

while i < edad:
    i += 1
    if i == 1:
        print(i , "año.")
    else:
        print(i , "años.")