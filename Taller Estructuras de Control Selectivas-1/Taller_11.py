temperatura=float(input(""))
deporte=""
if(temperatura>85 and temperatura<=200):
    print("Natacion")
elif(temperatura>70 and temperatura<=85):
    print("Tenis")
elif(temperatura>32 and temperatura<=70):
    print("Golf")
elif(temperatura>10 and temperatura<=32):
    print("Esqui")
elif(temperatura>=-1 and temperatura<=10):
    print("Marcha")
else:
    deporte= "no esta en el rango 😒"
    print(deporte)