#entrada
categoria =float(input ("Ingresa la categoria: "))
aumento=0
sueldo =float(input("Ingresa el valor de sueldo:"))
if categoria==1:
    aumento=sueldo*0.10
if categoria==2:
    aumento=sueldo*0.15
if categoria==3:
    aumento=sueldo*0.20
if categoria==4:
    aumento=sueldo*0.40
if categoria==5:
    aumento=sueldo*0.60
nuevo_sueldo=sueldo+aumento
print("categoria", categoria)
print ("Valor de nuevo sueldo bruto: " + repr (nuevo_sueldo))