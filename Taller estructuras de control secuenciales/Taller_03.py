#entradas
Venta_uno = float(input("Ingresa la venta uno: "))
Venta_dos = float(input("Ingresa la venta dos: "))
Venta_tres = float(input("Ingresa la venta tres: "))
Sueldo_base = float(input("Ingresa el sueldo base: "))
#caja negra
Comisiones = ((Venta_uno+ Venta_dos+ Venta_tres)*0.1)
Sueldo_total = Sueldo_base+((Venta_uno+Venta_dos+Venta_tres)*0.1)
#salida
print("Comisiones: ", Comisiones)
print("Sueldo total: ", Sueldo_total)