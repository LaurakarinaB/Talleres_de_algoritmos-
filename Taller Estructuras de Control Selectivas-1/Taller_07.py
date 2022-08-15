#entradas
distancia_km=float(input())
#caja negra
pago=int()
if(distancia_km<=300):
    pago=(50000)
    print(pago)
if(distancia_km>300 and distancia_km<1000):
    pago=(70000+(distancia_km-300)*30000)
    print(pago)
if(distancia_km>1000):
    pago=(150000+(distancia_km-300)*9000)
    print(pago)