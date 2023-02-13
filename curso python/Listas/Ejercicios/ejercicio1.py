'''En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]'''

lista = [20, 50, "Curso", 'Python', 3.14]
print(lista)

print("AÑADE DOS VALORES A LA LISTA, UNO AL INICIO Y UNO AL FINAL")

primerValor = input("Por favor digita el primer valor: ")

segundoValor = input("Por favor digita el segundo valor: ")

lista[0] = primerValor

lista[1] = segundoValor

'''lista.insert(0 , primerValor)
lista.append(segundoValor)'''

print(lista)
