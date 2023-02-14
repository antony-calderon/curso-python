'''Escribir un programa que solicite al usuario una vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas'''

vocal = input("Por favor digita una vocal en minuscula: ")
letra = input("Por favor digita una letra en mayuscula: ")

letra2 = letra.upper()
vocal2 = vocal.lower()

print(letra2, vocal2)