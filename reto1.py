usuario = 'AB1012'
cantidad = 650000
tiempo_cdt = 2

def CDT(usuario: str, cantidad: int, tiempo_cdt: int):

    porcentajeAperder = 0.0
    porcentajeInteres = 0.03
    valorInteres = (cantidad * porcentajeInteres * tiempo_cdt) / 12
    if(tiempo_cdt <= 2):
        porcentajeAperder = 0.02
        valorAperder = cantidad * porcentajeAperder
        valorTotal = cantidad - valorAperder
    else:
        porcentajeAperder = 0.0
        valorTotal = valorInteres + cantidad
    
    respuesta = ''

    if(tiempo_cdt > 2):
        respuesta = f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo_cdt} meses es: {valorTotal}'
    else:
        respuesta = f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo_cdt} meses es: {valorTotal}'

    return respuesta

print(CDT(usuario, cantidad, tiempo_cdt))