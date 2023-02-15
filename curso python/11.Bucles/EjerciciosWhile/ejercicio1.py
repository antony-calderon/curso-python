'''Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero'''

numero = int(input("Por favor digita el numero del que deseas la tabla de multiplicar: "))
i = 0
while i < 10:
    i += 1
    print(numero , "x" , i , "=" , numero*i)