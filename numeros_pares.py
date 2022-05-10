#Realizar un programa que lea un numero y nos  si es par o impar
# Operacion modulo, en Python el operador es %
#  ejemplo 8%3 = 2; 8%4 = 0 ; 8%2 = 0,9%2 = 1

# datos de entrada: Numero 
#Datos de Salida: Mensaje que diga si el numero es para o impar (str)
numero = int(input("Digite un numero entero\n"))
if numero%2 == 0:
    print("f el numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

#operadores de relacion >, <, >=, <=, !=(diferente), ==(Igual)
#operadores Aritmeticos +, -, /, %, *¨, **(potencio),//(Divicion de entero),
#operadores logicos: and, or, not
#operadores de asignacion =, +=, -=

a = True
print(not(a))