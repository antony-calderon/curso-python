'''Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal'''

letra = input("Por favor introduce una letra: ")

if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
    print("la letra que digitaste es vocal.")
else:
    print("La letra no es una vocal.")