lista={"Mikel": 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}
N=[]
C=0
for key in lista:
    if (not(lista[key] in N)):
        N.append(lista[key])
print(N)

