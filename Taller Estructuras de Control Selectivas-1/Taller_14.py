Lectura_anterior=float(input(""))
Lectura_actual=float(input(""))
Lectura=(Lectura_actual+Lectura_anterior)
if(Lectura <= 100):
    Monto_a_pagar=(Lectura*4600)
    print("Monto_a_pagar:", Monto_a_pagar)
if(Lectura <= 300):
    Monto_a_pagar=(Lectura*8000)
    print("Monto_a_pagar:", Monto_a_pagar)
if(Lectura <= 500):
    Monto_a_pagar=(Lectura*100000)
    print("Monto_a_pagar:", Monto_a_pagar)
if(Lectura > 500):
    Monto_a_pagar=(Lectura*120000)
    print("Monto_a_pagar:", Monto_a_pagar)
  