#entradas
Parcial_uno=float(input("ingrese el parcial uno: "))#float
Parcial_dos=float(input("ingrese el Parcial dos: "))#float
Parcial_tres=float(input("ingrese el Parcial tres: "))#float
examen_final=float(input("ingrese el examen final: "))#float
Trabajo_final=float(input("ingrese el Trabajo final: "))#float
#caja negra
calificacion_final=((Parcial_uno+Parcial_dos+Parcial_tres)/3)*0.55+examen_final*0.30+Trabajo_final*0.15
#salida
print("calificacion_final:", calificacion_final)
