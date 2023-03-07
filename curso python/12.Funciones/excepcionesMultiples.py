while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print(edad)
        break
    except ValueError:
        print("Has ingresado un valor incorrecto")
    except KeyboardInterrupt:
        print("\nHas cancelado la ejecución")
        break
