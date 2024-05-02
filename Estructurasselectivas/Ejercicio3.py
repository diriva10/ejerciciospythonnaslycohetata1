#pide el numero a comprar
compra=float(input("Digite el monto total de la compra: "))
#multiplica y saca el porcentaje
if compra>=500000:
    propioDinero= compra*0.55
    print(propioDinero)
    prestamo=compra*0.3
    print(prestamo)
    credito=compra*0.15
    valorCredito=credito+(credito*0.20)
    print(valorCredito)
#multiplica y saca porcentaje
elif compra<=500000:
    propioDinero=compra*0.70
    print(propioDinero)
    prestamo=compra*0.3
    print(prestamo)
    credito=compra*0.15
    valorCredito=credito+(credito*0.20)
    print(valorCredito)
    
