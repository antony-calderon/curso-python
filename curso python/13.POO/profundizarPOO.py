class FabricaTelefonos():
    def __init__(self , marca , peso , *colores , **modelos):
        self.marca = marca
        self.colores = colores
        self.peso = peso
        self.modelos = modelos
     

telefono = FabricaTelefonos("Alcatel" , 100 , "negro" , "rojo" , "azul" , m1 = 200 , m2 = 500)
print(telefono.marca)
print(telefono.peso)
print(telefono.colores)
print(telefono.modelos)

#Atributos temporales
telefono.memoria = 500
print(telefono.memoria)