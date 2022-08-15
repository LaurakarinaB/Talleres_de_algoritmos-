edad_en_meses=float(input(""))
rango_menor=float(input(""))

if(edad_en_meses<=1):
  if(rango_menor<=13):
    print("Positivo en anemia")
  else:
    print("Negativo en anemia")
    
elif(edad_en_meses>1 and edad_en_meses<=6):
  if(rango_menor<=10):
    print("Positivo en anemia")
  else:
    print("Negativo en anemia")
    
elif(edad_en_meses>6 and edad_en_meses<=12): 
  if(rango_menor<=11):
    print("Positivo en anemia")
  else:
    print("Negativo en anemia")

elif(edad_en_meses>12 and edad_en_meses<=60):
  if(rango_menor <= 11.5):
    print("Positivo en anemia")
  else:
    print("Negativo en anemia") 
elif(edad_en_meses>30 and edad_en_meses<=120):
  if(rango_menor<= 12.6):
     print("Positivo en anemia")
  else:
    print("Negativo en anemia")
    
elif(edad_en_meses>120 and edad_en_meses<=180): 
  if(rango_menor <= 13):
     print("Positivo en anemia")
  else:
    print("Negativo en anemia")
