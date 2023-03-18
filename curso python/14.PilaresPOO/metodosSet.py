class A():
    def __init__(self):
        self._contador = 0
        self._cuenta = 10

    @property
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter
    def cuenta(self , cuenta):
        self._cuenta = cuenta

    @property
    def contador(self):
        return self._contador

a = A()

print(a.cuenta)
print(a.contador)
a.cuenta = 20
print(a.cuenta)