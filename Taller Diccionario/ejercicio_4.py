S={}
for i in range(0,10):
    nombre=input("Nombre estudiante: ")
    nota=int(input("Nota: "))
    S.update({i:{"nombre":nombre,"nota":nota}})
suspendido=[]
aprobado=[]
media=[]
for key in S:
    nombre=S[key]["nombre"]
    notas=S[key]["nota"]
    if notas<6:
        suspendido.append(nombre)
    else:
        aprobado.append(nombre)
    media.append(notas)
print("Estudiantes suspendidos:",", ".join(suspendido))
print("Estudiantes aprobados:",", ".join(aprobado))
print("La media es ",round(sum(media)/len(media),2))