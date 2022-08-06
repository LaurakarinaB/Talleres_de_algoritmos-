#entradas
Nt=str(input("ingrese nombre de trabajador: "))
Ht=float(input("ingrese las horas de trabajo: "))
Ph=float(input("ingrese precio de la hora: "))
#caja negra
Salario= Ht*Ph
Salario_neto= Salario*0.2
#salida
print("Salario:", Salario)
print("Salario_neto:", Salario_neto)
