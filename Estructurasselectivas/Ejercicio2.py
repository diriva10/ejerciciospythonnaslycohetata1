#pide que escriba el numero de zapatillas y cantidad
valorZapatilla=float(input("Digite el valor de las zapatillas:"))#Imprime que escriba un numero decimal o entero
cantidad=int(input("digite el numero de zapatillas que compro:"))#Imprime pero pide que escfriba un numero entero
#calcula
multiplicacion=(valorZapatilla*cantidad)
#hace el calcula de procentaje
if cantidad>=3:#Identifica si es mayor o igual que 3
    valorPagar=multiplicacion-(multiplicacion*0.20)#se multiplica los numeros
    print(valorPagar)#Imprime el resultado 
elif cantidad<=3:#Identiica si es menos o igual que 3
   valorPagar=multiplicacion-(multiplicacion*0.10)#Se calcula el resultado 
   print(valorPagar)#Imprime resultado