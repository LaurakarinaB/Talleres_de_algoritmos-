#entradas
from ast import Str
HN=Str(input("Numero de horas normales: "))
PHN=float(input("Pago de las horas normales: "))
HE=float(input("Numero de horas extras: "))
PHE=""

PHE =(PHN*0.25)+PHN
print("Pago de las horas extras:",PHE ,"COP")
sueldo_base=(PHN+PHE)
print("Sueldo_base: ",sueldo_base ,"COP")
deducciones_PF =(sueldo_base-0.05)
deducciones_PH =(deducciones_PF-0.02)
deducciones_CH=(deducciones_PH-0.07)
total_deducciones=(deducciones_PF+deducciones_PH+deducciones_CH)
print("Total_deduccione: ",total_deducciones, "COP")
asignacion_academica =(total_deducciones+250.000)
asignacion_cada_hijo =(asignacion_academica+173.000)
asignacion_prima =(asignacion_cada_hijo+180000)
total_asignacion=(asignacion_academica+asignacion_cada_hijo+asignacion_prima)
print( "Total_asignacion: ",total_asignacion, "COP")
sueldo_neto=(sueldo_base+total_asignacion-total_deducciones)
print( "sueldo_neto: ",sueldo_neto, "COP")