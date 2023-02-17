'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''

def factura():
    cantidadSinIva = float(input("Digita el valor de la compra: "))
    iva = int(input("Digita el porcentaje del iva: "))

    valorIva = (cantidadSinIva * iva)/100
    total = cantidadSinIva + valorIva

    return total

print(factura())