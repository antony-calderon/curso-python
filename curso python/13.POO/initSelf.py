class FabricaTelefonos():
    marca = "samsung"

    def elaborarhuawei(self):
        self.marca = "huawei"

telefono = FabricaTelefonos()
print(telefono.marca)
telefono.elaborarhuawei()
print(telefono.marca)

print("******************************************************")

class FabricaCarros():
    def __init__(self , marca , color):
        self.marca = marca
        self.color = color

carro = FabricaCarros("Chevrolet" , "negro")
print(carro.color)
print(carro.marca)
        