'''Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas'''

lista = [7 , 6 , 5 , 4 , 3 , 2 , 1]
print(lista)

def agregar():
    i = 0
    while i < 3:
        numero = int(input("Añade un numero a la lista: "))
        lista.append(numero)
        print(lista)
        i += 1

agregar()

def ordenar(arreglo):
    pares = []
    impares = []
    for i in arreglo:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()    
    impares.sort()
    print(pares)
    print(impares)

ordenar(lista)

