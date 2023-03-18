class A():
    def __init__(self):
        self.__contador = 0
    
    def incremento(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador


a = A()
print(a.cuenta())
a.incremento()
print(a.cuenta())
print(a.__contador)