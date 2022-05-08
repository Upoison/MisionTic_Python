"""#Realizar un programa que indique si una persona debe presentar 
#la declacion de renta. Las condiciones para presentar este impuesto son:
#Ser mayor de edad y
#Tener ingresos anuales superiores o iguales a $50.831.000"""

""" A    B   and    or
    F   F   F       F
    F   V   F       V
    V   F   F       V
    V   V   V       V """


edad = int(input("Digite su edad:\n"))
ingresos = int(input("Ingrese sus ingresos sin puntos ni comas:\n"))
if edad < 18 or ingresos < 50831000:
    print("Usted no debe presentar la declaracion de renta")
else:
    print("Usted debe presentar la declaracion de renta")
