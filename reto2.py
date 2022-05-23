def cliente(informacion:dict)-> dict:

    id_cli = informacion['id_cliente']
    nombre_cli = informacion['nombre']
    edad_cli = informacion['edad']
    primerIngreso_cli = informacion['primer_ingreso']

    if edad_cli > 18:
        atraccion = 'X-Treme'
        apto = True
        if primerIngreso_cli == True:
            total_boleta = (20000 - (20000 * 0.05))
        else:
            total_boleta = 20000
    elif edad_cli >= 15 and edad_cli <= 18:
        atraccion = 'Carros chocones'
        apto = True
        if primerIngreso_cli == True:
            total_boleta = 5000 - (5000 * 0.07)
        else:
            total_boleta = 5000
    elif edad_cli >= 7 and edad_cli < 15:
        atraccion = 'Sillas voladoras'
        apto = True
        if primerIngreso_cli == True:
            total_boleta = 10000 - (10000 * 0.05)
        else:
            total_boleta = 10000
    else:
        atraccion = 'N/A'
        apto = False
        total_boleta = 'N/A'
    
    diccionario_respuesta = {
        'nombre' : nombre_cli,
        'edad' : edad_cli,
        'atraccion' : atraccion,
        'apto' : apto,
        'primer_ingreso' : primerIngreso_cli,
        'total_boleta' : total_boleta,
    }

    return diccionario_respuesta

informacion = {
    'id_cliente' : 1,
    'nombre': 'Johana Fernandez',
    'edad' : 20,
    'primer_ingreso' : True
}

print(cliente(informacion))