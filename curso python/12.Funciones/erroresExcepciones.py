while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print(edad)
        break
    except:
        print("Ingresaste un valor erroneo.")
    finally:
        print("Fin de la ejecución.")