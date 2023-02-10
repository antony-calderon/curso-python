def chat():
    print("Bienvenido al chat. Escriba 'salir' para terminar la conversación.")
    while True:
        mensaje = input("Tu mensaje: ")
        if mensaje == "salir":
            break
        print("Respuesta automática: ", mensaje)

chat()
