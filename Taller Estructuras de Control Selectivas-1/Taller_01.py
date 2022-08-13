#entrada
dinero=float(input())
tasa_interes=float(input())
#caja negra
intereses=(dinero*tasa_interes)
if(intereses>=100.000):
    print("los intereses generados", intereses, "supera los 100.000" )
else:
    print("los intereses generados", intereses, "no supera los 100.000" )