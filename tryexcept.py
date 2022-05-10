try:
    numero = int(input("Digite un numero:\n"))
    print(numero)
    print(x)
except ValueError:
    print("Usted debe digitar solo numeros, no se permiten letras ni caracteres especiales")
except NameError:
    print("Por favor declare todas las variables")