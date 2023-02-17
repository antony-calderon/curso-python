'''Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares'''

numero1 = int(input("Digita el primer numero: "))
numero2 = int(input("Digita el segundo numero: "))

if numero1 % 2 == 0:
    numero1 += 1
    for i in range(numero1 , numero2 + 1 , 2 ):
        print(i)
else:
    for i in range(numero1 , numero2 + 1 , 2):
        print(i)