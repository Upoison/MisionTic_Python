#realizar un programa que lea un numero entero y diga si es mayor o igual a 100
respuesta= "S" #= es un operador de asignacion
while respuesta == "S": #== es un operador de comparacion
    numero = int (input ("Digite un número entero:\n")) #int() convierte en entero, str() convierte a estring o cadena de caracteres 

    if numero >=100: #Condicional 
        print("El numero",numero, "es mayor o igual a 100")
    else:
        print(f"El numero {numero} es menor a 100")  #f-string deja anteponerle al mensaje con una letra f y deja poner cualquier mensaje entre corchetes 
    respuesta = input ("Presione 'S' para continuar o cualquier letra para salir\n") #\n para dar espacios como si fuera un enter
