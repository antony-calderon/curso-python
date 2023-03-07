def saludo():
    print("Hola mundo")

saludo()

def tabla(numero):
    for i in range(11):
        print(numero , "x" , i , "=" , numero * i)

numero = int(input("Digita el numero del que quieres su tabla de multiplicar: "))

tabla(numero)