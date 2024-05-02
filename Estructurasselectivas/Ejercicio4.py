from random import *
#Pide que escriba el numero 
valorComprar=int(input("Digite el numero de la compra de la balota"))
#describe cuales son las balotas por medio del color
balota=(choice(["rojo","verde","diferente"]))
#se describe cual va hacer el descuento
descuento=0

if balota=="rojo":
    descuento=15
elif balota=="verde":
    descuento=20
else:
    balota=="diferente"
    descuento==0

#se hace el calculo del valor balota con el descuento
valorPagar=valorComprar-((valorComprar*descuento)/100)

print("El balor de la compra es un total de",valorComprar,"el color de la balota es",balota,"el descuento es",descuento,"y valor a pagar es",valorPagar)

        

