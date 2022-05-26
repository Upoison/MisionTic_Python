#All y Any se aplican sobre objetos iterables
#All devuelve un true, si todos los elementos son True en Any devuelve un True, si algun elemento es True

print(all([True, False, True]))
print(all([True, True, True]))
print(any([True, False, True]))
print(any([False, False, False]))

# sum, suma los elementos de un objeto iterable
print(sum([5,5,8,4,1]))

# max y min 
print(min([5,2,8,4,5,9]), min([1,2,5,8,74,8]))
