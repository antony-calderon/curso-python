class Animales():
    def __init__(self , mensaje):
        self.mensaje = mensaje
    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago Guau!")

class Gato(Animales):
    def hablar(self):
        print("Yo hago miau!")

class Pez(Animales):
    def hablar(self):
        print("Nada")

animal = Animales("Nada")
animal.hablar()

perro = Perro("Perringo")
perro.hablar()

gato = Gato("Gatingo")
gato.hablar()

pez = Pez("Pezingo")
pez.hablar()
