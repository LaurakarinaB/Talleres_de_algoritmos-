#entradas
Producto_uno=float(input("Ingrese el valor uno: "))#float
Producto_dos=float(input("Ingrese el valor dos: "))#float
Producto_tres=float(input("Ingrese el valor tres: "))#float
#caja negra
Total_Sin_descuento=(Producto_uno+Producto_dos+Producto_tres)
descuento =((Producto_uno+Producto_dos+Producto_tres)*0.15)
total_a_pagar= (Producto_uno+Producto_dos+Producto_tres) - ((Producto_uno+Producto_dos+Producto_tres)*0.15)
#salida
print("Total_Sin_descuento: ", Total_Sin_descuento)
print("descuento: ", descuento)
print("total_a_pagar: ", total_a_pagar)


