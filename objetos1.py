# POO (Programacion Orientada a Objetos)
# Python es un leguaje orientado a objeto 
# Casi todo en Python es un objeto
# Python Clase es un modelo o patron de del cual se pueden crear multiples objetos 
# En una clASE se pueden definir metodos y atributos
#Hay que declarar una calse con la palabra class antes de crear una clase
# Al crear un objeto de una clase es lo mismo que decir : crear una instancia de una clase

#Crear una clase en Python

class Persona: #se puede crear una clase con la palabra class
    def crear(self, nombre:str):
        self.name = nombre

    def mostrar(self):
        print(self.name)

# Crear un objeto de la clase Persona
persona1 = Persona()
print(type(persona1))
persona1.crear('Juan')
persona1.mostrar()
persona2 = Persona()
persona2.crear('Ana')
persona2.mostrar()

# metodo especial __init__, es el metodo que se ejecuta al crear un objeto
# __init__ es un metodo especial que se ejecuta al crear un objeto
#  el metodo __init no retorna datos 

class Estudiante:
    def __init__(self):
        self.nombre = input('Ingrese su nombre: \n')
        self.nota = float(input('Ingrese su nota: \n'))
    def imprimir(self):
        print("Nombre", self.nombre)
        print("Nota", self.nota)
    def aprobar(self):
        if self.nota >= 3:
            print('Aprobado')
        else:
            print('Reprobado')

a = Estudiante() #instanciar la clase 
a.nota = 3.5 # modificar el atributo
a.imprimir()
a.aprobar()
