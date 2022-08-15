cantidad=int(input())

c1=cantidad/100000
cantidad=(cantidad-c1)*100000
c2= cantidad/50000
cantidad=(cantidad-c2)*50000
c3= cantidad/20000
cantidad=(cantidad-c3)*20000
c4= cantidad/10000
cantidad=(cantidad-c4)*10000
c5= cantidad/5000
cantidad=(cantidad-c5)*5000
c6= cantidad/2000
cantidad=(cantidad-c6)*2000
c7= cantidad/1000
cantidad=(cantidad-c7)*1000
m1=cantidad/500
cantidad=(cantidad-m1)*500
m2= cantidad/200
cantidad=(cantidad-m2)*200
m3= cantidad/100
cantidad=(cantidad-m3)*100
m4= cantidad/50
cantidad=(cantidad-m4)*50
print("numero de billetes de 100 000 :", c1)
print("numero de billetes de 50 000 :", c2)
print("numero de billetes de 20 000 :", c3)
print("numero de billetes de 10 000 :", c4)
print("numero de billetes de 5 000 :", c5)
print("numero de billetes de 2 000 :", c6)
print("numero de billetes de 1 000 :", c7)
print("numero de monedas de 500 :", m1)
print("numero de monedas de 200 :", m2)
print("numero de monedas de 100 :", m3)
print("numero de monedas de 50 :", m4)
