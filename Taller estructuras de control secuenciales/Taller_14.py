#entradas
#matematicas
Costo_k=float(input("ngrese el valor del consumo de energia electrica en kilovatio: "))#float
Lectura_ac=float(input("Ingrese la Lectura_actual: "))#float
Lectura_an=float(input("Ingrese la Lectura_anterior: "))#float
#caja negra
Pago= (Lectura_an-Lectura_ac)*Costo_k
#salida
print("monto del mes de luz:  ",Pago)


