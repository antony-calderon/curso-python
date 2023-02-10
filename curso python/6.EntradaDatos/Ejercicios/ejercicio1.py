'''Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”'''


import math
import sys

a = float(input("Por favor introduzca el término a: "))
b = float(input("Por favor introduzca el término b: "))
c = float(input("Por favor introduzca el término c: "))


operacion = float((b**2)-(4*a*c))

if operacion < 0:
    print("La raiz es negativa.")
    sys.exit()
else:
    raiz = math.sqrt(operacion)
    solucion1 = ((-b+raiz)/(2*a))
    solucion2 = ((-b-raiz)/(2*a))

    print("La solución uno es: " ,solucion1)
    print("La solución dos es: " ,solucion2)
