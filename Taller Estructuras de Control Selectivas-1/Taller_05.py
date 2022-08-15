#entradas
sueldo=float(input())
D1=float(input())
D2=float(input())
D3=float(input())
#caja negra 
venta_total=(D1+D2+D3)
Porcentaje=(venta_total*0.33)
if(D1>=Porcentaje):
    extra1=(sueldo+sueldo)*0.20
    print(extra1)
else:
    sueldo=sueldo
    print(sueldo)
if(D2>=Porcentaje):
    extra1=sueldo+sueldo*0.20
    print(extra1)

else:
    sueldo=sueldo
    print(sueldo)
if(D3>=Porcentaje):
    extra1=sueldo+sueldo*0.20
    print(extra1)
else:
    sueldo=sueldo
    print(sueldo)