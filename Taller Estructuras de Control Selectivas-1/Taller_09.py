#entrada
nombre=str(input("Ingresa el nombre del cliente: "))
compra=int(input("monto de compra: "))
#caja negra
if(compra<50000):
    print("no hay descuento")
if(compra>=50000 and compra<=100000):
    descuento=(0.05*compra)/100
    print("descuento:", descuento)
    monto_total=(compra-descuento)
    print("monto_total:", monto_total)
if(compra>=100000 and compra<=700000):
     descuento=(0.11*compra)/100
     print("descuento:", descuento)
     monto_total=(compra-descuento)
     print("monto_total:", monto_total)
if(compra>=700000 and compra<=1500000):
     descuento=(0.18*compra)/100
     print("descuento:", descuento)
     monto_total=(compra-descuento)
     print("monto_total:", monto_total)
if(compra>=1500000):
     descuento=(0.25*compra)/100
     print("descuento", descuento)
     monto_total=(compra-descuento)
     print("monto_total:", monto_total)
