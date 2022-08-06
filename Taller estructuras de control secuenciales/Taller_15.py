#entradas

Precio_final=float(input("Precio_final: "))#float
precio_de_venta_al_publico=float(input("Precio de venta al publico: "))#float
#caja negra
descuento=abs((Precio_final-precio_de_venta_al_publico)/100)
#salida
print ("descuento: ", descuento, "%" )