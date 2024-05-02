#pide el numero a comprar
compra=float(input("Digite el monto total de la compra: "))
#multiplica y saca el porcentaje
if compra>=500000:#Identifica si es mayor o menor
    propioDinero= compra*0.55#multiplica el propio dinero de cuanto es el descuento 
    print(propioDinero)#imprime resultado
    prestamo=compra*0.3#multiplica el propio dinero de la compra el descuento
    print(prestamo)#imprime el resultdo
    credito=compra*0.15#multiplica el resultado del descuento de la compra
    valorCredito=credito+(credito*0.20)#se suma y multiplica los creditos 
    print(valorCredito)#se imprime el resultado
#multiplica y saca porcentaje
elif compra<=500000:#Identifica si es mayor o menor
    propioDinero=compra*0.70#Se multiplica el propio dinero con el descuento
    print(propioDinero)#Imprime el resultado
    prestamo=compra*0.3# multiplica el descuento 
    print(prestamo)#imprime el resultado
    credito=compra*0.15#se multiplica el descuento con la compra 
    valorCredito=credito+(credito*0.20)#se da el resultado del credito
    print(valorCredito)#imprime el descuento 
    
