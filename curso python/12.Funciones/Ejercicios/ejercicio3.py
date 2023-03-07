'''Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0'''

def peticion():
    numero1 = int(input("Digita el primer numero: "))
    numero2 = int(input("Digita el segundo numero: "))

    if numero1 > numero2:
        return 1
    elif numero2 > numero1:
        return -1
    else:
        return 0

print(peticion())