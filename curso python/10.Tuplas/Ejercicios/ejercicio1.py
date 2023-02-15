'''Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla'''


meses = ("Enero" , "Febrero" , "Marzo" , "Abril" , "Mayo" , "Junio" , "Julio" , "Agosto" , "Septiembre" , "Octubre" , "Noviembre" , "Diciembre")

mes = int(input("Por favor digita el numero del mes que quieres consultar: "))

if meses[mes-1]:
    print("El mes numero" , mes , "es:" , meses[mes-1])
else:
    print("El mes numero", mes , "No existe.")