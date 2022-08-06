import math
#entradas
a=float(input("Ingrese la longitud A: "))#float
b=float(input("Ingrese la longitud b: "))#float
c=float(input("Ingrese la lngitud c: "))#float
#caja negra
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#salida
print("S: "+str(s))
print("Area: "+str(area))
