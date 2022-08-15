edad_en_meses=float(input(""))
nivel_de_hemoglobina=float(input(""))
rango_menor=float()
if(edad_en_meses<=1):
  rango_menor <= 13
elif(edad_en_meses>1 and edad_en_meses<=6):
  rango_menor<=10
    
elif(edad_en_meses>6 and edad_en_meses<=12): 
  rango_menor<=11

elif(edad_en_meses>12 and edad_en_meses<=60):
  rango_menor <- 11.5
    
elif(edad_en_meses>30 and edad_en_meses<=120): 
  rango_menor <- 12.6
    
elif(edad_en_meses>120 and edad_en_meses<=180): 
  rango_menor <- 13
 
elif(nivel_de_hemoglobina < rango_menor):
  print("Positivo en anemia")
else:
  print("Negativo en anemia")
    
print("Valor de rango menor: ", rango_menor)