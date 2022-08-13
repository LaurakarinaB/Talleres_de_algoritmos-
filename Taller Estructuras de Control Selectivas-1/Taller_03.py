#entrada
A=int(input())
B=int(input())
C=int(input())
D=int(input())
#caja negra
if(D==0):
    print("no se puede dividir por 0")
else:
    Resultado_1=(A-C)**2
    Resultado_2=((A-C)**3)/D
    print(Resultado_1)
    print(Resultado_2)
