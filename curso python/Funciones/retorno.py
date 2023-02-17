def entero():
    print("Este es un valor entero: ")
    return 10

def flotante():
    print("Este es un valor flotante: ")
    return 8.2

def frase():
    return "Yo soy Antony."

def asignacion():
    return 1 , 2 , 3 , 4 , 5

print(entero())
print(flotante())
print(frase())

a , b , c , d , e = asignacion()

print(a)
print(b)
print(c)
print(d)
print(e)