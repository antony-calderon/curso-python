'''Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras'''

for i in range(1 , 11):
    print(i)

print("A CONTINUACION DIGITA EL RANGO ENTRE 1 Y 10")

numero1 = int(input("Digita el primer numero: "))
numero2 = int(input("Digita el segundo numero: "))

for i in range(numero1 , numero2+1):
    print(i)