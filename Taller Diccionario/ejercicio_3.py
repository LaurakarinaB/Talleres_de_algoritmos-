usuarios={"iperurena":{"nombre":"inaki", "apellido": "perurena", "password":"654321"},
         "fmuguruza":{"nombre":"Fermín", "apellido": "Muguruza", "password":"654321"}, 
         "aolaizola":{"nombre":"Aimar", "apellido": "Olaizola", "password":"123456"}
}

for N in range (3):
    U=input("Ingrese su usuario: ")
    A=input("Ingrese su password: ")
    for i in usuarios:
        if(i==U and usuarios[i]["password"]==A):
            print(usuarios[i]["nombre"], usuarios[i]["apellido"])
            break