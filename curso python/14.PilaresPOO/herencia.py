class Animales():
    def hablar(self):
        print("Yo soy un animal.")

    def descripcion(self):
        print("Yo soy un {}".format(self.animal))

class Perro(Animales):
    pass

class Gato(Animales):
    def __init__(self , animal):
        self.animal = animal


animal = Animales()
animal.hablar()

perro = Perro()
perro.hablar()

gato = Gato("gato")
gato.descripcion()