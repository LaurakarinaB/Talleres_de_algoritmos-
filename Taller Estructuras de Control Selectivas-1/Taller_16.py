import math
#Entradas
A=int(input())
B=int(input())
C=int(input())
D=int(input())
if(D==0):
    X1 = X2= -B/(2*A)
    print(X1)
    print(X2)
elif(D>0):
    X1 = (-B+math.sqrt(B**2-4*A*C))/(2*A)
    X2 = (-B-math.sqrt(B**2-4*A*C))/(2*A)
    print(X1)
    print(X2)
elif(D<0):
    print("no tiene solución en los Reales")

