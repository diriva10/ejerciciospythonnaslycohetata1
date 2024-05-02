#pide que escriba el numero de zapatillas y cantidad
valorZapatilla=float(input("Digite el valor de las zapatillas:"))
cantidad=int(input("digite el numero de zapatillas que compro:"))
#calcula
multiplicacion=(valorZapatilla*cantidad)
#hace el calcula de procentaje
if cantidad>=3:
    valorPagar=multiplicacion-(multiplicacion*0.20)
    print(valorPagar)
elif cantidad<=3:
   valorPagar=multiplicacion-(multiplicacion*0.10)
   print(valorPagar)