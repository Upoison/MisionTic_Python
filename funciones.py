a=2
def saludo():
    print("Hola mundo")
    print("Esto es una funcion")

saludo() #llamando a la funcion saludo
saludo()

def suma(a,b,c): # a y b son los parametros de la funcion
    print(a + b + c)

a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))
suma(a,b,c) # a y b son los argumentos de la funcion suma

def resta(n1,n2):
    c = n1-n2
    d = n2-n1
    return c,d
print(resta(9,7))
