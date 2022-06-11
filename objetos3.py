# Herencia
# Hay propiedades y metodos que se repiten en todas las clases
# clase padre, calse principal = clase de la que se hereda
# clase hija, clase derivada = clase que hereda de la clase padre

class Persona: # clase padre
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

        def imprimir(self):
            print(self.nombre, self.apellido)

x = Persona('Carlos', 'Arrieta')
x.imprimir()

