class A():
    def __init__(self):
        self._contador = 0

    def incremento(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador

a = A()

print(a.cuenta())
a.incremento()
print(a._contador) # el guion bajo solo advierte a otro programador que se trata de un atributo privado y que no deberia invocarlo de esta manera