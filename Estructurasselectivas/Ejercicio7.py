#imprime para dar una pequeña información del descuento
print("PROMOCIÓN DE LLANTAS MARCA","TODO TERRENO",)#da la frace de que se va a dar el descuento
#se imprime la información del descuento 
print("Si se compra menos de cinco llantas el precio es de $300 cada una, de $250 si se compra de cinco a 10 y de $200 si se comprán más de 10 ")

cantidadDellantas=float(input("Escriba la cantida de llantas que va a comprar:"))#Pide que digite la cantidad de llantas
compra1=300#da un total de la compra 
compra2=250#da un total de la compra 
compra3=200#da un total de la compra 
#Identifica el valor si es menor que 5

if cantidadDellantas<5:#Identifica si es menor que 5
    descuento=cantidadDellantas*compra1 #calcula la cantidad de llantas con el valor del descuento
elif cantidadDellantas>=5 or cantidadDellantas<=10:#Identifica si es de menor o igual que 10 
    descuento=cantidadDellantas*compra2#calcula la cantidad de llantas con el valor del descuento
elif cantidadDellantas>10:#Identifica si es manor que 10
    descuento=cantidadDellantas*compra3#calcula la cantidad de llantas con el valor del descuento
print("El valor a pagar es de",descuento)#imprime el resultado 