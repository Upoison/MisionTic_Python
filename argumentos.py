def suma (a,b):
    return a+b

print(suma(6,5))

def suma2 (*args):
    total = 0
    for i in args:
        #total = total + i
        total = total +=i
    return total

print(suma2(3,4,5,72,56))
print(suma2(7,4,3,5,7,8,3,5,2,5,2,5,245,5))

def suma3 (**kwargs):
    total= 0
    for i in kwargs:
        total = total + kwargs[i]
        #total =+ kwargs[i]

    pass

print(suma3(a=1, b=2, c=50))
print(suma3(a=67, b=45, c=0, d=50))
