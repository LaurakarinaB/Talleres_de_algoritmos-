#entrada
Piezas=float(input())
Costo=float(input())
#caja negra
Total=Piezas*Costo
if(Total>=5000000):
    inversion=(Total*0.55)
    Banco=(Total*0.30)
    credito=(Total*0.15)
    intereses=(credito*0.20)
    print("Total inversion $",inversion)
    print("Total Banco $",Banco) 
    print("Total credito $",credito)
    print("Total intereses $",intereses)
else:
    inversion=(Total*0.70)
    credito=(Total*0.30)
    intereses=(credito*0.20)
    print("Total inversion $",inversion)
    print("Total credito $",credito)
    print("Total intereses $",intereses)
intereses=(credito*0.20)



