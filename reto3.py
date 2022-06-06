def AutoPartes(ventas:list):
    venta={}
    for IdProducto, dProducto, pnProducto, cvProducto, sProdducto, nComprador, cComprador, fVenta in ventas:
        if venta.get(IdProducto) == None:
            venta[IdProducto] = []
        venta[IdProducto].append((dProducto, pnProducto, cvProducto, sProdducto, nComprador, cComprador, fVenta))
    return venta

def consultaRegistro(ventas, idProducto):
    if idProducto in ventas:
        for dProducto, pnProducto, cvProducto, sProdducto, nComprador, cComprador, fVenta in ventas[idProducto]:
            print("Producto consultado :", idProducto,  " Descripción ", dProducto, " #Parte ", pnProducto, " Cantidad vendida ", cvProducto, " Stock ", sProdducto, " Comprador", nComprador, " Documento ", cComprador, " Fecha Venta ", fVenta)
    
    else:
        print("No hay registro de venta de ese producto")