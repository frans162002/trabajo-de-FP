#ejercicio numero 3.1
def determinarsiunapersonapuedevotar():
  #datos de entrada
  edad=int(input("ingrese una edad"))
  #proceso
  if edad>18:
    print("si pueden votar")
  elif edad<18:
    print("no pueden votar")
#determinarsiunapersonapuedevotar()
#ejercicio numero 3.2
def determinarelsueldodeuntrabajador():
  #datos de entrada
  horastrabajadas=int(input("ingrese las horas trabajadas"))
  pagoporhora=int(input("ingrese el pago por hora"))
  tiempoexedido=int(input("ingrese un numero exedido"))
  #proceso
  if horastrabajadas:
    if horastrabajadas:
      print("pagoporhorastrabajadas")
  if pagoporhora:
    if pagoporhora:
      print("pagoporhora")
  if tiempoexedido<40:
    if tiempoexedido:
      print("tiempoexedido")
#determinarelsueldodeuntrabajador()
#ejercicio numero 3.4
def cuantodebecobrarporelusodelestacionamiento():
  #datos de entrada
  horas=int(input("cantidad de horas"))
  #proceso
  if horas:
    if horas==2:print("5pesos")
    if horas==3:print("4pesos")
    if horas==5:print("3pesos")
    if horas>10:print("2pesos")
#cuantodebecobrarporelusodelestacionamiento()
#ejercicio 3.5
def nombreyedaddelapersonamenordeedad():
  #datos de entrada
  persona1=int(input("digite un numero"))
  persona2=int(input("digite un numero"))
  persona3=int(input("digite un numero"))
  #proceso
  if persona1<=persona2 and persona1<=persona3:
    print(f"la persona menor es {persona1}")
  elif persona2<=persona1 and persona2<=persona3:
    print(f"la perosna menor es {persona2}")
  elif persona3<=persona1 and persona3<=persona2:
    print(f"la persona menor es {persona3}")
#nombreyedaddelapersonamenordeedad()
#ejercicio numero 3.6
def costoydescuentoquetendraunarticulo():
  #datos de entrada
  articulo=int(input("determine costo y descuento"))
  #proceso
  if articulo:
    if articulo>=200:print("el descuento es 15%")
    if articulo>=100:print("el descuento es 12%")
    if articulo<=100:print("el descuento es 10%")
#costoydescuentoquetendraunarticulo()
#ejercicio numero 3.7
def asignaciondebecasmensuales():
  mayoresdeedad=int(input("determine el promedio"))
  menoresdeedad=int(input("determine el promedio"))
  #proceso
  if mayoresdeedad:
    if mayoresdeedad>=9:print("la beca es de $2000")
    if mayoresdeedad>=7.5:print("la beca es de $1000")
    if mayoresdeedad<7.5>6:print("la beca es de $500")
  if menoresdeedad:
    if menoresdeedad>=9:print("la beca es de $3000")
    if menoresdeedad<9>=8:print("la beca es de $2000")
    if menoresdeedad<8>=6:print("la beca es de $100")
#asignaciondebecasmensuales()
#ejercicio numero 3.8
def bonomensualasustrabajadores():
  #datos de entrada
  tiempotrabajado=int(input("cantidad de tiempo trabajados"))
  sueldotrabajado=int(input("cantidad de sueldo trabajados"))
  #proceso
  if tiempotrabajado:
    if tiempotrabajado>=2<5:
      print("bono obtenido es del 20%")
    elif tiempotrabajado>5:
      print("bono obtenido es del 30%")
  if sueldotrabajados:
    if sueldotrabajado<1000:
      print("bono obtenido es del 25%")
    elif sueldotrabajados1000<=3500:
      print("bono obtenido es del 15%")
#bonomensualasustrabajadores()
#ejercicio numero 3.11
def bonodeantiguedadparaempleados():
  #datos de entrada
  añostrabajados=int(input("cantidad de años trabajados"))
  #proceso
  if añostrabajados:
    if añostrabajados==1:print("bono obtenido de $100")
    if añostrabajados==2:print("bono obtenido de $200")
    if añostrabajados==3:print("bono obtenido de $300")
    if añostrabajados==4:print("bono obtenido de $400")
    if añostrabajados==5:print("bono obtenido de $500")
    if añostrabajados>5:print("bono obtenido de $1000")
#bonodeantiguedadparaempleados()
#ejercicio numero 3.15
def indiqueeldiadelasemanaquecorresponde():
  #datos de entrada
  numero=int(input("ingresa un numero: "))
  #proceso
  if numero==1:
    print("lunes")
  elif numero==2:
    print("martes")
  elif numero==3:
    print("miercoles")
  elif numero==4:
    print("jueves")
  elif numero==5:
    print("viernes")
  elif numero==6:
    print("sabado")
  elif numero==7:
    print("domingo")
  else:
    print("el dia no existe")
#indiqueeldiadelasemanaquecorresponde()
#ejercicio numero 3.16
def secretariodeeducacionysubono():
  #datos de entrada
  bono=int(input("ingrese un numero"))
  #proceso
  if bono:
    if bono==100:
      print("1 bono")
  elif bono==101-150:
    print("2 bono")
  elif bono==150:
    print("3 bono")
#secretariodeeducacionysubono()