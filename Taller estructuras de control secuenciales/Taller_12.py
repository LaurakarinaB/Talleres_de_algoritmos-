#entradas
#matematicas
exm=float(input("examen mate: "))#float
tar1m=float(input("tarea1 mate: "))#float
tar2m=float(input("tarea2 mate: "))#float
tar3m=float(input("tarea3 mate: "))#float
#quimica
exq=float(input("examen quimica: "))#float
tar1q=float(input("tarea1 quimica: "))#float
tar2q=float(input("tarea2 quimica: "))#float
tar3q=float(input("tarea3 quimica: "))#float
#fisica
exf=float(input("examen fisica: "))#float
tar1f=float(input("tarea1 fisica: "))#float
tar2f=float(input("tarea2 fisica: "))#float
#caja negra
ma=exm*0.90+((tar1m+tar2m+tar3m)/3*0.10)
qu=exm*0.85+((tar1q+tar2q+tar3q)/3*0.15)
fi=exm*0.80+((tar1f+tar2f)/2*0.20)
promedio=(ma+qu+fi)/3
#salida
print(f"matematicas{ma} , fisica{fi} , quimica{qu},El promedio del semestre es: {promedio}  " )


