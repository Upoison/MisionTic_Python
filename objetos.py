# implemente una clase llamada operaciones se deben cargar dos valores en el metodo ____init___ y realizar las operaciones aritmeticas

class Operaciones:
    def __init__(self, a:float, b:float) -> None:
        self.a = a
        self.b = b
    def suma(self):
        print(f' La suma es: {self.a + self.b}')

    def sub(self):
        print(f' La resta es: {self.a - self.b}')

    def mul(self):
        print(f' La multiplicacion es: {self.a * self.b}')

    def div(self):
        try:
            print(f' La division es: {self.a / self.b}')
        except:
            print(f'Operacion no valida')

a = Operaciones(10,5)
a.suma()
a.sub()
a.mul()
a.div()