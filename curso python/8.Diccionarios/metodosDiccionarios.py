diccionario = {1 : 'a' , 2 : 'b' , 3 : 'c'}
print(diccionario)

diccionario2 = {3 : 'c' , 4 : 'd' , 5 : 'e'}
diccionario.update(diccionario2)
print(diccionario)

print(diccionario.get(2))

print(diccionario.pop(3))
print(diccionario)

print(diccionario.copy())