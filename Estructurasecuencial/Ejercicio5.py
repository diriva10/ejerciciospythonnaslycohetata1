precio=int(input("Digite el precio de la muda de ropa que vaya a comprar:"))#pide que digite el precio 
print("Tiene un descuento de tan solo el 50%")#imprime y muestra en pantalla lo que se va a descontar
descuento=0.5#este es el descuento que se va a dar 
coste=precio*(1 - descuento)#calcula el precio con el descuento 
print("la compra fue de",precio, "$" ,"con un descuento de" , (descuento * 100) ,"%"," y el valor final a pagar es", "$", str(round(coste, 2)))#imprime o muestra el resultado en pantalla  

