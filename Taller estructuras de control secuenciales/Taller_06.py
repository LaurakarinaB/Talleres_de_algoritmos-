#entradas
Mujeres=float(input("Ingresa el total de mujeres:"))
Hombres=float(input("Ingresa el total de hombres:"))
#caja negra
Hombres=(float(Hombres/(Mujeres+Hombres))*100)
Mujeres=(float(Mujeres/(Mujeres+Hombres))*100)
#salida
print("El porcentaje de mujeres es:", Mujeres)
print("El porcentaje de Hombres es:", Hombres)
