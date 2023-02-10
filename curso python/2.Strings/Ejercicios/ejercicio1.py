'''Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.'''

cadena = "Te quiero solo como amigo"
cadena2= ""


print(cadena[:3])
print(cadena[len(cadena)-3:])

for n in range(0, len(cadena), 2):
    cadena2 += cadena[n]
print(cadena2)

print(cadena[::2])

print(cadena[::-1])

print(cadena + cadena[::-1])

