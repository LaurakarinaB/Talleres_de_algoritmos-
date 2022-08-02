Algoritmo Inicio_algoritmo
	// entradas
	Escribir "Producto_uno:"
	Leer Producto_uno
	Escribir "Producto_dos "
	Leer Producto_dos
	Escribir "Producto_tres "
	Leer Producto_tres
	// caja negra
	Escribir "Total Sin descuento: " ((Producto_uno+Producto_dos+Producto_tres))
	Escribir "descuento: " ((Producto_uno+Producto_dos+Producto_tres)*0.15)
	Escribir "total a pagar: " (Producto_uno+Producto_dos+Producto_tres) - ((Producto_uno+Producto_dos+Producto_tres)*0.15)
FinAlgoritmo
