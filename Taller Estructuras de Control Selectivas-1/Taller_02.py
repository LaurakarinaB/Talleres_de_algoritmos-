#entrada
S=float(input())
#caja negra

if(S<900.000):
    Aumento_15=(S*0.15)
    salario=(Aumento_15+S)
else:
    Aumento_12=(S*0.12)
    salario=(Aumento_12+S)
print(salario)